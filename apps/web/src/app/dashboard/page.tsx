'use client';

import { useEffect, useState } from 'react';
import { fetchCurrentUser } from '@/entities/user/api';
import { Sidebar } from '@/widgets/sidebar/ui/Sidebar';

export default function DashboardPage() {
  const [userEmail, setUserEmail] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    if (!token) {
      window.location.href = '/login';
      return;
    }

    fetchCurrentUser(token)
      .then((user) => {
        setUserEmail(user.email);
        setIsLoading(false);
      })
      .catch(() => {
        localStorage.removeItem('auth_token');
        window.location.href = '/login';
      });
  }, []);

  if (isLoading) {
    return (
      <div className='h-screen flex items-center justify-center bg-white'>
        <div className='text-gray-500'>Загрузка...</div>
      </div>
    );
  }

  return (
    <div className='flex h-screen bg-white'>
      <Sidebar userEmail={userEmail} />
      <main className='flex-1 p-8 overflow-y-auto'>
        <div className='max-w-4xl mx-auto'>
          <div className='flex justify-between items-center mb-8'>
            <h2 className='text-3xl font-bold text-gray-800'>Мои документы</h2>
            <button className='bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition font-medium'>
              + Новый документ
            </button>
          </div>

          <div className='bg-gray-50 border border-dashed border-gray-300 rounded-xl p-12 text-center'>
            <p className='text-gray-500 text-lg'>У вас пока нет документов.</p>
            <p className='text-gray-400 text-sm mt-2'>Нажмите Новый документ, чтобы начать.</p>
          </div>
        </div>
      </main>
    </div>
  );
}
