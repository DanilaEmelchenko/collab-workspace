'use client';

import type { Document } from '@/entities/document/model';
import { formatRelative } from '@/shared/lib/time';

interface DocumentListProps {
  documents: Document[];
  onOpen: (id: string) => void;
  onEmptyAction?: () => void;
}

export function DocumentList({ documents, onOpen, onEmptyAction }: DocumentListProps) {
  if (documents.length === 0) {
    return (
      <div className='relative overflow-hidden rounded-3xl border border-dashed border-[#D8D4C7] bg-[#FBFAF6]/60 p-14 text-center'>
        <div className='mx-auto mb-6 grid h-20 w-16 place-items-center rounded-lg bg-white text-3xl shadow-[0_10px_30px_-12px_rgba(22,21,15,0.3)] animate-float-soft'>
          📝
        </div>
        <h3 className='font-display text-2xl font-bold text-[#16150F]'>Пока пусто</h3>
        <p className='mx-auto mt-2 max-w-sm text-sm text-[#57534A] text-balance'>
          Создай первый документ и открой его в нескольких вкладках, чтобы увидеть магию совместного редактирования.
        </p>
        {onEmptyAction && (
          <div className='mt-7 flex justify-center'>
            <button
              onClick={onEmptyAction}
              className='inline-flex items-center gap-2 rounded-xl bg-[#047857] px-5 py-2.5 text-white font-medium shadow-sm transition-all duration-200 hover:bg-[#065f46] hover:shadow-md hover:-translate-y-0.5 active:scale-[0.97]'
            >
              + Создать документ
            </button>
          </div>
        )}
      </div>
    );
  }

  return (
    <div className='grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-3'>
      {documents.map((doc) => (
        <button
          key={doc.id}
          onClick={() => onOpen(doc.id)}
          className='group relative flex min-h-[168px] flex-col justify-between overflow-hidden rounded-2xl border border-[#D8D4C7] bg-[#FBFAF6] p-5 text-left transition-all duration-200 hover:-translate-y-1 hover:border-[#16150F]/20 hover:shadow-[0_18px_40px_-20px_rgba(22,21,15,0.4)]'
        >
          <span className='pointer-events-none absolute -right-6 -top-6 h-20 w-20 rounded-full bg-[#047857]/0 transition-colors duration-300 group-hover:bg-[#047857]/10' />
          <div>
            <h4 className='font-display text-lg font-bold leading-snug text-[#16150F] line-clamp-2'>{doc.title}</h4>
          </div>
          <div className='flex items-center justify-between text-xs text-[#57534A]'>
            <span>изменён {formatRelative(doc.updated_at)}</span>
            <span className='translate-x-1 opacity-0 transition-all duration-200 group-hover:translate-x-0 group-hover:opacity-100'>
              Открыть →
            </span>
          </div>
        </button>
      ))}
    </div>
  );
}
