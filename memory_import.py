
# This needs to be imported to/ added to all core modules for memory maximisation. 


from fractal_echo_memory import FractalEchoMemory

aethos_memory = FractalEchoMemory()
aethos_memory.create_carrier("Spot")
aethos_memory.add_echo("Spot", "She slept peacefully beside me", ["She is my calm", "She balances the noise"], depth=2, pulse=3)