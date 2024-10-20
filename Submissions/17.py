def printStatus(status):
    """
        Prints the marital status based on the input status code.

        Args:
            status (str): A single character representing the status. 
                        Valid values are:
                        'S' - Separated
                        'M' - Married
                        'D' - Divorced
                        'U' - Unmarried

        Returns:
            str: A string representing the marital status if a valid status code is passed.
                Otherwise, prints an error message for invalid input.
    """

    status_dict = {
        'S': "Separated",
        'M': "Married",
        'D': "Divorced",
        'U': "Unmarried"
    }

    if status not in status_dict:
        print("Inappropriate status passed")
        return
    else:
        return status_dict[status]


if __name__ == "__main__":
    print(printStatus("U"))
    print(printStatus("O"))