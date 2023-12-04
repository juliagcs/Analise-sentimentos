#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Object-relational mapping

from peewee import BooleanField, CompositeKey, DateField, ForeignKeyField, \
    IntegerField, Model, SQL, SqliteDatabase, TextField, FloatField

# TODO: Check options to increase performance
DATABASE = SqliteDatabase('dados.db')

class BaseModel(Model):
    '''
    Base ORM class
    '''

    def get_dict(self):
        '''
        Return data dictionary
        '''
        return self.__data__

    class Meta:  # pylint: disable=too-few-public-methods
        '''
        Connection database
        '''
        database = DATABASE

class Segmento(BaseModel):

    # Segmento

    class Meta:
        table_name = "segmentos"

    id = IntegerField()
    nome = TextField()

class Ativo(BaseModel):

    # Ativos

    class Meta:
        table_name = "ativos"

    id = TextField()
    nome = TextField()
    razao_social = TextField()
    segmento = ForeignKeyField(Segmento, backref="ativos")

class Fundo(BaseModel):

    # Fundo

    class Meta:
        table_name = "fundos"

    id = TextField()
    mandato = TextField()
    segmento = TextField()
    gestao = TextField()
    ultimo_relatorio = TextField()
    ultimo_info_trimestral = DateField()

class Provento(BaseModel):

    # Provento

    class Meta:
        table_name = "proventos"

    id = IntegerField()
    id_ativo = ForeignKeyField(Ativo, backref="proventos")
    data_base = DateField()
    data_pagamento = DateField()
    valor = FloatField()

class Caracteristica(BaseModel):

    # Caracteristica do imovel

    class Meta:
        table_name = "caracteristicas"

    id = IntegerField()
    nome_caracteristica = TextField()

class Cotacao(BaseModel):

    # Cotação

    class Meta:
        table_name = "cotacoes"

    id = DateField()
    id_ativo = ForeignKeyField(Fundo, backref="cotacoes")
    valor_abertura = FloatField()
    valor_maximo = FloatField()
    valor_minimo = FloatField()
    valor_fechamento = FloatField()
    valor_ajustado = FloatField()
    volume = IntegerField()
    divisao = FloatField()
    
class Composicao(BaseModel):

    # Composicao

    class Meta:
        table_name = "composicoes"

    id = IntegerField()
    nome_composicao = TextField()

class FundoComposicao(BaseModel):

    # Fundo Composicao

    class Meta:
        table_name = "fundocomps"

    id = DateField()
    id_fundo = ForeignKeyField(Fundo, backref="fundocomps")
    id_composicao = ForeignKeyField(Composicao, backref="fundocomps")
    porcentagem = FloatField()
   
class FundoDetalhe(BaseModel):

    # Fundo Detalhe

    class Meta:
        table_name = "fundodets"

    id = TextField()
    id_detalhe = ForeignKeyField(Fundo, backref="fundodets")
    data = DateField()
    valor = FloatField()

class Imovel(BaseModel):

    # Imovel

    class Meta:
        table_name = "imoveis"

    id = IntegerField()
    id_fundo = ForeignKeyField(Fundo, backref="imoveis")
    id_caracteristica = ForeignKeyField(Caracteristica, backref="imoveis")
    nome_imovel = IntegerField()
    endereco = TextField()
    area = FloatField()
    unidades = IntegerField()
    taxa_ocupacao = FloatField()
    inadimplencia = FloatField()
    porcentagem_receitas = FloatField()

DATABASE.connect()
DATABASE.create_tables([Fundo, Ativo, Segmento, Provento, Cotacao,
                  Balanco, Composicao, Caracteristica, Imovel])

cara = Caracteristica(id=10, caracteristica="papel")
cara.save()
