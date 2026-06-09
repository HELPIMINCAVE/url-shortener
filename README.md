# URL Shortener API

A lightweight, high-performance REST API built with Flask that generates shortened URLs, tracks link engagement metrics, and handles real-time user redirections.

## 🚀 Features
* **URL Shortening**: Convert long, clunky URLs into compact 6-character unique keys.
* **Redirection Engine**: Dynamically routes visitors from the short link directly to the target destination.
* **Analytics Tracking**: Tracks click-through metrics (`accessCount`) automatically on every retrieval.
* **Clean Architecture**: Follows the professional Controller-Service-Repository pattern.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Framework:** Flask
* **Environment:** Virtual Environments (`.venv`)

---

## 📦 Getting Started

### 1. Clone & Navigate to Project
```bash
cd url-shortener
```

### 2. Activate Virtual Environment
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Start the Flask Server
```bash
python3 app.py # or python app.py if you're on Windows
```
*The server will boot up in debug mode on http://127.0.0.1:8080.*

#### 🔌 API Reference & Usage
1. Shorten a URL
Endpoint: POST /shorten

Payload: JSON containing the original URL.

##### Example Request:
```bash
curl -s -X POST "[https://www.example.com/some/long/url](https://www.example.com/some/long/url)" \
     -H "Content-Type: application/json" \
     -d "{\"url\":\"[https://www.example.com/some/long/url](https://www.example.com/some/long/url)\"}"
```

##### Example Response (201 Created):
```json
{
  "accessCount": 0,
  "createdAt": "2026-06-08T12:55:59.875009+00:00",
  "id": "5a783087ba9a4bf3937b98a41be06941",
  "shortCode": "IBYFgR",
  "updatedAt": "2026-06-08T12:55:59.875009+00:00",
  "url": "[https://www.example.com/some/long/url](https://www.example.com/some/long/url)"
}
```

#### 2. Retrieve URL Statistics
**Endpoint**: ```GET /shorten/<shortcode>```

**Description**: Fetches full metadata record and increments the accessCount.

Example Request:
```bash
curl -s [http://127.0.0.1:8080/shorten/shortcode](http://127.0.0.1:8080/shorten/shortcode)
```

#### Example Response (200 OK):
```json
{
  "accessCount": 1,
  "url": "[https://www.example.com/some/long/url](https://www.example.com/some/long/url)"
}
```

#### 3. Live Web Browser Redirection

**Endpoint:** ```GET /<shortcode>```

**Description:** *Open this directly in your browser's address bar to redirect to the destination target.*

##### Usage:
```plaintext
[http://127.0.0.1:8080/IBYFgR](http://127.0.0.1:8080/shortcode)
```
*(Triggers an HTTP 302 Redirect to your destination url).*

#### 4. Delete a Shortened URL

**Endpoint:** ```DELETE /shorten/<shortcode>```

##### Example Request:
```bash 
curl -X DELETE [http://127.0.0.1:8080/shorten/shortcode](http://127.0.0.1:8080/shorten/shortcode)```
```

**Response:** ```204 No Content``` (Success)

---

### Pro-Tip for Git:
Since you just learned how to handle those single quotes for your commit message, you can save this file and commit it beautifully by running:

###### The project is from https://roadmap.sh/projects/url-shortening-service