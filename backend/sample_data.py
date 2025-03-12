from datetime import date

services = [
    {
        "name": "Home Cleaning",
        "description": "Complete house cleaning including rooms, kitchen, bathrooms, and windows",
        "price": 999.0,
        "time_required": 240
    },
    {
        "name": "Electrical Work",
        "description": "All electrical services including repairs, installations and maintenance",
        "price": 499.0,
        "time_required": 120
    },
    {
        "name": "Plumbing Services",
        "description": "Comprehensive plumbing solutions including repairs, installations and unclogging",
        "price": 599.0,
        "time_required": 120
    },
    {
        "name": "Carpentry",
        "description": "Furniture assembly, repairs, and custom woodworking solutions",
        "price": 799.0,
        "time_required": 180
    },
    {
        "name": "Beauty Services",
        "description": "Professional beauty and grooming services at home",
        "price": 699.0,
        "time_required": 120
    },
    {
        "name": "Home Cooking",
        "description": "Professional cooking services for daily meals or special events",
        "price": 899.0,
        "time_required": 180
    },
    {
        "name": "Painting",
        "description": "Interior and exterior painting services with proper finishing",
        "price": 2999.0,
        "time_required": 480
    },
    {
        "name": "Gardening",
        "description": "Garden maintenance, landscaping and plant care services",
        "price": 799.0,
        "time_required": 180
    },
    {
        "name": "Pest Control",
        "description": "Complete pest elimination and prevention services for your home",
        "price": 699.0,
        "time_required": 120
    },
]

customers = [
    {
        'email': 'customer1@example.com',
        'name': 'Customer 1',
        'location': 'XYZ',
        'pincode': '123456'
    },
    {
        'email': 'customer2@example.com',
        'name': 'Customer 2',
        'location': 'ABC',
        'pincode': '345678'
    },
]

professionals = [
    {
        'email': 'professional1@example.com',
        'name': 'Professional 1',
        'location': 'XYZ',
        'pincode': '123456',
        'service_id': 1,
    },
    {
        'email': 'professional2@example.com',
        'name': 'Professional 2',
        'location': 'ABC',
        'pincode': '123456',
        'service_id': 1,
    },
    {
        'email': 'professional3@example.com',
        'name': 'Professional 3',
        'location': 'PQR',
        'pincode': '123456',
        'service_id': 2,
    }
]

service_requests = [
    {
        'customer_id': 1,
        'professional_id': 1,
        'service_id': 1,
        'status': 'completed',
        'service_date': date(2025, 3, 10),
        'rating': 5,
        'remarks': 'Excellent service!'
    },
    {
        'customer_id': 1,
        'professional_id': 1,
        'service_id': 1,
        'status': 'accepted',
        'service_date': date(2025, 3, 20),
        'rating': None,
        'remarks': None
    },
    {
        'customer_id': 1,
        'professional_id': 1,
        'service_id': 1,
        'status': 'requested',
        'service_date': date(2025, 3, 20),
        'rating': None,
        'remarks': None
    }
]
