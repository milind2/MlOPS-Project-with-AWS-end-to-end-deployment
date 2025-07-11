import mlflow
import dagshub
from mlflow.exceptions import MlflowException

# --- Use your personal DagsHub details ---
REPO_OWNER = 'milind2'
REPO_NAME = 'MlOPS-Project-with-AWS-end-to-end-deployment'
MODEL_NAME = 'my_model'

print("--- 1. Initializing DagsHub and MLflow ---")
dagshub.init(repo_owner=REPO_OWNER, repo_name=REPO_NAME, mlflow=True)
mlflow.set_tracking_uri(f'https://dagshub.com/{REPO_OWNER}/{REPO_NAME}.mlflow')
print("Initialization complete.")
print("-" * 20)


print(f"--- 2. Trying to fetch model: '{MODEL_NAME}' from stage: 'Production' ---")
try:
    client = mlflow.tracking.MlflowClient()
    versions = client.get_latest_versions(MODEL_NAME, stages=["Production"])
    if versions:
        print("✅ SUCCESS! Found the following production versions:")
        for version in versions:
            print(f"   - Version: {version.version}, Run ID: {version.run_id}")
    else:
        print("❌ FAILED: Connection successful, but no model found in 'Production' stage.")

except MlflowException as e:
    print(f"❌ FAILED with MlflowException: {e}")
except Exception as e:
    print(f"❌ FAILED with a general exception: {e}")