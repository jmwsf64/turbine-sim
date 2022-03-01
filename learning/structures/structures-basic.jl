#=========================================================
structures are the closest thing to a class that julia has
=========================================================#
struct X
    a
    b
end

obj0 = X(1,2)
println(obj0.a)



#========================================================
mutable structures can be modified after they are defined
========================================================#
mutable struct Y
    a
    b
end

obj1 = Y(3,4)
obj1.b = 5
println(obj1.b)
