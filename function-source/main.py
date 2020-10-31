from googleapiclient.discovery import build

def execute_dataflow_template(event, context):
    project = <PROJECT_ID>
    job = "trialJob"
    template = "gs://dataflow-templates/latest/GCS_Text_to_BigQuery"
    parameters = {
        "javascriptTextTransformFunctionName": "transform",
        "JSONPath": "gs://dataflow-template-trial/schema.json",
        "javascriptTextTransformGcsPath": "gs://dataflow-template-trial/function.js",
        "inputFilePattern": "gs://dataflow-template-trial/FinancialSample.csv",
        "outputTable": project + ":dataflow_dataset.FinancialSample",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow-template-trial/tmp",
    }

    dataflow = build("dataflow", "v1b3")
    request = (
        dataflow.projects()
        .templates()
        .launch(
            projectId=project,
            gcsPath=template,
            body={
                "jobName": job,
                "parameters": parameters,
            },
        )
    )

    response = request.execute()
