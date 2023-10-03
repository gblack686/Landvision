from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Azure Key Vault credentials
key_vault_name = "AzureGbKeyVault1"
key_vault_uri = f"https://{key_vault_name}.vault.azure.net"
search_string = "Twitter"


# Authenticate to Azure Key Vault using the default Azure credential
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=key_vault_uri, credential=credential)

# List all secrets that match the search string
secrets = secret_client.list_properties_of_secrets()
twitter_secrets = {}

for secret in secrets:
    if search_string in secret.name:
        secret_value = secret_client.get_secret(secret.name).value
        twitter_secrets[secret.name] = secret_value

# Print the dictionary of Twitter-related secrets
print("Twitter-related secrets:")
for secret_name, secret_value in twitter_secrets.items():
    print(f"Secret Name: {secret_name}, Secret Value: {secret_value}")