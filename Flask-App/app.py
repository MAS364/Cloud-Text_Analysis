from flask import Flask, request, render_template
import boto3
import uuid
import json
import http.client
from concurrent.futures import ThreadPoolExecutor, as_completed

app = Flask(__name__)

UPLOAD_BUCKET = "input-a2-bucket"
s3 = boto3.client("s3")

API_HOST = "YOUR_API_ID.execute-api.us-east-1.amazonaws.com"
API_STAGE = "default"
API_RESOURCE = "s3-trigger-lambda"

MAX_WORKERS = 5

def call_lambda(bucket, key):
    conn = http.client.HTTPSConnection(API_HOST)
    payload = json.dumps({"input_bucket": bucket, "input_key": key})
    headers = {"Content-Type": "application/json"}
    conn.request("POST", f"/{API_STAGE}/{API_RESOURCE}", payload, headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode())
    return json.loads(data["body"])

@app.route("/")
def upload_page():
    return render_template("upload.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    files = request.files.getlist("files")
    uploaded = []

    for f in files:
        key = f"uploads/{uuid.uuid4()}_{f.filename}"
        s3.put_object(Bucket=UPLOAD_BUCKET, Key=key, Body=f.read())
        uploaded.append({"filename": f.filename, "key": key})

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(call_lambda, UPLOAD_BUCKET, item["key"]): item
            for item in uploaded
        }
        for future in as_completed(futures):
            item = futures[future]
            try:
                results.append({"filename": item["filename"], "data": future.result()})
            except Exception as e:
                results.append({"filename": item["filename"], "error": str(e)})

    return render_template("data.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
