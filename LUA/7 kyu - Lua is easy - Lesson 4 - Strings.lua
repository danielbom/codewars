-- https://www.codewars.com/kata/lua-is-easy-lesson-4-strings/train/lua
-- My solution
kata = {}

function isPalindrome(str)
    local k
    for i = 1, #str / 2 do
        k = #str + 1 - i
        if str:sub(i, i) ~= str:sub(k, k) then
            return false
        end
    end
    return true
end

function alternateCase(str)
    local res = ""
    for i = 1, #str do
        local ch = str:sub(i,i)
        res = res .. (i % 2 == 0 and ch:upper() or ch:lower())
    end
    return res
end

function countVowels(str)
    local vowels = "aeiou"
    local lower = str:lower()
    local count = 0
    local v, ch
    for i = 1, #lower do
        ch = lower:sub(i, i)
        for j = 1, #vowels do
            v = vowels:sub(j, j)
            count = count + (v == ch and 1 or 0)
        end
    end
    return count
end

function kata.solve(a, b, c)
    print(a, b, c)
    return string.format(
        "%s %s %d %d",
        isPalindrome(a),
        alternateCase(b),
        countVowels(c),
        #a + #b + #c
    )
end
return kata

-- ...
kata = {}
function kata.solve(a, b, c)
    return table.concat({tostring(string.reverse(a) == a),string.gsub(b,"(.)(.)",function(a,b) return string.lower(a)..string.upper(b) end),tostring(#string.gsub(c,"[^aeiou]","")),tostring(#a+#b+#c)},' ')
end
return kata

-- ...
Meme = {}
function Meme.solve(Q,S,R)
    s = ''
    J = false
    for T in S:gmatch'.' do
        J = not J
        s = s .. (J and T:lower() or T:upper())
    end
    c = 0
    for _ in R:gmatch'[aeiou]' do
        c = c + 1
    end
    return tostring(Q == string.reverse(Q)) .. ' ' ..
        s .. ' ' ..
        c .. ' ' ..
        #(Q .. S .. R)
end
return Meme

-- ...
kata = {}
function kata.solve(a, b, c)
    local palindrome = a == a:reverse()
    local _, vowels = c:gsub('[aeiou]', '')
    
    local wave = ''
    for i=1,#b do 
        local char = b:sub(i, i)
        wave = i % 2 == 0 and wave .. char:upper() or wave .. char
    end
    
    return string.format('%s %s %d %d', palindrome, wave, vowels, #a+#b+#c)
end
return kata