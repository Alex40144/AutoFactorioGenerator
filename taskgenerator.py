#this takes the raw tasks and turns them into the tasks.lua file
#this mainly reduces the need to number each task.
#may add more automation to this script in the future


def generate_lua_tasks():
    import os
    tasks = []

    basepath = os.path.dirname(__file__)
    luafile = os.path.abspath(os.path.join(basepath, "tasks.lua"))

    #extract info from text file
    with open(os.path.abspath(os.path.join(basepath,"tasks.txt"))) as file :
        for line in file :
            #used to have instructions at top of file
            if line[0] != "#":
                tasks.append(line.strip("\n"))

    #add necessary formattting to create table for lua
    for i in range(0, len(tasks)):
        tasks[i] = "task[#task+1] = " + tasks[i]

    #add info for lua
    tasks.insert(0, "task[0] = {\"research\"}") #this becomes line 2
    tasks.insert(0, "local task = {}") # this becomes line 1
    tasks.append("return task")

    luafile = open(luafile, "w")
    for line in tasks:
    # write line to output file
        luafile.write(line)
        luafile.write("\n")
    luafile.close()

    print("updated tasks.lua")

if __name__ == "__main__":
    generate_lua_tasks()
