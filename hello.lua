local a = -0.5
local b = 8
print(a*a-b/2)
for i = b,2*a,a do
  print(i)
end
local hello = {
  ["hello1"] = 1314,
  ["hello2"] = 520,
  ["hello3"] = 91,
}
for hellos,numbers in pairs(hello) do
  print(hellos)
  print(numbers)
end

print("Hello World from 'Lua 5.3'!")
