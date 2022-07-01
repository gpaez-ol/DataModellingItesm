from numpy import double

input_file_name = "chi_data.txt"

def parse_double(str):
    return double(str)

file_data = list(map(parse_double, open(input_file_name, "r").read().splitlines()))

n = len(file_data)
classes = 10
width = double(0.1)
expected_frequency = double(n / classes)
expected_chi_squared = double(16.91)

interval_limits = [double(0.0)]
for i in range(1, classes + 1):
    interval_limits.append(interval_limits[i-1] + width)

observed_frequencies = [0] * classes
for i in range(0, n):
    freqIndex = 0
    for j in range(0, classes):
        if file_data[i] < interval_limits[j]:
            break
        freqIndex = j
    observed_frequencies[freqIndex] += 1

chi_squared = double(0.0)
chi_squared_arr = []
for i in range(0, classes):
    chi_squared_arr.append(double(pow(observed_frequencies[i] - expected_frequency, double(2.0)) / expected_frequency))
    chi_squared += chi_squared_arr[i]

#printing
decimals = 4
spacing = 20
expected_frequency_str = "{0:.{1}f}".format(expected_frequency, decimals).format(expected_frequency, decimals)

print("{0:<{4}}{1:<{4}}{2:<{4}}{3}".format("Intervals", "Observed", "Expected", "(O-E)^2 / E", spacing))
for i in range(0, classes):
    interval = "[{0:.{2}f} - {1:.{2}f})".format(interval_limits[i], interval_limits[i+1], decimals)
    observed = "{}".format(observed_frequencies[i])
    chi_squared_part = "{0:.{1}f}".format(chi_squared_arr[i], decimals)
    print("{0:<{4}}{1:<{4}}{2:<{4}}{3}".format(interval, observed, expected_frequency_str, chi_squared_part, spacing))
print("chi^2 = {0:.{1}f}".format(chi_squared, decimals))

print("H0: Generated numbers are not different from the uniform distribution")
print("H1: Generated numbers are different from the uniform distribution")

if chi_squared > expected_chi_squared:
    print("Since {0:.{2}f} > {1:.{2}f}, H0 is rejected".format(chi_squared, expected_chi_squared, decimals))
else:
    print("Since {0:.{2}f} <= {1:.{2}f}, H0 is not rejected".format(chi_squared, expected_chi_squared, decimals))