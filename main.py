import importlib
import sys

# ==========================================
# 1. VISUAL ANCHORS & UTILITIES
# ==========================================

# 16x16 Grid ASCII Art Logo (PyChallenge Manager)
MENU_ART = """
+--------------+

|  __   __   __ |
| |__) /  ` |__) |
| |    \\__, |    |
|  __           |
| /  ` |__|  /\ |
| \\__, |  | /~~\\|
| |    |  |     |
| |    |__|     |
|  ___  ___  ___|
| |__  |__  |__ |
| |___ |___ |___|
|               |
|  [M E N U]    |
+--------------+
"""

def clear_screen():
    """Prints a separator to keep the terminal readable."""
    print("\n" + "="*40 + "\n")

def check_and_run_module(module_name, quiet_missing=False):
    """
    Attempts to import and run a module.
    Returns True if the file exists and runs, False if the file is missing.
    """
    try:
        misc = importlib.import_module(module_name)
        print(f"\n[Loading] {module_name}...")
        if hasattr(misc, 'main'):
            misc.main()
        else:
            print(f"[Error] {module_name} has no main() function defined.")
        return True
    except ModuleNotFoundError as e:
        # Verify the missing module is the file itself and not an internal import error
        if e.name == module_name:
            if not quiet_missing:
                print(f"[Skip] {module_name}.py not found.")
            return False
        else:
            # The file exists but failed inside because it tried to import a broken dependency
            print(f"\n[Error] {module_name}.py failed internal import: {e}")
            return True
    except Exception as e:
        print(f"\n[Error] Failed running {module_name}: {e}")
        return True

# ==========================================
# 2. MENU FUNCTIONS
# ==========================================

def run_all_challenges_unlimited():
    """Mode 1: Automatically steps through an unlimited number of days and challenges."""
    print("\n--- Mode 1: Run All Challenges Sequence (Unlimited Days) ---")
    challenges_per_day = int(input("Max challenges per day: "))
    
    day = 1
    while True:
        day_had_any_files = False
        print(f"\nChecking files for Day {day}...")
        
        for c in range(1, challenges_per_day + 1):
            file_exists = check_and_run_module(f"day{day}challenge{c}", quiet_missing=True)
            if file_exists:
                day_had_any_files = True
        
        # If absolutely no challenges were found for this day, stop the infinite sequence loop
        if not day_had_any_files:
            print(f"\n[Finished] No files found for Day {day}. Sequence concluded.")
            break
            
        day += 1

def skip_to_challenge():
    """Mode 2: Instantly skips to and runs one specific challenge file."""
    print("\n--- Mode 2: Skip to Specific Challenge ---")
    day = int(input("Target Day number: "))
    challenge = int(input("Target Challenge number: "))
    check_and_run_module(f"day{day}challenge{challenge}")

def run_range_on_day_one():
    """Mode 3: Runs challenges from 1 up to a specified number strictly on Day 1."""
    print("\n--- Mode 3: Day 1 Range Loop (1 -> X) ---")
    end_challenge = int(input("Run Day 1 challenges from 1 up to what number?: "))
    
    for c in range(1, end_challenge + 1):
        check_and_run_module(f"day1challenge{c}")

def skip_to_day_project():
    """Mode 4: Skips directly to a base day file without a challenge suffix."""
    print("\n--- Mode 4: Open Day Project (No Suffix) ---")
    day = int(input("Target Day project number: "))
    check_and_run_module(f"day{day}")

def run_all_day_projects_unlimited():
    """Mode 5: Steps through an unlimited number of suffixless day projects (day1, day2...)."""
    print("\n--- Mode 5: Run All Base Day Projects (Unlimited Days) ---")
    
    day = 1
    while True:
        file_exists = check_and_run_module(f"day{day}", quiet_missing=True)
        
        # Stops as soon as a consecutive base day file is missing
        if not file_exists:
            print(f"\n[Finished] No project file found for Day {day}. Sequence concluded.")
            break
            
        day += 1

# ==========================================
# 3. MAIN RUNNER & MENU LOOP
# ==========================================

def main_menu():
    while True:
        clear_screen()
        print(MENU_ART)
        print(" PYTHON CHALLENGE ARCHIVE")
        print("1. Run all challenges sequentially (Unlimited Days)")
        print("2. Skip directly to a specific challenge (dayXchallengeY)")
        print("3. Loop Day 1 challenges (from 1 to specified number)")
        print("4. Skip to a specific day project (dayX only)")
        print("5. Run all base day projects sequentially (Unlimited Days)")
        print("6. Exit Program")
        
        choice = input("\nSelect an option (1-6): ").strip()
        
        if choice == "1":
            run_all_challenges_unlimited()
        elif choice == "2":
            skip_to_challenge()
        elif choice == "3":
            run_range_on_day_one()
        elif choice == "4":
            skip_to_day_project()
        elif choice == "5":
            run_all_day_projects_unlimited()
        elif choice == "6":
            print("\nExiting. Happy coding!")
            sys.exit()
        else:
            print("\n[Invalid Selection] Please choose a number between 1 and 6.")
        
        input("\nPress Enter to return to the Main Menu...")

