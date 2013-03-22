#!/usr/bin/env python
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  author: terry.yinzhe@gmail.com
#

import unittest
from dub import translateTraceList
import re
from utility import assertTypeOFTranslatedLine

class TranslatorTest(unittest.TestCase):
    def testTranslateEmptyList(self):
        traceList = translateTraceList([])
        self.assertEquals([], traceList)


    def testTranslateTraceBack(self):
        traceList = translateTraceList(['Traceback (most recent call last):\n'])
        self.assertRegexpMatches(traceList[0], re.escape('Traceback (most recent call last):'))
        assertTypeOFTranslatedLine(self, traceList[1], 'Traceback')


    def testTranslateErrorWithArgument(self):
        line = translateTraceList(["NameError: name 'xxx' is not defined\n"])[1]
        assertTypeOFTranslatedLine(self, line, 'NameError')
        self.assertIn('xxx', line)