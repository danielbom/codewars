-- https://www.codewars.com/kata/lua-is-easy-lesson-5-arrays-1/train/lua
-- My solution
luaarrys = {}
function luaarrys.solve(arr)
    table.sort(arr)
    for i = #arr - 2, #arr do
        if arr[i] == arr[i+1] then
            table.remove(arr, arr[i])
        end
    end
    return #arr >= 2 and #arr - 2 or 0
end 
return luaarrys
-- ...
luaarrys = {}
function luaarrys.solve(arr)
    table.sort(arr)
    local count = 0
    for i = #arr - 1, 1, -1 do
    
        if(arr[i] < arr[i+1] or (i == #arr - 1 and arr[i+1] == arr[i])) then 
            count = count + 1
        end
        
        if(count == 2) then
            return i
        end
    end
    
    return 0
end 
return luaarrys