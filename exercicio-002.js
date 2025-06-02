function exibirDetalhesUsuario(usuario) {
    // Formatar e exibir nome completo
    let nomeFormatado = "Nome: ";
    if (usuario.titulo) {
        nomeFormatado += usuario.titulo + " ";
    }
    nomeFormatado += usuario.primeiroNome + " " + usuario.ultimoNome;
    console.log(nomeFormatado);

    // Formatar e exibir endereço
    let enderecoFormatado = "Endereço: ";
    if (usuario.tipoLogradouro) {
        enderecoFormatado += usuario.tipoLogradouro + " ";
    }

    enderecoFormatado += usuario.logradouro + ", " + usuario.numero;
    if (usuario.complemento) {
        enderecoFormatado += " - " + usuario.complemento;
    }
    console.log(enderecoFormatado);
}

const user = {
    titulo: "Dr.",
    primeiroNome: "João",
    ultimoNome: "Silva",
    tipoLogradouro: "Rua",
    logradouro: "Das Palmeiras",
    numero: "123",
    complemento: "Apto 4B"
};

exibirDetalhesUsuario(user);
