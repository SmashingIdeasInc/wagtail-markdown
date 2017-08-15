import unittest

from wagtailmarkdown.utils import render

class RenderTests(unittest.TestCase):
    def test_simple_render(self):
        self.assertEqual(render('test'), '<p>test</p>')

    def test_code_fence_plain(self):
        actual = render('```\nx=4\n```')
        expected = '<div class="codehilite"><pre><span></span>x=4\n</pre></div>'
        self.assertEqual(expected, actual)

    def test_code_fence_with_classname(self):
        term = 'fancy_css_class'
        config = {'extension_configs': {'codehilite': [('css_class', term)]}}
        expected = '<div class="{}">'.format(term)
        actual = render('```\nx=4\n```', markdown_custom=config)

        self.assertTrue(expected in actual)

    def test_code_fence_with_linenumbers(self):
        config = {'extension_configs': {'codehilite': [('linenums', True)]}}
        expected ='<div class="linenodiv"><pre>1</pre></div>'
        actual = render('```\nx=4\n```', markdown_custom=config)

        self.assertTrue(expected in actual)

    def test_code_fence_with_linenumbers_and_classname(self):
        term = 'fancy_css_class'
        config = {'extension_configs': {'codehilite': [('linenums', True), ('css_class', term)]}}
        expected_linenums = '<div class="linenodiv"><pre>1</pre></div>'
        expected_cssclass = '<div class="fancy_css_class">'.format(term)
        actual = render('```\nx=4\n```', markdown_custom=config)


        self.assertTrue(expected_linenums in actual)
        self.assertTrue(expected_cssclass in actual)

if __name__ == '__main__':
    unittest.main()
