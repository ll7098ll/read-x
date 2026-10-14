import React, { Component, ErrorInfo, ReactNode } from 'react';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

export class ErrorBoundary extends Component<Props, State> {
  public state: State = {
    hasError: false,
    error: null,
    errorInfo: null,
  };

  public static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error, errorInfo: null };
  }

  public componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Uncaught React Error caught by ErrorBoundary:', error, errorInfo);
    this.setState({ errorInfo });
  }

  private handleResetStorage = () => {
    try {
      localStorage.clear();
      sessionStorage.clear();
    } catch (e) {
      console.error('Failed to clear storage:', e);
    }
    window.location.href = '/';
  };

  private handleReload = () => {
    window.location.reload();
  };

  public render() {
    if (this.state.hasError) {
      return (
        <div className="min-h-screen bg-slate-50 flex items-center justify-center p-6 text-slate-800 font-sans">
          <div className="max-w-xl w-full bg-white rounded-2xl shadow-xl border border-rose-100 p-8 space-y-6">
            <div className="flex items-center gap-4">
              <div className="w-12 h-12 rounded-xl bg-rose-50 border border-rose-200 flex items-center justify-center text-rose-500 text-2xl font-bold">
                ⚠️
              </div>
              <div>
                <h1 className="text-xl font-bold text-slate-900 tracking-tight">화면 렌더링 중 오류가 발생했습니다</h1>
                <p className="text-sm text-slate-500 mt-0.5">ReadX-Ray Pro 런타임 안전 모드가 활성화되었습니다.</p>
              </div>
            </div>

            <div className="bg-slate-900 text-slate-100 rounded-xl p-4 text-xs font-mono overflow-auto max-h-60 leading-relaxed">
              <div className="text-rose-400 font-bold mb-1">
                {this.state.error?.name}: {this.state.error?.message}
              </div>
              <div className="text-slate-400 whitespace-pre-wrap text-[11px]">
                {this.state.error?.stack}
              </div>
              {this.state.errorInfo?.componentStack && (
                <div className="text-slate-500 mt-2 border-t border-slate-800 pt-2 whitespace-pre-wrap text-[10px]">
                  {this.state.errorInfo.componentStack}
                </div>
              )}
            </div>

            <div className="flex flex-col sm:flex-row gap-3 pt-2">
              <button
                onClick={this.handleResetStorage}
                className="flex-1 py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white font-medium text-sm transition shadow-sm flex items-center justify-center gap-2"
              >
                🔄 저장소 초기화 후 재시작 (권장)
              </button>
              <button
                onClick={this.handleReload}
                className="py-3 px-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-700 font-medium text-sm transition"
              >
                단순 새로고침
              </button>
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
