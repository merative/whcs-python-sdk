# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ibm_whcs_sdk.insights_for_medical_literature as wh

def test_year_and_hits():
    year_and_hits = wh.YearAndHits(date='2008', hits=10)
    year_and_hits_diff = wh.YearAndHits(date='2008', hits=1)
    year_and_hits_same = wh.YearAndHits(date='2008', hits=10)

    assert year_and_hits.__str__() is not None
    assert year_and_hits.__eq__(year_and_hits_same)
    assert year_and_hits.__ne__(year_and_hits_diff)
