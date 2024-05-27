export type Livro = {
    id: number;
    titulo: string;
    nota: number;
    valor: number;
    quantidade: number;
    autor: string;
    descricao: string;
    editora: string;
    idade: string;
    dataLancamento: string; // assumindo que a data será uma string no formato ISO
    publicacao: string;     // assumindo que a data será uma string no formato ISO
    categoria: string;
    fotoFK: string;
    numeroPaginas: number;
    formato: string;
    codEdicao: string;
    aprovado: string;
}
