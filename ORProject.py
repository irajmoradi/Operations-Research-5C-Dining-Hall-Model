#OR Project
def main():
    preLoc = []
    postLoc = []
    rushFac = []
    varFac = []
    meImp = []

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = ['Breakfast', 'Brunch', 'Lunch', 'Dinner']

    sdays = "set Days := Monday Tuesday Wednesday Thursday Friday Saturday Sunday;"
    shalls = "set Halls := Frank Frary Collins Hoch McConnell Mallot;"
    srest = "set Restrictions := None Vegan Allergies;"
    smeal = "set Meals := Breakfast Brunch Lunch Dinner;"
    sloc = "set Locations := Pomona Scripps CMC Pitzer Mudd;"

    wt = "param waitTime := \n [Breakfast, *]		Frank 0.1 Frary 0.1 Collins 0.1 Hoch 0.1 McConnell 0.1 Mallot 0.1 \n [Brunch, *]	Frank 10 Frary 2 Collins 2 Hoch 5 McConnell 2 Mallot 15 \n [Lunch, *]		Frank 5 Frary 5 Collins 2 Hoch 10 McConnell 7 Mallot 5 \n [Dinner, *]	Frank 5 Frary 5 Collins 2 Hoch 10 McConnell 7 Mallot 10;"

    op = "param options := \n [Breakfast, None, *] Frank 6 Frary 6 Collins 4 Hoch 3 McConnell 3 Mallot 4 \n [Breakfast, Vegan, *] Frank 1 Frary 1 Collins 1 Hoch 2 McConnell 0 Mallot 1 \n [Breakfast, Allergies, *] Frank 1 Frary 1 Collins 0 Hoch 0 McConnell 0 Mallot 0 \n [Brunch, None, *] Frank 9 Frary 6 Collins 5 Hoch 8 McConnell 3 Mallot 7 \n [Brunch, Vegan, *] Frank 2 Frary 1 Collins 1 Hoch 1 McConnell 0 Mallot 0  \n [Brunch, Allergies, *] Frank 1 Frary 1 Collins 1 Hoch 4 McConnell 0 Mallot 3 \n [Lunch, None, *] Frank 6 Frary 5 Collins 9 Hoch 10 McConnell 5 Mallot 7 \n [Lunch, Vegan, *] Frank 1 Frary 1 Collins 1 Hoch 5 McConnell 1 Mallot 2 \n [Lunch, Allergies, *] Frank 1 Frary 0 Collins 2 Hoch 1 McConnell 0 Mallot 1] \n [Dinner, None, *] Frank 6 Frary 6 Collins 8 Hoch 12 McConnell 7 Mallot 8 \n [Dinner, Vegan, *] Frank 2 Frary 2 Collins 2 Hoch 5 McConnell 2 Mallot 2 \n [Dinner, Allergies, *] Frank 1 Frary 0 Collins 1 Hoch 1 McConnell 0 Mallot 1;"

    qual = "param quality := \n [Breakfast, None, *] Frank .81 Frary .78 Collins .65 Hoch .95 McConnell .92 Mallot 1 \n [Breakfast, Vegan, *] Frank .76 Frary .65 Collins .53 Hoch .62 McConnell .83 Mallot 1 \n [Breakfast, Allergies, *] Frank .65 Frary .32 Collins .43 Hoch .69 McConnell 1 Mallot .93 \n [Brunch, None, *] Frank .81 Frary .78 Collins .65 Hoch .95 McConnell .92 Mallot 1 \n [Brunch, Vegan, *] Frank .76 Frary .65 Collins .53 Hoch .62 McConnell .83 Mallot 1 \n [Brunch, Allergies, *] Frank .65 Frary .32 Collins .43 Hoch .69 McConnell 1 Mallot .93 \n [Lunch, None, *] Frank .81 Frary .75 Collins .75 Hoch 1 McConnell .98 Mallot .95 \n [Lunch, Vegan, *] Frank .72 Frary .64 Collins .64 Hoch .64 McConnell .88 Mallot 1 \n [Lunch, Allergies, *] Frank .37 Frary .22 Collins .32 Hoch .67 McConnell 1 Mallot .83 \n [Dinner, None, *] Frank .73 Frary .67 Collins .72 Hoch 1 McConnell .89 Mallot .87 \n [Dinner, Vegan, *] Frank .75 Frary .58 Collins .73 Hoch .83 McConnell .94 Mallot 1 \n [Dinner, Allergies, *] Frank .52 Frary .19 Collins .66 Hoch .77 McConnell 1 Mallot .81;"

    prox = "param proximity := \n [*, Pomona] Frank 4 Frary 4 Collins 8 Hoch 13 McConnell 15 Mallot 7 \n [*, Scripps] Frank 10 Frary 5 Collins 5 Hoch 5 McConnell 5 Mallot 2 \n [*, CMC] Frank 9 Frary 4 Collins 2 Hoch 8 McConnell 6 Mallot 3 \n [*, Mudd] Frank 15 Frary 10 Collins 10 Hoch 2 McConnell 8 Mallot 7 \n [*, Pitzer] Frank 17 Frary 12 Collins 7 Hoch 7 McConnell 2 Mallot 7;"

    mex = "param mealExists := \n [*, Breakfast] Monday 1 Tuesday 1 Wednesday 1 Thursday 1 Friday 1 Saturday 0 Sunday 0 \n [*, Brunch] Monday 0 Tuesday 0 Wednesday 0 Thursday 0 Friday 0 Saturday 1 Sunday 1 \n [*, Lunch] Monday 1 Tuesday 1 Wednesday 1 Thursday 1 Friday 1 Saturday 0 Sunday 0 \n [*, Dinner] Monday 1 Tuesday 1 Wednesday 1 Thursday 1 Friday 1 Saturday 1 Sunday 1;"

    print("For the following questions please enter exactly one of the following: Pomona, Scripps, CMC, Pitzer, Mudd")
    for i in range(7):
        for j in range(4):
            #q1: Pre Meal Location
            question = "Which campus are you at before "+ meals[j] +" on "+ days[i] + "? "
            
            if ((days[i] == 'Saturday' or days[i] == 'Sunday') and meals[j] != 'Breakfast' and meals[j] != "Lunch") or (days[i] != 'Saturday' and days[i] != 'Sunday' and meals[j] != 'Brunch'):
                user_input = input(question)
            
            while user_input != 'Pomona' and user_input != 'Scripps' and user_input != 'CMC' and user_input != "Pitzer" and user_input != 'Mudd' :
                user_input = input("Please enter exactly one of the following: Pomona, Scripps, CMC, Pitzer, Mudd. "+question)
            
            preLoc += [days[i][0:3] + meals[j][0:3] + user_input]
    
    prmLoc = arrangePrLocsinTable(preLoc, days)

    for i in range(7):
        for j in range(4):
            #q2: Post Meal Location
            question = "Which campus are you at after "+ meals[j] +" on "+ days[i] + "? "
            
            if ((days[i] == 'Saturday' or days[i] == 'Sunday') and meals[j] != 'Breakfast' and meals[j] != 'Lunch') or (days[i] != 'Saturday' and days[i] != 'Sunday' and meals[j] != 'Brunch'):
                user_input = input(question)
            
            while user_input != 'Pomona' and user_input != 'Scripps' and user_input != 'CMC' and user_input != "Pitzer" and user_input != 'Mudd' :
                user_input = input("Please enter exactly one of the following: Pomona, Scripps, CMC, Pitzer, Mudd. "+question)
            
            postLoc += [days[i][0:3] + meals[j][0:3] + user_input]
    
    pomLoc = arrangePoLocsinTable(postLoc, days)

    for i in range(4):
        for j in range(7):
            #q3 rush factor
            question = "How much time do you have in minutes for "+ meals[i] + " on "+ days[j]+ "? "

            if ((days[j] == 'Saturday' or days[j] == 'Sunday') and meals[i] != 'Breakfast' and meals[i] != 'Lunch') or (days[j] != 'Saturday' and days[j] != 'Sunday' and meals[i] != 'Brunch'):
                user_input = input(question)
            
            while "minutes" in user_input:
                user_input = input("Please do not include any words in your answer. "+question)

            rushFac += [days[j][0:3] + meals[i][0:3] + user_input]
        
    rfUse = rushArrange(rushFac, days)

    for i in range(4):
        #q4 variety factor
        question = "On a scale of 1 to 10 (with 1 being the least, and 10 being the most) how much do you value variety, like going to different dining halls, for "+ meals[i] +"? "

        user_input = input(question)

        varFac += [meals[i] + user_input]

    vfUse = varArrange(varFac, meals)

    #q5 daily variety factor
    dvFac = input("On a scale of 1-10 (with 1 being the least and 10 being the most) how much do you value variety, like going to different dining halls across different days? ")

    #q6 actual restrictions
    rAc = input("Please type your dietary restriction from one of: None, Vegan, Allergies ")
    while rAc != "None" and rAc != 'Vegan' and rAc != "Allergies" :
        rAc = input("Please enter exactly None, Vegan or Allergies.  What is your dietary restriction? ")

    for i in range(4): 
        #q7 meal importance
        question = "On a scale of 0 to 1 (please round to two decimal places, where 0 is the least and 1 is the most), how important is "+meals[i]+ " to you? "

        user_input = input(question)

        meImp += [user_input]

    mIUse = mealArrange(meImp, meals)

    dvUse = 'param dailyVarietyFactor := ' + str(dvFac)
    rACU = restArrange(rAc)

    fileName = input('Enter what you would like to call your file (do not include any file extensions): ')
    
    with open(fileName, 'w') as file:
        file.write(sdays + '\n')
        file.write(shalls + '\n')
        file.write(srest + '\n')
        file.write(smeal + '\n')
        file.write(sloc + '\n')
        file.write(wt + '\n')
        file.write(op + '\n')
        file.write(qual + '\n')
        file.write(prox + '\n')
        file.write(mex + '\n')
        file.write(prmLoc + '\n')
        file.write(pomLoc + '\n')
        file.write(rfUse + '\n')
        file.write(vfUse + '\n')
        file.write(dvUse + '; \n')
        file.write(rACU + '\n')
        file.write(mIUse)

    txt_to_dat(fileName, fileName+'.dat')

