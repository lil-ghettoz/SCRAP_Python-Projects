#!/usr/bin/env python3
"""
phone_tracer.py - Updated version with fixes for empty region/carrier and country name cleanup.
See original comments for installation/usage.
"""

# Import required libraries (same as before)
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
from geopy.geocoders import Nominatim
from colorama import Fore, Style, init
init(autoreset=True)

def parse_phone_number(phone_str):
    """
    Parse the input phone string into a phonenumbers.PhoneNumber object.
    Returns None if invalid.
    """
    try:
        num = phonenumbers.parse(phone_str, None)
        if phonenumbers.is_valid_number(num):
            return num
        else:
            return None
    except phonenumbers.NumberParseException:
        return None

def get_phonenumbers_info(num):
    """
    Extract basic details using the phonenumbers library.
    Updated: Clean country name, ensure "Unknown" for empty fields, default region for mobiles.
    """
    # Get country name and clean it (remove extra like "(Republic of the)")
    country_raw = geocoder.country_name_for_number(num, 'en')
    country = country_raw.replace(" (Republic of the)", "").strip() if country_raw else "Unknown"
    
    # Get region/location description
    region_desc = geocoder.description_for_number(num, 'en') or ""  # Ensure not None
    # If empty or same as country, use "Mobile Network" for likely mobile numbers
    if not region_desc or region_desc == country_raw or region_desc == country:
        # Check if it's a mobile number
        if phonenumbers.number_type(num) == phonenumbers.PhoneNumberType.MOBILE:
            region = "Mobile Network"
        else:
            region = "Unknown"
    else:
        region = region_desc
    
    # Get carrier name (handle empty string as well as None)
    carrier_raw = carrier.name_for_number(num, 'en') or ""
    carrier_name = carrier_raw if carrier_raw else "Unknown"
    
    # Get timezone
    tz_list = timezone.time_zones_for_number(num)
    timezone_str = tz_list[0] if tz_list else "Unknown"
    
    return country, region, carrier_name, timezone_str

def get_api_info(num_str, api_key):
    """
    Fetch additional details from numverify API if key is provided.
    (Unchanged from original)
    """
    if not api_key:
        return None
    
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={num_str}&format=1"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('valid', False):
            return {
                'country_name': data.get('country_name', 'Unknown'),
                'location': data.get('location', 'Unknown'),
                'carrier': data.get('carrier', 'Unknown')
            }
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"⚠️  API request failed: {str(e)}. Using basic info only.")
        return None
    except ValueError:
        print(Fore.YELLOW + "⚠️  Invalid API response. Using basic info only.")
        return None

def get_coordinates(city, country):
    """
    Use geopy to get latitude and longitude.
    Updated: Handle "Mobile Network" by skipping (no specific coords).
    """
    if city in ["Unknown", "Mobile Network"] or not city:
        return None, None
    
    geolocator = Nominatim(user_agent="phone_tracer")
    try:
        full_query = f"{city}, {country}"
        location = geolocator.geocode(full_query, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except Exception as e:
        print(Fore.YELLOW + f"⚠️  Geocoding failed for '{full_query}': {str(e)}")
        return None, None

def main():
    """
    Main function: Updated to warn if API key is skipped.
    """
    phone_input = input(Fore.CYAN + "Enter phone number (e.g., +639171234567): ").strip()
    
    num = parse_phone_number(phone_input)
    if not num:
        print(Fore.RED + "❌ Invalid phone number. Please provide in international format (e.g., +countrycode).")
        return
    
    api_key = input(Fore.CYAN + "Enter numverify API key (press Enter to skip geolocation): ").strip()
    if not api_key:
        print(Fore.YELLOW + "⚠️  Skipping API—region/carrier may be limited. Enter key for better results!")
    
    country, region, carrier_name, timezone_str = get_phonenumbers_info(num)
    
    api_data = get_api_info(str(num), api_key) if api_key else None
    if api_data:
        country = api_data['country_name']
        api_location = api_data['location']
        if api_location != "Unknown":
            region = api_location
        if api_data['carrier'] != "Unknown":
            carrier_name = api_data['carrier']
    
    lat, lon = get_coordinates(region, country)
    
    print(Fore.CYAN + f"\n🔍 Tracing phone number: {phone_input}")
    print(Fore.GREEN + f"🌍 Country: {country}")
    print(Fore.GREEN + f"📍 Region: {region}")
    print(Fore.GREEN + f"🏢 Carrier: {carrier_name}")
    print(Fore.GREEN + f"🕐 Timezone: {timezone_str}")
    if lat is not None and lon is not None:
        lat_dir = "N" if lat >= 0 else "S"
        lon_dir = "E" if lon >= 0 else "W"
        print(Fore.GREEN + f"📡 Coordinates: {abs(lat):.4f}° {lat_dir}, {abs(lon):.4f}° {lon_dir}")
    print(Fore.GREEN + "✅ Status: Valid Number")

if __name__ == "__main__":
    main()