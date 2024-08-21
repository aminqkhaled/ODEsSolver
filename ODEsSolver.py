import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

def solveODE (dep_var, indep_var, lhs, rhs):
    
    # Initialize the independent variable
    x = sp.Symbol(indep_var)
    
    # Initialize the dependent variable
    y = sp.Function(dep_var)(x)
    
    # Process the LHS and the RHS (sympify them)
    # The local_dict parameter in parse_expr ensures that dep_var (e.g., y) is correctly recognized as a function of x.
    lhs = sp.parse_expr(lhs, local_dict={dep_var: y})
    rhs = sp.parse_expr(rhs, local_dict={dep_var: y})
    
    # Build the differential equation: LHS=RHS
    diff_eq = sp.Eq(lhs, rhs)
    
    # Store the order of the ODE built
    order = sp.ode_order(diff_eq, y)
    
    # Ask the user for initial conditions (ics)
    quest = input("Would you like to pass in initial conditions? [Y/n]? ")
    
    # soln to return
    sol = ''
    
    # if YES prompt the user to pass in ics
    if (quest == 'Y'):
        
        # Write a dictionary with the initial conditions
        ics = {}
        for i in range(order):
            xi = int(input("Enter the value for x"+str(i)+" : "))
            yi = int(input("Enter the value for y"+str(i)+" : "))
            ics.update({y.diff(x,i).subs(x,xi): yi})
            
        # Solve the IVP
        sol = sp.dsolve(diff_eq, ics=ics)
    else:
        sol = sp.dsolve(diff_eq,y)
        
    # if the ODE has both a +ve and a -ve soln    
    if type(sol) is list:
        # return both solns
        return str(sol[0].rhs) + ', OR ' + str(sol[1].rhs)
    else:
        return sol.rhs
        

x = "x"
y = "y"
lhs = input("Enter the LHS of your ODE: ")
rhs = input("Enter the RHS of your ODE: ")
print(solveODE(y,x,lhs,rhs))
