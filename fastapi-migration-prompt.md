# Migrate Node.js Backend to Python FastAPI

This document outlines the steps and considerations for migrating an existing Node.js backend to Python FastAPI, focusing on retaining all functionality and adapting Node.js-specific implementations to Pythonic equivalents.

## Requirements

- Python 3.8 or newer
- Core Dependencies:

  - FastAPI >= 0.104.1
  - Uvicorn >= 0.24.0
  - Motor >= 3.3.1 (MongoDB async driver)
  - Pydantic >= 2.4.2
  - python-jose[cryptography] >= 3.3.0 (for JWT)
  - python-multipart >= 0.0.6
  - bcrypt >= 4.0.1
  - python-dotenv >= 1.0.0
  - email-validator >= 2.1.0.post1

- Development Dependencies:
  - pytest >= 7.4.3 (for testing)
  - black >= 23.11.0 (for code formatting)
  - isort >= 5.12.0 (for import sorting)

## Key Components to Migrate

1. **Data Insertion Scripts:**

   - Translate data insertion scripts used in Node.js to Python scripts.
   - Utilize SQLAlchemy for database interactions instead of Mongoose.
   - Ensure data integrity and relations are maintained during the translation.

2. **Middleware Implementation:**

   - Adapt authentication and error handling middleware from Express.js to FastAPI.
   - Use FastAPI dependencies to handle authentication.
   - Use `starlette` responses and requests within middleware for error handling.

3. **Security Measures:**
   - Replace `bcryptjs` with `python-bcrypt` for password hashing.
   - Replace `jsonwebtoken` with `python-jose` for JWT creation and verification.
   - Implement CORS using FastAPI's middleware.

### API Route Structure

The FastAPI application uses the following route prefixes:

1. `/api/users` - User-related operations

   - Authentication and user management
   - Nested cart operations
   - Nested restaurant operations

2. `/api/addresses` - Address management

   - Create, update, and delete delivery addresses
   - Manage user address book

3. `/api/home` - Home page operations

   - Featured restaurants
   - Offers and promotions
   - Landing page data

4. Base route `/`
   - Welcome message endpoint

Note: Consider reorganizing nested routes under `/api/users` into separate prefixes:

- Moving cart routes to `/api/cart`
- Moving restaurant routes to `/api/restaurants`

## Step-by-Step Migration Guide

### Setup Python Environment

- Set up a virtual environment: `python -m venv venv`
- Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `.\venv\Scripts\activate` (Windows)
- Install required packages: `pip install fastapi uvicorn sqlalchemy bcrypt python-jose aiohttp`

### Translate Data Models

- Convert Mongoose schemas to SQLAlchemy models.
- Define relationships and constraints as per the original schema.

### Rewrite Routes and Controllers

- Convert Express routes to FastAPI routes.
- Use FastAPI's dependency injection for clean architecture.

### Implement Security

- Adapt JWT handling mechanisms to use `python-jose`.
- Ensure secure password hashing with `bcrypt`.

### Error Handling

- Create custom exception handlers in FastAPI to manage different error types, similar to `errorMiddleware.js`.

### Test and Debug

- Write tests using FastAPI's test client.
- Ensure all endpoints function as expected with new Python implementations.

## Files to Migrate

### Data Insertion Scripts

1. `best_offers.py` - Migrated from bestOffersProduct.js
2. `seed_top_restaurants.py` - Migrated from topRestaurantsProduct.js
3. `seed_cuisines.py` - Migrated from filterCuisinesProduct.js
4. `all_restaurants.py` - Migrated from allRestaurants.js
5. `seed_restaurant_details.py` - Migrated from singleRestaurant.js

### Router Files

1. `restaurant_router.py` - Handles restaurant-related endpoints
2. `home_router.py` - Manages home page data endpoints
3. `cart_router.py` - Handles shopping cart operations
4. `address_router.py` - Manages user address operations

## Tips for a Successful Migration

- Keep the Node.js server running in parallel to the new FastAPI server during initial testing phases.
- Use Postman or similar tools to compare responses from both servers to ensure feature parity.
- Consider using Docker to containerize the FastAPI application for easy deployment and scalability.

## Additional Resources

- FastAPI Documentation: [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- SQLAlchemy Tutorial: [SQLAlchemy Docs](https://www.sqlalchemy.org/)

This prompt aims to guide the developer through the necessary steps to ensure a smooth and efficient migration from a Node.js backend to a Python FastAPI backend, maintaining all existing functionality and leveraging Python’s asynchronous capabilities.
