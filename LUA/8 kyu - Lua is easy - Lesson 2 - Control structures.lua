-- https://www.codewars.com/kata/lua-is-easy-lesson-2-control-structures/train/lua
-- My solution
kata = {}
function kata.solve(n)
    kata[n] = n >= 2 and kata.solve(n-1) + kata.solve(n-2) + 1 or 1 -- Cached
    return kata[n]
end
return kata

-- ...
local function fibonacci(n)
    return n >= 2 and fibonacci(n - 1) + fibonacci(n - 2) or n
end

return {
    solve = function (n)
        return 2 * fibonacci(n + 1) - 1
    end
}

-- ...
kata = {}
function kata.solve(n) 
    local a, b = 1, 1
    for i = 1, n do
        a, b = b, a + b + 1
    end
    return a
end
return kata