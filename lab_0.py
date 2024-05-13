import matplotlib.pyplot as plt
import numpy as np

# Table 1: Ohm's Law - Voltage vs Current
voltage = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
current_var1 = np.array([0, 0.252, 0.514, 0.771, 1.021, 1.281, 1.532, 1.796, 2.048, 2.309, 2.567])
current_var2 = np.array([0, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])

plt.figure(figsize=(10, 6))
plt.plot(voltage, current_var1, label='Ohm\'s Law - Wariant 1')
plt.plot(voltage, current_var2, label='Ohm\'s Law - Wariant 2')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title("Ohm's Law - Voltage vs Current")
plt.legend()
plt.grid(True)
plt.show()

# Table 2: Resultant Resistance - Resistance Values
measurement_no = np.array([1, 2, 3, 4, 5])
resistance_var1 = np.array([1970, 2110, 1590, 5319, 3260])
resistance_var2 = np.array([2250, 2000, 1250, 6000, 4000])

plt.figure(figsize=(10, 6))
plt.scatter(measurement_no, resistance_var1, label='Resultant Resistance - Wariant 1')
plt.scatter(measurement_no, resistance_var2, label='Resultant Resistance - Wariant 2')
plt.xlabel('Measurement No.')
plt.ylabel('Resistance (Ω)')
plt.title("Resultant Resistance - Resistance Values")
plt.legend()
plt.grid(True)
plt.show()

# Table 3: Voltage Divider - Input vs Output Voltage
measurement_no_vd = np.array([1, 2, 3])
input_voltage = np.array([3.33, 2.51, 1.645])
output_voltage = np.array([3.3, 2.5, 1.6])

plt.figure(figsize=(10, 6))
plt.plot(measurement_no_vd, input_voltage, marker='o', label='Voltage Divider - Input Voltage')
plt.plot(measurement_no_vd, output_voltage, marker='o', label='Voltage Divider - Output Voltage')
plt.xlabel('Measurement No.')
plt.ylabel('Voltage (V)')
plt.title("Voltage Divider - Input vs Output Voltage")
plt.legend()
plt.grid(True)
plt.show()

# Table 4: First Kirchhoff's Law - Current Summation
measurement_no_kl1 = np.array([1, 2, 3])
total_current = np.array([6, 9, 11])

plt.figure(figsize=(10, 6))
plt.plot(measurement_no_kl1, total_current, marker='o', label='First Kirchhoff\'s Law - Total Current')
plt.xlabel('Measurement No.')
plt.ylabel('Total Current (mA)')
plt.title("First Kirchhoff's Law - Current Summation")
plt.legend()
plt.grid(True)
plt.show()

# Table 5: Second Kirchhoff's Law - Input vs Output Voltage
measurement_no_kl2 = np.array([1, 2, 3])
total_output_voltage = np.array([5.018, 5.02, 5.018])

plt.figure(figsize=(10, 6))
plt.plot(measurement_no_kl2, total_output_voltage, marker='o', label='Second Kirchhoff\'s Law - Total Output Voltage')
plt.xlabel('Measurement No.')
plt.ylabel('Total Output Voltage (V)')
plt.title("Second Kirchhoff's Law - Input vs Output Voltage")
plt.legend()
plt.grid(True)
plt.show()
