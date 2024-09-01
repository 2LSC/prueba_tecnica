############################
#####     Punto 1      ##### 
############################
from pprint import pprint

def agrupar_productos(productos):
    productos_agrupados = {}
    for producto in productos:
        fabricante = producto['fabricante']
        categoria = producto['categoria']
        genero = producto['genero']
        
        if fabricante not in productos_agrupados:
            productos_agrupados[fabricante] = {}
        if categoria not in productos_agrupados[fabricante]:
            productos_agrupados[fabricante][categoria] = {}
        if genero not in productos_agrupados[fabricante][categoria]:
            productos_agrupados[fabricante][categoria][genero] = []
        
        productos_agrupados[fabricante][categoria][genero].append(producto)
    
    return productos_agrupados

if __name__ == "__main__":
    productos = [
        {'nombre': 'Zapatos XYZ', 'codigo': '8569741233658', 'fabricante': 'Deportes XYZ', 'categoria': 'Zapatos', 'genero': 'Masculino'},
        {'nombre': 'Zapatos ABC', 'codigo': '7452136985471', 'fabricante': 'Deportes XYZ', 'categoria': 'Zapatos', 'genero': 'Femenino'},
        {'nombre': 'Camisa DEF', 'codigo': '5236412896324', 'fabricante': 'Deportes XYZ', 'categoria': 'Camisas', 'genero': 'Masculino'},
        {'nombre': 'Bolso KLM', 'codigo': '5863219635478', 'fabricante': 'Carteras Hi-Fashion', 'categoria': 'Bolsos', 'genero': 'Femenino'}
    ]

    resultado = agrupar_productos(productos)
    pprint(resultado, width=80, sort_dicts=False)

############################
#####     Punto 2      ##### 
############################
diccionario = {'nombre': 'Mario'}

# Ejemplo con try-except
try:
    valor = diccionario['edad']
except KeyError:
    valor = None
    print("Punto 2 ","La clave no existe en el diccionario.")

# Ejemplo con get()
valor = diccionario.get('edad', None)

##  Justificación:

##  try-except permite manejar los errores de manera explícita,
##  siendo útil para debug o cuando se necesita manejar múltiples tipos de excepciones.

##  get() es más limpio y evita que el programa se detenga si la clave no existe.


############################
#####     Punto 3      ##### 
############################

def calcular_descuento(total_venta):
    if total_venta > 500:  # Variable de entrada para calcular el descuento 
        return 0.10  # 10% de descuento
    elif 100 <= total_venta <= 500:
        return 0.05  # 5% de descuento
    else:
        return 0.0   # Sin descuento
    
total_venta =400
descuento = calcular_descuento(total_venta)
print("Punto 3 ",f"El descuento aplicable es del {descuento * 100}%")    

############################
#####     Punto 4      ##### 
############################

# SELECT order_id, amount_total, customer_name
# FROM sales_order
# WHERE amount_total > 1000;


############################
#####     Punto 5      ##### 
############################

# SELECT e.EmployeeID, e.FirstName, e.LastName, o.OrderID, p.ProductName, c.CategoryName
# FROM Employees e
# JOIN Orders o ON e.EmployeeID = o.EmployeeID
# JOIN OrderDetails od ON o.OrderID = od.OrderID
# JOIN Products p ON od.ProductID = p.ProductID
# JOIN Categories c ON p.CategoryID = c.CategoryID
# WHERE c.CategoryName = 'Beverages';