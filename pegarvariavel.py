from netCDF4 import Dataset

# Abrir o arquivo .nc
file_path = 'PACE_OCI.20241004.L3m.DAY.CHL.V2_0.chlor_a.0p1deg.NRT.nc'
dataset = Dataset(file_path, mode='r')

# Exibir informações do arquivo
print(dataset)

# Listar todas as variáveis no dataset
print("Variáveis disponíveis no dataset:")
print(dataset.variables.keys())

# Acessar uma variável específica (substitua 'nome_da_variavel' pelo nome correto da variável)
variable_name = 'nome_da_variavel'  # Substitua pelo nome real
if variable_name in dataset.variables:
    variable_data = dataset.variables[variable_name][:]
    print(f"Dados da variável '{variable_name}':")
    print(variable_data)
else:
    print(f"Variável '{variable_name}' não encontrada no dataset.")

# Fechar o arquivo
dataset.close()

