# django-core-api

## 🚀 Live Demo
[View Live Application](https://achi717.pythonanywhere.com/login/?next=/dashboard/)

## Description
This project serves as the backend for a Django-based web application, providing robust API endpoints, user authentication, and data management. It's a foundational component for a full-stack solution.

## Architecture
This project follows a standard Django application architecture, utilizing a Model-View-Controller (MVC) pattern (though Django refers to it as MVT - Model-View-Template). It integrates with PostgreSQL for data persistence and is designed to be consumed by a separate frontend application or through API clients.

## Key Features
*   **User Authentication:** Secure user registration, login, and session management.
*   **API Endpoints:** RESTful API for various data operations.
*   **Data Management:** Efficient handling and storage of application data.
*   **Scalable Design:** Built with Django's robust framework for future scalability.

## Technologies
- Python
- Django REST Framework
- PostgreSQL
- Docker
- python-decouple

## Installation
To set up the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/achiko10/django-core-api.git
    cd django-core-api
    ```

2.  **Set up environment variables:**
    Create a `.env` file in the root directory based on `.env.example`:
    ```
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

3.  **Using Docker (Recommended):**
    ```bash
    docker-compose up --build
    ```
    This will build the Docker images, set up the PostgreSQL database, and run the Django application.

4.  **Without Docker (Manual Setup):**
    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

## Usage
This is a backend service. Interact with its API endpoints using tools like Postman or integrate it with a frontend application. Refer to the API documentation (if available) for details.

## Testing
Basic unit tests are included to ensure core functionalities are working as expected.
To run tests:
```bash
python manage.py test
```

## Future Enhancements
*   Implement comprehensive integration tests.
*   Add CI/CD pipeline for automated testing and deployment.
*   Extend API with more advanced features and optimizations.

# django-core-api

## 🚀 ცოცხალი დემო
[აპლიკაციის ნახვა](https://achi717.pythonanywhere.com/login/?next=/dashboard/)

## აღწერა
ეს პროექტი წარმოადგენს Django-ზე დაფუძნებული ვებ აპლიკაციის ბექენდს, რომელიც უზრუნველყოფს მძლავრ API ენდპოინტებს, მომხმარებლის ავთენტიფიკაციას და მონაცემთა მართვას. ის არის სრული სტეკის გადაწყვეტის ფუნდამენტური კომპონენტი.

## არქიტექტურა
ეს პროექტი მიჰყვება სტანდარტულ Django აპლიკაციის არქიტექტურას, იყენებს Model-View-Controller (MVC) პატერნს (თუმცა Django მას MVT - Model-View-Template-ად მოიხსენიებს). ის ინტეგრირებულია PostgreSQL-თან მონაცემთა მუდმივობისთვის და შექმნილია იმისთვის, რომ მოიხმაროს ცალკე ფრონტენდ აპლიკაციამ ან API კლიენტებმა.

## ძირითადი მახასიათებლები
*   **მომხმარებლის ავთენტიფიკაცია:** მომხმარებლის უსაფრთხო რეგისტრაცია, შესვლა და სესიის მართვა.
*   **API ენდპოინტები:** RESTful API სხვადასხვა მონაცემთა ოპერაციებისთვის.
*   **მონაცემთა მართვა:** აპლიკაციის მონაცემების ეფექტური დამუშავება და შენახვა.
*   **მასშტაბირებადი დიზაინი:** აგებულია Django-ს მძლავრ ფრეიმვორკზე მომავალი მასშტაბირებისთვის.

## ტექნოლოგიები
- Python
- Django REST Framework
- PostgreSQL
- Docker
- python-decouple

## ინსტალაცია
პროექტის ლოკალურად გასაშვებად, მიჰყევით ამ ნაბიჯებს:

1.  **რეპოზიტორის კლონირება:**
    ```bash
    git clone https://github.com/achiko10/django-core-api.git
    cd django-core-api
    ```

2.  **გარემო ცვლადების დაყენება:**
    შექმენით `.env` ფაილი ძირ საქაღალდეში `.env.example`-ის მიხედვით:
    ```
    SECRET_KEY=your-secret-key-here
    DEBUG=True
    DATABASE_URL=postgres://user:password@localhost:5432/dbname
    ```

3.  **Docker-ის გამოყენებით (რეკომენდებულია):**
    ```bash
    docker-compose up --build
    ```
    ეს ააწყობს Docker-ის იმიჯებს, დააყენებს PostgreSQL მონაცემთა ბაზას და გაუშვებს Django აპლიკაციას.

4.  **Docker-ის გარეშე (ხელით დაყენება):**
    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

## გამოყენება
ეს არის ბექენდ სერვისი. მასთან ინტერაქცია შესაძლებელია API ენდპოინტების მეშვეობით ისეთი ხელსაწყოების გამოყენებით, როგორიცაა Postman, ან მისი ინტეგრირება ფრონტენდ აპლიკაციასთან. დეტალებისთვის იხილეთ API დოკუმენტაცია (ასეთის არსებობის შემთხვევაში).

## ტესტირება
ძირითადი Unit ტესტები შედის, რათა უზრუნველყოფილი იყოს ძირითადი ფუნქციონალურობის გამართული მუშაობა.
ტესტების გასაშვებად:
```bash
python manage.py test
```

## სამომავლო გაუმჯობესებები
*   სრული ინტეგრაციის ტესტების დანერგვა.
*   CI/CD კონვეიერის დამატება ავტომატური ტესტირებისა და დეპლოიმენტისთვის.
*   API-ის გაფართოება უფრო მოწინავე ფუნქციებითა და ოპტიმიზაციებით.
