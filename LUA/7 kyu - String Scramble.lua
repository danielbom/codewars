-- https://www.codewars.com/kata/string-scramble/train/lua
-- My solution
local kata = {}

function table.clone(org) return {table.unpack(org)} end

function kata.scramble(str, idxs)
    local sorted = table.clone(idxs)
    table.sort(sorted)
    local res = ""
    for i, v1 in pairs(sorted) do
        for j, v2 in pairs(idxs) do
            if v2 == v1 then
                res = res .. string.sub(str, j, j)
                break
            end
        end
    end
    return res
end

return kata

-- ...
local kata = {}

function kata.scramble(str, idxs)
    result = {}
    for i = 1, #idxs do
        result[idxs[i]] = string.sub(str, i, i)
    end
    return table.concat(result, "")
end

return kata