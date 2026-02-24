CREATE DATABASE IF NOT EXISTS agendamento_clinica;
USE agendamento_clinica;

CREATE TABLE IF NOT EXISTS pacientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100),
	cpf VARCHAR(14) UNIQUE,
	telefone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS medicos (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100),
	especialidade VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS consultas(
	id INT AUTO_INCREMENT PRIMARY KEY,
	paciente_id INT,
	medico_id INT,
	data_hora DATETIME,
	status VARCHAR(20),
	FOREIGN KEY (paciente_id) REFERENCES pacientes(id),
	FOREIGN KEY (medico_id) REFERENCES medicos(id)
);
select*from consultas