def txt_to_dat(input_filename, output_filename):
    with open(input_filename, 'r') as txt_file:
        # Read the content of the text file
        text_content = txt_file.read()

    with open(output_filename, 'wb') as dat_file:
        # Write the content to the binary .dat file
        dat_file.write(text_content.encode('utf-8'))

def arrangePrLocsinTable(locs, days):
    output = 'param preMealLocation := \n'
    mealV = ''
    dayV = ''
    for i in range(28):
        if i < 7:
            mealV = 'Breakfast'
        elif i < 14 and i >= 7:
            mealV = 'Brunch'
        elif i >= 14 and i < 21:
            mealV = "Lunch"
        else:
            mealV = "Dinner"
        dayV = days[(i % 7)]

        if ((dayV == 'Saturday' or dayV == "Sunday") and (mealV == 'Breakfast' or mealV == 'Lunch') or (dayV != 'Saturday' and dayV != 'Sunday' and mealV == 'Brunch')):
            output += "["+dayV+", "+mealV+", *] Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 0 \n"
        else:
            output += "["+dayV+", "+mealV+", *]"
            for j in range(len(locs)):
                if dayV[0:3] in locs[j] and mealV[0:3] in locs[j]:
                    if dayV == 'Sunday' and mealV == 'Dinner':
                        if 'Pomona' in locs[j]:
                            output += " Pomona 1 Scripps 0 CMC 0 Pitzer 0 Mudd 0;"
                        elif 'Scipps' in locs[j]:
                            output += " Pomona 0 Scripps 1 CMC 0 Pitzer 0 Mudd 0;"
                        elif 'CMC' in locs[j]:
                            output += " Pomona 0 Scripps 0 CMC 1 Pitzer 0 Mudd 0;"
                        elif 'Pitzer' in locs[j]:
                            output += " Pomona 0 Scripps 0 CMC 0 Pitzer 1 Mudd 0;"
                        else:
                            output += " Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 1;"
                    elif 'Pomona' in locs[j]:
                        output += " Pomona 1 Scripps 0 CMC 0 Pitzer 0 Mudd 0 \n"
                    elif 'Scipps' in locs[j]:
                        output += " Pomona 0 Scripps 1 CMC 0 Pitzer 0 Mudd 0 \n"
                    elif 'CMC' in locs[j]:
                        output += " Pomona 0 Scripps 0 CMC 1 Pitzer 0 Mudd 0 \n"
                    elif 'Pitzer' in locs[j]:
                        output += " Pomona 0 Scripps 0 CMC 0 Pitzer 1 Mudd 0 \n"
                    else:
                        output += " Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 1 \n"
    return output
    
