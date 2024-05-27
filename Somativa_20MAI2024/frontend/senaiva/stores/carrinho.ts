import type { Livro } from "~/models/livros";

export type CarrinhoItem = {
    livro: Livro;
    quantidade: number;
}

export type Carrinho = {
    livros: Array<CarrinhoItem>;    
}


// export const carrinho = defineStore('carrinhoStore', {
//     state: (): Carrinho => ({
//         livros: []
//     }),
//     actions: {
//       adicionarNoCarrinho(novoProduto: Livro){
//             const produtoJaExiste = this.getProdutoDoCarrinho(novoProduto);
//             if(produtoJaExiste){
//                 produtoJaExiste.quantidade += 1;
//                 this.livros = [
//                     ...this.livros.filter(item=>item.produto.id !== produtoJaExiste.produto.id),
//                     produtoJaExiste
//                 ];
//             }
//             //produto não está no carrinho ainda
//             else{
//                 this.livros.push({
//                     quantidade: 1,
//                     produto: novoProduto
//                 });
//             }
//       },}})