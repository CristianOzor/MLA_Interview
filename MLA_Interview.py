import requests
import json


def request_data():
	request_data = requests.get("https://api.mercadolibre.com/sites/MLA//search?seller_id=179571326").json()
	
	
	request_data = request_data['results']
	

	file_name = input("Por favor introduzca el nombre al archivo a guardar: ")
	
	try:
		with open(f"{file_name}.log", "w+") as file:
		
			file.write("ID --- TITLE --- CATEGORY_ID --- NAME\n")
		
			for key in request_data:
				id = key["id"]
				title = key["title"]
				category_id = key["category_id"]
				name = key["domain_id"]
			
				file.writelines(f"{id} +  ---  + {title} +  ---  + {category_id} +  ---  + {name}\n")
			
			print("Archivo log guardado exitosamente")
			
	except IOError:
		print("Hubo un error al procesar el archivo")

request_data()
