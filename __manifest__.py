# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Web POS Conf',
    'version': '1.0',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config.xml'
    ],
    'assets': {
        'point_of_sale.assets': [
            'wb_pos_config/static/src/js/web_simple_button.js',
            'wb_pos_config/static/src/xml/sample_button.xml',
            ],
    }
}
