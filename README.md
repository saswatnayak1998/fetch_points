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

### 3. Example Run
```bash 
curl -X POST \
  http://127.0.0.1:5001/receipts/process \
  -H "Content-Type: application/json" \
  -d '{
    "retailer": "Target",
    "purchaseDate": "2022-01-01",
    "purchaseTime": "13:01",
    "items": [
      {
        "shortDescription": "Mountain Dew 12PK",
        "price": "6.49"
      },
      {
        "shortDescription": "Emils Cheese Pizza",
        "price": "12.25"
      },
      {
        "shortDescription": "Knorr Creamy Chicken",
        "price": "1.26"
      },
      {
        "shortDescription": "Doritos Nacho Cheese",
        "price": "3.35"
      },
      {
        "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
        "price": "12.00"
      }
    ],
    "total": "35.35"
  }'
  ```
 ## Output: 
  ```bash
  {"id":"a35c4127-288d-47fe-bc99-e896d6f277e9"}
    ```
## Get Points

```bash
curl -X GET \
  http://127.0.0.1:5001/receipts/a35c4127-288d-47fe-bc99-e896d6f277e9/points \
  -H "accept: application/json"
```
Output

```bash
28
```