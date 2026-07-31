'use client';

import { useState } from 'react';
import { Button } from '@/shared/ui/button';
import { Input } from '@/shared/ui/input';

export function LoginForm() {
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
        window.location.href = '/dashboard';
      } else {
        setError(data.detail || 'Ошибка авторизации');
      }
    } catch {
      setError('Не удалось подключиться к серверу');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className='space-y-5'>
      <div>
        <p className='text-sm font-medium text-[#57534A]'>С возвращением</p>
        <h2 className='font-display text-3xl font-extrabold text-[#16150F]'>Вход в систему</h2>
      </div>

      {error && (
        <div className='rounded-xl border border-[#b91c1c]/30 bg-[#b91c1c]/10 px-4 py-2.5 text-sm text-[#b91c1c]'>
          {error}
        </div>
      )}

      <div className='space-y-1.5'>
        <label className='text-sm font-medium text-[#16150F]'>Email</label>
        <Input type='email' value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <div className='space-y-1.5'>
        <label className='text-sm font-medium text-[#16150F]'>Пароль</label>
        <Input type='password' value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>

      <Button type='submit' disabled={isLoading} className='w-full'>
        {isLoading ? 'Входим…' : 'Войти'}
      </Button>

      <p className='text-center text-sm text-[#57534A]'>
        Нет аккаунта?{' '}
        <a href='/register' className='font-semibold text-[#047857] hover:underline'>
          Зарегистрироваться
        </a>
      </p>
    </form>
  );
}
