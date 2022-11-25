# gcp-poc
### Necessary links
* [gcloud cli setup](https://www.youtube.com/watch?v=k-8qFh8EfFA )
* [Dialog-flow setup](https://cloud.google.com/dialogflow/cx/docs/quick/setup)
* [authetication](https://cloud.google.com/storage/docs/authentication)
> "For local testing, you can use the "gcloud auth application-default print-access-token command" to generate a token."
* [custom role](https://cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role)
* [dialogflowcx agent](https://cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3beta1.services.agents.AgentsClient)
* [list blob](https://cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket#google_cloud_storage_bucket_Bucket_list_blobs)

### Necessary Python module
* `pip3 install google-cloud-storage`
* `pip3 install google-cloud-dialogflow-cx`

### Necessary pages direct link
* [dialogflowcx](https://dialogflow.cloud.google.com/cx/projects)
* [gcp bucket](https://console.cloud.google.com/storage/browser?project=alien-hour-350703&prefix=)
* [IAM role](https://console.cloud.google.com/iam-admin/iam?project=prerprod-project)

### High level workflow
* preprod env (get file & release version from jenkin --> upload file to bucket --> restore agent from uploaded file)
* prod (get version from jenkin --> check file version available on preprod env bucket --> copy & rename preprod file to prod bucket --> restore agent from uploaded file)
