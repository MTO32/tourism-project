from huggingface_hub import HfApi
import os

api = HfApi(token=os.getenv("HF_TOKEN"))
api.upload_folder(
    folder_path="tourism_project/deployment",
    repo_id = "MTO32/tourism-project",
    repo_type="space",                     
    path_in_repo="",                       
)
