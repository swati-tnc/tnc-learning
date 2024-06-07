# -*- coding: utf-8 -*-
# from odoo import http


# class TncSalePurchase(http.Controller):
#     @http.route('/tnc_sale_purchase/tnc_sale_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tnc_sale_purchase/tnc_sale_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tnc_sale_purchase.listing', {
#             'root': '/tnc_sale_purchase/tnc_sale_purchase',
#             'objects': http.request.env['tnc_sale_purchase.tnc_sale_purchase'].search([]),
#         })

#     @http.route('/tnc_sale_purchase/tnc_sale_purchase/objects/<model("tnc_sale_purchase.tnc_sale_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tnc_sale_purchase.object', {
#             'object': obj
#         })

