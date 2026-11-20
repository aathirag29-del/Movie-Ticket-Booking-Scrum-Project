# Movie Ticket Booking System

## 1. Project Title and Brief Description

### Movie Ticket Booking System

The Movie Ticket Booking System is a web-based application developed as a mini-project using Flask, SQLite, HTML, CSS and JavaScript. It allows users to register and log in, search for movies and cinemas, view available show timings, select seats, make a demo payment, receive an e-ticket and view their booking history.

The project follows a Scrum-based development approach and uses Git and GitHub for version control.

---

## 2. Problem Statement and Objectives

### Problem Statement

Traditional movie ticket booking requires users to search for movies, check show timings, select seats and manage booking details through different steps. A simple centralized web application can make this process easier and more convenient.

### Objectives

- Provide a simple online movie ticket booking system.
- Allow users to register and securely log in.
- Allow users to search and filter movies and cinemas.
- Display available show timings.
- Allow users to select seats.
- Provide a demo online payment process.
- Generate an electronic ticket after booking.
- Allow users to view previous bookings.
- Provide movie reviews and recommendations.
- Demonstrate software development using Git, GitHub and Scrum practices.

---

## 3. Features / Modules Implemented

### User Registration and Login
- New user registration.
- Secure password hashing.
- User login and logout.
- Session-based authentication.

### Movie and Cinema Search
- Search movies by name.
- Search and filter available movies.
- Browse movie and cinema information.

### Show Timings
- Display available show dates and timings.
- Select a suitable show before booking.

### Seat Selection
- Display available and already-booked seats.
- Allow users to select seats.
- Prevent selection of unavailable seats.

### Booking and Checkout
- Calculate booking details and total amount.
- Confirm selected movie, show and seats.
- Provide demo payment options.

### Payment
The application provides a demonstration payment process using:

- UPI
- Card
- Net Banking

No real financial transaction is performed.

### E-Ticket
- Generate booking confirmation.
- Display movie, cinema, show and seat details.
- Provide an electronic ticket after successful booking.

### Booking History
- Users can view their previous bookings.
- Booking information is stored in the database.

### Reviews and Recommendations
- Users can provide movie reviews.
- Display movie recommendations and offers.

---

## 4. Technology Stack and Tools Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub
- Web Browser

### Version Control
- Git
- GitHub
- Feature branch
- Master branch
- Merge workflow

---

## 5. Prerequisites and Installation Steps

### Prerequisites

The following software is required:

- Python 3.x
- Git
- Web browser
- Internet connection for installing dependencies

### Installation Steps

1. Download or clone the project repository.

2. Open the project folder in the terminal.

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Make sure Python is installed correctly:

```bash
python --version
```

5. Run the Flask application:

```bash
python app.py
```

---

## 6. Instructions to Run the Application

1. Open Command Prompt or PowerShell.
2. Navigate to the project directory.

Example:

```bash
cd Movie_Ticket_Booking_Scrum_Project
```

3. Install dependencies if required:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
python app.py
```

5. Open a web browser.

6. Visit:

```text
http://127.0.0.1:5000
```

7. Register a new account or log in with an existing account.

8. Select a movie.

9. Select cinema and show timing.

10. Select available seats.

11. Continue to checkout.

12. Select a demo payment method.

13. Complete the booking.

14. View the generated e-ticket and booking history.

---

## 7. Sample Inputs and Outputs

### Sample Input

```text
Username: Aathira
Email: aathira@example.com
Password: ********

Movie: Leo
Cinema: City Cinema
Show: 07:00 PM
Seats: A5, A6
Payment Method: UPI
```

### Sample Output

```text
Booking Confirmed

Movie: Leo
Cinema: City Cinema
Show Time: 07:00 PM
Seats: A5, A6
Payment Status: Successful
Ticket Status: Confirmed
```

The application displays the booking confirmation and electronic ticket after successful completion of the booking process.

---

## 8. Testing Performed and Results

The application was tested for the major user workflows.

| Test Case | Expected Result | Status |
|---|---|---|
| User Registration | New account is created successfully | Passed |
| User Login | Registered user can log in | Passed |
| Movie Search | Matching movies are displayed | Passed |
| Cinema/Search Filtering | Relevant results are displayed | Passed |
| Show Selection | Available show timings are displayed | Passed |
| Seat Selection | Available seats can be selected | Passed |
| Booked Seat Handling | Already booked seats cannot be selected | Passed |
| Checkout | Booking details are displayed correctly | Passed |
| Demo Payment | Payment simulation completes successfully | Passed |
| E-Ticket | Ticket is generated after booking | Passed |
| Booking History | Previous bookings are displayed | Passed |
| Reviews | Users can submit movie reviews | Passed |
| Logout | User session is ended successfully | Passed |

---

## 9. Team Member Details and Individual Contributions

### Team Members

| Name | Register Number | Contribution |
|---|---|---|
| Aathira G | 2503917720522125 | Backend/application workflow, registration and login, movie search and filtering, booking and seat-selection workflow, Git/GitHub version control, README and project documentation |
| Ramya Sri S | 2503917720522198 | Frontend interface and page design, movie/show-time/checkout/e-ticket pages, reviews and recommendations, application testing, testing evidence and documentation |

Both team members contributed to the development, testing and documentation of the mini-project.

---

## 10. Known Limitations and Possible Future Enhancements

### Known Limitations

- Payment is currently a demo process and does not perform real transactions.
- Movie and cinema information is stored locally.
- Real-time movie availability is not connected to external services.
- Email and SMS notifications are not implemented.
- The application is currently intended for local/demo use.
- Advanced recommendation algorithms are not implemented.

### Future Enhancements

- Integrate real payment gateways.
- Add real-time movie and cinema information through APIs.
- Add email and SMS ticket notifications.
- Add QR code-based e-tickets.
- Improve the recommendation system using machine learning.
- Add administrator functionality for managing movies, cinemas, shows, and bookings.
- Add real-time seat availability.
- Deploy the application to a cloud platform.

---

## Project Status

The application has been implemented and tested as a working mini-project. The project uses Flask, SQLite, HTML, CSS and JavaScript and follows a Git-based development workflow with a feature branch and master branch.

## GitHub Repository

https://github.com/aathirag29-del/Movie-Ticket-Booking-Scrum-Project