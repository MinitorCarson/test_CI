import unittest
import process_pic



class TestDict(unittest.TestCase):

    def test_init(self):
        a=process_pic.generate_colorpic('get','re')
        #d = Dict(a=1, b='test')
        self.assertEqual(a, 1)
        #self.assertEquals(d.b, 'test')
        #self.assertTrue(isinstance(d, dict))

    def test_attr(self):
        m=9
        #d = Dict()
        #d.key = 'value'
        #self.assertTrue('key' in d)
        #self.assertEquals(d['key'], 'value')

