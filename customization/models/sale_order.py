# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    license_plate = fields.Char(string="# de Placa",store = True)
    container = fields.Char(string="# CTR",store = True)
    location_src_id = fields.Many2one('res.partner', string="Source Location",store = True)
    location_dst_id = fields.Many2one('res.partner', string="Destination Location",store = True)
    category_id = fields.Many2one('product.category', string="Catgegoría",store = True)
    ship_point_id = fields.Many2one('res.partner', string="Ship Point",store = True)
    carrier_id = fields.Many2one('res.partner', string="Carrier",store = True)
    driver_id = fields.Many2one('res.partner', string="Driver",store = True)
    driver_id_phone = fields.Char(related='driver_id.phone', string="Driver Phone",store = True)
    driver_vat_id = fields.Char(related='driver_id.vat', string="Driver ID",store = True)
    import_export = fields.Selection(
        [('imp', 'Import'),
        ('exp', 'Export'),
        ('other', 'Other'), 
        ],
        required=True,
        default='other'
    )
    uninstalled_by = fields.Many2one('res.partner', string="Desinstaldo por",store = True)
