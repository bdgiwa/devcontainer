from datetime import datetime, timedelta
from azure.storage.fileshare import ShareServiceClient, generate_account_sas, ResourceTypes, AccountSasPermissions

sas_token = generate_account_sas(
    account_name="vsoce5df35cc47b4a4d93af2",
    account_key="YXTRrLMNkxo4VaCsyNKRNeBw/Zgqd/vV8C/yEQlzdoHcRz3wfJowQEKjF9aqvSCytEEgtEqqhW40+ASt6w5HFQ==",
    resource_types=ResourceTypes(container=True),
    permission=AccountSasPermissions(read=True),
    expiry=datetime.utcnow() + timedelta(hours=1)
)


share_service_client = ShareServiceClient(
    account_url="https://vsoce5df35cc47b4a4d93af2.z25.file.storage.azure.net", 
    credential=sas_token)
    #credential="YXTRrLMNkxo4VaCsyNKRNeBw/Zgqd/vV8C/yEQlzdoHcRz3wfJowQEKjF9aqvSCytEEgtEqqhW40+ASt6w5HFQ==")

'''
connection_string = "DefaultEndpointsProtocol=https;AccountName=vsoce5df35cc47b4a4d93f2;AccountKey=YXTRrLMNkxo4VaCsyNKRNeBw/Zgqd/vV8C/yEQlzdoHcRz3wfJowQEKjF9aqvSCytEEgtEqqhW40+ASt6w5HFQ==;EndpointSuffix=z25.file.storage.azure.net"
share_service_client = ShareServiceClient.from_connection_string(conn_str=connection_string)
'''

'''
my_shares = list(share_service_client.list_shares())

# Print the shares
for share in my_shares:
    print(share)

'''
share = share_service_client.get_share_client("cloudenvdata")
# List files in the directory
my_files = list(share.list_directories_and_files(directory_name="containerlogs"))
print(my_files)
