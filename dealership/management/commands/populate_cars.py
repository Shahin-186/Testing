from django.core.management.base import BaseCommand
from dealership.models import Car


class Command(BaseCommand):
    help = 'Populate the database with sample car data'

    def handle(self, *args, **kwargs):
        # Clear existing cars
        Car.objects.all().delete()
        
        sample_cars = [
            {
                'make': 'Toyota',
                'model': 'Camry',
                'year': 2024,
                'price': 28500.00,
                'condition': 'new',
                'color': 'Silver',
                'mileage': 0,
                'description': 'Brand new 2024 Toyota Camry with advanced safety features and excellent fuel economy.',
                'vin': '1HGBH41JXMN109186',
            },
            {
                'make': 'Honda',
                'model': 'Civic',
                'year': 2023,
                'price': 24000.00,
                'condition': 'certified',
                'color': 'Blue',
                'mileage': 12000,
                'description': 'Certified pre-owned Honda Civic in excellent condition with low mileage.',
                'vin': '2HGFG12848H542391',
            },
            {
                'make': 'Ford',
                'model': 'F-150',
                'year': 2023,
                'price': 42000.00,
                'condition': 'new',
                'color': 'Black',
                'mileage': 0,
                'description': 'Powerful Ford F-150 pickup truck, perfect for work or adventure.',
                'vin': '1FTFW1E84MFB12345',
            },
            {
                'make': 'Tesla',
                'model': 'Model 3',
                'year': 2022,
                'price': 38000.00,
                'condition': 'used',
                'color': 'White',
                'mileage': 25000,
                'description': 'Electric Tesla Model 3 with autopilot, excellent battery health.',
                'vin': '5YJ3E1EA1JF012345',
            },
            {
                'make': 'BMW',
                'model': 'X5',
                'year': 2023,
                'price': 65000.00,
                'condition': 'certified',
                'color': 'Gray',
                'mileage': 8000,
                'description': 'Luxury BMW X5 SUV with premium interior and advanced technology.',
                'vin': 'WBAJL4C55HG567890',
            },
            {
                'make': 'Chevrolet',
                'model': 'Malibu',
                'year': 2021,
                'price': 18500.00,
                'condition': 'used',
                'color': 'Red',
                'mileage': 35000,
                'description': 'Reliable Chevrolet Malibu with comfortable ride and good fuel efficiency.',
                'vin': '1G1ZD5ST5MF123456',
            },
            {
                'make': 'Mercedes-Benz',
                'model': 'C-Class',
                'year': 2024,
                'price': 55000.00,
                'condition': 'new',
                'color': 'Black',
                'mileage': 0,
                'description': 'Elegant Mercedes-Benz C-Class with premium features and superior performance.',
                'vin': 'WDDWF8EB5KR234567',
            },
            {
                'make': 'Nissan',
                'model': 'Altima',
                'year': 2022,
                'price': 21000.00,
                'condition': 'used',
                'color': 'Silver',
                'mileage': 28000,
                'description': 'Well-maintained Nissan Altima with spacious interior.',
                'vin': '1N4BL4BV5NC345678',
            },
            {
                'make': 'Jeep',
                'model': 'Wrangler',
                'year': 2023,
                'price': 39000.00,
                'condition': 'certified',
                'color': 'Green',
                'mileage': 15000,
                'description': 'Adventure-ready Jeep Wrangler with 4x4 capability.',
                'vin': '1C4HJXDG2KW456789',
            },
            {
                'make': 'Audi',
                'model': 'A4',
                'year': 2024,
                'price': 48000.00,
                'condition': 'new',
                'color': 'White',
                'mileage': 0,
                'description': 'Sophisticated Audi A4 with cutting-edge technology and refined design.',
                'vin': 'WAUFFAFL5DA567890',
            },
        ]
        
        created_count = 0
        for car_data in sample_cars:
            car = Car.objects.create(**car_data)
            created_count += 1
            self.stdout.write(self.style.SUCCESS(f'Created: {car}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} sample cars!'))
