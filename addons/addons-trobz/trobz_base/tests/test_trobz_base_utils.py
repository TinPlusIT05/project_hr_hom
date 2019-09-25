# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging

from odoo.tests.common import SavepointCase
from odoo.addons.base.tests.test_ir_actions import TestServerActionsBase

_logger = logging.getLogger(__name__)


class TestTrobzBase(SavepointCase):
    def test_01_update_config(self):
        """
        Test the function to update the settings.
        """
        _logger.info('Test trobz_base > update_config. Check General Settings '
                     '> Manage multiple companies.')
        config_model = 'base.config.settings'
        ConfigEnv = self.env[config_model]

        # update boolean field configuration
        # module_name = 'auth_oauth'
        self.env['trobz.base'].update_config(
            config_model, {
                'group_multi_company': True,
                'alias_domain': 'testlocalhost',
                # 'module_%s' % module_name:  True
            })
        # get values of config after executing
        defaults = ConfigEnv.default_get(['alias_domain'])
        print self.env.user.sudo().has_group('base.group_multi_company')
        assert self.env.user.sudo().has_group('base.group_multi_company'),\
            'trobz_base > update_config boolean field failed'
        assert defaults.get('alias_domain') == 'testlocalhost', \
            'Alias domain is wrong !'

        # domain = [('name', '=', module_name), ('state', '=', 'installed')]
        # assert self.env['ir.module.module'].search(domain),\
        #     '%s is not installed' % module_name
        # assert module_name in self.env.registry._init_modules, \
        #     'Module %s is not installed' % module_name

    def test_02_get_ean13(self):
        pattern = '893112345678'
        tbz_base_env = self.env['trobz.base']
        ean13 = tbz_base_env.get_ean13(pattern)
        assert ean13 == '%s%s' % (pattern, '3'), \
            'Trobz base > generate ean13 failed'

        check_ean13 = tbz_base_env.check_ean13(ean13)
        assert check_ean13, \
            'Trobz base > generate ean13 failed'

    def test_03_load_language(self):
        langs_to_load = 'vi_VN,fr_FR'
        self.env['ir.config_parameter'].set_param('language_to_load',
                                                  langs_to_load)
        self.env['trobz.base'].load_language()
        langs = self.env['res.lang'].search([])
        lang_codes = langs.mapped('code')
        assert 'vi_VN' in lang_codes, 'Test load lang VN failed'

    def test_04_run_post_object_one_time(self):
        ir_conf_para_env = self.env['ir.config_parameter']
        post_object_fnc = 'update_language_date_format'
        model_name = 'post.object.trobz.base'
        self.env['trobz.base']\
            .run_post_object_one_time(model_name,
                                      [post_object_fnc])
        run_functions = ir_conf_para_env.\
            get_param('List_post_object_one_time_functions', '[]')
        run_functions = eval(run_functions)
        method_run = model_name + ':' + post_object_fnc
        assert method_run in run_functions, 'Failed'


class TestServerAction(TestServerActionsBase):
    def setUp(self):
        # call super
        super(TestServerAction, self).setUp()
        self.cr.execute('SAVEPOINT test_%s' % self._testMethodName)

    def tearDown(self):
        # call super
        super(TestServerAction, self).tearDown()

        self.cr.execute('ROLLBACK TO SAVEPOINT test_%s' % self._testMethodName)
        self.env.clear()
        self.registry.clear_caches()

    def test_send_get_email_dict(self):
        """ Test ir.actions.server email type """
        email_template = self.env['mail.template'].create({
            'name': 'TestTemplate',
            'email_from': 'myself@example.com',
            'email_to': 'brigitte@example.com',
            'partner_to': '%s' % self.test_partner.id,
            'model_id': self.res_partner_model.id,
            'subject': 'About ${object.name}',
            'body_html': '<p>Dear ${object.name}, your parent is \
            ${object.parent_id and object.parent_id.name or "False"}</p>',
        })
        self.action.write({'state': 'email', 'template_id': email_template.id})
        run_res = self.action.with_context(self.context).run()
        self.assertFalse(run_res, 'ir_actions_server: email server action \
        correctly finished should return False')
        # check an email is waiting for sending
        mail = self.env['mail.mail'].search([
            ('subject', '=', 'About TestingPartner')])
        self.assertEqual(len(mail), 1, 'ir_actions_server: TODO')
        # check email content
        self.assertEqual(
            mail.body, '<p>Dear TestingPartner, your parent is False</p>',
                       'ir_actions_server: TODO')
        email = mail.send_get_email_dict()
        _logger.info(">>>>>>>>>. %s", email)
        email_to = email.get('email_to')
        assert email_to != 'noone@trobz.com', 'Failed'
