import dis
from particleSimulator import ParticleSimulator
dis.dis(ParticleSimulator.evolve)
print(30*"#")
dis.dis(ParticleSimulator.evolve_fast)