// bank_system.cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <limits>
#include <lua5.3/lua.hpp>

class BankSystem {
private:
    lua_State* L;
    
    // Helper function to get validated double input
    double get_validated_double(const std::string& prompt) {
        double value;
        while (true) {
            std::cout << prompt;
            std::cin >> value;
            
            if (std::cin.fail()) {
                std::cout << "❌ Invalid input! Please enter a number." << std::endl;
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            } else {
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                return value;
            }
        }
    }
    
    // Helper function to get validated string input
    std::string get_validated_string(const std::string& prompt) {
        std::string input;
        while (true) {
            std::cout << prompt;
            std::getline(std::cin, input);
            
            if (input.empty()) {
                std::cout << "❌ Input cannot be empty! Please try again." << std::endl;
            } else {
                return input;
            }
        }
    }
    
    void print_result(bool success, const std::string& message, double balance = 0) {
        if (success) {
            std::cout << "✅ " << message;
            if (balance > 0) {
                std::cout << " | Balance: $" << std::fixed << std::setprecision(2) << balance;
            }
            std::cout << std::endl;
        } else {
            std::cout << "❌ " << message << std::endl;
        }
    }
    
    bool call_bank_function(const std::string& function_name, int num_args) {
        lua_getfield(L, -1, function_name.c_str());
        if (!lua_isfunction(L, -1)) {
            std::cout << "Error: Function '" << function_name << "' not found!" << std::endl;
            lua_pop(L, 1);
            return false;
        }
        
        if (lua_pcall(L, num_args, LUA_MULTRET, 0) != LUA_OK) {
            std::cout << "Lua error: " << lua_tostring(L, -1) << std::endl;
            lua_pop(L, 1);
            return false;
        }
        
        return true;
    }

public:
    BankSystem() {
        L = luaL_newstate();
        luaL_openlibs(L);
        
        if (luaL_dofile(L, "bank_backend.lua")) {
            std::cout << "Error loading bank backend: " << lua_tostring(L, -1) << std::endl;
            lua_pop(L, 1);
            return;
        }
        
        lua_getglobal(L, "bank_backend");
        std::cout << "✅ Bank system initialized successfully!" << std::endl;
    }
    
    ~BankSystem() {
        if (L) lua_close(L);
    }
    
    void create_account() {
        std::cout << "\n=== CREATE ACCOUNT ===" << std::endl;
        
        std::string name = get_validated_string("Account name: ");
        double balance = get_validated_double("Initial balance: $");
        
        lua_getfield(L, -1, "create_account");
        lua_pushstring(L, name.c_str());
        lua_pushnumber(L, balance);
        
        if (lua_pcall(L, 2, 2, 0) == LUA_OK) {
            bool success = lua_toboolean(L, -2);
            const char* message = lua_tostring(L, -1);
            print_result(success, message);
            lua_pop(L, 2);
        }
    }
    
    void activate_account() {
        std::cout << "\n=== ACTIVATE ACCOUNT ===" << std::endl;
        
        std::string name = get_validated_string("Account name: ");
        std::string password;
        
        while (true) {
            password = get_validated_string("8-digit password: ");
            if (password.length() == 8) {
                break;
            }
            std::cout << "❌ Password must be exactly 8 characters! Try again." << std::endl;
        }
        
        lua_getfield(L, -1, "activate_account");
        lua_pushstring(L, name.c_str());
        lua_pushstring(L, password.c_str());
        
        if (lua_pcall(L, 2, 2, 0) == LUA_OK) {
            bool success = lua_toboolean(L, -2);
            const char* message = lua_tostring(L, -1);
            print_result(success, message);
            lua_pop(L, 2);
        }
    }
    
    void deposit() {
        std::cout << "\n=== DEPOSIT MONEY ===" << std::endl;
        
        std::string name = get_validated_string("Account name: ");
        std::string password = get_validated_string("Password: ");
        double amount = get_validated_double("Amount to deposit: $");
        
        lua_getfield(L, -1, "deposit");
        lua_pushstring(L, name.c_str());
        lua_pushnumber(L, amount);
        lua_pushstring(L, password.c_str());
        
        if (lua_pcall(L, 3, 3, 0) == LUA_OK) {
            bool success = lua_toboolean(L, -3);
            const char* message = lua_tostring(L, -2);
            
            if (success) {
                double new_balance = lua_tonumber(L, -1);
                print_result(success, message, new_balance);
                lua_pop(L, 3);
            } else {
                print_result(success, message);
                lua_pop(L, 2);
            }
        }
    }
    
