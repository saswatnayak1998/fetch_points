# Fetch Points Flask Application

This is a Flask application that processes receipts and calculates points. It is designed to run in a Docker container.


## Getting Started

Follow these steps to run the application using Docker:

### 1. Clone the Repository

Clone the repository to your local machine:
bash
git clone <repository-url>
cd <repository-directory>

### 2. Build and Run
```bash
docker build -t fetch_points . 
docker run -p 5001:5001 fetch_points
```

