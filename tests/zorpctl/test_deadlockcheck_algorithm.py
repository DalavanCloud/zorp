#!/usr/bin/env python2.7

############################################################################
##
## Copyright (c) 2000-2015 BalaBit IT Ltd, Budapest, Hungary
## Copyright (c) 2015-2018 BalaSys IT Ltd, Budapest, Hungary
##
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License along
## with this program; if not, write to the Free Software Foundation, Inc.,
## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
##
############################################################################

import unittest
from HandlerMock import HandlerMock
from zorpctl.szig import SZIG
from zorpctl.ProcessAlgorithms import DeadlockCheckAlgorithm

class TestDeadLockCheckAlgorithm(unittest.TestCase):

    def setUp(self):
        handler_mock = HandlerMock
        szig = SZIG("", handler_mock)
        self.algorithm = DeadlockCheckAlgorithm()
        self.algorithm.szig = szig

    def test_get_deadlock_check(self):
        self.assertTrue(self.algorithm.getDeadlockcheck())

    def test_set_deadlock_check(self):
        self.assertTrue(self.algorithm.setDeadlockcheck(True))
        self.assertEquals(str(self.algorithm.getDeadlockcheck()), "deadlockcheck=True")
        self.assertTrue(self.algorithm.setDeadlockcheck(False))
        self.assertEquals(str(self.algorithm.getDeadlockcheck()), "deadlockcheck=False")

if __name__ == '__main__':
    unittest.main()
