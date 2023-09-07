# Use "," to split the string into substrings
# input e.g "2,3,4,5,6,1,4,2,5,1"

class data:
    def __init__(self, data_input):
        self.data_input = data_input

    def String_to_list_sorting(data_input):
        order_list = list(map(float, data_input.split(',')))
        order_list.sort()
        return order_list

    def standard_dev(data_input):
        import statistics                            # numpy std is n-1
        return statistics.stdev(list)                # stdev(N-1) and pstdev(N)
 
    def variance(standard_deviation):
        return standard_deviation * standard_deviation


#input
number_of_data = int(input("number of data:\n"))
input = {}                                              #a dictionary 
for number in range(number_of_data):
    input.update(dict({number: input("Input the data: \n")}))

#output
for number in number_of_data:
    print(data.String_to_list_sorting(input[number]))
    print(len(data.String_to_list_sorting(input[number])))
    print("standard deviation:", data.standard_dev(data.String_to_list_sorting(input[number])))
    print("variance:",data.variance(data.standard_dev(data.String_to_list_sorting(input[number]))))

