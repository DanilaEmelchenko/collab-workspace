import { useState, useEffect, useRef } from 'react';
import { WebsocketProvider } from 'y-websocket';
import * as Y from 'yjs';

interface DocumentEditorProps {
  documentId: string;
}

export default function DocumentEditor({ documentId }: DocumentEditorProps) {
  const editorRef = useRef<HTMLDivElement>(null);
  const [editorReady, setEditorReady] = useState(false);

  useEffect(() => {
    if (!editorRef.current) return;

    // 1. Создаем Yjs-документ
    const ydoc = new Y.Doc();

    // 2. Подключаемся к нашему WebSocket-серверу
    const token = localStorage.getItem('auth_token');
    if (!token) {
      console.error('Токен не найден! Сначала залогиньтесь.');
      return;
    }

    const provider = new WebsocketProvider('ws://localhost:8000', `ws/documents/${documentId}`, ydoc, {
      params: { token },
    });

    // 3. Создаем текстовую область
    const text = ydoc.getText('content');
    text.observe(() => {
      if (editorReady && editorRef.current) {
        editorRef.current.textContent = text.toString();
      }
    });

    // 4. Инициализируем редактор
    if (editorRef.current) {
      editorRef.current.textContent = text.toString();
      editorRef.current.contentEditable = 'true';

      // ✅ ИСПРАВЛЕНО: используем delete + insert вместо set
      editorRef.current.addEventListener('input', (e) => {
        const target = e.target as HTMLDivElement;
        const newText = target.textContent || '';

        // Полностью заменяем содержимое
        text.delete(0, text.length);
        text.insert(0, newText);
      });

      setEditorReady(true);
    }

    // 5. Очистка при размонтировании
    return () => {
      provider.destroy();
      ydoc.destroy();
    };
  }, [documentId, editorReady]);

  return (
    <div className='border rounded p-4 min-h-[300px]'>
      <h3 className='font-bold mb-2'>Документ #{documentId}</h3>
      <div
        ref={editorRef}
        className='border rounded p-3 focus:outline-none'
        style={{ minHeight: '200px' }}
        contentEditable={editorReady}
      />
    </div>
  );
}
