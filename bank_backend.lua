-- bank_backend.lua
bank_backend = {}

local accounts = {}
local transaction_id = 1

-- Helper function to check if value is a number
local function is_number(value)
    return type(value) == "number"
end

function bank_backend.create_account(name, initial_balance)
    -- Validate inputs
    if type(name) ~= "string" or name:len() == 0 then
        return false, "Invalid account name"
    end
    
    if not is_number(initial_balance) then
        return false, "Balance must be a number"
    end
    
    if initial_balance < 0 then
        return false, "Balance cannot be negative"
    end
    
    if accounts[name] then
        return false, "Account already exists: " .. name
    end
    
    accounts[name] = {
        name = name,
        balance = initial_balance,
        activated = false,
        password = nil,
        transactions = {}
    }
    
    return true, "Account created: " .. name .. " with $" .. initial_balance
end

function bank_backend.activate_account(name, password)
    if type(name) ~= "string" or type(password) ~= "string" then
        return false, "Invalid input types"
    end
    
    local account = accounts[name]
    if not account then
        return false, "Account not found: " .. name
    end
    
    if #password ~= 8 then
        return false, "Password must be 8 characters"
    end
    
    account.activated = true
    account.password = password
    
    return true, "Account activated: " .. name
end

function bank_backend.deposit(name, amount, password)
    if not is_number(amount) then
        return false, "Amount must be a number"
    end
    
    local account = accounts[name]
    if not account then
        return false, "Account not found"
    end
    
    if not account.activated then
        return false, "Account not activated"
    end
    
    if account.password ~= password then
        return false, "Invalid password"
    end
    
    if amount <= 0 then
        return false, "Amount must be positive"
    end
    
    account.balance = account.balance + amount
    
    -- Record transaction
    table.insert(account.transactions, {
        id = transaction_id,
        type = "DEPOSIT",
        amount = amount,
        balance_after = account.balance,
        timestamp = os.time()
    })
    transaction_id = transaction_id + 1
    
    return true, "Deposited $" .. amount, account.balance
end

function bank_backend.withdraw(name, amount, password)
    if not is_number(amount) then
        return false, "Amount must be a number"
    end
    
    local account = accounts[name]
    if not account then
        return false, "Account not found"
    end
    
    if not account.activated then
        return false, "Account not activated"
    end
    
    if account.password ~= password then
        return false, "Invalid password"
    end
    
    if amount <= 0 then
        return false, "Amount must be positive"
    end
    
    if amount > account.balance then
        return false, "Insufficient funds"
    end
    
    account.balance = account.balance - amount
    
    -- Record transaction
    table.insert(account.transactions, {
        id = transaction_id,
        type = "WITHDRAW",
        amount = amount,
        balance_after = account.balance,
        timestamp = os.time()
    })
    transaction_id = transaction_id + 1
    
    return true, "Withdrew $" .. amount, account.balance
end

function bank_backend.get_balance(name, password)
    local account = accounts[name]
    if not account then
        return false, "Account not found"
    end
    
    if not account.activated then
        return false, "Account not activated"
    end
    
    if account.password ~= password then
        return false, "Invalid password"
    end
    
    return true, "Current balance", account.balance
end

function bank_backend.get_account_info(name)
    local account = accounts[name]
    if not account then
        return false, "Account not found"
    end
    
    local info = {
        name = account.name,
        balance = account.balance,
        activated = account.activated,
        transaction_count = #account.transactions
    }
    
    return true, "Account information", info
end

function bank_backend.transfer(from_name, to_name, amount, password)
    if not is_number(amount) then
        return false, "Amount must be a number"
    end
    
    local from_account = accounts[from_name]
    local to_account = accounts[to_name]
    
    if not from_account or not to_account then
        return false, "One or both accounts not found"
    end
    
    if not from_account.activated or not to_account.activated then
        return false, "One or both accounts not activated"
    end
    
    if from_account.password ~= password then
        return false, "Invalid password"
    end
    
    if amount <= 0 then
        return false, "Amount must be positive"
    end
    
    if amount > from_account.balance then
        return false, "Insufficient funds"
    end
    
    -- Perform transfer
    from_account.balance = from_account.balance - amount
    to_account.balance = to_account.balance + amount
    
    -- Record transactions for both accounts
    table.insert(from_account.transactions, {
        id = transaction_id,
        type = "TRANSFER_OUT",
        amount = amount,
        to_account = to_name,
        balance_after = from_account.balance,
        timestamp = os.time()
    })
    
    table.insert(to_account.transactions, {
        id = transaction_id,
        type = "TRANSFER_IN", 
        amount = amount,
        from_account = from_name,
        balance_after = to_account.balance,
        timestamp = os.time()
    })
    
    transaction_id = transaction_id + 1
    
    return true, "Transfer successful", from_account.balance
end

print("Bank backend loaded successfully!")
