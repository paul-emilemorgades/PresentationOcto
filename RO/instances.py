
class Object:
    """
    Class that represents an object with a weight and an utility.
    
    Attributes:
        index (int): the cardinal of the object in the problem, useful for test.
        utility (int): the utility of the object.
        weight (int): the weight of the object.
    """
    def __init__(self, index, weight, utility):
        self.index = index
        self.utility = utility
        self.weight = weight


class SnapBack:
    """
    Class that represents a Snapback.
    
    Attributes: 
        index (int): the cardinal of the snapback in the problem, useful for test.
        contained (list): the list of object contained by the snapback.
        utility (int): the sum of the utility of the object contained.
        load (int): the sum of the weight of the object contained.
        capacity (int): the maximum load.
    """
    def __init__(self, index, capacity):
        self.index = index
        self.contained = []
        self.utility = 0
        self.load = 0
        self.capacity = capacity
        
    def add_object(self, obj: Object):
        """
        This method add an object to the backpack and the set the value of 
        load and utility.
        
        Args:
            obj (Object): the object that will be add.
        """
        self.contained.append(obj)
        self.utility += obj.utility
        self.load += obj.weight


class Instance:
    """
    Class that reprensents an instance of the snapback problem.
    Attributes:
        objects (list): list of the object of the instance of the problem.
        snapbacks (list): list of the snapback of the instance of the problem.
    """
    def __init__(self):
        self.objects = []
        self.snapbacks = []



