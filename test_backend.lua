-- Simple test backend
backend = {}

function backend.say_hello()
    return "Hello from Lua backend!"
end

function backend.calculate(x, y)
    return x + y, x * y
end
