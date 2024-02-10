Continuous Integration and Deployment
=====================================

.. image:: https://github.com/tanayseven/personal-website/actions/workflows/main.yml/badge.svg
    :target: https://github.com/tanayseven/personal-website/actions/workflows/main.yml
    :alt: CI

.. image:: https://img.shields.io/website?url=https%3A%2F%2Fblog.tanay.tech
    :target: https://blog.tanay.tech
    :alt: Website

.. image:: https://img.shields.io/github/license/tanayseven/personal-website
    :target: https://github.com/tanayseven/personal-website/blob/main/LICENSE.txt
    :alt: GitHub License

.. image:: https://img.shields.io/twitter/follow/tanayseven
    :target: https://twitter.com/tanayseven
    :alt: X (formerly Twitter) Follow

Website Performance Report (Lighthouse)
=======================================

.. image:: https://blog.tanay.tech/test_results/lighthouse_best-practices.svg
    :target: https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fblog.tanay.tech%2F&strategy=mobile&category=best-practices&utm_source=lh-chrome-ext
    :alt: Best Practices

.. image:: https://blog.tanay.tech/test_results/lighthouse_performance.svg
    :target: https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fblog.tanay.tech%2F&strategy=mobile&category=performance&utm_source=lh-chrome-ext
    :alt: Performance

.. image:: https://blog.tanay.tech/test_results/lighthouse_accessibility.svg
    :target: https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fblog.tanay.tech%2F&strategy=mobile&category=accessibility&utm_source=lh-chrome-ext
    :alt: Accessibility

.. image:: https://blog.tanay.tech/test_results/lighthouse_seo.svg
    :target: https://googlechrome.github.io/lighthouse/viewer/?psiurl=https%3A%2F%2Fblog.tanay.tech%2F&strategy=mobile&category=seo&utm_source=lh-chrome-ext
    :alt: SEO

Static Website Generator
========================

.. image:: personal_site.png
    :alt: Personal website picture

This repository is a static website that is a small yet powerful static website generator.
The pages are written using `reStructured`_ text and built using `Sphinx`_.
A very good reason for choosing reStructured text was to use the power of directives and not insert HTML
tags within Markdown. If I had to write some things in HTML, I'd write everything in HTML;
but that would not be very readable, would it? The blog was initially to be enabled by simply
using the `ablog`_ sphinx extension. The problem that I encountered with that is that it did not work
with my favourite Sphinx theme `Furo`_. In order to counter that I thought of writing my own plugin to
build it into blog format.


.. _reStructured: https://en.wikipedia.org/wiki/ReStructuredText

.. _Sphinx: https://www.sphinx-doc.org/en/master/

.. _ablog: https://ablog.readthedocs.io/

.. _Furo: https://pradyunsg.me/furo/

Inspired from the following websites:

1.  `errbufferoverfl`_
2.  `Doug Hellmann`_

.. _errbufferoverfl: https://www.errbufferoverfl.me/

.. _Doug Hellmann: https://www.errbufferoverfl.me/


Tanay's Personal Website
========================

To know commands to perform any activity like build, please run ``make help`` command

LICENSE
========================

The MIT License (MIT)

Copyright (c) 2018-2024 Tanay PrabhuDesai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
