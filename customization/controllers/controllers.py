# -*- coding: utf-8 -*-
# from odoo import http


# class Customization(http.Controller):
#     @http.route('/customization/customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customization/customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customization.listing', {
#             'root': '/customization/customization',
#             'objects': http.request.env['customization.customization'].search([]),
#         })

#     @http.route('/customization/customization/objects/<model("customization.customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customization.object', {
#             'object': obj
#         })
