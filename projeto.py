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
            "8. Olhar Paciente\n"
            "9. Olhar Medico\n"
            "10. Remover Consulta\n"
            "11. Remover Paciente\n"
            "12. Remover Medico\n"
            "PARA SAIR DIGITE:(sair)"
            )
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
                editar_consulta()
            case 5:
                editar_medico()
            case 6 :
                editar_paciente()
            case 7 :
                olhar_consulta()
            case 8 :
                olhar_paciente()
            case 9 :
                olhar_medico()
            case 10 :
                remover_consulta()
            case 11:
                remover_paciente()
            case 12:
                remover_medico()
            case 'sair':
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
    cur.execute('INSERT INTO consultas (paciente_id, medico_id, data_hora, status) VALUES (%s, %s, %s, %s)',(id_paciente, id_medico, data, status))
    conn.commit();cur.close();conn.close()

def editar_consulta():
    conn = conectar();cur = conn.cursor()
    cur.execute('SELECT * FROM consultas')
    linhas = cur.fetchall()
    if linhas == 0:print('não há consultas cadastradas')
    print("CONSULTAS CADASTRADAS....")
    for ID, paciente_id, medico_id, data_hora, status in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id Paciente: {paciente_id}")
        print(f"Id Medico: {medico_id}")
        print(f"Data e hora: {data_hora}")
        print(f"Status: {status}")
        print('==================================')
    update_id_consulta = int(input('Digite o id da consulta: '))
    update_idpaciente = int(input('Digite o id do paciente: '))
    update_idmedico = int(input('Digite o id do medico: '))
    update_date = datetime.now()
    update_status = input('Digite o Status: ')
    cur.execute('UPDATE consultas SET paciente_id = %s, medico_id = %s, data_hora = %s, status = %s WHERE id = %s;', (update_idpaciente, update_idmedico, update_date, update_status, update_id_consulta))

    time.sleep(1);print('salvando no sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close();conn.close()

def editar_medico():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM medicos')
    linhas = cur.fetchall()
    if not linhas: print('não há consultas cadastradas')
    for ID, medico_id, especialidade in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id medico: {medico_id}")
        print(f"Especialidade: {especialidade}")
        print('==================================')
    update_id_medico = int(input('Digite o id do medico: '))
    update_nome_medico = input('Digite o nome do medico: ')
    update_especialidade_medico = input('Digite a especialidade: ')
    cur.execute('UPDATE medicos SET nome = %s, especialidade = %s WHERE id = %s;', (update_nome_medico, update_especialidade_medico, update_id_medico))
 
    time.sleep(1);print('salvando no sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close(); conn.close()

def editar_paciente():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pacientes')
    linhas = cur.fetchall()
    print("CONSULTAS CADASTRADAS...")
    if not linhas: print('não há consultas cadastradas')
    for ID, nome, cpf, telefone in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print('==================================')
    idup_paciente = int(input('Digite o id do paciente: '))
    update_nome_paciente = input('Digite o nome do paciente: ')
    update_CPF = input('Digite o CPF: ')
    update_telefone = input('Digite o Telefone: ')
    cur.execute('UPDATE pacientes SET nome = %s, cpf = %s, telefone = %s WHERE id = %s;', (update_nome_paciente, update_CPF, update_telefone, idup_paciente))
 
    time.sleep(1);print('salvando no sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close(); conn.close()

def olhar_consulta():
    conn = conectar();cur = conn.cursor()
    cur.execute('SELECT * FROM consultas')
    linhas = cur.fetchall()
    if linhas == 0:print('não há consultas cadastradas')
    print("CONSULTAS CADASTRADAS....")
    for ID, paciente_id, medico_id, data_hora, status in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id Paciente: {paciente_id}")
        print(f"Id Medico: {medico_id}")
        print(f"Data e hora: {data_hora}")
        print(f"Status: {status}")
        print('==================================')

def olhar_paciente():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pacientes')
    linhas = cur.fetchall()
    print("CONSULTAS CADASTRADAS...")
    if not linhas: print('não há consultas cadastradas')
    for ID, nome, cpf, telefone in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print('==================================')

def olhar_medico():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM medicos')
    linhas = cur.fetchall()
    if not linhas: print('não há consultas cadastradas')
    for ID, medico_id, especialidade in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id medico: {medico_id}")
        print(f"Especialidade: {especialidade}")
        print('==================================')

def remover_consulta():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pacientes')
    linhas = cur.fetchall()
    print("CONSULTAS CADASTRADAS...")
    if not linhas: print('não há consultas cadastradas')
    for ID, nome, cpf, telefone in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print('==================================')
    delete_ID = input("Digite o ID da consulta a remover: ")
    cur.execute("DELETE FROM pacientes WHERE id = %s;", (delete_ID))
    time.sleep(1);print('retirando do sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close(); conn.close()

def remover_paciente():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM pacientes')
    linhas = cur.fetchall()
    print("CONSULTAS CADASTRADAS...")
    if not linhas: print('não há consultas cadastradas')
    for ID, nome, cpf, telefone in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Nome: {nome}")
        print(f"CPF: {cpf}")
        print(f"Telefone: {telefone}")
        print('==================================')
    delete_ID_paciente = input("Digite o ID da consulta a remover: ")
    cur.execute("DELETE FROM pacientes WHERE id = %s;", (delete_ID_paciente))
    time.sleep(1);print('retirando do sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close(); conn.close()

def remover_medico():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('SELECT * FROM medicos')
    linhas = cur.fetchall()
    if not linhas: print('não há consultas cadastradas')
    for ID, medico_id, especialidade in linhas:
        print('==================================')
        print(f"ID: {ID}")
        print(f"Id medico: {medico_id}")
        print(f"Especialidade: {especialidade}")
        print('==================================')
    delete_ID_medico = input("Digite o ID da consulta a remover: ")
    cur.execute("DELETE FROM pacientes WHERE id = %s;", (delete_ID_medico))
    time.sleep(1);print('retirando do sistema')
    for i in range(0, 5):
        time.sleep(1);print('.')
    time.sleep(1)
    conn.commit()
    cur.close(); conn.close()

painel_principal()


'''
CREATE TABLE IF NOT EXISTS pacientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100),
	cpf VARCHAR(14) UNIQUE,
	telefone VARCHAR(20)
);
'''