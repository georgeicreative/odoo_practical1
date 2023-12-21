from odoo import api, models, fields


class salp(models.Model):
    _inherit = "res.partner"

    vendor_type = fields.Many2one('res.partner.vendor.type',string='Vendor Type')
