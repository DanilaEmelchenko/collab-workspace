import type { Document } from './model';

const API_URL = 'http://localhost:8000/api';

export async function fetchMyDocuments(token: string): Promise<Document[]> {
  const res = await fetch(`${API_URL}/documents/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error('Failed to load documents');
  return res.json();
}

export async function createDocument(token: string, title: string): Promise<Document> {
  const res = await fetch(`${API_URL}/documents/`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title }),
  });
  if (!res.ok) throw new Error('Failed to create document');
  return res.json();
}
