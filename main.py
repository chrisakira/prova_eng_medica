import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Read the CSV file
    data = pd.read_csv('pressao.csv', sep=';', usecols=[0,1] ,header=0, names=['dc_data', 'ac_data'])  # Assuming the CSV file has a header

    dc_data = data['dc_data']
    ac_data = data['ac_data']

    data_index = len(dc_data) # The max number of samples
    initial_index = int(dc_data.idxmax() + dc_data.idxmax() * 0.1) # The initial index to start the search
    
    min = int(0)
    max = int(0)
    downs = int(0)
    angle = bool(False)
    
    i = initial_index
    while i < data_index:
        if ac_data[i+1] < (ac_data[i] + 3) and not angle:
            angle = True
            downs += 1    
            max += dc_data[i]
        
        if ac_data[i+1] > (ac_data[i] + 3) and angle:
            angle = False
            
        if downs >= 2:
            max = max / 2 
            break
        
        i += 1
        
    i = initial_index
    while i < data_index:
        if dc_data[i] < ac_data[i] and ac_data[i] < 114:
            min = dc_data[i]
            break
        i += 1

    print(max)    
    print(min)

    # Plot the data
    plt.plot(dc_data.index, dc_data, color='black', label='Valores de pressão DC')
    plt.plot(ac_data.index, ac_data, color='blue', label='Valores de pressão AC')
    plt.axhline(y=max, color='r', linestyle='--', label='Pressão maxima')
    plt.axhline(y=min, color='g', linestyle='--', label='Pressão minima')
    plt.text(len(dc_data) * 0.8, max, f'Pressão máxima: {max}', color='r', ha='left', va='bottom')
    plt.text(len(dc_data) * 0.8, min, f'Pressão minima: {min}', color='g', ha='left', va='bottom')
    plt.xlabel('Amostras')
    plt.ylabel('Pressão sanguinea PmmGh')
    plt.title('Estimador de pressão sanguinea')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()

    # Save the plot as a PNG file
    plt.savefig('plot.png')
    plt.show()

if __name__ == "__main__":
    main()
