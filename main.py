# ------------------------------------------------------------------------------- #
# Title: Employee Rating Main Module
# # Description: Main application module for employee ratings.
# ChangeLog: (Who, When, What)
# TPerkins,12.3.2023,Created Script for Module 8
# ------------------------------------------------------------------------------- #

import presentation_classes as pres
import processing_classes as proc
import data_classes as data

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                            employee_data=data.employees,
                                                            employee_type=data.Employee)

# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees, counter=0)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        list_counter = len(employees)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees,
                                                    employee_type=data.Employee)
            pres.IO.output_employee_data(employee_data=employees, counter=list_counter)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
