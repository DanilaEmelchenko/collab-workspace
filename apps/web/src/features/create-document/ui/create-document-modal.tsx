'use client';

import { useState } from 'react';
import { Button } from '@/shared/ui/button';
import { Input } from '@/shared/ui/input';

interface CreateDocumentModalProps {
  open: boolean;
  onClose: () => void;
  onCreate: (title: string) => Promise<void>;
}

export function CreateDocumentModal({ open, onClose, onCreate }: CreateDocumentModalProps) {
  const [title, setTitle] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState('');

  if (!open) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim()) return;
    setError('');
    setIsSubmitting(true);
    try {
      await onCreate(title.trim());
      setTitle('');
    } catch {
      setError('Не удалось создать документ');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className='fixed inset-0 z-50 grid place-items-center bg-[#16150F]/40 p-4 animate-fade-in' onClick={onClose}>
      <div
        className='w-full max-w-md rounded-2xl border border-[#D8D4C7] bg-[#FBFAF6] p-7 shadow-2xl animate-modal-pop'
        onClick={(e) => e.stopPropagation()}
      >
        <p className='text-sm font-medium text-[#047857]'>Новый документ</p>
        <h3 className='mt-1 font-display text-2xl font-extrabold text-[#16150F]'>О чём будем писать?</h3>

        <form onSubmit={handleSubmit} className='mt-6 space-y-4'>
          <Input
            autoFocus
            placeholder='Например: «План запуска продукта»'
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            maxLength={255}
          />
          {error && <p className='text-sm text-[#b91c1c]'>{error}</p>}

          <div className='flex justify-end gap-2'>
            <Button type='button' variant='ghost' onClick={onClose}>
              Отмена
            </Button>
            <Button type='submit' disabled={isSubmitting || !title.trim()}>
              {isSubmitting ? 'Создаём…' : 'Создать и открыть'}
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
}
