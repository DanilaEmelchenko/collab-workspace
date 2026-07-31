export function formatRelative(iso: string): string {
  const then = new Date(iso).getTime();
  const diff = Date.now() - then;
  const minute = 60_000;
  const hour = 60 * minute;
  const day = 24 * hour;

  if (diff < minute) return 'только что';
  if (diff < hour) {
    const m = Math.floor(diff / minute);
    return `${m} мин назад`;
  }
  if (diff < day) {
    const h = Math.floor(diff / hour);
    return `${h} ч назад`;
  }
  const d = Math.floor(diff / day);
  return `${d} дн назад`;
}
