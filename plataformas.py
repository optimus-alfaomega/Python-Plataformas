from platform import platform, machine, processor, system,version

print(platform())
print(platform(1))
print(platform(0, 1))

#imprime la arquitectura
print(machine())
#imprime el dato del procesador
print(processor)
#imprime el sistema operativo
print(system())
#imprime la version del sistema operativo
print(version())

