-- https://www.codewars.com/kata/word-values/train/lua
-- My solution
wordvalues = {}
function wordvalues.wordValues(arr)
    returned = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i,str in ipairs(arr) do 
        str = string.lower(str)
        sum = 0
        for chr in str:gmatch"." do
            k = 1
            for alpha in alphabet:gmatch"." do
                if chr == alpha then
                    sum = sum + k
                end
                k = k + 1
            end
        end
        returned[i] = sum * i
    end
    for key, value in ipairs(returned) do
        print(key, value)
    end
    return returned
end
return wordvalues

-- ...
wordvalues = {}
function wordvalues.wordValues(arr)

  outputArr = {}
  for index, value in ipairs(arr) do
    local sum = 0
    for charac in value:gmatch(".") do
      if charac ~= " " then
        sum = sum + (string.byte(charac) - 96)
      end
    end
    table.insert(outputArr, index*sum)
  end
  return outputArr
end
return wordvalues

-- ...
wordvalues = {}

function letter_value(ch) if ch==' ' then return 0 else return string.byte(ch)-string.byte('a')+1 end end

function str_foldl(op,e,str)
  local acc = e
  for i = 1, #str do acc = op(acc,string.sub(str,i,i)) end
  return acc
end

function string_value(s) return str_foldl(function(acc,x) return acc+letter_value(x) end, 0,s) end

function wordvalues.wordValues(arr)  
  local sums = {}
  for i,w in pairs(arr) do sums[i] = i*string_value(w) end
  return sums
end

return wordvalues

-- ...
wordvalues = {}
function wordvalues.wordValues(arr)
  local result = {}
  for index in pairs(arr) do
    local word = string.gsub(arr[index],"%s","")
    local sum = 0
    --print(word)
    for i = 1 , #word, 1 do
      local c = string.sub(word,i,i)
      local char = string.byte(c) - 96
      print(c..char)
      sum = sum + char
    end
    result[#result + 1] = sum * index
  end
  return result
end
return wordvalues

-- ...
wordvalues = {}
function wordvalues.wordValues(arr)
  local result = {}
  for i, v in ipairs(arr) do
    local sum = 0
    for k in v:gmatch('%a') do
      sum = (k:byte()-96) + sum
    end
    table.insert(result, sum*i)
  end
  return result
end
return wordvalues