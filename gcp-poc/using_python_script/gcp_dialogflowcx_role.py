from googleapiclient import discovery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('prerprod-project-iam-role.json')
client_options = {"api_endpoint": "asia-northeast1-dialogflow.googleapis.com"}
service = discovery.build(serviceName='iam', version='v1', credentials=credentials)

def create_role(project):
    role = service.projects().roles().create(
        parent=f'projects/{project}',
        body={
            'roleId': "Custom_DialogflowCX_Role",
            'role': {
                'title': "Custom DialogflowCX Role",
                'description': "Custom DialogflowCX Role",
                'stage': "Alpha",
                'includedPermissions': ["dialogflow.agents.create",]
            }
        }).execute()

    print('Created role: ' + role['name'])


def edit_role(role_name, project, permissions):
    role = service.projects().roles().patch(
        name=f'projects/{project}/roles/{role_name}',
        body={
            'title': "Custom DialogflowCX Role",
            'description': "Custom DialogflowCX Role",
            'stage': "Alpha",
            'includedPermissions': permissions
        }).execute()

    print('Updated role: ' + role['name'])

# create_role("prerprod-project")
edit_role("Custom_DialogflowCX_Role", "prerprod-project", [
                                        "dialogflow.agents.create",
                                        "dialogflow.agents.delete",
                                        "dialogflow.agents.get",
                                        "dialogflow.agents.list",
                                        "dialogflow.agents.restore",
                                        "serviceusage.services.use",
                                        "storage.objects.create",
                                        "storage.objects.delete",
                                        "storage.objects.get",
                                        "storage.objects.list",
                                        "storage.buckets.get",])

                                        

# Custom_DialogflowCX_Role,prerprod-project,storage.buckets.get
# name = "projects/prerprod-project/roles/Custom_DialogflowCX_Role"
# name = "projects/prod-project/roles/Custom_DialogflowCX_Role"
# https://cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role
# dialogflow.agents.export
# dialogflow.agents.import
# dialogflow.agents.search
# orgpolicy.policy.get
# resourcemanager.projects.get
# storage.multipartUploads.abort
# storage.multipartUploads.create
# storage.multipartUploads.listParts