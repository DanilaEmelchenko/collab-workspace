'use client';

import { useParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import DocumentEditor from '@/components/DocumentEditor';
import { RegisterForm } from '@/features/auth/ui/register-form';
//import RegisterForm from '@/components/RegisterForm';

export default function DocumentPage() {
  const { id } = useParams();
  // Состояние для отслеживания, что мы на клиенте
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    // Этот эффект выполняется только на клиенте
    // eslint-disable-next-line react-hooks/set-state-in-effect
    setIsClient(true);
  }, []);

  // На сервере и во время первого клиентского рендера показываем заглушку
  // Это гарантирует, что сервер и клиент всегда рендерят одинаковый HTML
  if (!isClient) {
    return (
      <div className='max-w-4xl mx-auto p-4'>
        <div className='text-center'>Загрузка...</div>
      </div>
    );
  }

  // Теперь этот код выполняется только на клиенте, после гидратации
  const token = localStorage.getItem('auth_token');

  if (!token) {
    return (
      <div className='max-w-4xl mx-auto p-4'>
        <h1 className='text-2xl font-bold mb-4'>Вход в систему</h1>
        <RegisterForm /> {/* ← используем RegisterForm */}
      </div>
    );
  }

  return (
    <div className='max-w-4xl mx-auto p-4'>
      <h1 className='text-2xl font-bold mb-4'>Документ #{id}</h1>
      <DocumentEditor documentId={id as string} />
    </div>
  );
}
