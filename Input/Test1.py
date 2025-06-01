import os

# Function to save profile data
def save_profile(first_name, middle_name, last_name, age):
    with open("profiles.txt", "a") as file:  # Append mode to save multiple profiles
        file.write(f"{first_name}\n{middle_name}\n{last_name}\n{age}\n")
    print("Profile saved successfully!")

# Function to load all profile data
def load_profiles():
    if os.path.exists("profiles.txt"):
        profiles = []
        with open("profiles.txt", "r") as file:
            lines = file.readlines()
            # Group every 4 lines as one profile (first, middle, last, and age)
            for i in range(0, len(lines), 4):
                first_name = lines[i].strip()
                middle_name = lines[i+1].strip()
                last_name = lines[i+2].strip()
                age = int(lines[i+3].strip())
                profiles.append((first_name, middle_name, last_name, age))
        return profiles
    else:
        print("No saved profiles found.")
        return []

# Function to delete a profile
def delete_profile(profile_index):
    profiles = load_profiles()
    if profiles and 0 <= profile_index < len(profiles):
        profiles.pop(profile_index)  # Remove the profile at the given index
        
        # Rewrite the remaining profiles back to the file
        with open("profiles.txt", "w") as file:
            for profile in profiles:
                first_name, middle_name, last_name, age = profile
                file.write(f"{first_name}\n{middle_name}\n{last_name}\n{age}\n")
        print("Profile deleted successfully!")
    else:
        print("Invalid profile index.")

while True:
    print("\n\n")
    print("  Choose:")
    choice = input(" [C]Create a profile, [L]Load all profiles, [D]Delete a profile, or [E]Exit? ").strip().lower()

    if choice == 'c':  # Create profile
        while True:
            print("---------------------------------------------------------")
            first_name = input("What is your first name? ")
            middle_name = input("What is your middle name? ")
            last_name = input("What is your last name? ")

            # Check if names contain only alphabetic characters
            if first_name.isalpha() and middle_name.isalpha() and last_name.isalpha():
                while True:
                    try:
                        age = int(input("How old are you? "))
                        print("---------------------------------------------------------")
                        break
                    except ValueError:
                        print("---------------------------------------------------------")
                        print("\033[91m \033[0m")
                        print("\033[91mPlease enter a valid age (a number).\033[0m")
                        print("\033[91m \033[0m")
                        print("---------------------------------------------------------")
                break
            else:
                print("---------------------------------------------------------")
                print("\033[91m \033[0m")
                print("\033[91mPlease enter valid names (only letters are allowed).\033[0m")
                print("\033[91m \033[0m")
                print("---------------------------------------------------------")

        # Save the profile
        save_profile(first_name, middle_name, last_name, age)

        # Print full name and age
        full_name = first_name + " " + middle_name + " " + last_name
        print('\nFull Name: ' + full_name + '\nAge: ' + str(age))

    elif choice == 'l':  # Load all profiles
        profiles = load_profiles()
        if profiles:
            print("---------------------------------------------------------")
            print("\nAll Saved Profiles:")
            for index, profile in enumerate(profiles):
                first_name, middle_name, last_name, age = profile
                full_name = first_name + " " + middle_name + " " + last_name
                print(f"{index + 1}. Full Name: {full_name}\n   Age: {age}")
            print("---------------------------------------------------------")
    
    elif choice == 'd':  # Delete a profile
        profiles = load_profiles()
        if profiles:
            print("---------------------------------------------------------")
            print("\nSelect a profile to delete:")
            for index, profile in enumerate(profiles):
                first_name, middle_name, last_name, age = profile
                full_name = first_name + " " + middle_name + " " + last_name
                print(f"{index + 1}. Full Name: {full_name}\n   Age: {age}")
        while True:   
            try:
                profile_index = int(input("\nEnter the profile number to delete: ")) - 1
                delete_profile(profile_index)
            except ValueError:
                print("---------------------------------------------------------")
                print("\033[91m \033[0m")
                print("\033[91mPlease enter a valid number.\033[0m")
                print("\033[91m \033[0m")
                print("---------------------------------------------------------")
            else:
                print("---------------------------------------------------------")
                print("\033[91m \033[0m")
                print("\033[91mNo profiles available to delete.\033[0m")
                print("---------------------------------------------------------")
    elif choice == 'e':  # Exit
        print("Exiting the program...")
        break  # Exit the program

    else:
        print("\033[91m \033[0m")
        print("\033[91mInvalid choice. Please enter 'C' to create, 'L' to load, 'D' to delete, or 'E' to exit.\033[0m")
        print("\033[91m \033[0m")
