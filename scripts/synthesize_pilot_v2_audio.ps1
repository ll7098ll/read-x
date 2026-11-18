param([Parameter(Mandatory=$true)][string]$RequestFile,[string]$AudioOutputDirectory)
# Run with Windows PowerShell 5.1: its WinRT projection exposes the installed Korean voice.
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$pilotRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$pilotRequestPath = (Resolve-Path -LiteralPath $RequestFile).Path
$pilotHasher = [System.Security.Cryptography.SHA256]::Create()
$pilotRequestBytes = [System.IO.File]::ReadAllBytes($pilotRequestPath)
$pilotRequestHash = [BitConverter]::ToString($pilotHasher.ComputeHash($pilotRequestBytes)).Replace('-','').ToLowerInvariant()
$pilotRequest = [System.Text.Encoding]::UTF8.GetString($pilotRequestBytes).TrimStart([char]0xfeff) | ConvertFrom-Json
$pilotReportName = 'synthesis-result'
if ($pilotRequest.reportName) {
    if ($pilotRequest.reportName -notmatch '^[A-Za-z0-9-]+$') { throw 'Unsafe report identifier.' }
    $pilotReportName = [string]$pilotRequest.reportName
}
$pilotOutput = Join-Path $pilotRoot 'output\pilot-v2\audio'
if ($AudioOutputDirectory) {
    $pilotOutputRoot = [System.IO.Path]::GetFullPath((Join-Path $pilotRoot 'output'))
    $pilotOutput = [System.IO.Path]::GetFullPath($AudioOutputDirectory)
    if (-not $pilotOutput.StartsWith($pilotOutputRoot + '\',[System.StringComparison]::OrdinalIgnoreCase)) { throw 'Audio output must stay under workspace output.' }
}
[System.IO.Directory]::CreateDirectory($pilotOutput) | Out-Null
$pilotOutput = (Resolve-Path -LiteralPath $pilotOutput).Path
$pilotSynthType = [Windows.Media.SpeechSynthesis.SpeechSynthesizer,Windows.Media.SpeechSynthesis,ContentType=WindowsRuntime]
$pilotSynth = New-Object Windows.Media.SpeechSynthesis.SpeechSynthesizer
$pilotVoice = [Windows.Media.SpeechSynthesis.SpeechSynthesizer,Windows.Media.SpeechSynthesis,ContentType=WindowsRuntime]::AllVoices |
    Where-Object { $_.Language -eq 'ko-KR' } | Select-Object -First 1
if ($null -eq $pilotVoice) { throw 'No installed Korean WinRT synthesis voice.' }
$pilotSynth.Voice = $pilotVoice
$pilotAwaitMethod = [System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
    $_.Name -eq 'AsTask' -and $_.IsGenericMethodDefinition -and $_.GetParameters().Count -eq 1 -and
    $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
} | Select-Object -First 1
$pilotResultType = [Windows.Media.SpeechSynthesis.SpeechSynthesisStream,Windows.Media.SpeechSynthesis,ContentType=WindowsRuntime]
$pilotResults = @()
foreach ($pilotItem in $pilotRequest.requests) {
    if ($pilotItem.id -notmatch '^[A-Za-z0-9-]+$') { throw 'Unsafe audio identifier.' }
    if ([string]::IsNullOrWhiteSpace($pilotItem.text)) { throw 'Empty speech text.' }
    $pilotDest = [System.IO.Path]::GetFullPath((Join-Path $pilotOutput ($pilotItem.id + '.wav')))
    if (-not $pilotDest.StartsWith($pilotOutput + '\',[System.StringComparison]::OrdinalIgnoreCase)) { throw 'Audio path outside output directory.' }
    $pilotOperation = $pilotSynth.SynthesizeTextToStreamAsync([string]$pilotItem.text)
    $pilotTask = $pilotAwaitMethod.MakeGenericMethod($pilotResultType).Invoke($null,@($pilotOperation))
    $pilotTask.Wait()
    $pilotSpeech = $pilotTask.Result
    $pilotContentType = $pilotSpeech.ContentType
    $pilotRead = [System.IO.WindowsRuntimeStreamExtensions]::AsStreamForRead($pilotSpeech.GetInputStreamAt(0))
    $pilotFile = [System.IO.File]::Open($pilotDest,[System.IO.FileMode]::Create,[System.IO.FileAccess]::Write)
    try { $pilotRead.CopyTo($pilotFile) } finally { $pilotFile.Dispose(); $pilotRead.Dispose() }
    $pilotTextHash = [BitConverter]::ToString($pilotHasher.ComputeHash([System.Text.Encoding]::UTF8.GetBytes([string]$pilotItem.text))).Replace('-','').ToLowerInvariant()
    $pilotWaveHash = [BitConverter]::ToString($pilotHasher.ComputeHash([System.IO.File]::ReadAllBytes($pilotDest))).Replace('-','').ToLowerInvariant()
    $pilotResults += [pscustomobject]@{id=$pilotItem.id;voice=$pilotVoice.DisplayName;language=$pilotVoice.Language;contentType=$pilotContentType;path=$pilotDest;authorship='synthetic_builtin_voice';listeningReview='pending';textHash=$pilotTextHash;fileHash=$pilotWaveHash}
    $pilotSpeech.Dispose()
}
$pilotReport = [pscustomobject]@{requestFile=$pilotRequestPath;requestHash=$pilotRequestHash;assets=$pilotResults}
$pilotReport | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $pilotOutput ($pilotReportName + '.json')) -Encoding UTF8
$pilotSynth.Dispose()
$pilotHasher.Dispose()
Write-Output ('Synthesized Korean audio files: ' + $pilotResults.Count)
