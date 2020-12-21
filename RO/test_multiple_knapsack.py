from unittest.mock import MagicMock
from multiple_knapsack import MakePacks
from instances import Instance, Object, SnapBack


#test unitaire et mock test

class MonitorCalls:
    """
    Class that counts the number of time its method increment_call is called.
    
    Attribute:
        number_of_calls (int): number_of_calls is the counter of the number of
        time increment call is called
    """
    def __init__(self):
        self.number_of_calls = 0
    def increment_call(self):
        """
        Method that increments the value of the attriutes number_of_calls
        """
        self.number_of_calls += 1
        
def define_test_value():
    instance = make_instance()
    make_packs = MakePacks(instance)
    monitor_calls = MonitorCalls()
    mock = MagicMock()
    increment_call = lambda x: monitor_calls.increment_call()
    mock.side_effect = increment_call
    return  make_packs, mock, monitor_calls
       
    
def test_mock_add_constraint():
    make_packs, mock, monitor_calls = define_test_value()
    make_packs.solver.Add = mock
    make_packs.add_constraints()
    assert monitor_calls.number_of_calls == 5, "mock_test_add_constraint failed"

def test_add_variables():
    instance = make_instance()
    make_packs = MakePacks(instance)
    make_packs.range_objects = range(5)
    make_packs.range_snapback = range(5)
    make_packs.add_variables()
    assert make_packs.variables[4, 4] == make_packs.solver.IntVar(0, 1, 'x_%i_%i' % (4, 4))

def make_instance():
    instance = Instance()
    obj1 = Object(0, 14, 24.)
    obj2 = Object(1, 1, 24.)
    obj3 = Object(2, 24, 1.)
    instance.objects = [obj1, obj2, obj3]
    snapback1 = SnapBack(0, 25)
    snapback2 = SnapBack(1, 25)
    instance.snapbacks = [snapback1, snapback2]
    return instance

# test end-to-end

def test_two_bin():
    instance = MakePacks(make_instance()).solve()
    assert instance.snapbacks[0].contained[0].index == 1, "test_two_bin failed"
    assert instance.snapbacks[0].contained[1].index == 2, "test_two_bin failed"
    assert instance.snapbacks[1].contained[0].index == 0, "test_two_bin failed"
    assert instance.snapbacks[0].load == 25, "test_two_bin failed"
    assert instance.snapbacks[0].utility == 25, "test_two_bin failed"

def make_instance_everything_fit():
    instance = Instance()
    obj1 = Object(0, 14, 24.)
    obj2 = Object(1, 1, 24.)
    obj3 = Object(2, 24, 1.)
    instance.objects = [obj1, obj2, obj3]
    snapback1 = SnapBack(0, 100)
    instance.snapbacks = [snapback1]
    return instance

def test_everything_fit():
    instance = MakePacks(make_instance_everything_fit()).solve()
    assert instance.snapbacks[0].contained[0].index == 0, "test_everything_fit failed"
    assert instance.snapbacks[0].contained[1].index == 1, "test_everything_fit failed"
    assert instance.snapbacks[0].contained[2].index == 2, "test_everything_fit failed"

