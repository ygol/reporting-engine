# Copyright 2015-2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


def uninstall_hook(cr, registry):
    # delete dirty data that could cause problems
    # while re-installing the module
    cr.execute("""
        delete from ir_model where model like 'x_bve.%'
    """)
    cr.execute("""
        delete from bve_view where model_name like 'x_bve.%'
        """)
