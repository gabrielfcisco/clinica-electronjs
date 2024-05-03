# ElectronJS Login System with Django API

This project is a login system built with ElectronJS for the frontend and Django for the backend API. It allows users to register, login, and manage their profiles, including automatic address retrieval based on the provided ZIP code.

## Features

- User authentication and authorization
- User registration with automatic address retrieval
- CRUD operations for user management
- Integration with external API for address retrieval

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gabrielfcisco/login-electronjs.git
   ```
2. **Install dependencies:**

    - Navigate to the project directory and install Node.js dependencies:
    
        ```bash
        cd electron
        npm install
        ```

3. **Run the application:**

   - Start the ElectronJS application:

     ```bash
     npm start
     ```

   - Build and run the Django API using Docker:

     ```bash
     cd django_api
     docker compose up -d --build
     ```

4. **Access the application:**

   - Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the ElectronJS application.

## Testing
To run tests, execute the following commands:
- For ElectronJS tests:
```bash
npm test
```
- For Django API tests:
```bash
docker exec -it api bash
python manage.py test
```

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).
