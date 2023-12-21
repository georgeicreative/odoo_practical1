{
    'name':'practical1',
    'author':'George',
    'website':'www.oddopractical.com',
    'depends':['crm','purchase','base'],
    'data':[

        'security/ir.model.access.csv',
        'views/crm_lead.xml',
        'views/crm_stage.xml',
        'views/vendor_type.xml',
        'views/rec_partner.xml',
        'views/purchase.xml'
    ],
    'installable':True,
    'application':True,
    'license':'LGPL-3',

}