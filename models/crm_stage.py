from odoo import api,fields,models

class CrmSatge(models.Model):
    _inherit='crm.stage'


    is_quote_ready_stage=fields.Boolean(string='Is Quote Ready Satge',default=False)


