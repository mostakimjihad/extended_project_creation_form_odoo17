from odoo import models, fields, api


class ProjectInherit(models.Model):
    _inherit = 'project.project'

    # Adding the required fields
    file_attachment = fields.Binary(string="File Attachment")
    file_name = fields.Char(string="File Name")  # To store the name of the file
    description = fields.Html(string="Description")  # HTML editor for description
    customer_name = fields.Many2one('res.partner', string="Customer Name")  # Link to customer
    project_manager = fields.Many2one('res.users', string="Project Manager")  # Link to project manager

    @api.model
    def create(self, vals):
        # Create the project record
        project = super(ProjectInherit, self).create(vals)

        # Check if description or file is provided, and post to log note
        if vals.get('description'):
            project.message_post(body=f"Description added: {vals.get('description')}")
        if vals.get('file_attachment'):
            file_name = vals.get('file_name', 'Attachment')
            attachment = self.env['ir.attachment'].create({
                'name': file_name,
                'datas': vals.get('file_attachment'),
                'res_model': 'project.project',
                'res_id': project.id,
            })
            project.message_post(body=f"File attached: {file_name}", attachment_ids=[attachment.id])

        return project

    def write(self, vals):
        # Update the project record
        res = super(ProjectInherit, self).write(vals)

        # Post to log note if description or file is updated
        for project in self:
            if vals.get('description'):
                project.message_post(body=f"Updated Description: {vals.get('description')}")
            if vals.get('file_attachment'):
                file_name = vals.get('file_name', 'Attachment')
                attachment = self.env['ir.attachment'].create({
                    'name': file_name,
                    'datas': vals.get('file_attachment'),
                    'res_model': 'project.project',
                    'res_id': project.id,
                })
                project.message_post(body=f"Updated File: {file_name}", attachment_ids=[attachment.id])

        return res