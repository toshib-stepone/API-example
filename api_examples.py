"""
API Integration — Examples
===========================
"""

import json
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def example_1_get_user() -> None:
    print("EXAMPLE 1: GET one user")
    response = requests.get(f"{BASE_URL}/users/1", timeout=10)
    print("Status:", response.status_code)
    if response.status_code == 200:
        user = response.json()
        print("Name:", user["name"])
        print("Email:", user["email"])


def example_2_get_all_users() -> None:
    print("\nEXAMPLE 2: GET all users (first 3)")
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    users = response.json()
    for user in users[:3]:
        print(f"- {user['id']}: {user['name']}")


def example_3_post_data() -> None:
    print("\nEXAMPLE 3: POST new post")
    new_post = {"title": "Internship", "body": "Learning API", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())


def example_4_save_api_to_json() -> None:
    print("\nEXAMPLE 4: Save API data to JSON file")
    from pathlib import Path

    response = requests.get(f"{BASE_URL}/users/2", timeout=10)
    user = response.json()
    file_path = Path(__file__).parent / "user_from_api.json"
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(user, file, indent=2)
    print(f"Saved API data to {file_path.name}")


def example_5_handle_errors() -> None:
    print("\nEXAMPLE 5: Handle API errors")
    try:
        response = requests.get(f"{BASE_URL}/users/9999", timeout=10)
        if response.status_code == 404:
            print("User not found on server")
        else:
            print(response.json())
    except requests.RequestException as error:
        print("Network error:", error)


if __name__ == "__main__":
    example_1_get_user()
    example_2_get_all_users()
    example_3_post_data()
    example_4_save_api_to_json()
    example_5_handle_errors()
    print("\nAPI examples completed.")
