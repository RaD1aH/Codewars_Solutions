# For every good kata idea there seem to be quite a few bad ones!
#
# In this kata you need to check the provided array (x) for good ideas 
# 'Publish!', if there are more than 2 return 'I smell a series!'. If there 
# are no good ideas, as is often the case, return 'Fail!'.

def well(x):
    if x.count('good') >= 3:
        return "I smell a series!"
    elif x.count('good') >= 1:
        return "Publish!"
    else:
        return "Fail!"