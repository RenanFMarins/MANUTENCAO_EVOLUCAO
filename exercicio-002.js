function formatarInformacao(rotulo, ...partes) {
    let informacaoFormatada = rotulo + ": ";
    informacaoFormatada += partes
        .filter(parte => parte)
        .join(" ");
    console.log(informacaoFormatada);
}

function exibirDetalhesUsuario(usuario) {
    formatarInformacao("Nome", usuario.titulo, usuario.primeiroNome, usuario.ultimoNome);

    const enderecoPrincipal = `${usuario.tipoLogradouro || ""} ${usuario.logradouro}, ${usuario.numero}`;
    formatarInformacao("Endereço", enderecoPrincipal.trim(), usuario.complemento);
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
