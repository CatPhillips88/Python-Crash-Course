# Printing Modules: Create a function in a separate file called printing_functions.py. Write an import statement at the top
# of this file and modify the file to use the imported functions.

def engagement_ring_purchases(orders, finished_orders):
    while orders:
        completed = orders.pop()
        finished_orders.append(completed)

def shipped_rings(shipped_list):
    print('HERE ARE THE FOLLOWING RINGS SHIPPED FOR DELIVERY:')

    for ring in shipped_list:
        print(f'{ring.title()}')