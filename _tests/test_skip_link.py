"""Offline structural regressions for the shared layout's keyboard skip link.

Run: python -m unittest discover -s _tests -v
These checks inspect template structure; they do not emulate a browser or Jekyll.
"""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class Elements(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.elements = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class SkipLinkTests(unittest.TestCase):
    def setUp(self):
        self.layout = (ROOT / '_layouts/default.html').read_text()
        # Include the actual navigation/footer in document order, without
        # evaluating Liquid expressions or loading any external resources.
        markup = re.sub(
            r'{%-?\s*include\s+(\S+)\s*-?%}',
            lambda match: (ROOT / '_includes' / match[1]).read_text(),
            self.layout,
        )
        self.elements = Elements(markup).elements
        self.skip_links = [attrs for tag, attrs in self.elements
                           if tag == 'a' and 'skip-link' in attrs.get('class', '').split()]

    def test_exactly_one_skip_link(self):
        self.assertEqual(len(self.skip_links), 1)

    def test_skip_link_is_first_body_element(self):
        body = next(i for i, (tag, _) in enumerate(self.elements) if tag == 'body')
        tag, attrs = self.elements[body + 1]
        self.assertEqual(tag, 'a')
        self.assertIn('skip-link', attrs.get('class', '').split())

    def test_skip_target_is_unique_focusable_main_landmark(self):
        href = self.skip_links[0]['href']
        self.assertTrue(href.startswith('#'))
        targets = [(tag, attrs) for tag, attrs in self.elements
                   if attrs.get('id') == href[1:]]
        self.assertEqual(len(targets), 1)
        tag, attrs = targets[0]
        self.assertEqual(tag, 'main')
        self.assertEqual(attrs.get('tabindex'), '-1')

    def test_home_posts_and_archive_share_default_layout(self):
        for name in ('_layouts/home.html', '_layouts/post.html', 'archive.html'):
            with self.subTest(template=name):
                front_matter = (ROOT / name).read_text().split('---')[1]
                self.assertRegex(front_matter, r'(?m)^layout:\s*default\s*$')


if __name__ == '__main__':
    unittest.main()
