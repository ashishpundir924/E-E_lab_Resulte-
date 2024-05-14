import matplotlib.pyplot as plt

# Input characteristics data
IB_input = [20, 22, 30, 40, 70, 130, 200, 230, 265, 300]  # Base current in µA
UBE = [0.62, 0.625, 0.632, 0.641, 0.655, 0.674, 0.686, 0.691, 0.693, 0.694]  # Base-emitter voltage in V

# Transition characteristics data
IC_transition = [2.095, 3.605, 4.713, 11.895, 15.259, 20.196, 24.196, 28.307, 31.2, 38.644]  # Collector current in mA

# Output characteristics data for different IB values
UCE_IB1 = [1.4, 2.1, 3.6, 4, 5.1, 6, 7.1, 8.5, 9.3, 11.9]
IC_IB1 = [2.29, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2]
UCE_IB2 = [1.6, 2.4, 3.2, 4.4, 5.2, 6.1, 7.4, 8.9, 9.4, 9.9]
IC_IB2 = [4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.7, 4.8, 4.8]
UCE_IB3 = [0.6, 1, 1.3, 1.8, 2.2, 2.5, 3, 3.5, 4.5, 5]
IC_IB3 = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7.1]

# Plotting the input characteristics
plt.figure(figsize=(10, 6))
plt.plot(UBE, IB_input, 'bo-', label='Input Characteristics')
plt.xlabel('Base-Emitter Voltage (V)')
plt.ylabel('Base Current (µA)')
plt.title('Input Characteristics of a Bipolar Transistor')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the transition characteristics
plt.figure(figsize=(10, 6))
plt.plot(IB_input, IC_transition, 'ro-', label='Transition Characteristics')
plt.xlabel('Base Current (µA)')
plt.ylabel('Collector Current (mA)')
plt.title('Transition Characteristics of a Bipolar Transistor')
plt.legend()
plt.grid(True)
plt.show()

# Plotting the output characteristics for different base currents
plt.figure(figsize=(10, 6))
plt.plot(UCE_IB1, IC_IB1, 'go-', label='IB = 25µA')
plt.plot(UCE_IB2, IC_IB2, 'mo-', label='IB = 50µA')
plt.plot(UCE_IB3, IC_IB3, 'co-', label='IB = 75µA')
plt.xlabel('Collector-Emitter Voltage (V)')
plt.ylabel('Collector Current (mA)')
plt.title('Output Characteristics of a Bipolar Transistor')
plt.legend()
plt.grid(True)
plt.show()
