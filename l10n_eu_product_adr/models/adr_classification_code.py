# Copyright 2021 Stefan Rijnhart <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import fields, models


class AdrClassificationCode(models.Model):
    _name = "adr.classification.code"
    _description = "Dangerous Goods Classification Code"
    _rec_name = "code"

    code = fields.Char(required=True)

    _sql_constraints = [
        (
            "code_unique",
            "unique(code)",
            "This dangerous good classification code already exists",
        )
    ]
