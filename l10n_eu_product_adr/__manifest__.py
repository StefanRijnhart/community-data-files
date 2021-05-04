# Copyright 2019 Camptocamp SA
# Copyright 2021 Opener B.V.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "ADR Dangerous Goods",
    "summary": "Allows to set appropriate danger class and components",
    "version": "14.0.1.0.0",
    "category": "Inventory/Delivery",
    "website": "https://github.com/OCA/community-data-files",
    "author": "Opener B.V., Camptocamp, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["product", "stock"],
    "development_status": "Beta",
    "data": [
        "data/adr_class.xml",
        "data/adr_label.xml",
        "data/adr_goods.xml",
        "views/adr_class.xml",
        "views/adr_goods.xml",
        "views/adr_label.xml",
        "views/menu.xml",
        "security/ir.model.access.csv",
        "views/product_template_view.xml",
    ],
}
