# -*- coding: utf-8 -*-
# from odoo import http


# class RondouUpdate(http.Controller):
#     @http.route('/rondou_update/rondou_update', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rondou_update/rondou_update/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rondou_update.listing', {
#             'root': '/rondou_update/rondou_update',
#             'objects': http.request.env['rondou_update.rondou_update'].search([]),
#         })

#     @http.route('/rondou_update/rondou_update/objects/<model("rondou_update.rondou_update"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rondou_update.object', {
#             'object': obj
#         })

