#  AI Agent for DevOps

This project builds and deploys an AI Agent that assists with DevOps tasks such as:

- Log analysis
- System health checks

##  Getting Started

### Prerequisites

- Python 3.11
- Docker
- Kubernetes (e.g., Minikube or EKS)
- OpenAI API Key

### Run Locally

```bash
pip install -r agent/requirements.txt
python agent/main.py
```

### Build & Push Docker

```bash
docker build -t yourdockerhub/ai-devops-agent:latest -f docker/Dockerfile .
docker push yourdockerhub/ai-devops-agent:latest
```

### Deploy to Kubernetes

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

---
##  Future of AI in DevOps

This project shows how AI can:
- Monitor and diagnose issues automatically
- Perform proactive remediation
- Offer intelligent insights for DevOps teams
<img width="657" height="374" alt="image" src="https://github.com/user-attachments/assets/1bcbf7bd-6d8d-4a8b-a0aa-c04278fd0051" />
