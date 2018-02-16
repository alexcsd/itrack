#a helper module that does the mapping from the matrix
def get_track(result):
    #takes a result list of the form [1,0...]
    #result=[]

    #it converts the answers from 0 and 1 to the index of the question
    result=[int(x) for x in result]
    result=[i for i,y in enumerate(result) if y==1]

    print (result)

    result=set(result)
#the matrix
    subjects={
    'AI':								{0,1,4,5,6,7,8,9},
    'Advanceddatastructures':			{0,1,2,4,9},
    'Intro to algorithms':              {0 ,1 ,2, 9},
    'Advanced algorithms':              {0,1,2,4,9},
    'Security':                         {0, 5 ,6 ,9},
    'Mathematics for computer science': {0},
    'Computer Graphics':                {0,2,3,8,9,10},
    'Neural network':                   {0,1,2,5,8,9},
    'Data analysis':                    {0,1,4,5,8,9},
    'Data visualization':               {},
    'Intro to CS and programming':      {0,2,4},
    'OS':                               {2,8,10},
    'ML':                               {0,1,2,5,8,9},
    'Database systems':                 {0,1,2,4,},
    }



    current_max=0
    current_name=''

    subjects_list=[]

    for subject in subjects:
        x=set(subjects[subject]).intersection(result)
        if len(x)>=current_max:
            current_max=len(x)
            current_name=subject
            #pushing the subject and the intersection count as a tuple
            #(subject, intersections)
            subjects_list.append((subject,len(x)))

    #filtering the list and keeping only the subjects with max intersections
    subjects_list=[y for y in subjects_list if y[1]==current_max]
    return(current_name)
    print(subjects_list)
