from google.cloud import dialogflowcx_v3beta1, storage
from google.oauth2 import service_account
import os, yaml, pprint

credFile = "prerprod-project-dialogflowcx.json"
credentials = service_account.Credentials.from_service_account_file(f'{credFile}')
client_options = {"api_endpoint": "asia-northeast1-dialogflow.googleapis.com"}
client = dialogflowcx_v3beta1.AgentsClient(credentials=credentials, client_options=client_options)
storage_client = storage.Client(credentials=credentials)

# load yaml file
def read_yaml_file():
    os.chdir(f"{os.getcwd()}/gcp-poc/using_python_script")
    yaml_file = open("release_info.yaml",'r')
    content = yaml.full_load(yaml_file)

    create_agents = []
    create_blob_files = []

    update_agents = []
    update_blob_files = []

    delete_agents = []
    task = ["create", "update", "delete"]

    i = 0
    while (i < len(task)):
        if task[i] in content["release_info"]:
            for each_agent in content["release_info"][f"{task[i]}"]:
                if task[i] == "create": 
                    create_agents.append(each_agent["agent_name"])
                    create_blob_files.append(each_agent["blob_file_name"])
                elif task[i] == "update": 
                    update_agents.append(each_agent["agent_name"])
                    update_blob_files.append(each_agent["blob_file_name"])
                elif task[i] == "delete": delete_agents.append(each_agent["agent_name"])
        i+=1

    return [create_agents, create_blob_files,
            update_agents, update_blob_files,
            delete_agents]

# Copy blob file from local to bucket
def upload_blob_to_bucket(bucket_name, version, agent_name, blob_file_name, task_type):
    output = os.popen(f'find . -type f -name {blob_file_name}.blob').read()
    source_file_name = output.strip()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"dialogflowcx/preprod/{version}/{task_type}/{agent_name}/{blob_file_name}.blob")
    blob.upload_from_filename(source_file_name)
    print(f"--> File:{blob_file_name} is uploaded to bucket:{bucket_name}")

# get agent
def get_existing_agentName_n_id(project_id, location):
    existing_agentName_n_id = {}
    page_result = client.list_agents(
        request = dialogflowcx_v3beta1.ListAgentsRequest(
            parent=f"projects/{project_id}/locations/{location}",
    ))
    for response in page_result:
        agent_nme = response.display_name
        agent_id = (response.name).split('/').pop(-1)
        existing_agentName_n_id[f'{agent_nme}']=f'{agent_id}'
    
    return existing_agentName_n_id

# Create agent (if necessary)
def create_agent(project_id, location, agent_name):
    agent = dialogflowcx_v3beta1.Agent()
    agent.display_name = f"{agent_name}" 
    agent.default_language_code = "en" 
    agent.time_zone = "Asia/Tokyo" 
    agent.description = f"{agent_name} agent"
    response = client.create_agent(
        request=dialogflowcx_v3beta1.CreateAgentRequest(
        parent=f"projects/{project_id}/locations/{location}", 
        agent=agent,
    ))
    return (response.name).split('/').pop(-1)

# restore agent
def restore_agent(project_id, location, bucket_name, version, agent_id, task_type, agent_name, blob_file_name):
    client.restore_agent(
        request=dialogflowcx_v3beta1.RestoreAgentRequest(
            agent_uri=f"gs://{bucket_name}/dialogflowcx/preprod/{version}/{task_type}/{agent_name}/{blob_file_name}.blob",
            name=f"projects/{project_id}/locations/{location}/agents/{agent_id}",
        ))

# delete agent
def delete_agent(project_id, location, agent_id):
    client.delete_agent(request = dialogflowcx_v3beta1.DeleteAgentRequest(
        name=f"projects/{project_id}/locations/{location}/agents/{agent_id}",
    ))

def task_exec():
    project_id = "prerprod-project"
    location = "asia-northeast1"
    bucket_name = "dialogflow-bucket-preprod"
    existing_agent_dictionary = get_existing_agentName_n_id(project_id, location)
    load_release_info = read_yaml_file()
    if len(load_release_info[0]) != 0:
        for (each_agent, each_blob_file) in zip(load_release_info[0],load_release_info[1]):
            upload_blob_to_bucket(bucket_name, version, each_agent, each_blob_file, "create-agent")
    if len(load_release_info[2]) != 0:
        for (each_agent, each_blob_file) in zip(load_release_info[2],load_release_info[3]):
            upload_blob_to_bucket(bucket_name, version, each_agent, each_blob_file, "update-agent")

    if len(load_release_info[0]) != 0: 
        print("\n** Start CREATING agent **")
        for (each_agent, each_blob_file) in zip(load_release_info[0],load_release_info[1]):
            if each_agent not in existing_agent_dictionary.keys():
                agent_id = create_agent(project_id, location, each_agent) 
                print(f"--> agent is created: [{each_agent}: {agent_id}]")
                restore_agent(project_id, location, bucket_name, version, agent_id, "create-agent", each_agent, each_blob_file)
                print(f"--> {each_agent} is restored")
            else: print (f"--> {each_agent} already exist. Can't be recreated.")

    if len(load_release_info[2]) != 0:
        print("\n** Start RESTORING agent **")
        for (each_agent, each_blob_file) in zip(load_release_info[2],load_release_info[3]):
            if each_agent in existing_agent_dictionary.keys():
                agent_id = existing_agent_dictionary[each_agent]
                print(f"--> Found the agent:[{each_agent}: {existing_agent_dictionary[each_agent]}]")
                restore_agent(project_id, location, bucket_name, version, agent_id, "update-agent", each_agent, each_blob_file)
                print(f"--> {each_agent} is updated")
            else: print (f"--> {each_agent} doesn't exist.")
    
    if len(load_release_info[4]) != 0:
        print("\n** Start DELETE agent **")
        for each_agent in load_release_info[4]:
            if each_agent in existing_agent_dictionary.keys():
                agent_id = existing_agent_dictionary[each_agent]
                delete_agent(project_id, location, agent_id)
                print(f"--> {each_agent} is deleted")
            else: print(f"--> {each_agent} doesn't exist.")
        print(f"after deletion left agents:{get_existing_agentName_n_id(project_id, location)}")
    

version = input("version: ") # "v0.0.0" 
task_exec()