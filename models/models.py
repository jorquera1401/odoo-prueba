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


    @api.onchange('name')
    def _setear_descripcion(self):
        self.description = self.name

class Carrera(models.Model):
    _name='prueba.carrera'
    _description='Carrera Test'

    name = fields.Char('Nombre',required=True)
    
 

    

# class prueba(models.Model):
#     _name = 'prueba.prueba'
#     _description = 'prueba.prueba'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
