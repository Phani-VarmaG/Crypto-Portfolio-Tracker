# Cryptocurrency Portfolio Tracker

This project is a full‑stack cryptocurrency portfolio tracker that provides users with real‑time portfolio analytics and management. It integrates real‑time market data from the CoinGecko API, secures user authentication via JWT tokens, and offers dynamic dashboards with interactive data visualizations—all backed by PostgreSQL and deployed using Docker.

## Features

- **User Authentication:**  
  Secure user registration and login using JWT tokens. Backend routes (see [auth.py](d:/WebDev/crypto-portfolio-tracker/backend/app/routes/auth.py)) require a valid token for accessing protected endpoints.
  
- **Portfolio Management:**  
  Users can track their cryptocurrency transactions by adding transactions (buys/sells). The backend aggregates user transactions ([portfolio.py](d:/WebDev/crypto-portfolio-tracker/backend/app/routes/portfolio.py)) and calculates current portfolio values using live coin market data.

- **Real-Time Data Integration:**  
  Latest coin prices are fetched from the CoinGecko API ([coingecko.py](d:/WebDev/crypto-portfolio-tracker/backend/app/utils/coingecko.py)). This allows portfolio values to reflect real‑time market changes.

- **Interactive Dashboards:**  
  The React frontend provides dynamic dashboards with data visualizations via charts ([PortfolioSummary.js](d:/WebDev/crypto-portfolio-tracker/frontend/src/components/Dashboard/PortfolioSummary.js)). Users can monitor their portfolio allocation and performance.

- **Dockerized Deployment:**  
  Both the frontend and backend are containerized. Using the provided Dockerfiles and [docker-compose.yml](d:/WebDev/crypto-portfolio-tracker/docker-compose.yml), deployment to the cloud is straightforward.

## Technology Stack

- **Frontend:**  
  - React (with React Router for navigation)  
  - Axios for API requests  
  - Chart.js via react-chartjs-2 for data visualization

- **Backend:**  
  - Flask framework  
  - SQLAlchemy ORM and Flask-Migrate for PostgreSQL  
  - Flask-CORS for handling cross-origin requests  
  - JWT (via PyJWT) for user authentication

- **Database:**  
  - PostgreSQL for secure and relational data storage

- **Deployment:**  
  - Docker and Docker Compose for containerization  
  - Cloud deployment ready with environment configuration

## Project Structure

- **Frontend:**  
  - `src/`: Contains React components, pages (e.g., Portfolio, Login, Settings), and service files (e.g., [auth.js](d:/WebDev/crypto-portfolio-tracker/frontend/src/services/auth.js), [api.js](d:/WebDev/crypto-portfolio-tracker/frontend/src/services/api.js)).
  - Docker: Dockerfile for the Node.js-based frontend.

- **Backend:**  
  - `app/`: Contains models (e.g., [user.py](d:/WebDev/crypto-portfolio-tracker/backend/app/models/user.py), [transaction.py](d:/WebDev/crypto-portfolio-tracker/backend/app/models/transaction.py)), routes (e.g., [auth.py](d:/WebDev/crypto-portfolio-tracker/backend/app/routes/auth.py), [transactions.py](d:/WebDev/crypto-portfolio-tracker/backend/app/routes/transactions.py), [portfolio.py](d:/WebDev/crypto-portfolio-tracker/backend/app/routes/portfolio.py)), and utility functions (e.g., [auth.py](d:/WebDev/crypto-portfolio-tracker/backend/app/utils/auth.py), [coingecko.py](d:/WebDev/crypto-portfolio-tracker/backend/app/utils/coingecko.py)).
  - config.py: Contains configuration settings including the `SECRET_KEY` and database URI.
  - Docker: Dockerfile for the Python-based backend.
  - Requirements.txt: Lists all Python dependencies.

- **Docker Compose:**  
  - [docker-compose.yml](d:/WebDev/crypto-portfolio-tracker/docker-compose.yml) orchestrates the multi-container deployment including frontend, backend, PostgreSQL, and Redis.

## Setup and Running

### Prerequisites

- Docker and Docker Compose installed on your machine.
- An environment file (`.env`) configured with the necessary variables (e.g., `SECRET_KEY`, `DATABASE_URL`).

### Running Locally

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd crypto-portfolio-tracker
   ```

2. **Build and Start the Containers:**

   ```bash
   docker-compose up --build
   ```

   - The backend will be available on [http://localhost:5000](http://localhost:5000).
   - The frontend will be available on [http://localhost:3000](http://localhost:3000).

### Running Without Docker

1. **Backend:**

   - Set up a Python virtual environment and install dependencies from Requirements.txt.
   - Configure environment variables as per your local setup.
   - Run the Flask app using the boot script (e.g., `./boot.sh` on Windows via Git Bash or modify accordingly).

2. **Frontend:**

   - Navigate to the frontend folder.
   - Install dependencies with `npm install`.
   - Start the development server with `npm start`.

## Code Highlights

- **JWT-Based Authentication:**  
  The `token_required` decorator in [auth.py](d:/WebDev/crypto-portfolio-tracker/backend/app/utils/auth.py) secures endpoints by verifying the token in the request headers.

- **Real-Time Price Updates:**  
  The backend fetches updated coin prices from the CoinGecko API and recalculates portfolio values accordingly.

- **Interactive Dashboard:**  
  The [PortfolioSummary](d:/WebDev/crypto-portfolio-tracker/frontend/src/components/Dashboard/PortfolioSummary.js) component displays portfolio allocation via a dynamic line chart built with Chart.js.

- **Seamless API Integration:**  
  The Axios instance in [api.js](d:/WebDev/crypto-portfolio-tracker/frontend/src/services/api.js) automatically injects JWT tokens into request headers, ensuring secure communication between the frontend and backend.

## Why This Project?

- **User Experience:**  
  With a dynamic dashboard and real-time data integration, users can effortlessly track and manage their cryptocurrency investments.

- **Security:**  
  Secure password handling and JWT-based authentication protect user data and investments.

- **Scalability:**  
  The use of Flask and Docker ensures the backend scales, while the modular React frontend is easy to maintain and extend.

- **Modern Web Technologies:**  
  Leveraging current best practices in web development allows for a robust and responsive application design.