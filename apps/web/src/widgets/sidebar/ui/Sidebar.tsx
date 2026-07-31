'use client';

import { useRouter, usePathname } from 'next/navigation';
import { Button } from '@/shared/ui/button';

interface SidebarProps {
  userEmail: string;
}

export function Sidebar({ userEmail }: SidebarProps) {
  const router = useRouter();
  const pathname = usePathname();

  const handleLogout = () => {
    localStorage.removeItem('auth_token');
    window.location.href = '/login';
  };

  const navItem = (label: string, icon: string, href: string, active: boolean) => (
    <button
      onClick={() => router.push(href)}
      className={`group flex w-full items-center gap-3 rounded-xl px-3.5 py-2.5 text-left text-sm font-medium transition-all duration-200 ${
        active
          ? 'bg-white text-[#0c1f1c] shadow-sm'
          : 'text-white/60 hover:bg-white/5 hover:text-white hover:translate-x-0.5'
      }`}
    >
      <span className='text-base transition-transform duration-200 group-hover:scale-110'>{icon}</span>
      {label}
    </button>
  );

  return (
    <aside className='flex h-screen w-72 flex-col bg-[#0c1f1c] text-white'>
      <div className='border-b border-white/10 p-6'>
        <div className='flex items-center gap-2.5'>
          <span className='grid h-9 w-9 place-items-center rounded-lg bg-[#047857] font-display text-lg font-extrabold'>
            C
          </span>
          <div className='leading-tight'>
            <p className='font-display text-base font-bold tracking-tight'>Collab</p>
            <p className='text-[11px] text-white/40'>Workspace</p>
          </div>
        </div>
      </div>

      <nav className='flex-1 space-y-1 p-3'>
        {navItem('Мои документы', '📄', '/dashboard', pathname === '/dashboard')}
        {navItem('Настройки', '⚙️', '/dashboard', false)}
      </nav>

      <div className='border-t border-white/10 p-4'>
        <div className='mb-3 flex items-center gap-3 rounded-xl bg-white/5 px-3 py-2.5'>
          <span className='grid h-8 w-8 place-items-center rounded-full bg-[#047857] text-xs font-bold uppercase'>
            {userEmail.charAt(0)}
          </span>
          <span className='truncate text-xs text-white/70' title={userEmail}>
            {userEmail}
          </span>
        </div>
        <Button
          variant='ghost'
          onClick={handleLogout}
          className='w-full justify-start text-white/60 hover:bg-white/5 hover:text-white'
        >
          🚪 Выйти
        </Button>
      </div>
    </aside>
  );
}
