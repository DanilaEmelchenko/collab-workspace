import type { ReactNode } from 'react';

interface BadgeProps {
  children: ReactNode;
  tone?: 'live' | 'neutral';
}

export function Badge({ children, tone = 'neutral' }: BadgeProps) {
  const styles =
    tone === 'live'
      ? 'bg-[#D97706]/10 text-[#b45309] border-[#D97706]/30'
      : 'bg-black/5 text-[#57534A] border-black/10';

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-xs font-medium ${styles}`}
    >
      {tone === 'live' && <span className='h-1.5 w-1.5 rounded-full bg-[#D97706] animate-pulse-ring' />}
      {children}
    </span>
  );
}
