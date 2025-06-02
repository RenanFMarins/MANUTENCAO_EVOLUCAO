function registrarUsuario(primeiroNome, ultimoNome, email, telefone, rua, numero, cidade, estado, cep, dataNascimento) {
    // Lógica para validar dados e salvar usuário
    if (!email || !primeiroNome || !ultimoNome) {
        console.error("Dados essenciais ausentes!");
        return null;
    }

    console.log(`Registrando usuário: ${primeiroNome} ${ultimoNome}`);
    console.log(`Contato: ${email}, ${telefone}`);
    console.log(`Endereço: ${rua}, ${numero}, ${cidade}/${estado} - CEP: ${cep}`);
    console.log(`Nascimento: ${dataNascimento}`);

    // Lógica de persistência...
    return { id: Date.now(), email: email };
}

registrarUsuario(
    "Ana", "Souza", "ana.souza@email.com", "11987554321",
    "Av. Principal", "100", "São Paulo", "SP", "01000-000", "1990-05-15"
);
