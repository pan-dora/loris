#-*- coding: utf-8 -*-

from os.path import exists
from os.path import islink
from os.path import isfile
from os.path import join
from urllib import unquote
from loris import img, img_info
import loris_t


"""
Image and ImageCache tests. This may need to be modified if you change the resolver
implementation. To run this test on its own, do:

$ python -m unittest tests.img_t

from the `/loris` (not `/loris/loris`) directory.
"""

class Test_ImageCache(loris_t.LorisTest):

    def test_cache_entry_added(self):

        ident = self.test_jp2_color_id
        request_path = '/%s/full/pct:10/0/default.jpg' % (ident,)
        self.client.get(request_path)

        # the canonical path
        rel_cache_path = '%s/full/590,/0/default.jpg' % (unquote(ident),)
        expect_cache_path = join(self.app.img_cache.cache_root, rel_cache_path)

        self.assertTrue(exists(expect_cache_path))

    def test_symlink_added(self):
        ident = self.test_jp2_color_id
        params = 'full/pct:10/0/default.jpg'
        request_path = '/%s/%s' % (ident, params)

        self.client.get(request_path)

        # the symlink path
        rel_cache_path = '%s/%s' % (unquote(ident), params)
        expect_symlink = join(self.app.img_cache.cache_root, rel_cache_path)

        self.assertTrue(islink(expect_symlink))

    def test_canonical_requests_cache_at_canonical_path(self):
        ident = self.test_jp2_color_id
        # This is a canonical style request
        request_path = '%s/full/202,/0/default.jpg' % (ident,)
        self.client.get('/%s' % (request_path,))

        rel_cache_path = '%s/full/202,/0/default.jpg' % (unquote(ident),)
        expect_cache_path = join(self.app.img_cache.cache_root, rel_cache_path)

        self.assertTrue(exists(expect_cache_path))
        self.assertFalse(islink(expect_cache_path))

    def test_cache_dir_already_exists(self):
        ident = 'id1'
        image_info = img_info.ImageInfo()
        image_info.width = 100
        image_info.height = 100
        image_request = img.ImageRequest(ident, 'full', 'full', '0', 'default', 'jpg')
        image_request.info = image_info
        self.app.img_cache.create_dir_and_return_file_path(image_request)
        #call request again, so cache directory should already be there
        # throws an exception if we don't handle that existence properly
        self.app.img_cache.create_dir_and_return_file_path(image_request)


def suite():
    import unittest
    test_suites = []
    test_suites.append(unittest.makeSuite(Test_ImageCache, 'test'))
    test_suite = unittest.TestSuite(test_suites)
    return test_suite
