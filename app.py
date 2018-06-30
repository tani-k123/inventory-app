import csv
import os

def menu(username="@some-user", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath =  os.path.join(os.path.dirname(__file__), "db", filename) #code for creating a path --> look at notes on os
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    #TODO: open the file and populate the products list with product dictionaries

    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise...csv.reader(csv_file)
        for row in reader:
            products.append (dict (row))
        #print(row["price"], row["name"])
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    # print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() # uses fieldnames set above
        for p in products:
            writer.writerow(p)

    # writer.writerow({"city": "New York", "name": "Yankees"})
    # writer.writerow({"city": "New York", "name": "Mets"})
    # writer.writerow({"city": "Boston", "name": "Red Sox"})
    # writer.writerow({"city": "New Haven", "name": "Ravens"})

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    #print (products)
    write_products_to_file(filename, products)

def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    # print(menu(username="@some-user")) #TODO instead of printing, capture user input
    operation = input (menu(username="@some-user", products_count = len(products)))
    print ("You chose: ", operation)

    operation = operation.title()  #allows to use any case for user inputs
    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print ("..." + p["id"] + " " + p["name"])

    elif operation == "Show":
        product_id = input("Please, provide product identifier: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print (matching_product)

    elif operation == "Create":
        for p in products:
            new_id = int(p["id"]) + 1
        new_product = {
            "id": new_id,
            "name": "New Product",
            "aisle": "new aisle",
            "department": "new department",
            "price": 100.00
        } #todo: capture user inputs
        print ("For new product with identifier no. " + str(new_id) + ":")
        new_name = input("Please, provide name of new product: ")
        new_aisle = input("Please, provide aisle name for new product: ")
        new_department = input("Please, provide department of new product: ")
        new_price = input("Please, provide price of new product: ")
        #new_products = [p for p in products: (p["id"]) == new_id]
        new_product = {
            "id": new_id,
            "name": new_name,
            "aisle": new_aisle,
            "department": new_department,
            "price": new_price
        }
        products.append(new_product)
        print ("CREATING A NEW PRODUCT", new_product)

    elif operation == "Update":
        product_id = input("Please, provide product identifier: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]

        attribute_to_edit = input("Please, choose an attribute to edit from the following list: name, aisle, product, price: ")
        if attribute_to_edit == "price":
            new_price = 200.00
            new_price = input("Please, provide new price: ")
            matching_product ["price"] = new_price
            print ("UPDATING A PRODUCT")
        elif attribute_to_edit == "name":
            new_name = "something"
            new_name = input("Please, provide new name: ")
            matching_product ["name"] = new_name
            print ("UPDATING A PRODUCT")
        elif attribute_to_edit == "aisle":
            new_aisle = "something"
            new_aisle = input("Please, provide new aisle name: ")
            matching_product ["aisle"] = new_aisle
            print ("UPDATING A PRODUCT")
        elif attribute_to_edit == "department":
            new_department = "something"
            new_department = input("Please, provide new department name: ")
            matching_product ["department"] = new_department
            print ("UPDATING A PRODUCT")
        else:
            print ("That is not an editable attribute. Please, try again.")

    elif operation == "Destroy":
        product_id = input("Please, provide product identifier: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print ("DELETING A PRODUCT")

    elif operation == "Reset":
        reset_products_file()
    else:
        print ("OOPS, unrecognized operation, please select above operations only")



    #print (f"RAEADING PRODUCTS FROM FILE: '{filepath}'")
    #products = []

    #with open(filepath, "r") as csv_file:
    #    reader = csv.DictReader(csv_file) #assuming csv has headers otherwise csv.reader
    #    for row in reader:
            #print (row["name"], row["price"])
    #        products.append(dict(row))

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #todo: handle selected operation

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
#syntax for if run from command line then, invoke function that follows; this allows us to
#import/export functions from this file to another file like in reset.py
