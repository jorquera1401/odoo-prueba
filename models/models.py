#-*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date 

class Curso(models.Model):
    _name="prueba.course"
    _description = "Prueba Courses"

    name = fields.Char(string="Title",required=True)
    description=fields.Text(string="Descripcion")
    fecha = fields.Date(default=date.today())
    campo  = fields.Char(default="valor defecto")
    precio = fields.Integer(string="precio")
    impuesto = fields.Float(default="0")
    total = fields.Float(default="0")

    #hace la relacion con la otra clase 
    carrera_nombre = fields.Many2one('prueba.carrera', ondelete='cascade',string='Carrera')
    recname="nombre"
    @api.onchange('name')
    def _setear_descripcion(self):
        self.description = self.name

    @api.onchange('precio')
    def _calcular_impuesto(self):
        self.impuesto = self.precio*0.19
        self.total = self.precio - self.impuesto
    @api.model  
    def calcular(self,context=None):
        precio = self.precio+self.precio*0.5
        self.precio=precio
        if context is None:
            context = {'precio':precio}
        self.write(context)

class Carrera(models.Model):
    _name='prueba.carrera'
    _description='Carrera Test'
    _rec_name = "nombre"

    nombre = fields.Char('Nombre',required=True)
    descripcion = fields.Text(string="Agregar Descripcion")
    arancel = fields.Integer(string="Arancel",default="0")
    vacantes = fields.Integer(string="Vacantes",fefault="0")
    impuesto=fields.Float(default="0")
    total = fields.Float(default="0")
    
class Alumno(models.Model):
    _name="prueba.alumno"
    _description="Alumno Test"
    _rec_name = "combinacion"
    nombre= fields.Char(string='Nombres', required=True)
    apellido_p = fields.Char(string='Apellido Paterno', required=True)
    apellido_m=fields.Char(string='Apellido Materno', required=True)
    rut = fields.Char(string='Rut (sin digito verificador)', required=True)
    fecha_nacimiento = fields.Date(default=date.today())
    carrera = fields.Many2one('prueba.carrera', ondelete='cascade', string="Carrera")
    
    combinacion  =fields.Char(string="nombre completo",compute='_visualizar_modulo')

    @api.depends('nombre','apellido_p')
    def _visualizar_modulo(self):
        for campos in self:
            campos.combinacion = campos.apellido_p + ' '+campos.nombre

    #funcion que permite validar un rut 
    @api.onchange('rut')
    def _validarRut(self):
        orut = str(self.rut)
        if len(orut)>0:
            valores  =orut.split("-")
            rut_number  =valores[0]
            digito=""
            if rut_number.isdigit():
                if len(valores)>1:
                    digito = valores[1]
                valor =2
                sumatoria=0
                print("digito: ",digito," rut: ", orut)
                for i in range(0,len(rut_number)):
                    posicion = (len(rut_number)-1)-i
                    sumatoria+=int(rut_number[posicion])*valor 
                    valor+=1
                    if valor > 7:
                        valor=2    
                modulo=int(sumatoria/11)
                modulo*=11
                dv = sumatoria-modulo
                dv = 11-dv
                resultado =str(dv)
                if dv==11:
                    resultado="0"
                if dv==10:
                    resultado="k"
                if(len(digito)>0):
                    if resultado == digito:
                        self.rut = rut_number+resultado
                    else:
                        self.rut = "Rut invalido"
                else:
                    self.rut = rut_number+resultado
            else:
                self.rut = "Rut invalido"            