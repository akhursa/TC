# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ToolsControl(models.Model):
    _name = 'tools_control.tools_control'
    _description = 'tools_control.tools_control'

    action = fields.Char()
    date = fields.Char()
    area = fields.Char()
    photo = fields.Binary(
        string="Image",
        compute="_compute_image",
        store=True,
        attachment=False
    )

    @api.model
    def create(self, vals):
        vals['photo'] = vals['photo'].split(',')[1]
        return super(ToolsControl, self).create(vals)


