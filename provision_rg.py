# Following Imports needs to be done to run the sdk.
from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os

# Can acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()

#use the subscription you want to provision resources to
sub_id="xx-xx-xx-xx"

# retrieve subscription ID from environment variable.
# subscription_id = os.environ[sub_id]

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, sub_id)

# Provision the resource group.
rg_result2 = resource_client.resource_groups.list()

# Show the groups in formatted output
column_width = 40

print("Resource Group".ljust(column_width) + "Location")
print("-" * (column_width * 2))

for group in list(rg_result2):
    print(f"{group.name:<{column_width}}{group.location}{group.tags}")

# rg_result = resource_client.resource_groups.create_or_update(
#     "PythonAzureExample-rg",
#     {
#         "location": "centralus"
#     }
# )

# Within the ResourceManagementClient is an object named resource_groups,
# which is of class ResourceGroupsOperations, which contains methods like
# create_or_update.
#
# The second parameter to create_or_update here is technically a ResourceGroup
# object. You can create the object directly using ResourceGroup(location=LOCATION)
# or you can express the object as inline JSON as shown here. For details,
# see Inline JSON pattern for object arguments at
# https://docs.microsoft.com/azure/developer/python/azure-sdk-overview#inline-json-pattern-for-object-arguments.

# print(f"Provisioned resource group {rg_result.name} in the {rg_result.location} region")

# The return value is another ResourceGroup object with all the details of the
# new group. In this case the call is synchronous: the resource group has been
# provisioned by the time the call returns.

# To update the resource group, repeat the call with different properties, such
# as tags:
rg_result = resource_client.resource_groups.create_or_update(
    "PythonAzureExample-rg",
    {
        "location": "centralus",
        "tags": { "environment":"test", "department":"tech" }
    }
)

print(f"Updated resource group {rg_result.name} with tags")

# Optional lines to delete the resource group. begin_delete is asynchronous.
# poller = resource_client.resource_groups.begin_delete(rg_result.name)
# result = poller.result()