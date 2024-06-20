-- Criação do banco de dados
CREATE DATABASE crm_simples;

-- Utilização do banco de dados
USE crm_simples;

-- Tabela para armazenar informações dos clientes
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    endereco VARCHAR(200),
    cidade VARCHAR(100),
    estado VARCHAR(50),
    cep VARCHAR(15),
    pais VARCHAR(50)
);

-- Tabela para armazenar informações dos usuários
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    papel VARCHAR(50)
);

use crm_simples;
select*from clientes;
