from odoo import api,fields,models

class CrmQuoet(models.Model):
    _inherit='crm.lead'

    import_quote_status=fields.Selection([('import_quote_request','Import Quote Requested'),
                                          ('import_quote_ready','Import Quote Ready'),
                                          ('import_quote_submitted','Import Quote Submitted'),
                                          ('import_quote_revision_request','Import Quote Revision Request')],string='Import Quote Status')

    domestic_quote_status=fields.Selection([('domestic_quote_request','Domestic Quote Requested'),
                                            ('domestic_quote_ready','Domestic Quote Ready'),
                                            ('domestic_quote_submitted','Domestic Quote Submitted'),
                                            ('domestic_quote_revision_request','Domestic Quote Revision Request')],string='Domestic Quote Status',readonly=False)


    @api.onchange('import_quote_status','domestic_quote_status')
    def _onchange_change_status(self):
        if (self.domestic_quote_status==False):
            if(self.import_quote_status=='import_quote_ready'):
                x=self.env['crm.stage'].search([('name','=','Quote Ready')])
                self.stage_id=x
        elif(self.import_quote_status==False):
            if(self.domestic_quote_status=='domestic_quote_status'):
                x=self.env['crm.stage'].search([('is_quote_ready_stage','=',True)])
                self.stage_id=x
        elif(self.import_quote_status=='import_quote_ready'):
            if(self.domestic_quote_status=='domestic_quote_status'):
                x=self.env['crm.stage'].search([('is_quote_ready_stage','=',True)])
                self.stage_id=x
