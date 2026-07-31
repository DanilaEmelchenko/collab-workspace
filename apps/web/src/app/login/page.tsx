import { AuthShell } from '@/features/auth/ui/auth-shell';
import { LoginForm } from '@/features/auth/ui/login-form';

export default function LoginPage() {
  return (
    <AuthShell>
      <LoginForm />
    </AuthShell>
  );
}
