import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient

# Set up the Azure API client
subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID'] 
)
compute_client = ComputeManagementClient(credentials, subscription_id)
resource_client = ResourceManagementClient(credentials, subscription_id)

# Create a new resource group
resource_group_name = 'myresourcegroup'
location = 'eastus'
resource_client.resource_groups.create_or_update(
    resource_group_name,
    {'location': location}
)


# Create a new VM
vm_name = 'myvm'
vm_size = 'Standard_D1_v2'
image_reference = {
    'publisher': 'Canonical',
    'offer': 'UbuntuServer',
    'sku': '18.04-LTS',
    'version': 'latest'
}
nic = compute_client.network_interfaces.create_or_update(
    resource_group_name,
    'mynic',
    {
        'location': location,
        'ip_configurations': [{
            'name': 'myipconfig',
            'subnet': {
                'id': '/subscriptions/{}/resourceGroups/{}/providers/Microsoft.Network/virtualNetworks/myvnet/subnets/mysubnet'.format(subscription_id, resource_group_name)
            }
        }]
    }
)
vm = compute_client.virtual_machines.create_or_update(
    resource_group_name,
    vm_name,
    {
        'location': location,
        'hardware_profile': {
            'vm_size': vm_size
        },
        'storage_profile': {
            'image_reference': image_reference
        },
        'network_profile': {
            'network_interfaces': [{
                'id': nic.id
            }]
        }
    }
)

print(f'Created VM: {vm_name}')