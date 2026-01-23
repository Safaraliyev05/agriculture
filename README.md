# 📁 Project Structure

``` bash
agriculture/
├── agriculture/        # Helm chart for Kubernetes deployment
│   ├── charts/
│   ├── templates/
│   ├── Chart.yaml
│   └── values.yaml
│
├── apps/               # Main Django application
│   ├── migrations/
│   ├── views/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── tasks.py
│   ├── urls.py
│   └── admin.py
│
├── root/               # Project-level configuration
├── manage.py
├── db.sqlite3          # Local development database
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

# ⚙️ Installation

1️⃣ Clone the repository

``` bash
git clone <your-repository-url>
cd agriculture
```

2️⃣ Create and activate virtual environment

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

4️⃣ Apply database migrations

``` bash
python manage.py migrate
```

6️⃣ Run the development server

``` bash
python manage.py runserver
```

# 🐳 Run with Docker

Build and start containers

``` bash
docker-compose up --build
```

# Test Helm chart
```bash
helm template agriculture agriculture/
```

# Install Helm release
```bash
kubectl create namespace agriculture
helm install agriculture agriculture/ -n agriculture
helm upgrade agriculture agriculture/ -n agriculture
```

# Verify deployment
```bash
kubectl get pods -n agriculture
kubectl get svc -n agriculture
kubectl logs deploy/agriculture -n agriculture
```

# Argocd
```bash
kubectl apply -f application.yaml
```
![img.png](img.png)