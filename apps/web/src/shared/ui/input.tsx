import type { InputHTMLAttributes } from 'react';

export function Input({ className = '', ...props }: InputHTMLAttributes<HTMLInputElement>) {
  return (
    <input
      className={`w-full rounded-xl border border-[#D8D4C7] bg-[#FBFAF6] px-4 py-3 text-[#16150F] placeholder:text-[#9b958a] outline-none transition-all duration-200 focus:border-[#047857] focus:ring-4 focus:ring-[#047857]/10 ${className}`}
      {...props}
    />
  );
}
