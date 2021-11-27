from sales_person import SalesPerson
class SalesForce:
    """
    encapsulates data for a sales person
    """

    def __init__(self):
        """
        initializes sales_people to an empty list
        """
        self.sales_people = []

    def add_data(self, file_name):
        """
        imports info for all salespeople from the specified file.
        the imported data should be added to the sales_people list.
        each line of the file will contain info in the form:
        <employee_id>, <name>, <sale amount>, <sale amount>,...
        """
        in_file = open(file_name, 'r')  # open data file
        lines = in_file.readlines()  # turns it into a list by lines
        # create SalesPerson objects using Salesperson class
        for ea_line in lines:  # splitting up the individual lines
            separated_line = ea_line.split(",")
            emp_id, name = separated_line[0], separated_line[1]
            person = SalesPerson(emp_id, name)  # creates SalesPerson object

            # enter sales info
            emp_sales_string = separated_line[2]
            emp_sales_list = emp_sales_string.split()  # break up sales into list
            # get the person's total sales (?)
            for ea_sale in emp_sales_list:
                person.enter_sale(ea_sale)  # enter each sale into person's object (sales list)

            self.sales_people.append(person)  # add the object and its info to the list
        in_file.close()

    def quota_report(self, quota):
        """
        returns list[list[int, string, float, bool]]
        returns a list, where each element is itself a list
        of each seller's employee_id, name, total sales, and a boolean value
        of whether or not they hit the specified quota - T if they hit it, F is they did not
        """
        force_list = []
        for person in self.sales_people:  # so it will focus on one person object at a time
            # get the info from object
            emp_id = person.get_id()  # get the person's id from the object
            name = person.get_name()  # get the person's name
            total_sales = person.total_sales()  # compute & get the person's total sales
            hit_quota = person.met_quota(quota)  # bool, see if hit quota or not

            # combine info into lists (this is for the output, putting it together)
            individ_info = [emp_id, name, total_sales, hit_quota]  # list
            force_list.append(individ_info)  # adds list to list
        return force_list  # not sure if there should be a self. in this

    def top_seller(self):
        """
        returns list[SalesPerson]
        returns a list of SalesPerson objects with the highest sales amount.
        if there are no ties, the list should contain one record.
        In the case of a tie, the list should include all of the top sales people.
        """
        # if bubble sort also doesn't work, can try utilizing dictionaries.
        # set up dictionaries
        sales_dict = {}
        for person in self.sales_people:
            employee_information = person.__str__()
            emp_info_split = employee_information.split(": ")
            person_key = emp_info_split[0]
            person_total_sales = emp_info_split[1]

        # take the total sales aspect of dictionary, sort them
        # call the names/objects to the appropriate sales

    def individual_sales(self, employee_id):
        """
        returns SalesPerson
        returns the SalesPerson with the given employee_id
        or None if the id does not exist.
        """
        # I'm really sorry, I have too many other things that I'm worried about.
        # I can't seem to focus on this any more.
