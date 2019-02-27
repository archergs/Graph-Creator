import matplotlib.pyplot as plt

def graphMaker():
    graphType = raw_input("Enter graph type (S = Scatter, B = Bar or L = Line: ")
    if graphType == 'S':
        xAxis = []
        yAxis = []

        count = int(input("Enter the number of data points: "))

        for i in range(count):
            xData = raw_input("Enter value " + str(i + 1) + ": ")
            xAxis.append(xData)

        print xAxis

        print ("Now enter values for Y Axis!")
        for i in range(count):
            yData = raw_input("Enter value " + str(i + 1) + ": ")
            yAxis.append(yData)

        print yAxis
        print ("Creating graph...")

        plt.scatter(xAxis,yAxis)
        plt.title(raw_input("Enter graph title: "))
        plt.xlabel(raw_input("Enter X Axis title: "))
        plt.ylabel(raw_input("Enter Y Axis title: "))
        plt.grid(True)
        plt.show()

    elif graphType == 'L':
        xAxis = []
        yAxis = []

        count = int(input("Enter the number of data points: "))

        for i in range(count):
            xData = raw_input("Enter value " + str(i + 1) + ": ")
            xAxis.append(xData)

        print xAxis

        print ("Now enter values for Y Axis!")
        for i in range(count):
            yData = raw_input("Enter value " + str(i + 1) + ": ")
            yAxis.append(yData)

        print yAxis
        print ("Creating graph...")

        plt.plot(xAxis,yAxis)
        plt.title(raw_input("Enter graph title: "))
        plt.xlabel(raw_input("Enter X Axis title: "))
        plt.ylabel(raw_input("Enter Y Axis title: "))
        plt.grid(True)
        plt.show()

    elif graphType == 'B':
        xAxis = []
        yAxis = []

        count = int(input("Enter the number of data points: "))

        for i in range(count):
            xData = raw_input("Enter value " + str(i + 1) + ": ")
            xAxis.append(xData)

        print xAxis
        formatXAxis = [i + 0.5 for i, _ in enumerate(xAxis)]

        print ("Now enter values for Y Axis!")
        for i in range(count):
            yData = raw_input("Enter value " + str(i + 1) + ": ")
            yAxis.append(yData)

        print yAxis
        print ("Creating graph...")

        plt.bar(formatXAxis,yAxis)
        plt.title(raw_input("Enter graph title: "))
        plt.xlabel(raw_input("Enter X Axis title: "), fontsize=14)
        plt.ylabel(raw_input("Enter Y Axis title: "), fontsize=14)
        plt.grid(True)
        plt.xticks([i + 0.5 for i, _ in enumerate(xAxis)], xAxis)
        plt.show()
        
    elif graphType == "E":
        exit()
        
    else:
        inputError()

def inputError():
    print ("Input Error. Start Again.")
    #graphType = raw_input("Enter graph type (S = Scatter, B = Bar or L = Line: ")
    graphMaker()
    
graphMaker()
    
