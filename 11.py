from datetime import datetime

def data_por_extenso(data):
    try:
        data_obj = datetime.strptime(data, '%d/%m/%Y')
        data_formatada = data_obj.strftime('%d de %B de %Y')

        return data_formatada
    except ValueError:
        return None

data1 = '27/03/2024'
data2 = '23/10/2001'
data3 = '31/02/2025'

print(data_por_extenso(data1))
print(data_por_extenso(data2))
print(data_por_extenso(data3))