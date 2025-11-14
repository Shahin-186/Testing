# Car Dealership Django App

A simple Django web application for managing a car dealership inventory. This application allows users to browse available cars, view detailed information about each vehicle, and provides an admin interface for managing the inventory.

## Features

- **Home Page**: Welcome page with featured cars and dealership statistics
- **Car Listing**: Browse all available cars with filtering options (condition, make, max price)
- **Car Details**: Detailed view of individual cars with all specifications
- **Admin Interface**: Full-featured Django admin for managing car inventory
- **Responsive Design**: Modern, clean UI with gradient styling
- **Sample Data**: Pre-populated with 10 sample cars for demonstration

## Screenshots

### Home Page
![Home Page](https://github.com/user-attachments/assets/a86988b5-830a-405d-af55-ea568e07cba1)

### Car Inventory
![Car List](https://github.com/user-attachments/assets/d0e729ae-ea56-47da-9006-04ca76df091c)

### Car Details
![Car Detail](https://github.com/user-attachments/assets/c6e1b8f1-1640-423f-a044-0065348317c8)

### Admin Interface
![Admin Page](https://github.com/user-attachments/assets/7bad3760-b416-4f5b-97c2-29211a6d548b)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shahin-186/Testing.git
   cd Testing
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser (for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Populate sample data (optional)**
   ```bash
   python manage.py populate_cars
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Home page: http://localhost:8000/
   - Car list: http://localhost:8000/cars/
   - Admin interface: http://localhost:8000/admin/

## Default Admin Credentials

If using the pre-configured setup:
- **Username**: admin
- **Password**: admin123

⚠️ **Note**: Change these credentials in production!

## Car Model

The Car model includes the following fields:

- **make**: Car manufacturer (e.g., Toyota, Ford)
- **model**: Car model name
- **year**: Manufacturing year
- **price**: Price in USD
- **condition**: New, Used, or Certified Pre-Owned
- **color**: Exterior color
- **mileage**: Mileage in miles
- **description**: Detailed description
- **vin**: Vehicle Identification Number (unique)
- **is_available**: Availability status
- **created_at**: Timestamp when added
- **updated_at**: Timestamp of last update

## Usage

### Browsing Cars
- Visit the home page to see featured cars
- Click "Browse All Cars" to view the complete inventory
- Use filters to narrow down your search by condition, make, or price

### Viewing Car Details
- Click "View Details" on any car card to see complete information
- View specifications, description, and availability status
- Contact sales or schedule test drives (demo buttons)

### Admin Management
- Log in to the admin interface at `/admin/`
- Add, edit, or delete cars from the inventory
- Filter cars by condition, availability, make, or year
- Search cars by make, model, VIN, or description
- Toggle availability status directly from the list view

## Project Structure

```
Testing/
├── car_dealership/          # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI configuration
├── dealership/              # Main application
│   ├── admin.py             # Admin interface configuration
│   ├── models.py            # Car model definition
│   ├── views.py             # View logic
│   ├── urls.py              # App URL routing
│   ├── templates/           # HTML templates
│   │   └── dealership/
│   │       ├── base.html    # Base template
│   │       ├── home.html    # Home page
│   │       ├── car_list.html    # Car listing page
│   │       └── car_detail.html  # Car detail page
│   └── management/          # Custom management commands
│       └── commands/
│           └── populate_cars.py  # Sample data generator
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Technologies Used

- **Django 5.2.8**: Python web framework
- **SQLite**: Database (default)
- **HTML/CSS**: Frontend styling
- **Python 3.12**: Programming language

## Contributing

Feel free to submit issues or pull requests to improve the application.

## License

This project is open source and available for educational purposes.