    void withdraw() {
        std::cout << "\n=== WITHDRAW MONEY ===" << std::endl;
        
        std::string name = get_validated_string("Account name: ");
        std::string password = get_validated_string("Password: ");
        double amount = get_validated_double("Amount to withdraw: $");
        
        lua_getfield(L, -1, "withdraw");
        lua_pushstring(L, name.c_str());
        lua_pushnumber(L, amount);
        lua_pushstring(L, password.c_str());
        
        if (lua_pcall(L, 3, 3, 0) == LUA_OK) {
            bool success = lua_toboolean(L, -3);
            const char* message = lua_tostring(L, -2);
            
            if (success) {
                double new_balance = lua_tonumber(L, -1);
                print_result(success, message, new_balance);
                lua_pop(L, 3);
            } else {
                print_result(success, message);
                lua_pop(L, 2);
            }
        }
    }
    
    void check_balance() {
        std::cout << "\n=== CHECK BALANCE ===" << std::endl;
        
        std::string name = get_validated_string("Account name: ");
        std::string password = get_validated_string("Password: ");
        
        lua_getfield(L, -1, "get_balance");
        lua_pushstring(L, name.c_str());
        lua_pushstring(L, password.c_str());
        
        if (lua_pcall(L, 2, 3, 0) == LUA_OK) {
            bool success = lua_toboolean(L, -3);
            const char* message = lua_tostring(L, -2);
            
            if (success) {
                double balance = lua_tonumber(L, -1);
                print_result(success, message, balance);
                lua_pop(L, 3);
            } else {
                print_result(success, message);
                lua_pop(L, 2);
            }
        }
    }
    
    void show_menu() {
        while (true) {
            std::cout << "\n" << std::string(50, '=') << std::endl;
            std::cout << "           BANK MANAGEMENT SYSTEM" << std::endl;
            std::cout << std::string(50, '=') << std::endl;
            std::cout << "1. 🆕 Create Account" << std::endl;
            std::cout << "2. 🔓 Activate Account" << std::endl;
            std::cout << "3. 💰 Deposit Money" << std::endl;
            std::cout << "4. 🏧 Withdraw Money" << std::endl;
            std::cout << "5. 📊 Check Balance" << std::endl;
            std::cout << "6. 🔄 Transfer Money" << std::endl;
            std::cout << "7. 📋 Account Info" << std::endl;
            std::cout << "0. 🚪 Exit" << std::endl;
            std::cout << std::string(50, '=') << std::endl;
            std::cout << "Choose option: ";
            
            int choice;
            std::cin >> choice;
            std::cin.ignore(); // Clear the newline character
            
            switch (choice) {
                case 1: create_account(); break;
                case 2: activate_account(); break;
                case 3: deposit(); break;
                case 4: withdraw(); break;
                case 5: check_balance(); break;
                case 6: transfer_money(); break;
                case 7: account_info(); break;
                case 0: 
                    std::cout << "Thank you for using our banking system! 👋" << std::endl;
                    return;
                default: 
                    std::cout << "❌ Invalid option! Please try again." << std::endl;
            }
            
            std::cout << "\nPress Enter to continue...";
            std::cin.get();
        }
    }
    
    // You can add transfer_money() and account_info() methods later
    void transfer_money() {
        std::cout << "\n⚠️  Transfer feature coming soon!" << std::endl;
    }
    
    void account_info() {
    std::cout << "\n=== ACCOUNT INFORMATION ===" << std::endl;
    
    std::string name;
    std::cout << "Account name: ";
    std::cin >> name;
    
    lua_getfield(L, -1, "get_account_info");
    lua_pushstring(L, name.c_str());
    
    // Call: 1 arg, expect 3 results (bool, string, table)
    if (lua_pcall(L, 1, 3, 0) == LUA_OK) {
        bool success = lua_toboolean(L, -3);
        const char* message = lua_tostring(L, -2);
        
        if (success && lua_istable(L, -1)) {
            std::cout << "✅ " << message << std::endl;
            
            // Extract values from the table
            lua_getfield(L, -1, "name");
            const char* account_name = lua_tostring(L, -1);
            lua_pop(L, 1);
            
            lua_getfield(L, -1, "balance");
            double balance = lua_tonumber(L, -1);
            lua_pop(L, 1);
            
            lua_getfield(L, -1, "activated");
            bool activated = lua_toboolean(L, -1);
            lua_pop(L, 1);
            
            lua_getfield(L, -1, "transaction_count");
            int transaction_count = lua_tointeger(L, -1);
            lua_pop(L, 1);
            
            // Display the information
            std::cout << "📋 Account Details:" << std::endl;
            std::cout << "   Name: " << account_name << std::endl;
            std::cout << "   Balance: $" << std::fixed << std::setprecision(2) << balance << std::endl;
            std::cout << "   Status: " << (activated ? "🟢 Activated" : "🔴 Inactive") << std::endl;
            std::cout << "   Transactions: " << transaction_count << std::endl;
            
        } else {
            std::cout << "❌ " << message << std::endl;
        }
        
        lua_pop(L, 3);  // Clean up all 3 return values
    }
}
};

int main() {
    BankSystem bank;
    bank.show_menu();
    return 0;
}
