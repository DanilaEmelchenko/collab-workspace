'use client';

import { useState } from 'react';

export default function AuthForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ username: email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem('auth_token', data.access_token);
        // Используем window.location.href для полной перезагрузки
        window.location.href = '/documents/doc-123';
      } else {
        setError(data.detail || 'Ошибка авторизации');
      }
    } catch (error) {
      console.error('Ошибка:', error);
      setError('Не удалось подключиться к серверу');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className='space-y-4 max-w-md mx-auto'>
      <h2 className='text-2xl font-bold text-center'>Вход</h2>

      <div>
        <label className='block mb-1'>Email</label>
        <input
          type='email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className='w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
          required
        />
      </div>

      <div>
        <label className='block mb-1'>Пароль</label>
        <input
          type='password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className='w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500'
          required
        />
      </div>

      {error && <div className='bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded'>{error}</div>}

      <button
        type='submit'
        disabled={isLoading}
        className='w-full bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:bg-blue-300'
      >
        {isLoading ? 'Вход...' : 'Войти'}
      </button>
    </form>
  );
}
