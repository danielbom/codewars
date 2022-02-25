-- https://www.codewars.com/kata/lua-is-easy-lesson-3-numbers/train/lua
-- My solution
kata = {}
function kata.numbers(n)
    local res = n % 2 == 0
        and math.ceil((math.floor(n / 3) ^ 3) * math.pi)
        or math.floor((math.ceil(n / 2) ^ 2) * math.exp(2))

    local sum,max,v = 0,0
    for ch in string.gmatch(tostring(res), '.') do
        v = tonumber(ch)
        sum = sum + v
        max = max < v and v or max
    end
    
    return string.format("%d %d", max, sum)
end

return kata