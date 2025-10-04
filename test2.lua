io.write("hello!\n")
io.write("Please Input a number: ")
local Input = tonumber(io.read())
if not Input then return end
io.write("\n")
local A = Input%2
io.write("The number is ")
if A == 0 then
  io.write("Even\n")
elseif A == 1 then
  io.write("Odd\n")
else
  io.write("Decimal,Remainder: " ..  A .. "\n")
end
io.write("The number has ")
if Input > 0 then
  local B = math.sqrt(Input)
  io.write("two roots: " .. B .. "and" .. -B  .."\n")
elseif Input == 0 then
  local B = 0
  io.write("one root: " .. B .. "\n")
else 
  local B = math.sqrt(-Input)
  io.write("no real root\n")
  io.write("Two of Imaginary roots: " .. B .. "i and " .. -B .. "i\n")
end
