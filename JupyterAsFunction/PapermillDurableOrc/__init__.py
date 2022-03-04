# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    payload = context.get_input()
    url = payload.pop("url")
    params = payload

    logging.info(
        f"Notebook url: {url}"
    )

    logging.info(
        f"Notebook params: {params}"
    )

    notebook_result = yield context.call_activity('runNotebook', 
        {
            "url": url,
            "params": params
        }
    )

    return notebook_result

main = df.Orchestrator.create(orchestrator_function)