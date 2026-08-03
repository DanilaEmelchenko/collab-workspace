'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { createDocument, fetchMyDocuments } from '@/entities/document/api';
import type { Document } from '@/entities/document/model';
import { fetchCurrentUser } from '@/entities/user/api';
import { CreateDocumentModal } from '@/features/create-document/ui/create-document-modal';
import { useReveal } from '@/shared/lib/use-reveal';
import { DocumentList } from '@/widgets/document-list/ui/document-list';
import { Sidebar } from '@/widgets/sidebar/ui/Sidebar';

function greeting(): string {
  const h = new Date().getHours();
  if (h < 6) return 'Доброй ночи';
  if (h < 12) return 'Доброе утро';
  if (h < 18) return 'Добрый день';
  return 'Добрый вечер';
}

export default function DashboardPage() {
  const router = useRouter();
  const [userEmail, setUserEmail] = useState('');
  const [documents, setDocuments] = useState<Document[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [headRef, headVisible] = useReveal<HTMLDivElement>();
  const [bodyRef, bodyVisible] = useReveal<HTMLDivElement>();

  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    if (!token) {
      window.location.href = '/login';
      return;
    }

    Promise.all([fetchCurrentUser(token), fetchMyDocuments(token)])
      .then(([user, docs]) => {
        setUserEmail(user.email);
        setDocuments(docs);
        setIsLoading(false);
      })
      .catch(() => {
        localStorage.removeItem('auth_token');
        window.location.href = '/login';
      });
  }, []);

  const handleCreate = async (title: string) => {
    const token = localStorage.getItem('auth_token');
    if (!token) return;
    const doc = await createDocument(token, title);
    setIsModalOpen(false);
    router.push(`/documents/${doc.id}`);
  };

  const openModal = () => setIsModalOpen(true);

  if (isLoading) {
    return (
      <div className='dot-grid grid h-screen place-items-center bg-[#EDEBE4]'>
        <div className='font-display text-lg text-[#57534A]'>Загружаем рабочее пространство…</div>
      </div>
    );
  }

  return (
    <div className='flex h-screen bg-[#EDEBE4]'>
      <Sidebar userEmail={userEmail} />

      <main className='dot-grid relative flex-1 overflow-y-auto'>
        <div className='ambient absolute inset-0' />
        <div className='relative z-10 mx-auto max-w-5xl px-8 py-12'>
          <div ref={headRef} className={`reveal ${headVisible ? 'is-visible' : ''}`}>
            <div className='flex items-start justify-between gap-4'>
              <div className='flex-1'>
                <p className='text-sm font-medium text-[#047857]'>{greeting()}</p>
                <h1 className='mt-1 font-display text-4xl font-extrabold leading-tight text-[#16150F] sm:text-5xl'>
                  Ваши документы
                </h1>
                <p className='mt-3 max-w-xl text-[#57534A] text-balance'>
                  Все рабочие пространства в одном месте. Открывайте, делитесь ссылкой и редактируйте вместе в реальном
                  времени.
                </p>
              </div>
              <button
                onClick={openModal}
                className='inline-flex items-center gap-2 rounded-xl bg-[#047857] px-5 py-2.5 text-white font-medium shadow-sm transition-all duration-200 hover:bg-[#065f46] hover:shadow-md hover:-translate-y-0.5 active:scale-[0.97]'
              >
                + Новый документ
              </button>
            </div>
          </div>

          <div ref={bodyRef} className={`reveal mt-10 ${bodyVisible ? 'is-visible' : ''}`}>
            <DocumentList
              documents={documents}
              onOpen={(id) => router.push(`/documents/${id}`)}
              onEmptyAction={openModal}
            />
          </div>
        </div>
      </main>

      <CreateDocumentModal open={isModalOpen} onClose={() => setIsModalOpen(false)} onCreate={handleCreate} />
    </div>
  );
}
