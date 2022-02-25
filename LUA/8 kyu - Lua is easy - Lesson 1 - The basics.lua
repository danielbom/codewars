-- https://www.codewars.com/kata/lua-is-easy-lesson-1-the-basics/train/lua
-- My solution
kata = {}
function kata.firstLua(a,b,c)
    local res = string.format("%i %i ", a, a * b)
    return res .. (b >= c and "Lua" or "Codewars")
end

return kata
-- ...
kata = {}
function kata.firstLua(a, b, c)
    return a .. ' ' .. a * b .. (b >= c and ' Lua' or ' Codewars')
end

return kata
-- ...
kata = {}
function kata.firstLua(a,b,c)
    return table.concat({a, a*b, b>=c and 'Lua' or 'Codewars'}, ' ')
end

return kata
-- ...
