#!/usr/bin/python3

from rich import print

class CostPlanner:

    def __init__(self):
        self.estimate_type = ''
        self.lower_bound = 0
        self.upper_bound = 0
        print("[cyan]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[/]")
        print("[cyan]Thank you for creating a Cost Planner! Are you ready to plan your project's costs? Let's go![/]")
        print("[cyan]~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~[/]", end="\n\n")

    def calculate_estimate_range(self, base_value):
        """ Calculate the lower and upper bound of the project cost estimate. """
        if self.estimate_type == "ROM" or self.estimate_type == "rom":
            self.lower_bound = base_value - base_value / 4
            self.upper_bound = base_value + base_value * 3 / 4
            print("Your [yellow]Range of Magnitude[/] estimate is $", format(self.lower_bound, '.2f'), " to $", format(self.upper_bound, '.2f'))
        elif self.estimate_type == "R" or self.estimate_type == "r":
            self.lower_bound = base_value - base_value * 7 / 20
            self.upper_bound = base_value + base_value * 7 / 20
            print("Your [yellow]Range of[/] estimate is $", format(self.lower_bound, '.2f'), " to $", format(self.upper_bound, '.2f'))
        elif self.estimate_type == "A" or self.estimate_type == "a":
            self.lower_bound = base_value - base_value * 3 / 20
            self.upper_bound = base_value + base_value * 3 / 20
            print("Your [yellow]Approximate[/] estimate is $", format(self.lower_bound, '.2f'), " to $", format(self.upper_bound, '.2f'))
        elif self.estimate_type == "D" or self.estimate_type == "d":
            self.lower_bound = base_value - base_Value * 1 / 20
            self.upper_bound = base_value + base_value * 1 / 10
            print("Your [yellow]Definitive[/] estimate is $", format(self.lower_bound, '.2f'), " to $", format(self.upper_bound, '.2f'))

    def ROM_or_range_of_estimate(self):
        """ Prompt user to perform a ROM or Range of estimate.  """
        print("You want to use a [yellow]ROM[/], or [yellow]Range of Magnitude[/] estimate! The accuracy of this estimate is [red]-25% <--> +75%[/].")
        print("Another estimate you may want to use is a [yellow]Range of[/] estimate! The accuracy of this estimate is [red]-35% <--> +35%[/].", end="\n\n")
        print("Would you like to use a [yellow]ROM[/] or [yellow]Range of[/] estimate?")
        self.estimate_type = input("Enter ROM or R or press enter to continue...")
        print()
        if self.estimate_type == 'ROM' or self.estimate_type == 'rom':
            print("You have chosen to use a [yellow]ROM[/] estimate!")

        elif self.estimate_type == 'R' or self.estimate_type == 'r':
            print("You have chosen to use a [yellow]Range of[/] estimate!")

    def approximate_estimate(self):
        """ Prompt user to perform an Approximate estimate. """
        print("You want to use a [yellow]Approximate[/] estimate! The accuracy of this estimate is [red]-15% <--> +15%[/].")
        self.estimate_type = input("Enter A or press enter to continue...")
        if self.estimate_type == 'A' or self.estimate_type == 'a':
            print("You have chosen to use an [yellow]Approximate[/] estimate!")

    def definitive_estimate(self):
        """ Prompt user to perform a Definitive estimate. """
        print("You want to use a [yellow]Definitive[/], or [yellow]Control[/] or [yellow]Detailed[/], estimate! The accuracy of this estimate is [red]-5% <--> +10%[/].")
        self.estimate_type = input("Enter D or press enter to continue...")
        if self.estimate_type == 'D' or self.estimate_type == 'd':
            print("You have chosen to use a [yellow]Definitive[/] estimate!")

    def set_estimate_type(self):
        """ Configure instance estimate type.  """
        print("How much information do you have available for your estimate?")
        print("[purple]Very little. I might have some high-level historical data from other projects, experts to advise me, or a costing model to use.[/]")
        selection = input("Type Y to select or enter to continue...")
        print()
        if selection == 'Y' or selection == 'y':
            self.ROM_or_range_of_estimate()

        print("[purple]A moderate amount. I might have a proven costing model or detailed historical data for a similar project.[/]")
        selection = input("Type Y to select or enter to continue...")
        print()
        if selection == 'Y' or selection == 'y':
            self.approximate_estimate()

        print("[purple]A lot. I have the WBS completed and cost estimations available for each work package.[/]")
        selection = input("Type Y to select or enter to continue...")
        print()
        if selection == 'Y' or selection == 'y':
            self.definitive_estimate()

    def estimate_type_is_set(self):
        """ Return True if instance estimate_type is recognized as valid. """
        recognized_estimate_types = [
                "ROM", "rom",
                "R", "r",
                "A", "a",
                "D", "d"
                ]

        if self.estimate_type in recognized_estimate_types:
            return True
        return False

    def set_base_value_estimate(self):
        """ Set base value for calculating the estimate range. """
        looping = True
        while looping:
            try:
                figure = float(input("Enter an initial estimate for your project: ").strip("$"))
                self.calculate_estimate_range(figure)
                looping = False
            except:
                print("[magenta]Please enter a valid dollar amount![/]")

    def estimate_costs(self):
        """ Estimate project costs for project planning.  """
        self.set_estimate_type()
        if self.estimate_type_is_set():
            self.set_base_value_estimate()


if __name__ == "__main__":
    planner = CostPlanner()
    planner.estimate_costs()
