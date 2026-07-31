import type { ReactNode } from 'react';

interface AuthShellProps {
  children: ReactNode;
}

export function AuthShell({ children }: AuthShellProps) {
  return (
    <div className='grid min-h-screen lg:grid-cols-2'>
      {/* Левая витрина */}
      <div className='ambient relative hidden overflow-hidden bg-[#0c1f1c] p-12 text-white lg:flex lg:flex-col lg:justify-between'>
        <div className='dot-grid absolute inset-0 opacity-40' />
        <div className='relative z-10 flex items-center gap-2.5'>
          <span className='grid h-9 w-9 place-items-center rounded-lg bg-[#047857] font-display text-lg font-extrabold'>
            C
          </span>
          <span className='font-display text-lg font-bold'>Collab Workspace</span>
        </div>

        <div className='relative z-10 max-w-md'>
          <p className='mb-4 inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-3 py-1 text-xs text-white/70'>
            <span className='h-1.5 w-1.5 rounded-full bg-[#D97706] animate-pulse-ring' />
            реальное время · без перезагрузок
          </p>
          <h1 className='font-display text-5xl font-extrabold leading-[1.05] text-balance'>
            Пишите вместе —<br />
            как в одной комнате.
          </h1>
          <p className='mt-5 text-base leading-relaxed text-white/60'>
            Курсоры коллег, мгновенная синхронизация и история каждого символа. Ваш рабочий стол для документов.
          </p>
        </div>

        <div className='relative z-10 flex -space-x-2'>
          {['#047857', '#D97706', '#0c1f1c'].map((c, i) => (
            <span
              key={i}
              className='grid h-9 w-9 place-items-center rounded-full border-2 border-[#0c1f1c] text-xs font-bold'
              style={{ background: c === '#0c1f1c' ? '#FBFAF6' : c, color: c === '#0c1f1c' ? '#0c1f1c' : '#fff' }}
            >
              {['А', 'М', 'К'][i]}
            </span>
          ))}
          <span className='grid h-9 w-9 place-items-center rounded-full border-2 border-[#0c1f1c] bg-white/10 text-[11px] text-white/70'>
            +12
          </span>
        </div>
      </div>

      {/* Правая форма */}
      <div className='dot-grid relative flex items-center justify-center bg-[#EDEBE4] p-6'>
        <div className='w-full max-w-sm'>{children}</div>
      </div>
    </div>
  );
}