def arrangePoLocsinTable(locs, days):
    output = 'param postMealLocation := \n'
    mealV = ''
    dayV = ''
    for i in range(28):
        if i < 7:
            mealV = 'Breakfast'
        elif i < 14 and i >= 7:
            mealV = 'Brunch'
        elif i >= 14 and i < 21:
            mealV = "Lunch"
        else:
            mealV = "Dinner"
        dayV = days[(i % 7)]

        if ((dayV == 'Saturday' or dayV == "Sunday") and (mealV == 'Breakfast' or mealV == 'Lunch') or (dayV != 'Saturday' and dayV != 'Sunday' and mealV == 'Brunch')):
            output += "["+dayV+", "+mealV+", *] Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 0 \n"
        else:
            output += "["+dayV+", "+mealV+", *]"
            for j in range(len(locs)):
                if dayV[0:3] in locs[j] and mealV[0:3] in locs[j]:
                    if dayV == 'Sunday' and mealV == 'Dinner':
                        if 'Pomona' in locs[j]:
                            output += " Pomona 1 Scripps 0 CMC 0 Pitzer 0 Mudd 0;"
                        elif 'Scipps' in locs[j]:
                            output += " Pomona 0 Scripps 1 CMC 0 Pitzer 0 Mudd 0;"
                        elif 'CMC' in locs[j]:
                            output += " Pomona 0 Scripps 0 CMC 1 Pitzer 0 Mudd 0;"
                        elif 'Pitzer' in locs[j]:
                            output += " Pomona 0 Scripps 0 CMC 0 Pitzer 1 Mudd 0;"
                        else:
                            output += " Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 1;"
                    elif 'Pomona' in locs[j]:
                        output += " Pomona 1 Scripps 0 CMC 0 Pitzer 0 Mudd 0 \n"
                    elif 'Scipps' in locs[j]:
                        output += " Pomona 0 Scripps 1 CMC 0 Pitzer 0 Mudd 0 \n"
                    elif 'CMC' in locs[j]:
                        output += " Pomona 0 Scripps 0 CMC 1 Pitzer 0 Mudd 0 \n"
                    elif 'Pitzer' in locs[j]:
                        output += " Pomona 0 Scripps 0 CMC 0 Pitzer 1 Mudd 0 \n"
                    else:
                        output += " Pomona 0 Scripps 0 CMC 0 Pitzer 0 Mudd 1 \n"
    return output

