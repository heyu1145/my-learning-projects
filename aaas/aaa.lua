io.write("Please input a number: \n")
local dou_a = tonumber(io.read())
if not dou_a then io.write("Please input a number!\n") return end
local a = math.floor(dou_a)
if dou_a ~= a then io.write("Please input a Integer!\n") return end
if a < 0 or a > 99999 then io.write("The number is too small or too large!\n") return end

str_a = tostring(a)
io.write("The number have " .. #str_a .. " char(s)!\n")
local char_a = {}
for i = 1, #str_a do table.insert(char_a,str_a:sub(i,i)) end
for i, char in ipairs(char_a) do io.write("Char " .. i .. " : " .. char .. "\n") end
local reversed_a = ""
for i = #char_a, 1,-1 do reversed_a = reversed_a .. char_a[i] end
io.write("The number after reverse: " .. reversed_a .. "\n") 
