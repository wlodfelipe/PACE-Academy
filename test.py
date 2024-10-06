import netCDF4 as nc

# Abrir el archivo
dataset = nc.Dataset('1.nc')

# Ver las variables
print(dataset.variables)

# Leer una variable
variable = dataset.variables['lat'][:]
print(variable)

# Cerrar el archivo cuando termines
dataset.close()
