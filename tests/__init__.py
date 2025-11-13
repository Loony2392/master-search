#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite für Master Search

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
"""

import unittest

# Auto-discovery of tests
loader = unittest.TestLoader()
suite = loader.discover('.', pattern='test_*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
