CREATE DATABASE cliente;

USE cliente;

CREATE TABLE base(
idbase INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(100) NOT NULL,
cpf VARCHAR(11) NOT NULL, 
numero VARCHAR(12),
nascimento DATETIME,
cluster ENUM('Jovem','Adulto','Senior') NOT NULL,
CONSTRAINT pk_base PRIMARY KEY (idbase)
);