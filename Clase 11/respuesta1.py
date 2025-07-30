class calcular_area:
    
    # Método para calcular el área de un triángulo
    def triangulo(base, altura):
        return (base * altura) / 2
    
    # Método para calcular el área de un rectángulo
    def rectangulo(base, altura):
        return base * altura
    
    

# instancia de la clase calcular_area
ca = calcular_area()

base_triangulo = 5
altura_triangulo = 8
area_triangulo = calcular_area.triangulo(base_triangulo, altura_triangulo)
print(f"Área del triángulo: {area_triangulo}")

base_rectangulo = 6
altura_rectangulo = 4
area_rectangulo = calcular_area.rectangulo(base_rectangulo, altura_rectangulo)
print(f"Área del rectángulo: {area_rectangulo}")