def rushArrange(times, days):
    output = 'param rushFactor := \n [*, Breakfast]    '
    for i in range(5):
        output += days[i] +' '+ times[i][6:] + ' '
    output += "Saturday 1000 Sunday 1000 \n [*, Brunch]    Monday 1000 Tuesday 1000 Wednesday 1000 Thursday 1000 Friday 1000 Saturday " + times[5][6:] + ' Sunday ' + times[6][6:] + '\n [*, Lunch]    '
    for i in range(5):
        output += days[i] +' '+ times[i+7][6:] + ' '
    output += 'Saturday 1000 Sunday 1000 \n [*, Dinner]     '
    for i in range(6):
        output += days[i] +' '+ times[i+12][6:] + ' '
    output += 'Sunday ' + times[-1][6:] + ';'

    return output

def restArrange(rests):
    if rests == 'None':
        output = "param restrictionActual := None 1 Vegan 0 Allergies 0;"
    elif rests == "Vegan":
        output = "param restrictionActual := None 0 Vegan 1 Allergies 0;"
    else:
        output = "param restrictionActual := None 0 Vegan 0 Allergies 1;"
    return output

def varArrange(select, meals):
    output = 'param varietyFactor := '
    for i in range(3):
        output += meals[i] + ' ' + select[i][-1] + ' '
    output += 'Dinner ' + select[-1][1] + ';'
    return output

def mealArrange(select, meals):
    output = 'param mealImportance := '
    for i in range(3):
        output += meals[i] + ' ' + select[i] + ' '
    output += 'Dinner ' + select[-1]

    return output

main()