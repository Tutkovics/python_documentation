#!/media/tutkovics/ac83ef47-9d5a-49bf-83f2-791a94dcfef7/Egyetem/Tanulási/Msc_1/Agile/python_documentation/python/bin/python

# $Id: rst2xml.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Docutils XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates Docutils-native XML from standalone '
               'reStructuredText sources.  ' + default_description)

publish_cmdline(writer_name='xml', description=description)
