import type { ButtonHTMLAttributes, ReactNode } from 'react';

type Variant = 'primary' | 'ghost' | 'danger' | 'outline';

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
  children: ReactNode;
}

const base =
  'inline-flex items-center justify-center gap-2 rounded-xl font-medium transition-all duration-200 active:scale-[0.97] focus:outline-none focus-visible:ring-2 focus-visible:ring-[#047857] focus-visible:ring-offset-2 focus-visible:ring-offset-[#EDEBE4] disabled:opacity-50 disabled:pointer-events-none';

const variants: Record<Variant, string> = {
  primary: 'bg-[#047857] text-white px-5 py-2.5 shadow-sm hover:bg-[#065f46] hover:shadow-md hover:-translate-y-0.5',
  outline:
    'border border-[#D8D4C7] bg-[#FBFAF6] text-[#16150F] px-5 py-2.5 hover:border-[#16150F] hover:-translate-y-0.5',
  ghost: 'text-[#57534A] px-3 py-2 hover:bg-black/5 hover:text-[#16150F]',
  danger: 'text-[#b91c1c] px-3 py-2 hover:bg-[#b91c1c]/10',
};

export function Button({ variant = 'primary', className = '', children, ...props }: ButtonProps) {
  return (
    <button className={`${base} ${variants[variant]} ${className}`} {...props}>
      {children}
    </button>
  );
}
