'''

 PROBLEM:

 "A local baselball team sells tickets with two price zones.
 
 Seats closer to field are $20 per ticket. All other seats that
 are further away cost $10 per ticket.
 
 If 5,332 fans were in attendance and the total ticket revenue was
 $71,750: How many tickets in each prize zone were sold?"







 SOLUTION:

 Ok, let's classify the $20/ticket zone as X and the $10/ticket zone as Y

 Now let's try to forumulate some sort of equation out of this:

 20*x + 10*y = 71750
 x + y = 5,332

 As you can see, we have formed a system of equations out of this. Now it's actually
 solvable.

 Now we can just pass this to sympy for us to solve but I'd actually like to
 show you how you can solve without python.

 -> x + y = 5,332

 -> y = 5,332 - x              (isolate y by subtracting x from both sides) 

 
 -> 20x + 10y = 71750

 -> 20x + 10(5,332-x) = 71750

 -> 20x + 53,320 - 10x = 71750      (multiplied each elements in the bracket by 10)

 -> 10x + 53,320 = 71,750            (simplified 20x and -10x into 10x
 
 -> 10x = 18430

 -> x = 1,843

 This means that 1,843 tickets of the $20 zone were sold.

 Now let's substitute x by 1,843 in the equation x + y = 5,332 to find the value of y

 -> x + y = 5,332

 -> 1,843 + y = 5,332

 -> y = 3,489

 This means 3,489 tickets of the $10 znoe were sold.

 To recap, what we did was we got isolated one of the variable's in one of the equations
 so it's expression contains the other variable then used that expression to express that
 variable in the other equation so that way we were solving an equation that had
 only 2 of the same variable (2 x's or 2 y's) which is possible to solve.

'''