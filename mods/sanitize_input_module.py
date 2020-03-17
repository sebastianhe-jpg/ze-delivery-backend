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
    """
    cleaner xss class
    """
    def __init__(self):
        self.rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
        self.rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
        self.re_scripts = re.compile('(%s)|(%s)' % (self.rjs, self.rvb), re.IGNORECASE)
        self.valid_tags = 'p i strong b u a h1 h2 h3 pre br img type id name value '.split()
        self.valid_attrs = 'href src width height'.split()
        self.url_attrs = 'href src'.split() # Attributes which should have a URL

    def sanitize_html(self, msg):
        """
        general function, change logic depending on datatype
        :param msg:
        :return:
        """
        if isinstance(msg, str):
            msg = self.__sanitize_str(msg)
        return msg

    def __sanitize_str(self, text, base_url=None):
        """
        sanitize data when string
        :param text:
        :param base_url:
        :return:
        """
        soup = BeautifulSoup(text, features='html.parser')
        for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
            comment.extract()
        for tag in soup.findAll(True):

            if tag.name not in self.valid_tags:
                tag.hidden = True

            attrs = tag.attrs
            tag.attrs = []
            for attr, val in attrs.items():
                if attr in self.valid_attrs:
                    val = self.re_scripts.sub('', val)  # Remove scripts (vbs & js)
                    if attr in self.url_attrs:
                        val = urljoin(base_url, val)  # Calculate the absolute url
                    tag.attrs.append((attr, val))

        return soup.renderContents().decode('utf8')


def entry_clean(input_data):
    """
    clean json values from malicious code
    :param input_data:
    :return:
    """
    input_data = XssCleaner().sanitize_html(input_data)
    input_data = input_data.strip() if isinstance(input_data, str) else input_data
    return input_data
