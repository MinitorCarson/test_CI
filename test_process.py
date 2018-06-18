import unittest
import resize_pic



class TestDict(unittest.TestCase):

    def test_init(self):
        #a=process_pic.generate_colorpic('get','re')
        a=resize_pic.pre_process('get')
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

    def test_attr2(self):
        print 'Finish  all'
        #d = Dict()
        #d.key = 'value'
        #self.assertTrue('key' in d)
        #self.assertEquals(d['key'], 'value')

