from google.cloud import bigquery
import glob
import os
import sys

def get_query(query_file_path):
    with open(query_file_path, 'r', encoding='utf-8') as f:
        query = f.read()
    return query

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/run/secrets/gcp_secret'

client = bigquery.Client()

job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)

query_file_paths = glob.glob('./sql/*.sql')

for query_file_path in query_file_paths:
  try:
    query = get_query(query_file_path)
    query_job = client.query(query,job_config=job_config)
    print("query in {} will process {} bytes.".format(query_file_path, query_job.total_bytes_processed))
  except:
    print("Oops!", sys.exc_info()[1], "occurred in ", query_file_path)
    continue
