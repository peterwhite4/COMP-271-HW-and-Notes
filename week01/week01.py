#Isomorphic Strings problem
def are_isomorphic(s, t):

    #Define a counter variable to be able to go through the letters in each string and keep loop going/stop it if needed
    i = 0

    #Define lists to keep track of letters that have already been seen
    s_seen = []
    t_seen = []

    #Boolean variable to keep track of isomporphic or not because of only 1 return statement
    boolean = True
    
    #Check and make sure that the index we are looking at only has letters in them, per constraints.
    if not (('a' <= s[i] and s[i] <= 'z') or ('A' <= s[i] and s[i] <= 'Z')):
            boolean = False
    if not (('a' <= t[i] and t[i] <= 'z') or ('A' <= t[i] and t[i] <= 'Z')):
            boolean = False

    #Then make sure the two strings are the same length, >= 1 and <= 500, per constraints
    if (len(s) == len(t)) and (1 <= len(s) <= 500):
                
        #Make a while loop to make sure we go through each index of both strings but not past it.
        while i < len(s) and boolean == True:

            #Character variables for each string at index i
            sc = s[i]
            tc = t[i]
            
            #index variable for inner loop
            j = 0
            #Boolean for a found "s" variable
            s_found = False
            #Start of inner toop to check s_seen

            #First we make sure j isn't past the s_seen list length
            while j < len(s_seen):
                #Then we check if the character at s_seen at j matches sc
                if s_seen[j] == sc:
                    #If it does, we set s_found to true
                    s_found = True
                    #Then we check if the corresponding t_seen at THIS j matches to tc
                    if t_seen[j] != tc:
                        #If it doesn't, it can't be isomorphic
                        boolean = False

                #index up for s_seen loop if all goes well and keep going through s_seen
                j += 1

            #We now need to make sure its isomorphic from the t side as well going to s

            #Reset j for t_seen loop
            j = 0
            #Boolean for a found "t" variable
            t_found = False
            #Start of inner loop for t_seen
            #All of this is the same thing as the s_seen loop but reversed
            while j < len(t_seen):
                if t_seen[j] == tc:
                    t_found = True
                    if s_seen[j] != sc:
                        boolean = False

                #index up for t_seen loop
                j += 1

            #Index up for outer loop
            i += 1     

            #If neither letter in s or t have been seen before, write them to the seen lists
            if s_found == False and t_found == False: 
                s_seen += [sc]
                t_seen += [tc]

            #Elif statement. Only one letter has been seen before, this means the strings can't be isomorphic
            elif s_found != t_found:
                boolean = False

    else:
        boolean = False

    #Our one return statement
    return boolean 



#Interleaving Strings problem
def is_interleaved(s1, s2, s3):

    #Define counter variables for loop
    counter1 = 0
    counter2 = 0

    #Define bool to return True or False at the End for ONE return statement
    boolean = True

    #Define an empty string to compare to s3
    new_string = ""

    #Check constraints
    if (0 <= len(s1) <= 100) and (0 <= len(s2) <= 100) and (0 <= len(s3) <= 200):

        #Create a while loop that checks the size of the counters
        while (counter1 < len(s1)) and (counter2 < len(s2)) and boolean == True:
            
            #Check and make sure constraints are followed for lowercase letters'
            #Create char variables for s1, s2, and s3
            s1_char = s1[counter1]
            s2_char = s2[counter2]
            
            #Since s3 is supposed to be interleaved, we use s1 and s2 counters added together
            s3_char = s3[counter1 + counter2]

            if (s1_char < 'a' or s1_char > 'z') or (s2_char < 'a' or s2_char > 'z') or (s3_char < 'a' or s3_char > 'z'):
                boolean = False

            #Create a way to interleave the characters from s1 and s2 to make s3
            new_string += s1[counter1] + s2[counter2]

            #Add to our counters to move onto next index of s1 and s2
            counter1 += 1
            counter2 += 1

    else:
        boolean = False

    if new_string != s3:
        boolean = False

    return boolean



#Contiguous Length problem
def contiguous_length(nums):

    #index variable for loop
    i = 0

    #Variable to keep track of longest length
    longest_length = 0

    #Make sure constraints are followed
    if (nums[i] == 0 or nums[i] == 1) and (1 <= len(nums) <= 100000):

        #Start outer loop to go through the array and set up count variables
        while i < len(nums):

            #Keep seperate counts of 0s and 1s.
            #These have to reset in loop because we move down the list, but the length value is still kept inside inner loop
            count0 = 0
            count1 = 0

            #New variable set equal to i to check count in inner loop
            j = i

            #Start of inner loop
            while j < len(nums):

                #Add 0 or 1 to their count based on what nums[j] is
                if nums[j] == 0:
                    count0 += 1
                else:
                    count1 += 1

                #Only contiguous if both counts are equal
                if count0 == count1:
                    #We need j - i + 1 to get the length of the subarray (j-i gives the numbers in the middle, +1 gets the ends)
                    length = j - i + 1
                    #Since we keep going through the array from the start to finish, we need to find the biggest length
                    if length > longest_length:
                        longest_length = length

                #Index up for j inner loop
                j += 1
        
            #Index up for outer loop
            i += 1
    
    else:
        longest_length = 0

    #Return the length of the count list
    return longest_length

