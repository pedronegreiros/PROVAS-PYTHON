#ALUNO: PEDRO NEGREIROS ANDRADE

# Defina o email e senha cadastrados antecipadamente
email_cadastrado = "user@gmail.com"
pasword_cadastrada = "pasword123"

# Inicialize as variáveis de email e senha do usuário como vazias
email_user = ""
pasword_user = ""

# Use um loop para solicitar email e senha até que correspondam aos cadastrados
while email_user != email_cadastrado or pasword_user != pasword_cadastrada:
    # Solicite ao usuário o email e a senha
    email_user = input("Digite seu email: ")
    pasword_user = input("Digite sua senha: ")

    # Verifique se o email e a senha digitados correspondem aos cadastrados
    if email_user == email_cadastrado and pasword_user == pasword_cadastrada:
        print("Acesso concedido. Bem-vindo!")
    else:
        print("Email ou senha incorretos. Tente novamente.")

# O programa continua aqui após o loop quando o acesso é concedido
print("Programa encerrado.")


