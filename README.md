<h1 align="center">🌟 LangChain — Models Component Overview 🌟</h1>

---

### **💡 What is the Models Component?**

The **Models Component** in **LangChain** provides a **common interface** to interact with different AI models such as:

- **LLMs (Language Models)**
- **Chat Models**
- **Embedding Models**

Because different models behave differently, LangChain **standardizes communication**, making integration simple and consistent.

---

## **🧠 Types of Models in LangChain**

---

### 🔹 **1️⃣ Language Models**

> **Input:** Text  
> **Output:** Text  

📌 *Example:*  
**Input:** _"What is the capital of India?"_  
**Output:** _"New Delhi"_

#### **✨ Sub-Types**
| Model Type | Description | Use Cases |
|------------|------------|------------|
| **LLMs** | Single prompt → single text output | Text generation, summarization, code gen |
| **Chat Models** | Multi-turn conversations with context | Chatbots, assistants, dialogue systems |

---

### 🔹 **2️⃣ Embedding Models**

> Input: Text → Output: **Vectors (Numbers)**

✨ Used for:
- 🔍 **Semantic Search**
- 📚 **RAG Applications**
- 📄 **Document Similarity**

➡ Embeddings convert text into a **vector representation** that captures meaning.

---

## **🔐 Closed-Source vs 🌍 Open-Source Models**

---

### 🔐 **Closed-Source Models**
| Provider | Examples |
|----------|----------|
| OpenAI | GPT-4, GPT-3.5 |
| Anthropic | Claude |
| Google | Gemini |

⚠ Characteristics:
- Hosted on provider servers
- Access via API (paid)
- Limited control & customization

---

### 🌍 **Open-Source Models**
| Model | Source | Params |
|--------|--------|--------|
| **LLaMA 2** | Meta AI | 7B–70B |
| **Falcon** | TII UAE | 7B–40B |

✔ Benefits:
- Downloadable
- Fine-tunable
- Self-hostable

⚡ **Main Source:** **Hugging Face Model Hub**

#### 🔧 Ways to Use Open-Source Models:
| Method | Description |
|--------|------------|
| **Inference API** | Run remotely via HF API |
| **Local Execution** | Download & run on machine |

---

### ⚠ Limitations of Open-Source Models
- Require **powerful GPU**
- Setup complexity
- Less polished vs closed models
- Often text-only (no multimodal)

---

## **📌 Embedding Models (Summary)**

| Feature | Purpose |
|---------|---------|
| **Embeddings** | Convert text to vectors |
| **Used For** | Semantic search, RAG |
| **Examples** | OpenAI Embeddings, Hugging Face embeddings |

---

## **⚙ Setup Instructions**

```bash
# 1️⃣ Create virtual environment
python -m venv venv

# 2️⃣ Activate
venv\Scripts\Activate

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

### **✔ Verify Installation**

Create `test.py`:

```python
import langchain
print(langchain.__version__)
```

Run:

```bash
python test.py
```

---

## **📍 Summary Table**

| Feature | Closed-Source | Open-Source |
|---------|--------------|-------------|
| Cost | Paid | Mostly Free |
| Control | Limited | Full control |
| Hosting | Provider servers | Local / cloud |
| Customization | Restricted | Fine-tunable |
| Hardware Need | None | High |

---

### **🚀 What You Can Build**
| Category | Example |
|----------|---------|
| Chatbot | Conversational AI |
| Search | Semantic document search |
| RAG | AI with knowledge base |

<img width="940" height="457" alt="image" src="https://github.com/user-attachments/assets/bc48076f-9949-4c4a-a73f-0ef11a397063" />
<img width="940" height="549" alt="image" src="https://github.com/user-attachments/assets/1b1d8969-c042-450d-8bd6-b66b33547b2c" />
<img width="940" height="511" alt="image" src="https://github.com/user-attachments/assets/9b838af1-16cd-42b9-8b35-d5d91b37d111" />
<img width="940" height="436" alt="image" src="https://github.com/user-attachments/assets/8afcff4e-7e13-45b7-a5f3-de6c9f7420ed" />
<img width="940" height="429" alt="image" src="https://github.com/user-attachments/assets/6fda3bbb-7b54-4a61-a47d-8f1b2e87a3da" />
<img width="1316" height="874" alt="image" src="https://github.com/user-attachments/assets/ca96891d-9f2e-42c2-b07e-aaa5cd752044" />







