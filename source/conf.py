# -*- coding: utf-8 -*-

import sys
import os
import shlex

extensions = [
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'DigitalOcean 導入ガイド'
copyright = u'2016, Pocketstudio.net Documentation Project'
author = u'Masahito Zembutsu'
version = '0.1.0'
release = '0.1-beta'
language = 'ja'

exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['./_themes/']
html_static_path = ['_static']
html_search_language = 'ja'
htmlhelp_basename = 'DigitalOcean-Guide'

# for sphinx-docxbuilder ( To output document with Microsoft Word Format )
extensions = ['sphinx-docxbuilder']
docx_title = u'DigitalOcean 導入ガイド'
docx_subject = 'Version 0.1.0'
docx_descriptions = 'https://github.com/zembutsu/digitalocean-doc'
docx_creator = 'Masahito Zembutsu <m.zembutsu@gmail.com> (@zembutsu)'
docx_keywords = ['Sphinx', 'OpenXML']
docx_style= '/home/zembutsu/Desktop/DigitalOcean/digitalocean-doc/style.docx'

