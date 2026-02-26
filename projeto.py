import mysql.connector
from datetime import datetime
import time


def conectar ():
    return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'InfoLabin012025',
    database = 'agendamento_clinica'
    )
def painel_principal():
    while True:
        print("" \
        "========================================================= \n"
                    'SISTEMA DE AGENDAMENTO CLINICO\n'   
        "========================================================="
        )

        print(f"Escolha uma das opções abaixo:\n"
            "1. Cadastrar Paciente\n"
            "2. Cadastrar Médico\n"
            "3. Cadastrar Consulta\n"
            "4. Editar Consulta\n"
            "5. Editar Médico\n"
            "6. Editar Paciente\n"
            "7. Olhar Consulta\n"
            "8. Apagar Consulta\n"
            "9. SAIR")
        try:
            escolha = int(input("Escreva Aqui: "))
        except ValueError:
            print("Digite apenas números!")

        match escolha:
            case 1:
                cadastrar_paciente()
            case 2:
                cadastrar_medico()
            case 3:
                cadastrar_consulta()
            case 4:
                mostrar_consulta()
            case 9:
                break
            case _:
                return 'Opção invalida'


def cadastrar_paciente():
    nome_paciente = input('Digite o nome aqui: ')
    cpf = input('Digite o CPF aqui: ')
    telefone = input('Digite o telefone aqui: ')
    conn = conectar()
    cur = conn.cursor()

    
    cur.execute('INSERT INTO pacientes (nome, cpf, telefone) VALUES (%s, %s, %s)',
                (nome_paciente, cpf, telefone))

    conn.commit()
    cur.close()
    conn.close()


def cadastrar_medico():
    nome_medico = input('Digite o nome aqui: ')
    especialidade = input('Especialidade: ')
    conn = conectar()
    cur = conn.cursor()

    
    cur.execute('INSERT INTO medicos (nome, especialidade) VALUES (%s, %s)',
                (nome_medico, especialidade))

    conn.commit()
    cur.close()
    conn.close()


def cadastrar_consulta():
    id_paciente = input('Digite o Id do paciente: ')
    id_medico = input('Digite o Id do medico: ')
    data = datetime.now()
    status = input('Status do paciente: ')
    conn = conectar()
    cur = conn.cursor()

    
    cur.execute('INSERT INTO consultas (paciente_id, medico_id, data_hora, status) VALUES (%s, %s, %s, %s)',
                (id_paciente, id_medico, data, status))

    conn.commit()
    cur.close()
    conn.close()


def mostrar_consulta():
    conn = conectar()
    cur = conn.cursor()

    cur.execute('SELECT * FROM consultas')
    linhas = cur.fetchall()
    for ID, paciente_id, medico_id, data_hora, status in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id Paciente: {paciente_id}")
        print(f"Id Medico: {medico_id}")
        print(f"Data e hora: {data_hora}")
        print(f"Status: {status}")
        print('==================================')

    for i in range(0,5):
        time.sleep(1); print('.')

    cur.close()
    conn.close()

painel_principal()


