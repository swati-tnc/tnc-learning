# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class UserInfo(http.Controller):
    @http.route('/webform', auth='public', website=True)
    def web_form(self,**kw):
        return request.render('tnc_user_info.user_information')
    

    @http.route('/webform/submit', type='http', auth="public", website=True, methods=['POST'])
    def web_form_submit(self, **post):
        request.env['user.information'].sudo().create({
                    'first_name': post.get('first_name'),
                    'middle_name': post.get('middle_name'),
                    'last_name': post.get('last_name'),
                    'mobile_no': post.get('mobile_no'),
                    'email': post.get('email'),
                    'father_name': post.get('father_name'),
                    'education': post.get('education'),
 
               })
        return request.redirect('/thank-you')
    
    @http.route('/thank-you', type='http', auth='public', website=True)
    def thank_you_page(self, **kw):
        return http.request.render('tnc_user_info.user_form_success', {})
