# -*- coding: utf-8 -*-
"""
Rúbia Reis Guerra
rubia-rg@github
Test cases for extracting parameters with HTMLParser
"""
import unittest

from lxml import etree
from formparser import HTMLParser, HTMLExtractor
from formparser import utils

PORTAL_COMPRAS = 'https://www1.compras.mg.gov.br/processocompra/processo/consultaProcessoCompra.html'
TEST_FORM_FIELD = {'type': 'text', 'name': 'codigoUnidadeCompra', 'maxlength': '7', 'size': '', 'value': '',
                   'onkeydown': ' return IsNumericKey(event, false);', 'onkeyup':
                       'return numericMask(this,0,7,false, event, false );testarBackspaceEDelete();',
                   'onkeypress': 'campoAlterado();', 'onchange': 'campoAlterado();',
                   'onblur': 'numericValidate(this,0,7,false,false);', 'id': 'codigoUnidadeCompra', 'class': ''}

HTML = HTMLExtractor(PORTAL_COMPRAS)
Form = HTMLParser(HTML.get_forms()[0])


class TestPortalCompras(unittest.TestCase):
    def test_request_headers(self):
        headers = utils.request_headers()
        self.assertIn(headers['User-Agent'], utils.USER_AGENT_LIST)

    def test_html_response(self):
        self.assertEqual(HTML.html_response.status_code, 200)

    def test_html_text(self):
        self.assertIsInstance(HTML.html_text(), str)

    def test_html_content(self):
        self.assertIsInstance(HTML.html_content(), bytes)

    def test_get_etree(self):
        self.assertIsInstance(HTML.get_etree(), etree._Element)

    def test_get_forms(self):
        self.assertIsInstance(HTML.get_forms(), list)

    def test_number_of_forms(self):
        self.assertIs(len(HTML.get_forms()), 1)

    def test_check_for_string(self):
        self.assertIs(HTML.check_for_string('Ocultar pesquisa'), True)


class TestFormPortalCompras(unittest.TestCase):
    def test_list_field_types(self):
        self.assertListEqual(sorted(list(Form.list_field_types())), sorted(['checkbox', 'hidden', 'text']))

    def test_required_fields(self):
        self.assertEqual(Form.required_fields(), [])

    def test_fields(self):
        self.assertEqual(sum([len(Form.fields()[key]) for key in Form.fields().keys()]), Form.get_number_fields())

    def test_select_fields(self):
        self.assertEqual(len(Form.select_fields()), 10)

    def test_option_fields(self):
        self.assertEqual(len(Form.option_fields()), 122)

    def test_select_fields_with_options(self):
        num_options = sum([len(Form.select_with_option_fields()[key])
                           for key in Form.select_with_option_fields().keys()])
        num_selects = len(Form.select_with_option_fields().keys())
        self.assertEqual((num_selects, num_options), (10, 122))

    def test_list_field_attributes(self):
        field = Form.fields()['text'][0]
        self.assertEqual(Form.list_field_attributes(field), TEST_FORM_FIELD)


if __name__ == '__main__':
    unittest.main()