if __name__ == "__main__":
    main_menu()
    import importlib
    import sys
    
    # ==========================================
    # 1. VISUAL ANCHORS & UTILITIES
    # ==========================================
    
    # 16x16 Grid ASCII Art Logo (PyChallenge Manager)
    MENU_ART = """
    +--------------+
    
    |  __   __   __ |
    | |__) /  ` |__) |
    | |    \\__, |    |
    |  __           |
    | /  ` |__|  /\ |
    | \\__, |  | /~~\\|
    | |    |  |     |
    | |    |__|     |
    |  ___  ___  ___|
    | |__  |__  |__ |
    | |___ |___ |___|
    |               |
    |  [M E N U]    |
    +--------------+
    """
    
    def clear_screen():
        """Prints a separator to keep the terminal readable."""
        print("\n" + "="*40 + "\n")
    
    def check_and_run_module(module_name, quiet_missing=False):
        """
        Attempts to import and run a module.
        Returns True if the file exists and runs, False if the file is missing.
        """
        try:
            misc = importlib.import_module(module_name)
            print(f"\n[Loading] {module_name}...")
            if hasattr(misc, 'main'):
                misc.main()
            else:
                print(f"[Error] {module_name} has no main() function defined.")
            return True
        except ModuleNotFoundError as e:
            # Verify the missing module is the file itself and not an internal import error
            if e.name == module_name:
                if not quiet_missing:
                    print(f"[Skip] {module_name}.py not found.")
                return False
            else:
                # The file exists but failed inside because it tried to import a broken dependency
                print(f"\n[Error] {module_name}.py failed internal import: {e}")
                return True
        except Exception as e:
            print(f"\n[Error] Failed running {module_name}: {e}")
            return True
    
    # ==========================================
    # 2. MENU FUNCTIONS
    # ==========================================
    
    def run_all_challenges_unlimited():
        """Mode 1: Automatically steps through an unlimited number of days and challenges."""
        print("\n--- Mode 1: Run All Challenges Sequence (Unlimited Days) ---")
        challenges_per_day = int(input("Max challenges per day: "))
        
        day = 1
        while True:
            day_had_any_files = False
            print(f"\nChecking files for Day {day}...")
            
            for c in range(1, challenges_per_day + 1):
                file_exists = check_and_run_module(f"day{day}challenge{c}", quiet_missing=True)
                if file_exists:
                    day_had_any_files = True
            
            # If absolutely no challenges were found for this day, stop the infinite sequence loop
            if not day_had_any_files:
                print(f"\n[Finished] No files found for Day {day}. Sequence concluded.")
                break
                
            day += 1
    
    def skip_to_challenge():
        """Mode 2: Instantly skips to and runs one specific challenge file."""
        print("\n--- Mode 2: Skip to Specific Challenge ---")
        day = int(input("Target Day number: "))
        challenge = int(input("Target Challenge number: "))
        check_and_run_module(f"day{day}challenge{challenge}")
    
    def run_range_on_day_one():
        """Mode 3: Runs challenges from 1 up to a specified number strictly on Day 1."""
        print("\n--- Mode 3: Day 1 Range Loop (1 -> X) ---")
        end_challenge = int(input("Run Day 1 challenges from 1 up to what number?: "))
        
        for c in range(1, end_challenge + 1):
            check_and_run_module(f"day1challenge{c}")
    
    def skip_to_day_project():
        """Mode 4: Skips directly to a base day file without a challenge suffix."""
        print("\n--- Mode 4: Open Day Project (No Suffix) ---")
        day = int(input("Target Day project number: "))
        check_and_run_module(f"day{day}")
    
    def run_all_day_projects_unlimited():
        """Mode 5: Steps through an unlimited number of suffixless day projects (day1, day2...)."""
        print("\n--- Mode 5: Run All Base Day Projects (Unlimited Days) ---")
        
        day = 1
        while True:
            file_exists = check_and_run_module(f"day{day}", quiet_missing=True)
            
            # Stops as soon as a consecutive base day file is missing
            if not file_exists:
                print(f"\n[Finished] No project file found for Day {day}. Sequence concluded.")
                break
                
            day += 1
    
    # ==========================================
    # 3. MAIN RUNNER & MENU LOOP
    # ==========================================
    
    def main_menu():
        while True:
            clear_screen()
            print(MENU_ART)
            print(" PYTHON CHALLENGE ARCHIVE")
            print("1. Run all challenges sequentially (Unlimited Days)")
            print("2. Skip directly to a specific challenge (dayXchallengeY)")
            print("3. Loop Day 1 challenges (from 1 to specified number)")
            print("4. Skip to a specific day project (dayX only)")
            print("5. Run all base day projects sequentially (Unlimited Days)")
            print("6. Exit Program")
            
            choice = input("\nSelect an option (1-6): ").strip()
            
            if choice == "1":
                run_all_challenges_unlimited()
            elif choice == "2":
                skip_to_challenge()
            elif choice == "3":
                run_range_on_day_one()
            elif choice == "4":
                skip_to_day_project()
            elif choice == "5":
                run_all_day_projects_unlimited()
            elif choice == "6":
                print("\nExiting. Happy coding!")
                sys.exit()
            else:
                print("\n[Invalid Selection] Please choose a number between 1 and 6.")
            
            input("\nPress Enter to return to the Main Menu...")
    
    if __name__ == "__main__":
        main_menu()
    