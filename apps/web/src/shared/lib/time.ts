export function formatRelative(iso: string | null): string {
  if (!iso) return 'только что';

  const diff = Date.now() - new Date(iso).getTime();
  const minute = 60_000;
  const hour = 60 * minute;
  const day = 24 * hour;

  if (diff < minute) return 'только что';
  if (diff < hour) return `${Math.floor(diff / minute)} мин назад`;
  if (diff < day) return `${Math.floor(diff / hour)} ч назад`;
  return `${Math.floor(diff / day)} дн назад`;
}
