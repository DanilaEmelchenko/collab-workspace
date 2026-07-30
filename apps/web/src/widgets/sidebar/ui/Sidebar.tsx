'use client';

import { useRouter } from 'next/navigation';

interface SidebarProps {
  userEmail: string;
}

export function Sidebar({ userEmail }: SidebarProps) {
  const router = useRouter();

  const handleLogout = () => {
    localStorage.removeItem('auth_token');
    window.location.href = '/login';
  };

  return (
    <aside className='w-64 bg-gray-50 border-r border-gray-200 h-screen flex flex-col'>
      <div className='p-6 border-b border-gray-200'>
        <h1 className='text-xl font-bold text-gray-800'>Collab Workspace</h1>
        <p className='text-xs text-gray-500 mt-1 truncate' title={userEmail}>
          {userEmail}
        </p>
      </div>

      <nav className='flex-1 p-4 space-y-2'>
        <button
          onClick={() => router.push('/dashboard')}
          className='w-full text-left px-4 py-2 rounded-lg bg-blue-50 text-blue-700 font-medium transition'
        >
          📄 Мои документы
        </button>
        <button className='w-full text-left px-4 py-2 rounded-lg text-gray-600 hover:bg-gray-100 transition'>
          ⚙️ Настройки
        </button>
      </nav>

      <div className='p-4 border-t border-gray-200'>
        <button
          onClick={handleLogout}
          className='w-full text-left px-4 py-2 rounded-lg text-red-600 hover:bg-red-50 transition font-medium'
        >
          🚪 Выйти
        </button>
      </div>
    </aside>
  );
}
