import { defineStore, CommitFunction } from 'vuex';
import type { Livro } from "~/models/livros";

export type CarrinhoItem = {
    livro: Livro;
    quantidade: number;
}

export type CarrinhoState = {
    livros: CarrinhoItem[];    
}

export const carrinho = defineStore({
    state: (): CarrinhoState => ({
        livros: []
    }),
    actions: {
        adicionarNoCarrinho({ state, commit }: { state: CarrinhoState; commit: CommitFunction }, novoLivro: Livro) {
            const livroJaExiste = state.livros.find(item => item.livro.id === novoLivro.id);
            if (livroJaExiste) {
                commit('incrementarQuantidade', livroJaExiste);
            } else {
                commit('adicionarLivro', novoLivro);
            }
        },
        removerDoCarinho({ state, commit }: { state: CarrinhoState; commit: CommitFunction }, carrinhoItem: CarrinhoItem) {
            const posicaoNoCarrinho = state.livros.findIndex(item => item.livro.id === carrinhoItem.livro.id);
            if (posicaoNoCarrinho !== -1) {
                commit('removerLivro', posicaoNoCarrinho);
            }
        },
        esvaziarCarrinho({ commit }: { commit: CommitFunction }) {
            commit('esvaziarCarrinho');
        }
    },
    mutations: {
        adicionarLivro(state: CarrinhoState, novoLivro: Livro) {
            state.livros.push({
                quantidade: 1,
                livro: novoLivro
            });
        },
        incrementarQuantidade(state: CarrinhoState, carrinhoItem: CarrinhoItem) {
            carrinhoItem.quantidade++;
        },
        removerLivro(state: CarrinhoState, posicao: number) {
            state.livros.splice(posicao, 1);
        },
        esvaziarCarrinho(state: CarrinhoState) {
            state.livros = [];
        }
    },
    getters: {
        estaNoCarrinho(state: CarrinhoState) {
            return (livroParaEncontrar: Livro) => state.livros.some(item => item.livro.id === livroParaEncontrar.id);
        },
        getLivroDoCarrinho(state: CarrinhoState) {
            return (livroParaEncontrar: Livro) => state.livros.find(item => item.livro.id === livroParaEncontrar.id);
        },
        getValorTotalDoCarrinho(state: CarrinhoState) {
            return state.livros.reduce((total, item) => total + (item.livro.valor * item.quantidade), 0);
        }
    }
});
