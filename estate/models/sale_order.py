from odoo import api, models, _, fields
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    def action_confirm(self):
        
        res = super().action_confirm()
        
        event = self.env['calendar.event'].create({
            'name': self.name,
            'start': self.training_date,
            'stop': self.training_date,
            'allday': True,
            'partner_id': self.partner_id.id,
            'employee_id': self.employee_id.id,
            'description' : self.description,
        })
        
        return res
