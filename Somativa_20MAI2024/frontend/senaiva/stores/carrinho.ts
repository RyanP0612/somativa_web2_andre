// import { defineStore } from "pinia";
// import type { Livro } from "~/models/livros";

// export type CarrinhoItem = {
//     produto: Livro;
//     quantidade: number;
// }

// export type Carrinho = {
//     produtos: Array<CarrinhoItem>;    
// }

// export const carrinho = defineStore('carrinhoStore', {
//     state: (): Carrinho => ({
//         produtos: []
//     }),
//     actions: {
//       adicionarNoCarrinho(novoProduto: Livro){
//             const produtoJaExiste = this.getProdutoDoCarrinho(novoProduto);
//             if(produtoJaExiste){
//                 produtoJaExiste.quantidade += 1;
//                 this.produtos = [
//                     ...this.produtos.filter(item=>item.produto.id !== produtoJaExiste.produto.id),
//                     produtoJaExiste
//                 ];
//             }
//             //produto não está no carrinho ainda
//             else{
//                 this.produtos.push({
//                     quantidade: 1,
//                     produto: novoProduto
//                 });
//             }
//       },
//       removerDoCarinho(carrinhoItem: CarrinhoItem){
//         const posicaoNoCarrinho = this.getProdutoDoCarrinhoIndex(carrinhoItem.produto);
//         //remover o item inteiro do carrinho
//         this.produtos.splice(posicaoNoCarrinho,1);

//         if(carrinhoItem.quantidade){
//             this.produtos = [
//                 ...this.produtos,
//                 carrinhoItem
//             ];
//         }
//       },
//       esvaziarCarrinho(){
//         this.produtos = [];
//       }
//     },
//     getters: {
//         estaNoCarrinho: (carrinho:Carrinho) => (produtoParaEncontrar: Livro): boolean =>{
//             return carrinho.produtos.findIndex(item=>item.produto.id === produtoParaEncontrar.id) !== -1;
//         },
//         getProdutoDoCarrinho: (carrinho:Carrinho) => (produtoParaEncontrar: Livro)=>{
//             return carrinho.produtos.find(item=>item.produto.id === produtoParaEncontrar.id);
//         },
//         getProdutoDoCarrinhoIndex: (carrinho:Carrinho) => (produtoParaEncontrar: Livro)=>{
//             return carrinho.produtos.findIndex(item=>item.produto.id === produtoParaEncontrar.id);
//         },
//         getCarrinho: (carrinho: Carrinho) => () : Array<CarrinhoItem> => {
//             return carrinho.produtos;
//         },
//         getValorTotalDoCarrinho: (carrinho: Carrinho) => () : Number => {
//             let soma = 0;
//             carrinho.produtos.forEach(item=>{
//                 soma += (item.produto.valor * item.quantidade)
//             })
//             return soma;
//         }
//     }
//   })