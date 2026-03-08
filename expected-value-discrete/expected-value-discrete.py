import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    sum=0.0
    for i in range(0,len(x)):
        sum+=p[i]
    if sum==1.0:
        r=0.0
        for i in range(0,len(x)):
            r+=(x[i]*p[i])
        return r
    raise ValueError("Not Possible")
            
