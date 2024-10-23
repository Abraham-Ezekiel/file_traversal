#!/usr/bin/env python3

import os

def validate_file_path(base_dir, user_input):
    user_path = os.path.realpath(user_input)
    base_path = os.path.realpath(base_dir)

    if not user_path.startswith(base_path):
        raise ValueError("Invalid file path")

    return user_path

# Example usage
base_directory = "/var/www/uploads"
user_input = "/var/www/uploads/../../etc/passwd"

try:
    validated_path = validate_file_path(base_directory, user_input)
    print("Validated path:", validated_path)
except ValueError as e:
    print(e)

