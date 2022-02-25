-- https://www.codewars.com/kata/find-nearest-square-number/train/lua
-- My solution
return {
    nearest_sq = function(n)
        while true do
            sqrt = math.sqrt(n)
            _, frac = math.modf(sqrt)
            if frac == 0 then return n end
            n = frac > 0.5 and n + 1 or n - 1
        end
    end
}
-- ...
return {
    nearest_sq = function(n)
        return math.floor(math.sqrt(n)+0.5)^2
    end
}
-- ...
return {
    nearest_sq = function(n)
        return math.ceil((n^.5)-0.5)^2
    end
}