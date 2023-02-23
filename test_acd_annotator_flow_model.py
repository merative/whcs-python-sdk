# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_AnnotatorFlow_model():
    flow_data = wh.Flow()
    model = wh.AnnotatorFlow(profile="mine", flow=flow_data)
    assert model.__str__() is not None