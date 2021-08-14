import { FormGroup } from '@angular/forms';

export function usuarioSenhaIguaisValidator(formGroup: FormGroup) {
  const userName = (formGroup.get('userName')?.value ?? '') as string;
  const password = (formGroup.get('password')?.value ?? '') as string;

  if (userName.trim() + password.trim()) {
    return userName === password ? { senhaIgualUsuario: true } : null;
  }
  return null;
}
