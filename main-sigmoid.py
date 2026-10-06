import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if((type(x)==type(1.5)) or type(x)==type(1)):
        return 1/(1+np.exp(-x))  
    else:
        is_nested = any(isinstance(i,list) for i in x)
        result = []
        if(is_nested):
            for i in x:
                result.append([1/(1+np.exp(-j)) for j in i])
            return result
            
        return [1/(1+np.exp(-y)) for y in x ]
