"""
    Name: Emily Turner
    sales_person.py

    Problem: create a class encapsulating a sales person

    Certification of Authenticity:
    I certify that this assignment is entirely my own work.
"""
class SalesPerson:
    """
    class that encapsulates data for a sales person
    """

    def __init__(self, employee_id, name):
        self.employee_id = employee_id  # an int
        self.name = name  # a string that is a person's full name
        self.sales = []  # list of floats that represents to amount of ea. sale

    def get_id(self):
        """
        returns the sales person's employee_id as an int
        """
        employee_id = self.employee_id
        return employee_id

    def get_name(self):
        """
        returns the sales person's name as a string
        """
        name = self.name
        return name

    def set_name(self, name):
        """
        sets the sales person's name, returns void
        """
        self.name = name

    def enter_sale(self, sale):
        """
        adds the value of the sale to the sales list
        """
        self.sales.append(sale)

    def total_sales(self):
        """
        returns the sum of the sales person's sales as a float
        """
        total_sales = sum(self.sales)
        return total_sales

    def get_sales(self):
        """
        returns the list of sales
        returns list[float]
        """
        sales = self.sales
        return sales

    def met_quota(self, quota):
        """
        returns Boolean.
        True if the total sales meet or exceed the quota provided,
        False otherwise.
        """
        total_sales = self.total_sales()  # get the total sales
        met_quota = bool(total_sales >= quota)
        return met_quota

    def compare_to(self, other):
        """
        returns int.
        other is another sales person.
        returns -1 if other has more in total sales than self,
        1 if self has more in total sales than other,
        0 if their total sales are the same
        """
        person_total = self.total_sales()  # get total from self
        other_total = other.total_sales()  # get total from Other (get it from another object)
        # compare them, return correct number
        if other_total > person_total:
            comparison_num = -1
        elif person_total > other_total:
            comparison_num = 1
        else:
            comparison_num = 0
        return comparison_num

    def __str__(self):
        """
        returns string.
        returns "<employee_id>-<name>: <total sales>"
        """
        employee_id = self.employee_id
        name = self.name
        total_sales = self.total_sales()  # wait is that how you do it? it is, isn't it.
        employee_information = ("{0}-{1}: {2}".format(employee_id, name, total_sales))
        return employee_information
