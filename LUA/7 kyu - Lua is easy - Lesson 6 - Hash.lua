-- https://www.codewars.com/kata/lua-is-easy-lesson-6-hash/train/lua
-- My solution
LuaArrays = {}
function LuaArrays.solve(arr)
    local map, res = {}, {}
    for i = 1, #arr do map[arr[i]] = true end
    for i = 1, math.max(table.unpack(arr)) do
        if not map[i] then table.insert(res, i) end
    end
    return res
end
return LuaArrays