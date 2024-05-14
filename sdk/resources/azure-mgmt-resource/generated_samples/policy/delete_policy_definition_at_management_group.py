# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import PolicyClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python delete_policy_definition_at_management_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PolicyClient(
        credential=DefaultAzureCredential(),
        policy_definition_name="ResourceNaming",
        policy_definition_version="POLICY_DEFINITION_VERSION",
        policy_set_definition_name="POLICY_SET_DEFINITION_NAME",
        subscription_id="SUBSCRIPTION_ID",
    )

    client.policy_definitions.delete_at_management_group(
        management_group_id="MyManagementGroup",
        policy_definition_name="ResourceNaming",
    )


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2023-04-01/examples/deletePolicyDefinitionAtManagementGroup.json
if __name__ == "__main__":
    main()
