# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import (
    get_default_location_from_resource_group,
    validate_file_or_dict
)
from azext_elastic.action import AddFilteringTags


def load_arguments(self, _):

    with self.argument_context('elastic monitor list') as c:
        c.argument('resource_group_name', resource_group_name_type)

    with self.argument_context('elastic monitor show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('elastic monitor create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')
        c.argument('tags', tags_type)
        c.argument('location', arg_type=get_location_type(self.cli_ctx), required=False,
                   validator=get_default_location_from_resource_group)
        c.argument('provisioning_state', arg_type=get_enum_type(['Accepted', 'Creating', 'Updating', 'Deleting',
                                                                 'Succeeded', 'Failed', 'Canceled', 'Deleted',
                                                                 'NotSpecified']), help='Provisioning state of the '
                   'monitor resource.')
        c.argument('monitoring_status', arg_type=get_enum_type(['Enabled', 'Disabled']), help='Flag specifying if the '
                   'resource monitoring is enabled or disabled.')
        c.argument('elastic_properties', type=validate_file_or_dict, help='Elastic cloud properties. Expected value: '
                   'json-string/json-file/@json-file.')
        c.argument('user_info', type=validate_file_or_dict, help='User information. Expected value: '
                   'json-string/json-file/@json-file.')
        c.argument('sku', type=str, help='Name of the SKU.', arg_group='Sku')

    with self.argument_context('elastic monitor update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')
        c.argument('tags', tags_type)

    with self.argument_context('elastic monitor delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('elastic monitor list-deployment-info') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')

    with self.argument_context('elastic monitor list-resource') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')

    with self.argument_context('elastic monitor list-vm-host') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')

    with self.argument_context('elastic monitor list-vm-ingestion-detail') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name')

    with self.argument_context('elastic monitor update-vm-collection') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')
        c.argument('vm_resource_id', type=str, help='ARM id of the VM resource.')
        c.argument('operation_name', arg_type=get_enum_type(['Add', 'Delete']), help='Operation to be performed for '
                   'given VM.')

    with self.argument_context('elastic monitor wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', options_list=['--name', '-n', '--monitor-name'], type=str, help='Monitor resource '
                   'name', id_part='name')

    with self.argument_context('elastic monitor tag-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')

    with self.argument_context('elastic monitor tag-rule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Tag Rule Set resource name', id_part='child_name_1')

    with self.argument_context('elastic monitor tag-rule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name')
        c.argument('rule_set_name', type=str, help='Tag Rule Set resource name')
        c.argument('provisioning_state', arg_type=get_enum_type(['Accepted', 'Creating', 'Updating', 'Deleting',
                                                                 'Succeeded', 'Failed', 'Canceled', 'Deleted',
                                                                 'NotSpecified']), help='Provisioning state of the '
                   'monitoring tag rules.')
        c.argument('send_aad_logs', arg_type=get_three_state_flag(), help='Flag specifying if AAD logs should be sent '
                   'for the Monitor resource.', arg_group='Log Rules')
        c.argument('send_subscription_logs', arg_type=get_three_state_flag(), help='Flag specifying if subscription '
                   'logs should be sent for the Monitor resource.', arg_group='Log Rules')
        c.argument('send_activity_logs', arg_type=get_three_state_flag(), help='Flag specifying if activity logs from '
                   'Azure resources should be sent for the Monitor resource.', arg_group='Log Rules')
        c.argument('filtering_tags', action=AddFilteringTags, nargs='+', help='List of filtering tags to be used for '
                   'capturing logs. This only takes effect if SendActivityLogs flag is enabled. If empty, all '
                   'resources will be captured. If only Exclude action is specified, the rules will apply to the list '
                   'of all available resources. If Include actions are specified, the rules will only include '
                   'resources with the associated tags.', arg_group='Log Rules')

    with self.argument_context('elastic monitor tag-rule update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Tag Rule Set resource name', id_part='child_name_1')
        c.argument('provisioning_state', arg_type=get_enum_type(['Accepted', 'Creating', 'Updating', 'Deleting',
                                                                 'Succeeded', 'Failed', 'Canceled', 'Deleted',
                                                                 'NotSpecified']), help='Provisioning state of the '
                   'monitoring tag rules.')
        c.argument('send_aad_logs', arg_type=get_three_state_flag(), help='Flag specifying if AAD logs should be sent '
                   'for the Monitor resource.', arg_group='Log Rules')
        c.argument('send_subscription_logs', arg_type=get_three_state_flag(), help='Flag specifying if subscription '
                   'logs should be sent for the Monitor resource.', arg_group='Log Rules')
        c.argument('send_activity_logs', arg_type=get_three_state_flag(), help='Flag specifying if activity logs from '
                   'Azure resources should be sent for the Monitor resource.', arg_group='Log Rules')
        c.argument('filtering_tags', action=AddFilteringTags, nargs='+', help='List of filtering tags to be used for '
                   'capturing logs. This only takes effect if SendActivityLogs flag is enabled. If empty, all '
                   'resources will be captured. If only Exclude action is specified, the rules will apply to the list '
                   'of all available resources. If Include actions are specified, the rules will only include '
                   'resources with the associated tags.', arg_group='Log Rules')
        c.ignore('body')

    with self.argument_context('elastic monitor tag-rule delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Tag Rule Set resource name', id_part='child_name_1')

    with self.argument_context('elastic monitor tag-rule wait') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('monitor_name', type=str, help='Monitor resource name', id_part='name')
        c.argument('rule_set_name', type=str, help='Tag Rule Set resource name', id_part='child_name_1')
