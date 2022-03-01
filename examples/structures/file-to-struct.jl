#================
define the struct
================#
mutable struct X
    a
end

#==========================
# function to read the file
==========================#
function readInputFile(a, fileName)
    f = open(fileName, "r")
    line_count = 0
    for line in readlines(f)
        line_count += 1
        a[line_count] = parse(Int64, line)
    end
    return a
end

#============================================
initialize the object with placeholder values
============================================#
obj = X([0,0,0])

#=========================================
redefine the value of the object attribute
=========================================#
obj.a = readInputFile(obj.a, "input-file.txt")

#===============
print the output
===============#
println(obj.a)
