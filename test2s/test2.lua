io.write("hello!\n")
io.write("Please Input a number: ")
local Input = tonumber(io.read())
local isOdd = false
if not Input then io.write("Please insert a number!") return end
io.write("\n")
local A = Input%2
io.write("The number is ")
if A == 0 then
  io.write("Even\n")
elseif A == 1 then
  io.write("Odd\n")
  isOdd = true
else
  io.write("Decimal,Remainder: " ..  A .. "\n")
end
local isPositive = false
io.write("The number has ")
if Input > 0 then
  local B = math.sqrt(Input)
  isPositive = true
  io.write("two roots: " .. B .. " and " .. -B  .."\n")
elseif Input == 0 then
  io.write("one root: 0\n")
else 
  local B = math.sqrt(-Input)
  io.write("no real root\n")
  io.write("Two of Imaginary roots: " .. B .. "i and " .. -B .. "i\n")
end
io.write("The number is ")
if Input == 2 then io.write("a prime\n")
elseif Input == 1 then io.write("NOT a prime\n")
elseif isOdd and isPositive then
  local match = nil
  for i = 3,math.ceil(math.sqrt(Input)),2 do
    if Input%i == 0 then
      io.write("NOT a prime\n")
      match = i
      break
    end
  end
  if match == nil then io.write("a prime\n") end
else io.write("NOT a prime\n") end
