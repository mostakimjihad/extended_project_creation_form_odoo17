# -*- coding: utf-8 -*-
# from odoo import http


# class MhlProjectManagement(http.Controller):
#     @http.route('/mhl_project_management/mhl_project_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mhl_project_management/mhl_project_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mhl_project_management.listing', {
#             'root': '/mhl_project_management/mhl_project_management',
#             'objects': http.request.env['mhl_project_management.mhl_project_management'].search([]),
#         })

#     @http.route('/mhl_project_management/mhl_project_management/objects/<model("mhl_project_management.mhl_project_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mhl_project_management.object', {
#             'object': obj
#         })

