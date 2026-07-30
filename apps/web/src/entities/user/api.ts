import { type User } from './model';

export const fetchCurrentUser = async (token: string): Promise<User> => {
  const response = await fetch('http://localhost:8000/api/users/me', {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    throw new Error('Unauthorized');
  }

  return response.json();
};
