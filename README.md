# Movie Ticket Booking Application

## 1. Project Description

The **Movie Ticket Booking Application** is a web-based application developed using Flask and SQLite. It provides a simple platform for users to browse movies, search and filter movies, select cinemas and show timings, choose seats, complete a demo payment, generate an e-ticket, view booking history, submit reviews, and receive personalized movie recommendations.

The application includes movies in **Tamil, English, Malayalam, and Telugu**.

---

## 2. Problem Statement and Objectives

### Problem Statement

Movie ticket booking involves checking movie details, show timings, cinema information, seat availability, and booking details. This project provides a simple web-based system that brings these activities together in one application.

### Objectives

- To develop a simple and user-friendly movie ticket booking application.
- To provide movie search and filtering facilities.
- To display cinema and show-time information.
- To allow users to select available seats.
- To provide a demo online payment process.
- To generate an electronic ticket after booking.
- To maintain booking history.
- To allow users to submit movie reviews.
- To provide personalized movie recommendations.

---

## 3. Features / Modules Implemented

### User Registration and Login
- User registration.
- User login and logout.
- Input validation.
- Password hashing.

### Movie Search and Filtering
- Browse available movies.
- Search movies by name.
- Filter movies by language.
- Filter movies by genre.

### Cinema and Show Timings
- Cinema selection.
- Show-time selection.
- Movie and cinema details.

### Seat Selection
- Display available and booked seats.
- Select seats for a booking.
- Supports selection of up to 8 seats.

### Demo Payment
- UPI payment.
- Card payment.
- Net Banking.
- Demo payment confirmation without real transactions.

### E-Ticket
- Booking confirmation.
- Selected movie, cinema, show timing, and seat details.
- E-ticket generation.

### Booking History
- View previous bookings.

### Reviews
- Submit movie ratings and reviews.

### Personalized Recommendations
- Recommendations based on preferred language.
- Highly rated movies and preferred genres are considered.

---

## 4. Technology Stack and Tools Used

| Component | Technology / Tool |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Database | SQLite |
| Version Control | Git |
| Repository | GitHub |
| Development | Visual Studio Code / PowerShell |
| Browser | Google Chrome / Microsoft Edge |

---

## 5. Prerequisites and Installation Steps

### Prerequisites

- Python 3.x
- Git
- Web browser
- Internet connection for installing Python packages

### Installation

#### Step 1: Clone the Repository

```powershell
git clone https://github.com/aathirag29-del/Movie-Ticket-Booking-Scrum-Project.git
```

#### Step 2: Enter the Project Folder

```powershell
cd Movie-Ticket-Booking-Scrum-Project
```

#### Step 3: Create a Virtual Environment

```powershell
python -m venv venv
```

#### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

#### Step 5: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 6. Instructions to Run the Application

Run the following command:

```powershell
python app.py
```

The Flask application will start on:

```text
http://127.0.0.1:5000
```

Open the above address in a web browser to access the application.

---

## 7. Sample Inputs and Outputs

### User Registration

**Input:**

```text
Name: Aathira
Email: aathira@example.com
Password: ********
```

**Output:**

```text
Registration successful
```

### Movie Search

**Input:**

```text
Search: Tamil
```

**Output:**

```text
Matching Tamil movies are displayed.
```

### Seat Selection

**Input:**

```text
Seats: A1, A2
```

**Output:**

```text
Selected seats: A1, A2
```

### Booking

**Input:**

```text
Movie: Selected Movie
Cinema: Selected Cinema
Show Time: Selected Show
Seats: A1, A2
Payment: Demo UPI
```

**Output:**

```text
Booking confirmed
E-ticket generated
```

---

## 8. Testing Performed and Results

The main features of the application were tested during development.

| Test Case | Expected Result | Result |
|---|---|---|
| User Registration | User can register successfully | Passed |
| User Login | Registered user can log in | Passed |
| Movie Search | Matching movies are displayed | Passed |
| Language Filter | Movies are filtered by language | Passed |
| Genre Filter | Movies are filtered by genre | Passed |
| Cinema Selection | Cinema can be selected | Passed |
| Show-Time Selection | Available show can be selected | Passed |
| Seat Selection | Available seats can be selected | Passed |
| Demo Payment | Payment confirmation is displayed | Passed |
| E-Ticket | Ticket is generated after booking | Passed |
| Booking History | Previous bookings are displayed | Passed |
| Reviews | User can submit a review | Passed |
| Recommendations | Recommended movies are displayed | Passed |

Detailed test cases are available in:

```text
docs/TEST_CASES.md
```

---

## 9. Team Members and Individual Contributions

### Team Member 1

**Name:** Aathira G  
**Register Number:** 2503917720522125  
**Contribution:**
- Developed the Flask backend and application workflow.
- Worked on user registration and login functionality.
- Implemented movie search, filtering, booking, and seat selection.
- Worked on Git and GitHub version control.
- Maintained the project README and documentation.

### Team Member 2

**Name:** Ramya Sri S  
**Register Number:** 2503917720522198  
**Contribution:**
- Worked on the frontend interface and page design.
- Worked on movie display, show-time, checkout, and e-ticket pages.
- Worked on reviews and movie recommendation features.
- Performed application testing and identified functional issues.
- Contributed to project documentation and testing evidence.

## 10. Known Limitations and Future Enhancements

### Known Limitations

- The payment system is a demo payment system and does not process real transactions.
- The application uses sample movie and cinema data.
- Real-time cinema availability is not implemented.
- Real-time seat synchronization is not implemented.
- The recommendation system uses simple rule-based logic.

### Future Enhancements

- Integration with a real payment gateway.
- Real-time movie and theatre availability.
- Real-time seat locking.
- Integration with external movie APIs.
- Advanced machine-learning-based recommendations.
- Email or SMS ticket notifications.
- QR code generation and ticket verification.
- Admin dashboard for managing movies, cinemas, shows, and bookings.
- Deployment to a cloud platform.
