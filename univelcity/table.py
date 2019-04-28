class Statistics():
    

    def __init__(self, x_list, y_list):
        self.x = x_list
        self.y = y_list

    
    def sum_x(self):
        total_x = sum(self.x)
        # print(total_x)
        return total_x
    
    def mean_x(self):
        nx = len(self.x)
        mean = self.sum_x() / nx
        print(mean)
        return mean


    def sum_y(self):
        total_y = sum(self.y)
        # print(total_y)
        return total_y

    def mean_y(self):
        ny = len(self.y)
        mean = self.sum_y() / ny
        print(mean)
        return mean

    def x_xbar(self):
        
        pass
    
    def y_ybar(self):

        pass


x = [1,2,3,4,5,6,7]
y = [4,6,8,10,12,16,18] 
stat = Statistics(x,y)
stat.sum_x()
stat.sum_y()
stat.mean_x()
stat.mean_y()

