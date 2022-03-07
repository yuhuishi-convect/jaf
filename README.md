# jaf

---

jaf stands for Jupyter notebook as functions. This is a project for [Azure trial hackathon](https://dev.to/devteam/hack-the-microsoft-azure-trial-on-dev-2ne5).

jaf skaffolds an Azure Duration Function project to enable a jupyter notebook be deployed as a web endpoint. 

## Usage

### Prerequisites
* Azure cli
* Azure functions core tools

### Skaffold a project

```bash
pip install cookiecutter

cookiecutter https://github.com/yuhuishi-convect/jaf

project_name [JupyterAsFunction]: HelloWorld
notebook_url [https://raw.githubusercontent.com/nteract/papermill/main/binder/cli-simple/simple_output.ipynb]: 

```

### Test locally

```bash
# start the local runtime

$ func start 
Found Python version 3.8.5 (python3).

Azure Functions Core Tools
Core Tools Version:       4.0.3971 Commit hash: d0775d487c93ebd49e9c1166d5c3c01f3c76eaaf  (64-bit)
Function Runtime Version: 4.0.1.16815


Functions:

        PapermillTrigger: [POST] http://localhost:7071/api/HelloWorld

        PapermillDurableOrc: orchestrationTrigger

        PapermillRunnotebook: activityTrigger

For detailed output, run func with --verbose flag.
info: Microsoft.AspNetCore.Hosting.Diagnostics[1]
      Request starting HTTP/2 POST http://127.0.0.1:46327/AzureFunctionsRpcMessages.FunctionRpc/EventStream application/grpc -
info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0]
      Executing endpoint 'gRPC - /AzureFunctionsRpcMessages.FunctionRpc/EventStream'
[2022-03-07T20:00:52.941Z] Worker process started and initialized.
[2022-03-07T20:00:58.149Z] Host lock lease acquired by instance ID '000000000000000000000000EBCD312A'.
```
<details>
<summary>Call the endpoint </summary>

```bash

# we can specify the parameters in the payload

$ http http://localhost:7071/api/HelloWorld msg=hellowrld
HTTP/1.1 202 Accepted
Content-Type: application/json
Date: Mon, 07 Mar 2022 20:01:22 GMT
Location: http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==
Retry-After: 10
Server: Kestrel
Transfer-Encoding: chunked

{
    "id": "92340eba029644c2a4cc92b88eb92c65",
    "purgeHistoryDeleteUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==",
    "restartPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65/restart?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==",
    "rewindPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65/rewind?reason={text}&taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==",
    "sendEventPostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65/raiseEvent/{eventName}?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==",
    "statusQueryGetUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ==",
    "terminatePostUri": "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65/terminate?reason={text}&taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ=="
}
```

</details>

<details>
<summary>Query the status of the workloads</summary>


```bash
$ http "http://localhost:7071/runtime/webhooks/durabletask/instances/92340eba029644c2a4cc92b88eb92c65?taskHub=TestHubName&connection=Storage&code=WeTn3kKacKD97mRTYr1UaP4KPgb5eJMQBqQFGMnquPmCJNuW0aiUAQ=="                                                  
HTTP/1.1 200 OK
Content-Length: 2864
Content-Type: application/json; charset=utf-8
Date: Mon, 07 Mar 2022 20:02:41 GMT
Server: Kestrel

{
    "createdTime": "2022-03-07T20:01:22Z",
    "customStatus": null,
    "input": "{\"msg\": \"hellowrld\"}",
    "instanceId": "92340eba029644c2a4cc92b88eb92c65",
    "lastUpdatedTime": "2022-03-07T20:01:25Z",
    "name": "PapermillDurableOrc",
    "output": {
        "cells": [
            {
                "cell_type": "markdown",
                "id": "2423b240",
                "metadata": {
                    "papermill": {
                        "duration": 0.002853,
                        "end_time": "2022-03-07T20:01:24.582226",
                        "exception": false,
                        "start_time": "2022-03-07T20:01:24.579373",
                        "status": "completed"
                    },
                    "tags": []
                },
                "source": "# Simple input notebook with parameters"
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "id": "0b095f0b",
                "metadata": {
                    "execution": {
                        "iopub.execute_input": "2022-03-07T20:01:24.591766Z",
                        "iopub.status.busy": "2022-03-07T20:01:24.591607Z",
                        "iopub.status.idle": "2022-03-07T20:01:24.596259Z",
                        "shell.execute_reply": "2022-03-07T20:01:24.595924Z"
                    },
                    "papermill": {
                        "duration": 0.008369,
                        "end_time": "2022-03-07T20:01:24.597145",
                        "exception": false,
                        "start_time": "2022-03-07T20:01:24.588776",
                        "status": "completed"
                    },
                    "tags": [
                        "parameters"
                    ]
                },
                "outputs": [],
                "source": "msg = None"
            },
            {
                "cell_type": "code",
                "execution_count": 2,
                "id": "f7e403be",
                "metadata": {
                    "execution": {
                        "iopub.execute_input": "2022-03-07T20:01:24.601899Z",
                        "iopub.status.busy": "2022-03-07T20:01:24.601774Z",
                        "iopub.status.idle": "2022-03-07T20:01:24.603540Z",
                        "shell.execute_reply": "2022-03-07T20:01:24.603281Z"
                    },
                    "papermill": {
                        "duration": 0.005037,
                        "end_time": "2022-03-07T20:01:24.604344",
                        "exception": false,
                        "start_time": "2022-03-07T20:01:24.599307",
                        "status": "completed"
                    },
                    "tags": [
                        "injected-parameters"
                    ]
                },
                "outputs": [],
                "source": "# Parameters\nmsg = \"hellowrld\"\n"
            },
            {
                "cell_type": "code",
                "execution_count": 3,
                "id": "13859a47",
                "metadata": {
                    "execution": {
                        "iopub.execute_input": "2022-03-07T20:01:24.609052Z",
                        "iopub.status.busy": "2022-03-07T20:01:24.608930Z",
                        "iopub.status.idle": "2022-03-07T20:01:24.611030Z",
                        "shell.execute_reply": "2022-03-07T20:01:24.610761Z"
                    },
                    "papermill": {
                        "duration": 0.005376,
                        "end_time": "2022-03-07T20:01:24.611845",
                        "exception": false,
                        "start_time": "2022-03-07T20:01:24.606469",
                        "status": "completed"
                    },
                    "tags": []
                },
                "outputs": [
                    {
                        "name": "stdout",
                        "output_type": "stream",
                        "text": "hellowrld\n"
                    }
                ],
                "source": "print(msg)"
            }
        ],
        "metadata": {
            "celltoolbar": "Tags",
            "hide_input": false,
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.5"
            },
            "orig_nbformat_minor": 1,
            "papermill": {
                "duration": 1.014578,
                "end_time": "2022-03-07T20:01:24.727322",
                "environment_variables": {},
                "exception": null,
                "input_path": "https://raw.githubusercontent.com/nteract/papermill/main/binder/cli-simple/simple_output.ipynb",
                "output_path": "/tmp/output.ipynb",
                "parameters": {
                    "msg": "hellowrld"
                },
                "start_time": "2022-03-07T20:01:23.712744",
                "version": "2.1.3"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    },
    "runtimeStatus": "Completed"
}
```

</details>

### Publish to Azure

```bash
az login
az config param-persist on
# create a resource group
az group create --name <RESOURCE_GROUP_NAME> --location eastus

# create a storage account
az storage account create --name <STORAGE_NAME> --sku Standard_LRS

# create a function app 
az functionapp create --consumption-plan-location eastus --runtime python --runtime-version 3.8 --functions-version 3 --name <APP_NAME> --os-type linux --storage-account <STORAGE_NAME>

# publish
func azure functionapp publish <APP_NAME>
```


```bash
# test the remote endpoint
http 
```


## Why 

[Jupyter notebooks](https://jupyter.org/) are widely used as interactive programming environment to experiment data science and machine learning ideas.
However, going from development to deployment once a notebook is drafted is extremely hard. The process usually involves an engineer to rewrite significant portion of the jupyter notebook as a web/rpc service in order to make the model/procedure written in the notebook to be callable to other services.

With jaf, you can quickly spin up a web service that makes the jupyter notebook as a callable function, thus expediting greatly the speed to come from dev to deployment for data science solutions.

## How

To allow notebooks receive external parameters, we use [Papermill](https://papermill.readthedocs.io/en/latest/) to parameterize the notebook.

Then we implement the web service using [Azure Durable Function](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=csharp) to allow async call to the web service, since notebooks are usually long running and computationally expensive.

For the skaffolding, we use [Cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/README.html#).



