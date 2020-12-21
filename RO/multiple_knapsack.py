from ortools.linear_solver import pywraplp


class MakePacks:
    """
    Class that solves snpaback problem.

    Attributes:
        
        instance (instance): the instance of the snpabacl problem
        
        solver (ortools.linear_solver.pywraplp.Solver): the ortools solver that
        will solve the knapsack problem.
        
        range_snapback (range): a range from 0 to the number of snapback -1
        range_objects (range): a range from 0 to the number of objects -1
    """
    def __init__(self, instance):
        """
        Constructor of the class.
        
        Args:
            
            instance (instance): the instance of the problem.
        """
        self.instance = instance
        self.solver = pywraplp.Solver.CreateSolver('SCIP')
        self.range_snapback = range(len(instance.snapbacks))
        self.range_objects = range(len(instance.objects))
        self.add_variables()
        self.add_constraints()
        self.set_objective()
        
    def add_variables(self):
        """
        Method that create all the varibles of the problem.
        """
        self.variables = {}
        for i in self.range_objects:
            for j in self.range_snapback:
                self.variables[i, j] = self.solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    def add_constraints(self):
        """
        Method that add constraints the problem
        """
        for i in self.range_objects:
            self.solver.Add(sum(self.variables[i, j] for j in self.range_snapback) <= 1)
        for j in self.range_snapback:
            self.solver.Add(sum(self.variables[i, j] * self.instance.objects[i].weight
                for i in self.range_objects) <= self.instance.snapbacks[j].capacity)

    def set_objective(self):
        """
        Method that sets the objective ofthe solver
        """
        objective = self.solver.Objective()
        values = [i.utility for i in self.instance.objects]
        for i in self.range_objects:
            for j in self.range_snapback:
                objective.SetCoefficient(self.variables[i, j], values[i])
        objective.SetMaximization()
    
    def solve(self):
        """
        Method that runs the solver.
        """
        self.solver.Solve()
        self.from_solution_to_instance()
        return self.instance
    
    def from_solution_to_instance(self):
        """
        Method that set the result in the instance.
        """
        for j in self.range_snapback:
            for i in self.range_objects:
                if self.variables[i, j].solution_value() > 0:
                    self.instance.snapbacks[j].add_object(self.instance.objects[i])

    
