# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api
from odoo.exceptions import ValidationError



class UserInformation(models.Model):
    _name = 'user.information'
    _description = 'User Information'

    first_name = fields.Char(string="First Name", required=True)
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name", required=True)
    mobile_no = fields.Char(string="Mobile No.", required=True)  
    email = fields.Char(string="Email", required=True)  
    father_name = fields.Char(string="Father's Name")
    education = fields.Selection([
        ('btech_ece', 'BTech in ECE'),
        ('btech_cse', 'BTech in CSE'),
        ('btech_me', 'BTech in ME'),
        ('btech_ce', 'BTech in CE'),
        ('mtech', 'MTech'),
        ('phd', 'PhD'),
        ('other', 'Other'),
    ], string="Education", required=True)


    @api.constrains('email')
    def check_valid_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError("Invalid email address. Please enter a valid email.")
            

