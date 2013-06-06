# constants.py
# -*- coding: utf-8 -*-

IMG_API_NS='http://library.stanford.edu/iiif/image-api/ns/'

COMPLIANCE='http://library.stanford.edu/iiif/image-api/compliance.html#level1'

__formats = (
	('png','image/png'),
	('tif','image/tiff'),
	('jp2','image/jp2'),
	('jpg','image/jpeg')
)

FORMATS_BY_EXTENSION = dict(__formats)

FORMATS_BY_MEDIA_TYPE = dict([(f[1],f[0]) for f in __formats])

DERIV_FORMATS_SUPPORTED = (
	FORMATS_BY_EXTENSION['png'],
	FORMATS_BY_EXTENSION['jpg']
)

SRC_FORMATS_SUPPORTED = (
	FORMATS_BY_MEDIA_TYPE['image/jpeg'],
	FORMATS_BY_MEDIA_TYPE['image/jp2'],
	FORMATS_BY_MEDIA_TYPE['image/tiff']
)

BITONAL = 'bitonal'
COLOR = 'color'
GREY = 'grey'
NATIVE = 'native'
QUALITIES = (BITONAL, COLOR, GREY, NATIVE)