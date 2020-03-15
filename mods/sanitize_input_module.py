# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
sanitize input module
"""
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from bs4 import Comment


class XssCleaner:

    def __init__(self):
        self.rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
        self.rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
        self.re_scripts = re.compile('(%s)|(%s)' % (self.rjs, self.rvb), re.IGNORECASE)
        self.validTags = 'p i strong b u a h1 h2 h3 pre br img type id name value '.split()
        self.validAttrs = 'href src width height'.split()
        self.urlAttrs = 'href src'.split() # Attributes which should have a URL

    def sanitize_html(self, msg):
        if isinstance(msg, str):
            return self.__sanitize_str(msg)
        if isinstance(msg, (float, int)):
            return msg

    def __sanitize_str(self, text, base_url=None):
        rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
        rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
        re_scripts = re.compile('(%s)|(%s)' % (rjs, rvb), re.IGNORECASE)
        validTags = 'p i strong b u a h1 h2 h3 pre br img type id name value '.split()
        validAttrs = 'href src width height'.split()
        urlAttrs = 'href src'.split()  # Attributes which should have a URL
        soup = BeautifulSoup(text, features='html.parser')
        for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comment.extract()
        for tag in soup.findAll(True):

            if tag.name not in validTags:
                tag.hidden = True

            attrs = tag.attrs
            tag.attrs = []
            for attr, val in attrs.items():
                if attr in validAttrs:
                    val = re_scripts.sub('', val)  # Remove scripts (vbs & js)
                    if attr in urlAttrs:
                        val = urljoin(base_url, val)  # Calculate the absolute url
                    tag.attrs.append((attr, val))

        return soup.renderContents().decode('utf8')


def entry_clean(input_data):
    """
    clean json values from malicious code
    TODO: implement data
    :param input_data:
    :return:
    """
    input_data = XssCleaner().sanitize_html(input_data)
    input_data = input_data.strip() if isinstance(input_data, str) else input_data
    return input_data
