import type { Metadata } from 'next';
import { Bricolage_Grotesque, Plus_Jakarta_Sans } from 'next/font/google';
import './globals.css';

const bricolage = Bricolage_Grotesque({
  subsets: ['latin'],
  weight: ['400', '600', '700', '800'],
  variable: '--font-display',
  display: 'swap',
});

const jakarta = Plus_Jakarta_Sans({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  variable: '--font-body',
  display: 'swap',
});

export const metadata: Metadata = {
  title: 'Collab Workspace',
  description: 'Редактор документов с совместной работой в реальном времени',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang='ru' className={`${bricolage.variable} ${jakarta.variable}`}>
      <body className='bg-[#EDEBE4] text-[#16150F] antialiased selection:bg-[#047857] selection:text-white'>
        {children}
      </body>
    </html>
  );
}
