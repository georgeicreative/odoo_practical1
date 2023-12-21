from odoo import api, fields, models


class VendorType(models.Model):
    _name = 'res.partner.vendor.type'





    name = fields.Char(string='name' ,store=True)
    Description = fields.Char(srting='Description')




