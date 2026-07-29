import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  // Проксируем запрос к бэкенду
  const response = await fetch('http://localhost:8000/api/auth/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      ...request.headers,
    },
    body: await request.text(),
  });

  return new NextResponse(response.body, {
    status: response.status,
    headers: {
      'Content-Type': 'application/json',
    },
  });
}
