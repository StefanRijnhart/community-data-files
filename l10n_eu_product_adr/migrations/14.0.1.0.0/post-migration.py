# Copyright 2021 Opener B.V. <stefan@opener.amsterdam>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)


def migrate(cr, version):
    """Basic migration from previous version"""
    cr.execute(
        """
        SELECT column_name
        FROM information_schema.columns
        WHERE table_name='product_template' and column_name='un_ref'
        """
    )
    if cr.fetchone():
        cr.execute(
            """
            UPDATE product_template pt
            SET adr_goods_id = ag.id
            FROM adr_goods ag WHERE pt.un_ref = ag.un_number
            """
        )
