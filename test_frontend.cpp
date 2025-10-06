#include <iostream>
#include <lua5.3/lua.hpp>

int main() {
    std::cout << "Testing Lua + C++ in Termux..." << std::endl;
    
    // Create Lua state
    lua_State* L = luaL_newstate();
    luaL_openlibs(L);
    
    // Load Lua script
    if (luaL_dofile(L, "test_backend.lua")) {
        std::cerr << "Error loading Lua script: " << lua_tostring(L, -1) << std::endl;
        lua_pop(L, 1);
        return 1;
    }
    
    // Get the backend table
    lua_getglobal(L, "backend");
    if (!lua_istable(L, -1)) {
        std::cerr << "Backend table not found!" << std::endl;
        lua_close(L);
        return 1;
    }
    
    // Call say_hello function
    lua_getfield(L, -1, "say_hello");
    if (lua_pcall(L, 0, 1, 0) == LUA_OK) {
        std::cout << "Lua: " << lua_tostring(L, -1) << std::endl;
        lua_pop(L, 1);
    } else {
        std::cerr << "Error calling function: " << lua_tostring(L, -1) << std::endl;
        lua_pop(L, 1);
    }
    
    // Call calculate function
    lua_getfield(L, -1, "calculate");
    lua_pushnumber(L, 5);
    lua_pushnumber(L, 3);
    if (lua_pcall(L, 2, 2, 0) == LUA_OK) {
        double sum = lua_tonumber(L, -2);
        double product = lua_tonumber(L, -1);
        std::cout << "5 + 3 = " << sum << std::endl;
        std::cout << "5 * 3 = " << product << std::endl;
        lua_pop(L, 2);
    }
    
    lua_close(L);
    std::cout << "Test completed successfully!" << std::endl;
    return 0;
}
