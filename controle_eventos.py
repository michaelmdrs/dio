# Versão 1.0
# Autor: Michael
# Data: 2025-06-28
# Descrição: Programa para controlar eventos e participantes
# Entrada: Número de eventos e lista de participantes com seus temas
# Saída: Lista de temas com os participantes correspondentes
# Exemplo de entrada:
# 3
# Evento A, Tecnologia
# Evento B, Saúde
# Evento C, Tecnologia
eventos = {}

n = int(input().strip())

for _ in range(n):
    linha = input().strip()
    nome, tema = linha.split(', ')
    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

for tema, participantes in eventos.items():
    print(f'{tema}: {", ".join(participantes)}')


# Versão 1.1
# Autor: Michael
# Data: 2025-06-29
# Descrição: Programa para controlar eventos e participantes
# Entrada: Número de eventos e lista de participantes com seus temas
# Saída: Lista de temas com os participantes correspondentes
# Exemplo de entrada:
# 3
# Evento A, Tecnologia
# Evento B, Saúde
# Evento C, Tecnologia
eventos = {}

n = int(input('Quantidade de participantes: '))
for i in range(n):
    participantes = input('Nome dos participantes: ').strip().split(', ')
    tema = input('Digite o tema do evento: ').strip()
    if tema in eventos:
        eventos[tema].extend(participantes)
    else:
        eventos[tema] = participantes
for tema, participantes in eventos.items():
    print('=' * 20)
    print('RESUMO DO EVENTO')
    print('=' * 20)
    print(f'{tema}: {", ".join(participantes)}')
print('=' * 40)
print('Total de eventos:', len(eventos))
print('Total de participantes:', sum(len(part) for part in eventos.values()))