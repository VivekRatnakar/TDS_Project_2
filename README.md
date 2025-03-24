# **TDS Solver API**  
This API automatically answers questions from graded assignments for the **IIT Madras Online Degree in Data Science**.  

---

## **Setup**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/VivekRatnakar/TDS_Project_2.git
cd TDS_Project_2
```

### **2️⃣ Create & Activate Virtual Environment**  
#### **Windows:**  
```bash
python -m venv venv
venv\Scripts\activate
```
#### **Unix/MacOS:**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4️⃣ Setup Environment Variables**  
Create a `.env` file and add the following:  
```
AIPROXY_TOKEN=your-api-key
```

### **5️⃣ Run the Server**  
```bash
uvicorn app.main:app --reload
```
The API will be available at **http://localhost:8000**.  

---

## **Usage**  

### **📌 API Endpoint**  
**`POST /api/`**  
**Parameters:**  
| Name      | Type      | Required | Description |
|-----------|----------|----------|-------------|
| `question` | `string`  | ✅ Yes  | The graded assignment question |
| `file`    | `file`    | ❌ No  | (Optional) A related file needed for the answer |

### **Example Request (cURL)**  
```bash
curl -X POST "http://localhost:8000/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the 'answer' column of the CSV file?" \
  -F "file=@abcd.zip"
```

### **Example Response**  
```json
{
  "answer": "1234567890"
}
```

---

## **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  
