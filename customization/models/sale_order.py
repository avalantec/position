# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Sales Order Custom"

    license_plate = fields.Char(string="# de Placa",store = True)
    container = fields.Char(string="# CTR",store = True)
    booking = fields.Char(string="# BK",store = True)
    location_src_id = fields.Many2one('res.partner', string="Source Location",store = True)
    location_dst_id = fields.Many2one('res.partner', string="Destination Location",store = True)
    category_id = fields.Many2one('product.category', string="Catgegoría",store = True)
    ship_point_id = fields.Many2one('res.partner', string="Ship Point",store = True)
    carrier_id = fields.Many2one('res.partner', string="Carrier",store = True)
    driver_id = fields.Many2one('res.partner', string="Driver",store = True)
    driver_vat_id = fields.Char(related='driver_id.vat', string="Driver ID",store = True)
    driver_id_phone = fields.Char(related='driver_id.phone', string="Driver Phone",store = True)
    import_export = fields.Selection(
        [('imp', 'Import'),
        ('exp', 'Export'),
        ('other', 'Other'), 
        ],
        required=False,
        store=True
    )
    uninstalled_by = fields.Many2one('res.partner', string="Desinstaldo por",store = True)
    
    def action_pickup_send(self):
        self.ensure_one()
        template_id = self.env['mail.template'].sudo().search([('name','=','Pick UP Order: Send by email')], limit=1).id
        
        lang = self.env.context.get('lang')

        template = self.env['mail.template'].browse(template_id)
        if template.lang:
            lang = template._render_template(template.lang, 'sale.order', self.ids[0])
        ctx = {
            'default_model': 'sale.order',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
            'proforma': self.env.context.get('proforma', False),
            'force_email': True,
            'model_description': self.with_context(lang=lang).type_name,
        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }
