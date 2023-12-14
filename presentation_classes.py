# ------------------------------------------------------------------------------- #
# Title: Employee Rating Presentation Classes
# # Description: A collection of presentation classes for managing the application.
# ChangeLog: (Who, When, What)
# TPerkins,12.3.2023,Created Script for Module 8
# ------------------------------------------------------------------------------- #

import data_classes as data


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    TPerkins,12.3.2023,Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None) -> object:
        """ This function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        TPerkins,12.3.2023,Created function

        :rtype: object
        :param: message: string with message data to display
        :param: error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        TPerkins,12.3.2023,Created function

        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        TPerkins,12.3.2023,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list, counter: int):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        TPerkins,12.3.2023,Created function

        :param employee_data: list of employee object data to be displayed
        :param counter: the previous count of employee records

        :return: None
        """

        message: str = ''
        print()
        print("-" * 50)
        cur_rec: int = 0
        for employee in employee_data:
            cur_rec += 1
            if employee.review_rating == 5:
                message = " {} {} is rated as 5 (Leading)"
            elif employee.review_rating == 4:
                message = " {} {} is rated as 4 (Strong)"
            elif employee.review_rating == 3:
                message = " {} {} is rated as 3 (Solid)"
            elif employee.review_rating == 2:
                message = " {} {} is rated as 2 (Building)"
            elif employee.review_rating == 1:
                message = " {} {} is rated as 1 (Not Meeting Expectations)"
            if cur_rec > counter:
                print(message.format(employee.first_name, employee.last_name, employee.review_date,
                                     employee.review_rating))
        print("-" * 50)
        print()

    @staticmethod
    def input_employee_data(employee_data: list, employee_type: data.Employee):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: (Who, When, What)
        TPerkins,12.3.2023,Created function

        :param employee_data: list of dictionary rows to be filled with input data
        :param employee_type: a reference to the Employee Class

        :return: list
        """

        try:
            # Input the data
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            if employee_object.first_name == "":
                raise ValueError("The first name should not be blank. ")
            employee_object.last_name = input("What is the employee's last name? ")
            if employee_object.last_name == "":
                raise ValueError("The last name should not be blank. ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
