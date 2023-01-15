solution = lambda emergency : list(map(lambda i : i[0]+1, 
                                       sorted(enumerate(
                                           sorted(enumerate(emergency), key=lambda x:x[1], reverse=True)
                                       ),key=lambda x:x[1])
                                      )) 