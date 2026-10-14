import React, { useRef, useState, useEffect } from 'react';

interface StylusInkingLayerProps {
  isEnabled: boolean;
  inkColor?: string;
  onSnapToText?: () => void;
  children: React.ReactNode;
}

export const StylusInkingLayer: React.FC<StylusInkingLayerProps> = ({
  isEnabled,
  inkColor = 'rgba(251, 191, 36, 0.45)', // warm amber highlighter
  onSnapToText,
  children,
}) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [hasStrokes, setHasStrokes] = useState(false);

  // Resize canvas to match container
  const updateCanvasSize = () => {
    const canvas = canvasRef.current;
    const container = containerRef.current;
    if (canvas && container) {
      canvas.width = container.offsetWidth;
      canvas.height = container.offsetHeight;
    }
  };

  useEffect(() => {
    updateCanvasSize();
    window.addEventListener('resize', updateCanvasSize);
    return () => window.removeEventListener('resize', updateCanvasSize);
  }, []);

  const handlePointerDown = (e: React.PointerEvent<HTMLCanvasElement>) => {
    if (!isEnabled) return;
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.strokeStyle = inkColor;
    ctx.lineWidth = e.pointerType === 'pen' ? 14 : 16;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';
    setIsDrawing(true);
    setHasStrokes(true);
  };

  const handlePointerMove = (e: React.PointerEvent<HTMLCanvasElement>) => {
    if (!isDrawing || !isEnabled) return;
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    ctx.lineTo(x, y);
    ctx.stroke();
  };

  const handlePointerUp = () => {
    if (!isDrawing) return;
    setIsDrawing(false);
    onSnapToText?.();
  };

  const handleClear = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      ctx?.clearRect(0, 0, canvas.width, canvas.height);
      setHasStrokes(false);
    }
  };

  return (
    <div ref={containerRef} className="relative w-full">
      {/* Underlying Content */}
      <div className="relative z-10">{children}</div>

      {/* Inking Canvas Layer */}
      {isEnabled && (
        <canvas
          ref={canvasRef}
          onPointerDown={handlePointerDown}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerLeave={handlePointerUp}
          className="absolute inset-0 z-20 touch-none cursor-crosshair"
          style={{ mixBlendMode: 'multiply' }}
        />
      )}

      {/* Floating Inking Status Pill */}
      {isEnabled && (
        <div className="absolute top-2 right-2 z-30 flex items-center gap-1.5 bg-slate-900/90 text-white text-[11px] px-2.5 py-1 rounded-full shadow-md backdrop-blur-xs select-none">
          <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse" />
          <span className="font-bold">🖊️ 스타일러스 펜슬 모드</span>
          {hasStrokes && (
            <button
              onClick={handleClear}
              className="ml-1 text-slate-300 hover:text-white underline cursor-pointer"
            >
              지우기 ✕
            </button>
          )}
        </div>
      )}
    </div>
  );
};
