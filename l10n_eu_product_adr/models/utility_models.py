# Copyright 2020 Iryna Vyshnevska (Camptocamp)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
from odoo import fields, models


class DangerousUOM(models.Model):
    _name = "dangerous.uom"
    _description = "Dangerous UOM"

    name = fields.Char(string="Name", required=True, translate=True)


class Great(models.Model):
    _name = "great.class"
    _description = "Great"

    name = fields.Char(string="Name", required=True)


class LimitedAmount(models.Model):
    _name = "limited.amount"
    _description = "Limited Amount"

    name = fields.Char(string="Name", required=True)


class StorageClass(models.Model):
    _name = "storage.class"
    _description = "Storage class"

    name = fields.Char(string="Name", required=True)


class PackagingType(models.Model):
    _name = "packaging.type"
    _description = "Packaging"

    name = fields.Char(string="Name", required=True)


class StorageTemp(models.Model):
    _name = "storage.temp"
    _description = "Storage Temp"

    name = fields.Char(string="Name", required=True, translate=True)


class DangerousGoods(models.Model):
    _name = "dangerous.goods"
    _description = "Dangerous Goods"

    name = fields.Char(string="Name", required=True)


class WGKClass(models.Model):
    _name = "wgk.class"
    _description = "WGK class"

    name = fields.Char(string="Name", required=True)
