# entrada do usuáro
email = input('Digite seu email: ').strip()


# Função para validar o email
def validar_email(email):
    if (
        '@' in email and
        '.' in email.split('@')[-1] and
        not email.startswith('@') and
        not email.endswith('@') and
        ' ' not in email
    ):
        print(f"Email {email} é válido.")
        return True
    else:
        print(f"Email {email} é inválido.")
        return False


validar_email(email)


'''
email = input('Digite seu email: ').strip()


# Função para validar o email
def validar_email(email):
    if '@' in email and '.' in email:
        print(f"Email {email} é válido.")
        return True
    else:
        print(f"Email {email} é inválido.")
    return False


validar_email(email)
'''


