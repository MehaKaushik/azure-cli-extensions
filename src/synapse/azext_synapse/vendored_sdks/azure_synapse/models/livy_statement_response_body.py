# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LivyStatementResponseBody(Model):
    """LivyStatementResponseBody.

    :param id:
    :type id: int
    :param code:
    :type code: str
    :param state:
    :type state: str
    :param output:
    :type output: ~azure.synapse.models.LivyStatementOutput
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'code': {'key': 'code', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'output': {'key': 'output', 'type': 'LivyStatementOutput'},
    }

    def __init__(self, **kwargs):
        super(LivyStatementResponseBody, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.code = kwargs.get('code', None)
        self.state = kwargs.get('state', None)
        self.output = kwargs.get('output', None)