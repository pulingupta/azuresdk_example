## Azure Sdk to create resource group as well list them with properties

The Sample code is written in python and uses azure libraries to fetch the resource groups in a given subscription

## Prerequisites to run the code
1. Install python3
    ```bash
    brew install python3
    ```
2. install pip using 
    ```bash
    python3 install pip
    ```
3. execute az commands as below as you would need to login unless correct credentials are already provided in the az cli code.

```bash
    az login
    az account set "subscription_name"
```

4. Run the command
    ```bash
      pip install requirements.txt // to install python libraries required to run azure sdk
    ```
5. Run the command to provision resource in azure
    ```bash
    python provision_rg.py
    ```
    


