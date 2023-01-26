# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:37:04 2023

@author: alexr
"""

import mysql.connector
import datetime

#Conexão com banco de dados

def conectar_mysql():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Agui@100",
        database="cliente"
        )
    return connection


class cliente:
    
    def __init__(self, name, cpf, numero, nascimento):
        self.name = name
        self.cpf = cpf
        self.numero = numero
        
        lista_nascimento = [int(i) for i in nascimento.split("/")]
        self.nascimento = datetime.datetime(lista_nascimento[2],lista_nascimento[1],lista_nascimento[0])
        
        idade = datetime.datetime.now() - self.nascimento
        self.cluster = "Jovem" if int(idade.days/365) <= 18 else "Adulto" if int(idade.days/365) <= 60 else "Senior"
        
                              
    def cadastro(self,connection):
        cursor = connection.cursor()
        cadastro_cliente = f'INSERT INTO base (nome,cpf,numero,nascimento,cluster) VALUES ("{self.name}","{self.cpf}","{self.numero}","{self.nascimento}","{self.cluster}");'
        
        cursor.execute(cadastro_cliente)
        connection.commit()
        
        userid = cursor.lastrowid
        
        cursor.close()
        connection.close()
        
        print(f"Novo cliente cadastrado: {userid} - {self.name}")
        
    def acessar_BD(self,connection):
        cursor  = connection.cursor()
        visualizar_bd = 'SELECT * FROM base'
        
        cursor.execute(visualizar_bd)
        results = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        print("Acessar Banco de Dados")
        
        for result in results:
            print(result)
             
    def update_cadastro(self,id_cliente,connection):
        cursor = connection.cursor()
        update_cliente = f'UPDATE base SET nome = "{self.name}",cpf = "{self.cpf}",numero = "{self.numero}", nascimento = "{self.nascimento}", cluster = "{self.cluster}" WHERE idbase = {id_cliente};'
        
        cursor.execute(update_cliente)
        connection.commit()
        
        recordsaffected = cursor.rowcount
        
        cursor.close()
        connection.close()
        
        print(f"{recordsaffected} Registros alterados | Update cadastro: {id_cliente} - {self.name}")
        
    def remover(self,id_cliente,connection):
        cursor = connection.cursor()
        remover_cliente = f'DELETE FROM base WHERE idbase = {id_cliente}'
        
        cursor.execute(remover_cliente)
        connection.commit()
        
        recordsaffected = cursor.rowcount
        
        cursor.close()
        connection.close()
        
        print(f"{recordsaffected} Registros Alterados")
        

#Cadastrando um novo cliente:
#novo_cliente = cliente("Sueli", "01009809800","011912341234","12/08/1960")

# FUNCOES:
# 
# CADASTRO - cluster connection  
# ACESSAR BD - connection
# UPDATE CADASTRO - id_cliente cluster connection
# REMOVER - id_cliente connection

#novo_cliente.cadastro(connection=conectar_mysql())
#novo_cliente.acessar_BD(connection=conectar_mysql())

novo_cliente = cliente("Sophia", "01009809800","011912341234","12/08/2005")
#novo_cliente.update_cadastro(6,connection=conectar_mysql())
#novo_cliente.acessar_BD(connection=conectar_mysql())

novo_cliente.remover(6,connection=conectar_mysql())
novo_cliente.acessar_BD(connection=conectar_mysql())


#novo_cliente.cadastro(cluster=novo_cliente.cluster())
#novo_cliente.remover(4)
