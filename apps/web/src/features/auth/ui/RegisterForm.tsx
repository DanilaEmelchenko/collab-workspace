'use client';
/*
import { useState } from 'react';

export function RegisterForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    try {
      // 1. Регистрируем пользователя
      const regRes = await fetch('http://localhost:8000/api/users/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });

      if (!regRes.ok) {
        const data = await regRes.json();
        throw new Error(data.detail || 'Ошибка регистрации');
      }

      // 2. Сразу логинимся
      const loginRes = await fetch('http://localhost:8000/api/auth/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({ username: email, password }),
      });

      if (loginRes.ok) {
        const data = await loginRes.json();
        localStorage.setItem('auth_token', data.access_token);
        window.location.href = '/dashboard';
      }
    } catch (err: any) {
      setError(err.message || 'Не удалось подключиться к серверу');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className='space-y-4 w-full max-w-sm'>
      <h2 className='text-2xl font-bold text-center text-gray-800'>Создать аккаунт</h2>
      {error && <div className='bg-red-50 border border-red-200 text-red-600 px-4 py-2 rounded text-sm'>{error}</div>}

      <div>
        <label className='block text-sm font-medium text-gray-700 mb-1'>Email</label>
        <input
          type='email'
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className='w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition'
          required
        />
      </div>
      <div>
        <label className='block text-sm font-medium text-gray-700 mb-1'>Пароль</label>
        <input
          type='password'
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className='w-full p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none transition'
          required
        />
      </div>
      <button
        type='submit'
        disabled={isLoading}
        className='w-full bg-blue-600 text-white py-2.5 rounded-lg font-medium hover:bg-blue-700 disabled:bg-blue-300 transition'
      >
        {isLoading ? 'Создание...' : 'Зарегистрироваться'}
      </button>
      <p className='text-center text-sm text-gray-600 mt-4'>
        Уже есть аккаунт?{' '}
        <a href='/login' className='text-blue-600 hover:underline font-medium'>
          Войти
        </a>
      </p>
    </form>
  );
}
*/
