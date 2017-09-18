import unittest
from apps.helpers.url_decomposer import decompose_inner_path

class URLDecomposerTestCase(unittest.TestCase):
    def test_decompose_inner_path(self):
        assert decompose_inner_path('rog') == {
            'rate': 'rog',
            'agg': None,
            'start': None,
            'end': None
        }
        assert decompose_inner_path('yoy/') == {
            'rate': 'yoy',
            'agg': None,
            'start': None,
            'end': None
        }
        assert decompose_inner_path('avg/1991/') == {
            'rate': None,
            'agg': 'avg',
            'start': '1991',
            'end': None
        }
        assert decompose_inner_path('base/1998/2017') == {
            'rate': 'base',
            'agg': None,
            'start': '1998',
            'end': '2017'
        }

        # FIXME: the test below must fail
        # assert decompose_inner_path('yoy/eop/1998/2000/csv') == {
        #     'rate': 'yoy',
        #     'agg': 'eop',
        #     'start': '1998',
        #     'end': '2000'
        # }
