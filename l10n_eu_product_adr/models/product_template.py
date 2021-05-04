# Copyright 2019 Iryna Vyshnevska (Camptocamp)
# Copyright 2021 Opener B.V. <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_dangerous = fields.Boolean(help="This product belongs to a dangerous class")
    adr_goods_id = fields.Many2one("adr.goods", "Dangerous Goods")
    adr_class_id = fields.Many2one(
        "adr.class", related="adr_goods_id.class_id", readonly=True
    )
    adr_classification_code = fields.Char(
        related="adr_goods_id.classification_code", readonly=True
    )
    adr_label_ids = fields.Many2many(
        "adr.label", related="adr_goods_id.label_ids", readonly=True
    )
    adr_transport_category = fields.Selection(
        related="adr_goods_id.transport_category", readonly=True
    )
    adr_tunnel_restriction_code = fields.Selection(
        related="adr_goods_id.tunnel_restriction_code", readonly=True
    )

    @api.onchange("is_dangerous")
    def onchange_is_dangerous(self):
        """Remove the dangerous goods attribute from the product

        (when is_dangerous is deselected)
        """
        if self.is_dangerous and self.adr_goods_id:
            self.adr_goods_id = False
