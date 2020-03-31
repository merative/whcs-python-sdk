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

def test_concept_model():
    props = []
    props = 'test'
    parent_count = wh.Count()
    child_count = wh.Count()
    sibling_count = wh.Count()
    related_count = wh.Count()
    doc_ids = []
    doc_ids.append('test')

    concept = wh.Concept(
        ontology='test',
        cui='test',
        preferred_name='test',
        alternative_name='test',
        semantic_type='test',
        count=5,
        hit_count=0,
        idf=0.7,
        score=0.7,
        parents=parent_count,
        children=child_count,
        siblings=sibling_count,
        related=related_count,
        document_ids=doc_ids,
        data_type='test',
        unit='test',
        operator='test',
        min_value='test',
        max_value='test',
        vocab='test',
        properties=props
    )

    concept_diff = wh.Concept(
        ontology='test',
        cui='test',
        preferred_name='test',
        alternative_name='test',
        semantic_type='test',
        count=5
    )

    concept_same = wh.Concept(
        ontology='test',
        cui='test',
        preferred_name='test',
        alternative_name='test',
        semantic_type='test',
        count=5
    )

    assert concept.__str__() is not None
    assert concept_diff.__eq__(concept_same)
    assert concept.__ne__(concept_diff)
