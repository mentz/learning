import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Animais } from '../animais';

@Component({
  selector: 'app-lista-animais',
  templateUrl: './lista-animais.component.html',
  styleUrls: ['./lista-animais.component.css'],
})
export class ListaAnimaisComponent implements OnInit {
  animais!: Animais;

  constructor(private activatedRoute: ActivatedRoute) {}

  ngOnInit(): void {
    // Olha que feio isso ali embaixo, um subscribe hell. Eca.
    // this.usuarioService.retornaUsuario().subscribe((usuario) => {
    //   const userName = usuario.name ?? '';
    //   this.animaisService.listaDoUsuario(userName).subscribe((animais) => {
    //     this.animais = animais;
    //   });
    // });

    // Não precisamos mais desse procedimento também, já que o Resolver
    //  pega os dados para nós durante a renderização da página.
    // this.animais$ = this.usuarioService.retornaUsuario().pipe(
    //   switchMap((usuario) => {
    //     const userName = usuario.name ?? '';
    //     return this.animaisService.listaDoUsuario(userName);
    //   })
    // );

    this.activatedRoute.params.subscribe(() => {
      this.animais = this.activatedRoute.snapshot.data['animais'];
    });
  }
}
