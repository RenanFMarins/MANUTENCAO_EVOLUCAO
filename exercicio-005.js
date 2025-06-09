class Endereco {
    constructor(rua, numero, cidade, estado, cep, complemento = '') {
        this.rua = rua;
        this.numero = numero;
        this.cidade = cidade;
        this.estado = estado;
        this.cep = cep;
        this.complemento = complemento;
    }
}

class DadosUsuario {
    constructor(primeiroNome, ultimoNome, email, telefone, endereco, dataNascimento) {
        this.primeiroNome = primeiroNome;
        this.ultimoNome = ultimoNome;
        this.email = email;
        this.telefone = telefone;
        this.endereco = endereco;
        this.dataNascimento = dataNascimento;
    }
}

function registrarUsuario(dadosUsuario) {
    if (!dadosUsuario.email || !dadosUsuario.primeiroNome || !dadosUsuario.ultimoNome) {
        console.error("Dados essenciais ausentes!");
        return null;
    }

    console.log(`Registrando usuário: ${dadosUsuario.primeiroNome} ${dadosUsuario.ultimoNome}`);
    console.log(`Contato: ${dadosUsuario.email}, ${dadosUsuario.telefone}`);
    const e = dadosUsuario.endereco;
    console.log(`Endereço: ${e.rua}, ${e.numero}, ${e.cidade}/${e.estado} - CEP: ${e.cep}`);
    console.log(`Nascimento: ${dadosUsuario.dataNascimento}`);

    return { id: Date.now(), email: dadosUsuario.email };
}

const enderecoAna = new Endereco("Av. Principal", "100", "São Paulo", "SP", "01000-000");
const dadosAna = new DadosUsuario("Ana", "Souza", "ana.souza@email.com", "11987554321", enderecoAna, "1990-05-15");

registrarUsuario(dadosAna);