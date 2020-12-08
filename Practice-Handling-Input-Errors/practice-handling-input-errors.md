# Handling Input Errors

The `party_planner` function below takes as input a number of party people and cookies and figures out how many cookies each person gets at the party, assuming equitable distribution of cookies. Then, it returns that number along with how many cookies will be left over.

Right now, calling the function with an input of 0 people will cause an error, because it creates a ZeroDivisionError exception. Edit the `party_planner` function to handle this invalid input. If it runs into this exception, it should print a warning message to the user and request they input a different number of people.

After you've edited the function, try running the file again and make sure it does what you intended. Try it with several different input values, including 0 and other values for the number of people.
