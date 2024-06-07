# -*- coding: utf-8 -*-
{
    'name': "tnc_user_info",
    'summary': "Stores user's personal info",
    'sequence':'2',
    'description': "Stores user's personal info",
    'author': "TraceNcode Technologies",
    'website': "https://www.tracencode.com",
    'category': 'Uncategorized',
    'version': '17.0.0.0.1',
    'depends': ['website'],

    'data': [
        # 'security/ir.model.access.csv',
        'data/website_menus.xml',
        'views/submit.xml',
        'views/userform.xml',
        'views/userviews.xml',
    ],
      'assets': {
        'web.assets_backend': [
            
        ],
        'web.assets_frontend': [
           'tnc_user_info/static/src/css/user.css',
        ]
    },

   
}

