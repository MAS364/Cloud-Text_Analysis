
# ☁️ AWS Cloud Text Analysis (Serverless NLP Pipeline)

## 📌 Problem
Process and analyse multiple text files efficiently using a scalable, serverless cloud architecture, demonstrating event-driven computing and parallel processing on AWS.

---

## 📊 Data
- User-uploaded `.txt` files  
- Multi-file batch processing supported  
- Text data containing unstructured natural language content  

---

## ⚙️ Approach

### Architecture
Built a fully event-driven AWS pipeline:

Flask UI → S3 → API Gateway → AWS Lambda → JSON Response → Flask UI

- Flask handles file upload and UI rendering  
- S3 stores input files  
- API Gateway triggers Lambda  
- Lambda performs text analysis and returns structured results  

---

### Text Processing (Lambda)
Implemented NLP-based analysis:
- Word frequency analysis (Top 20 words, stop-word removal)  
- Sentence-start frequency analysis (Top 10 patterns)  
- Sentence statistics (mean, median, standard deviation)  
- Regex-based text cleaning pipeline  

---

### Scalability & Parallelism
- Multi-file upload support  
- Parallel processing using ThreadPoolExecutor  
- Independent Lambda execution per file  
- UUID-based file handling to avoid collisions  
- Fault isolation per request  

---

## 🚀 Deployment
- Flask hosted on EC2  
- Fully serverless backend using AWS Lambda  
- API Gateway for secure HTTP endpoints  
- S3 for scalable file storage  
- Real-time result rendering in web UI  

Access:
http://<EC2_PUBLIC_IP>:8080

---

## 📈 Result
- Successfully processed single and batch file uploads  
- Near real-time text analytics using serverless execution  
- Scalable architecture with automatic AWS resource scaling  
- Parallel processing significantly improved throughput


<img width="1083" height="567" alt="Screenshot 2026-06-08 at 01 34 33" src="https://github.com/user-attachments/assets/c8498f6f-7896-4d29-83bd-d3e9e882bdc9" />
<img width="1164" height="735" alt="Screenshot 2026-06-08 at 01 35 35" src="https://github.com/user-attachments/assets/bbe1e98b-fe70-4f03-ad0e-efd89b42c6f9" />
<img width="1093" height="719" alt="Screenshot 2026-06-08 at 01 36 16" src="https://github.com/user-attachments/assets/504243d4-8706-4b1f-87b6-313eebd981f7" />





---

## 💡 Impact / Insight
- Demonstrates production-grade serverless architecture design  
- Shows ability to integrate multiple AWS services into one pipeline  
- Highlights scalability through event-driven computing  
- Enables efficient processing of large-scale unstructured text data  
- Strong foundation for NLP-based cloud applications  

---

## 🧠 Skills Demonstrated
- AWS (Lambda, S3, API Gateway, EC2)  
- Serverless architecture design  
- Event-driven systems  
- Parallel processing (Python ThreadPoolExecutor)  
- Flask web development  
- NLP preprocessing (tokenization, frequency analysis)  
