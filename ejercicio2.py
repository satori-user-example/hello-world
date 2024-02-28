'''
Dadas las variables: product_name y quantity, complete la función
is_product_available con el siguiente objetivo:

~ Buscar en un pandas DataFrame y devolver True si existe stock, False caso
contrario.

'''

import pandas as pd
from colorama import init, deinit, Fore

def show_products(list):
    print()
    print(Fore.MAGENTA + 'Los productos disponibles son:\n')
    init()
    print(Fore.GREEN + "-" * 65)
    print("Product Name:".ljust(25) ,'\t', '\t', 'Cantidad:'.rjust(13))
    print("-"*65 + Fore.RESET)
    deinit()
    for i, row in list.iterrows():
        print(f"{row['product_name'].ljust(25)}\t\t{str(row['quantity']).rjust(13)}")


def is_product_available(product_name,product_df):
    product_name = product_name.lower()
    product_row = product_df.loc[product_df['product_name'] == product_name]
    if not product_row.empty:
        quantity_available = product_row.iloc[0]['quantity']
        if quantity_available > 0:
            print('Hay stock del producto seleccionado')
            return True
        else:
            print('No hay stock o no existe el producto seleccionado')
            return False
    else:
        print('No hay stock o no existe el producto seleccionado')
        return False


def main():
    _PRODUCT_DF = pd.DataFrame({"product_name": ["chocolate",
    "granizado", "limon", "dulce de leche"], "quantity":
    [3,10,0,5]})

    show_products(_PRODUCT_DF)
    print()
    print(is_product_available('Chocolate', _PRODUCT_DF)) #comentario para el examinador: Si en vez de chocolate, el parametro fuera limon, el output seria "False"

if __name__ == '__main__':
    main()


