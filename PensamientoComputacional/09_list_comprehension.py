import math

def run():
    data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = [value for value in data if not math.isnan(value)]
    print(filtered_data)

if __name__ == "__main__":
    run()