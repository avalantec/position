# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
log = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    carrier_id = fields.Many2one('res.partner', string="Carrier",store = True)
    category_id = fields.Many2one('product.category', string="Categoría",store = True)
    ship_from_id = fields.Many2one('res.partner', string="Ship From",store = True)
    incoterm_id_code = fields.Char(related="incoterm_id.code", string="Incoterm Code")