0x06-regular_expressions

Comments: Use # for single-line comments. For multiline comments, you can use =begin and =end.

# This is a single-line comment

=begin
This is a
multiline comment
=end

------------------------------------
Variables: You can declare variables without specifying a type. Variable names are case-sensitive.

x = 10
name = "John"

------------------------------------
Output: To display output, you can use the puts or print methods.

puts "Hello, World!"
print "Hello, World!"

-------------------------------------
Data Types: Ruby has various data types, including integers, strings, arrays, hashes, and more.

x = 42
name = "Alice"
fruits = ["apple", "banana", "cherry"]
person = { name: "Bob", age: 30 }

--------------------------------------
Conditionals: Use if, elsif, and else for conditional statements.

if x > 10
  puts "x is greater than 10"
elsif x == 10
  puts "x is equal to 10"
else
  puts "x is less than 10"
end

---------------------------------------
Loops: Ruby supports loops like while, for, and iterators.

# Using a while loop
i = 0
while i < 5
  puts i
  i += 1
end

# Using an iterator
fruits.each do |fruit|
  puts fruit
end

----------------------------------------
Functions: Define functions using the def keyword.

def add(a, b)
  return a + b
end

result = add(3, 4)
puts result  # Output: 7
----------------------------------------
Classes and Objects: Ruby is an object-oriented language. You can define classes and create objects from them.

class Person
  def initialize(name, age)
    @name = name
    @age = age
  end

  def greet
    puts "Hello, my name is #{@name}, and I'm #{@age} years old."
  end
end

person = Person.new("Alice", 25)
person.greet
-----------------------------------------
