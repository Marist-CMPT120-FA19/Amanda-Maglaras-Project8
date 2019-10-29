#Amanda Maglaras
#amanda.maglaras1@marist.edu
#Cooling and Heating Degree Days


def main():
        temp= input("Enter the average tempurature per day separated by spaces: ")
        temp=temp.split(" ")
        cooling=0
        heating=0

        for i in temp:
            if float(i)> 80 or float(i)<60:
                if float(i)> 80:
                    cooling += float(i)-80
                else:
                    heating += 60-float(i)

        print("There are", cooling, "cooling degrees days and there are ", heating, "heating degrees days")
main()
