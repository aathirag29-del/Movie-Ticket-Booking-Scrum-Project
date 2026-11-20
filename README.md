# Movie Ticket Booking Application

**Agile/Scrum Mini-Project — Assignment 2**

A Flask + SQLite movie ticket booking application that allows users to register, browse movies, search and filter movies, select cinema and show timings, choose seats, complete a demo payment, receive an e-ticket, view booking history, submit reviews, and get personalized movie recommendations.

## 1. Project Title and Brief Description

### Project Title
**Movie Ticket Booking Application**

### Description
The Movie Ticket Booking Application is a web-based application developed using Flask and SQLite. It provides a simple platform for users to browse movies, select shows, choose seats, complete a demo payment, and manage their bookings.

The application includes Tamil, English, Malayalam, and Telugu movies and provides a responsive user interface.

## 2. Problem Statement and Objectives

### Problem Statement

Traditional movie ticket booking requires users to check movie details, show timings, seat availability, and booking information separately. This project provides a single web application to simplify the movie ticket booking process.

### Objectives

- Provide user registration and login.
- Allow users to browse available movies.
- Provide movie search and filtering.
- Display cinema and show timings.
- Allow users to select available seats.
- Provide a demo online payment process.
- Generate an e-ticket after successful booking.
- Maintain booking history.
- Allow users to submit movie reviews.
- Provide personalized movie recommendations.

## 3. Features / Modules Implemented

### User Management
- User registration.
- User login and logout.
- Password hashing and validation.

### Movie Browsing
- 16 sample movies.
- Tamil, English, Malayalam, and Telugu movies.
- Search by movie name.
- Filter by language and genre.
- Movie details and show information.

### Cinema and Show Timings
- Cinema selection.
- Available show timings.
- Movie and show selection.

### Seat Selection
- Interactive seat selection.
- Selection of 1–8 seats.
- Already-booked seats are displayed as unavailable.

### Payment
- Demo UPI payment.
- Demo Card payment.
- Demo Net Banking payment.
- Payment validation.

> This is a demonstration payment system and does not process real money.

### E-Ticket
- Booking confirmation.
- Ticket generation.
- Movie, cinema, show, seat, and booking details.

### Booking History
- Users can view their previous bookings.

### Reviews
- Users can submit movie ratings and reviews.
- Ratings are used by the recommendation feature.

### Personalized Recommendations
The recommendation system uses the user's preferred language and highly rated movie genres to suggest suitable movies.

## 4. Technology Stack and Tools Used

| Category | Technology / Tool |
|---|---|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python, Flask |
| Database | SQLite |
| Authentication | Werkzeug Password Hashing |
| Version Control | Git |
| Repository | GitHub |
| Development Tool | Visual Studio Code / Any Code Editor |
| Browser | Google Chrome / Microsoft Edge |

## 5. Prerequisites and Installation Steps

### Prerequisites

The following software is required:

- Python 3.x
- Git
- Web browser
- Internet connection for initial package installation

### Installation

Clone the repository:

```powershell
git clone https://github.com/aathirag29-del/Movie-Ticket-Booking-Scrum-Project.git
```

Navigate to the project folder:

```powershell
cd Movie-Ticket-Booking-Scrum-Project
```

Create a virtual environment:

```powershell
python -m venv venv
```

Activate the virtual environment in Windows PowerShell:

```powershell
venv\Scripts\activate
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

## 6. Instructions to Run the Application

Run the Flask application:

```powershell
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open the above address in a web browser.

### Basic Usage

1. Register a new account.
2. Login using the registered account.
3. Browse available movies.
4. Search or filter movies.
5. Select a movie.
6. Select cinema and show timing.
7. Choose available seats.
8. Continue to checkout.
9. Select a demo payment method.
10. Confirm the booking.
11. View the generated e-ticket.
12. Check booking history.
13. Submit reviews and view recommendations.

## 7. Sample Inputs and Outputs

### Sample Input

```text
Username: Aathira
Email: aathira@example.com
Password: ********

Movie: Retro
Language: Tamil
Show Time: 06:30 PM
Seats: A1, A2
Payment Method: UPI
```

### Sample Output

```text
Booking Confirmed

Movie: Retro
Show Time: 06:30 PM
Seats: A1, A2
Payment Status: Successful
E-Ticket: Generated
```

### Movie Search Example

```text
Search: Tamil
```

Output:

```text
Tamil movies matching the selected search/filter criteria are displayed.
```

## 8. Testing Performed and Results

The application was tested for the major functional modules.

| Test Case | Expected Result | Status |
|---|---|---|
| User Registration | New user account is created | Passed |
| User Login | Valid user can login | Passed |
| Invalid Login | Invalid credentials are rejected | Passed |
| Movie Search | Matching movies are displayed | Passed |
| Language Filter | Movies of selected language are displayed | Passed |
| Genre Filter | Movies of selected genre are displayed | Passed |
| Show Selection | Available shows are displayed | Passed |
| Seat Selection | Available seats can be selected | Passed |
| Booked Seat Check | Already booked seats cannot be selected | Passed |
| Demo Payment | Valid payment details are accepted | Passed |
| E-Ticket | Ticket is generated after booking | Passed |
| Booking History | Previous bookings are displayed | Passed |
| Review Submission | User can submit a review | Passed |
| Recommendations | Suitable movies are recommended | Passed |

## 9. Team Member Details and Individual Contributions

### Team Members

| Team Member | Register Number | Contribution |
|---|---|---|
| Aathira G | 2503917720522125 | Backend/application workflow, registration and login, movie search/filtering, booking and seat-selection workflow, Git/GitHub version control, README and project documentation |
| Ramya Sri S | 2503917720522198 | Frontend interface and page design, movie/show-time/checkout/e-ticket pages, reviews and recommendations, application testing, testing evidence and documentation |

### Scrum / Development Workflow

The project was developed using an Agile/Scrum-oriented workflow.

- **Sprint 1:** Registration and Login
- **Sprint 2:** Movie Search, Filtering and Show Timings
- **Sprint 3:** Seat Selection and Booking
- **Sprint 4:** Demo Payment and E-Ticket
- **Sprint 5:** Booking History, Reviews and Recommendations

Git and GitHub were used to maintain the project source code and development history. A separate feature branch was used for development before integration into the main branch.

## 10. Known Limitations and Possible Future Enhancements

### Limitations

- Payment is a demo implementation and does not process real transactions.
- Movie and cinema information is based on sample data.
- The application does not use a live movie or cinema API.
- Seat availability is maintained within the application database.
- Recommendations use a simple rule-based approach.

### Future Enhancements

- Integrate real payment gateways.
- Add real-time movie and cinema information through APIs.
- Add email and SMS ticket notifications.
- Add QR code-based e-tickets.
- Improve the recommendation system using machine learning.
- Add administrator functionality for managing movies, cinemas, shows, and bookings.
- Add real-time seat availability.
- Deploy the application to a cloud platform.

## Project Status

The application has been implemented and tested as a working mini-project. The project uses Flask, SQLite, HTML, CSS and JavaScript and follows a Git-based development workflow with a feature branch and master branch.

## GitHub Repository

https://github.com/aathirag29-del/Movie-Ticket-Booking-Scrum-Project