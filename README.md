# Coffee Machine Design Problem

## Problem statement

Write the working code to create a working coffee machine. Here are the desired features
1. It will be serving some beverages.
2. Each beverage will be made using some ingredients.
3. Assume time to prepare a beverage is the same for all cases.
4. The quantity of ingredients used for each beverage can vary. Also, the same ingredient (ex:
water) can be used for multiple beverages.
5. There would be **N (N is an integer)** outlets from which beverages can be served.
7. Maximum **N** beverages can be served in **parallel**.
8. Any beverage can be served only if all the ingredients are available in terms of quantity.
9. There would be an indicator that would show which all ingredients are running low. We need
some methods to refill them.
10.Please provide functional integration test cases for maximum coverage.

## File Structure

 - `coffee_machine.py` - contains the behaviour and properties of a Coffee Machine
 - `coffee_machine_driver.py` - driver program to run tests
 - `test_cases` - contains the default test data as well as some other test cases
 
 ## Test Cases
 
  - `default_test_data.json` - the default data as per the problem statement
  - `test_case_1.json` - the drinks contain ingredients that are **not present** in the machine
  - `test_case_2.json` - sufficient ingredients are present for all the drinks
  - `test_case_3.json` - the coffee machine contains zero outlets which is not allowed
  
  ## Running the code
  
  Navigate to the folder containing the driver file, and run the following command
  ```
  python coffee_machine_driver.py test_case_1.json
  ```
  
  If no filename is provided, it will run with the default test data. No external libraries are needed for the compilation of this project.
