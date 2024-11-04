from odoo import models, fields, api


class ProjectInherit(models.Model):
    _inherit = 'project.project'

    # Allow multiple file attachments
    file_attachment = fields.Many2many(
        'ir.attachment',
        string="File Attachments",
        help="Attach multiple files related to the project"
    )
    file_name = fields.Char(string="File Name")  # To store the name of the file if needed
    description = fields.Html(string="Description")  # HTML editor for description
    customer_name = fields.Many2one('res.partner', string="Customer Name")  # Link to customer
    project_manager = fields.Many2one('res.users', string="Project Manager")  # Link to project manager

    @api.model
    def create(self, vals):
        # Create the project record
        project = super(ProjectInherit, self).create(vals)

        # Check if description or files are provided, and post to log note
        if vals.get('description'):
            project.message_post(body=f"Description added: {vals.get('description')}")

        if vals.get('file_attachment'):
            attachment_ids = []
            for i in vals.get('file_attachment'):
                attachment_ids.append(i[1])
            project.message_post(body="Files attached:", attachment_ids=attachment_ids)

        return project

    def write(self, vals):
        # Update the project record
        res = super(ProjectInherit, self).write(vals)

        # Post to log note if description or files are updated
        for project in self:
            if vals.get('description'):
                project.message_post(body=f"Updated Description: {vals.get('description')}")
            if vals.get('file_attachment'):
                attachment_ids = vals.get('file_attachment')[0][2]
                project.message_post(body="New files attached:", attachment_ids=attachment_ids)

        return res
