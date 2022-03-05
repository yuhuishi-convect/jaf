# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import papermill as pm
import tempfile
import os.path
import tempfile
import json

NB_NODE = """
{\n "cells": [\n  {\n   "cell_type": "markdown",\n   "metadata": {\n    "papermill": {\n     "duration": 0.00964,\n     "end_time": "2020-08-17T19:57:24.239226",\n     "exception": false,\n     "start_time": "2020-08-17T19:57:24.229586",\n     "status": "completed"\n    },\n    "tags": []\n   },\n   "source": [\n    "# Simple input notebook with parameters"\n   ]\n  },\n  {\n   "cell_type": "code",\n   "execution_count": 1,\n   "metadata": {\n    "execution": {\n     "iopub.execute_input": "2020-08-17T19:57:24.263404Z",\n     "iopub.status.busy": "2020-08-17T19:57:24.262659Z",\n     "iopub.status.idle": "2020-08-17T19:57:24.265395Z",\n     "shell.execute_reply": "2020-08-17T19:57:24.264689Z"\n    },\n    "papermill": {\n     "duration": 0.012719,\n     "end_time": "2020-08-17T19:57:24.265567",\n     "exception": false,\n     "start_time": "2020-08-17T19:57:24.252848",\n     "status": "completed"\n    },\n    "tags": [\n     "parameters"\n    ]\n   },\n   "outputs": [],\n   "source": [\n    "msg = None"\n   ]\n  },\n  {\n   "cell_type": "code",\n   "execution_count": 2,\n   "metadata": {\n    "execution": {\n     "iopub.execute_input": "2020-08-17T19:57:24.274405Z",\n     "iopub.status.busy": "2020-08-17T19:57:24.273934Z",\n     "iopub.status.idle": "2020-08-17T19:57:24.276194Z",\n     "shell.execute_reply": "2020-08-17T19:57:24.275695Z"\n    },\n    "papermill": {\n     "duration": 0.007713,\n     "end_time": "2020-08-17T19:57:24.276300",\n     "exception": false,\n     "start_time": "2020-08-17T19:57:24.268587",\n     "status": "completed"\n    },\n    "tags": [\n     "injected-parameters"\n    ]\n   },\n   "outputs": [],\n   "source": [\n    "# Parameters\\n",\n    "msg = \\"Hello\\"\\n"\n   ]\n  },\n  {\n   "cell_type": "code",\n   "execution_count": 3,\n   "metadata": {\n    "execution": {\n     "iopub.execute_input": "2020-08-17T19:57:24.283119Z",\n     "iopub.status.busy": "2020-08-17T19:57:24.282711Z",\n     "iopub.status.idle": "2020-08-17T19:57:24.284846Z",\n     "shell.execute_reply": "2020-08-17T19:57:24.284482Z"\n    },\n    "papermill": {\n     "duration": 0.006366,\n     "end_time": "2020-08-17T19:57:24.284929",\n     "exception": false,\n     "start_time": "2020-08-17T19:57:24.278563",\n     "status": "completed"\n    },\n    "tags": []\n   },\n   "outputs": [\n    {\n     "name": "stdout",\n     "output_type": "stream",\n     "text": [\n      "Hello\\n"\n     ]\n    }\n   ],\n   "source": [\n    "print(msg)"\n   ]\n  }\n ],\n "metadata": {\n  "celltoolbar": "Tags",\n  "hide_input": false,\n  "kernelspec": {\n   "display_name": "Python 3",\n   "language": "python",\n   "name": "python3"\n  },\n  "language_info": {\n   "codemirror_mode": {\n    "name": "ipython",\n    "version": 3\n   },\n   "file_extension": ".py",\n   "mimetype": "text/x-python",\n   "name": "python",\n   "nbconvert_exporter": "python",\n   "pygments_lexer": "ipython3",\n   "version": "3.8.2"\n  },\n  "papermill": {\n   "duration": 0.727728,\n   "end_time": "2020-08-17T19:57:24.494284",\n   "environment_variables": {},\n   "exception": null,\n   "input_path": "binder/cli-simple/simple_input.ipynb",\n   "output_path": "binder/cli-simple/simple_output.ipynb",\n   "parameters": {\n    "msg": "Hello"\n   },\n   "start_time": "2020-08-17T19:57:23.766556",\n   "version": "2.1.3"\n  }\n },\n "nbformat": 4,\n "nbformat_minor": 1\n}
"""


with tempfile.NamedTemporaryFile("w", delete=False) as f:
    json.dump(json.loads(NB_NODE), f)
    
    FILENAME = f.name




def main(message) -> str:
    logging.info(
        "Notebook running activity function started."
    )
    logging.info(
        f"Message: {message}"
    )

    message_body = message

    input_path = FILENAME

    params = message_body.get("params")

    output_path = os.path.join(
        tempfile.gettempdir(), "output.ipynb"
    )

    returned_notebook = pm.execute_notebook(
        input_path=input_path,
        output_path=output_path,
        parameters=params
    )

    return returned_notebook
    


