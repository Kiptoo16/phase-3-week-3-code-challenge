#!/usr/bin/env python3

def pytest_itemcollected(item):
    """Customize the node ID of collected test items for better readability."""
    # Get the parent (usually the class or module) and the test function or method
    parent = item.parent.obj
    test = item.obj
    
    # Extract prefix from parent class/module docstring or name
    prefix = parent.__doc__.strip() if parent.__doc__ else parent.__class__.__name__
    
    # Extract suffix from test function/method docstring or name
    suffix = test.__doc__.strip() if test.__doc__ else test.__name__
    
    # Combine prefix and suffix to form the custom node ID
    if prefix or suffix:
        item._nodeid = " ".join((prefix, suffix))
