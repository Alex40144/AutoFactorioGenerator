#this takes the raw tasks and turns them into the tasks.lua file
#this mainly reduces the need to number each task.
#may add more automation to this script in the future


def generate_lua_tasks():
    import os, shutil
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
        tasks[i] = "task[" + str(i) + "] = " + tasks[i]

    #add info for lua
    tasks.insert(0, "local task = {}")
    tasks.append("return task")

    luafile = open(luafile, "w")
    for line in tasks:
    # write line to output file
        luafile.write(line)
        luafile.write("\n")
    luafile.close()

    print("updated tasks.lua")
    shutil.copy("tasks.lua", r'C:\Users\giddy\Desktop\repos\AutoFactorio')

if __name__ == "__main__":
    generate_lua_tasks()
