# -*- coding: utf-8 -*-
from odoo import api, fields, models, _, tools


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True, translate=True)
    age = fields.Char(string='Age', required=True, translate=True)
    type = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other')
    note = fields.Text(string='Description')