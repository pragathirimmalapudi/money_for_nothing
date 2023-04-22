import sys
from itertools import islice

def profit(no_of_producers, no_of_consumers ,producer_list, consumer_list):
    
    profits_list = []
    
    for i in range(no_of_producers):
        
        for j in range(no_of_consumers):
            
            if consumer_list[j][1] - 1 >= producer_list[i][1] :
                
                profit = consumer_list[j][0] - producer_list[i][0]
                
                profits_list.append(profit)
                
    if  profits_list == [] or max(profits_list) < 0:
        
        return 0
    else:
        
        return max(profits_list)

no_of_producers = int(sys.argv[1])
no_of_consumers = int(sys.argv[2])

producers = [int(sys.argv[i]) for i in range(3,(2*no_of_producers+3))]

i = 2*no_of_producers+3
consumers = [int(sys.argv[j]) for j in range((2*no_of_producers+3),(i+no_of_consumers*2))]

length1 = [2 for i in range(no_of_producers)]
length2 = [2 for i in range(no_of_consumers)]

pl_input=iter(producers)
cl_input=iter(consumers)

producers_list = [list(islice(pl_input, i)) for i in length1]
consumers_list = [list(islice(cl_input, i)) for i in length2]

print(profit(no_of_producers, no_of_consumers, producers_list, consumers_list))