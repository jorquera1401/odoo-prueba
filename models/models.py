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

    @api.onchange('name')
    def _setear_descripcion(self):
        self.description = self.name

    @api.onchange('precio')
    def _calcular_impuesto(self):
        self.impuesto = self.precio*0.19
        self.total = self.precio - self.impuesto
  #  @api.one
    def calcular(self,context=None):
        precio = self.precio+self.precio*0.5
        if context is None:
            context = {'precio':precio}
        self.write(context)
 

class Carrera(models.Model):
    _name='prueba.carrera'
    _description='Carrera Test'

    nombre = fields.Char('Nombre',required=True)

 

    

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
