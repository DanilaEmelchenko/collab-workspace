import { AuthShell } from '@/features/auth/ui/auth-shell';
import { RegisterForm } from '@/features/auth/ui/register-form';

export default function RegisterPage() {
  return (
    <AuthShell>
      <RegisterForm />
    </AuthShell>
  );
}
