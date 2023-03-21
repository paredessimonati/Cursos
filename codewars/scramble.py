def scramble(s1, s2):
    s1 = {s1}
    s2 = {s2}
    if s2.difference_update(s1) == None:
        return True
    return False
    
    
    
    
    
    
    
    
    # s2 = [*s2]   
    # for letter in s1:
    #     if letter in s2:
    #         s2.remove(letter)
    #     if not s2:
    #         print("True")
    #         return True
    # print("True")
    # return False
            
    
    
    
    
    
    
    

scramble('rkqodlw', 'world')# ==> True
scramble('cedewaraaossoqqyt', 'codewars')# ==> True
scramble('katas', 'steak')# ==> False