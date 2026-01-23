📁 Project Structure
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

⚙️ Installation
1️⃣ Clone the repository
git clone <your-repository-url>
cd agriculture
2️⃣ Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Apply database migrations
python manage.py migrate
6️⃣ Run the development server
python manage.py runserver

🐳 Run with Docker
Build and start containers
docker-compose up --build
