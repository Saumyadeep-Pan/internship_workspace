total_jumping_jacks=0

for set_num in range(1,11):
    total_jumping_jacks+=10
    print(f"Perform 10 jumping jacks. Total done: {total_jumping_jacks}")
    
    if total_jumping_jacks == 100:
        print("Congratulations! You completed the workout")
        break
        
    tired=input("Are you tired? ").strip().lower()
    
    if tired in ["yes","y"]:
        skip=input("Do you want to skip the remaining sets? ").strip().lower()
        if skip in ["yes","y"]:
            print(f"You completed a total of {total_jumping_jacks} jumping jacks.")
            break
        else:
            remaining=100-total_jumping_jacks
            print(f"{remaining} jumping jacks are remaining.")
    elif tired in ["no","n"]:
        remaining=100-total_jumping_jacks
        print(f"{remaining} jumping jacks are remaining.")
