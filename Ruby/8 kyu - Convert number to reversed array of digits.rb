# https://www.codewars.com/kata/convert-number-to-reversed-array-of-digits/train/ruby
# My solution
def digitize(n)
    $numbers = []
    while n > 0 do
        $numbers.push(n % 10)
        n /= 10
    end
    return $numbers
end

# ...
def digitize(n)
    n.to_s.chars.reverse.map(&:to_i)
end

# ...
def digitize(n)
    n.to_s.chars.reverse.map(&:to_i)
end

# ...
def digitize(n)
    n.to_s.split('').reverse!.map(&:to_i)
end

# ...
def digitize(n)
    n.to_s.each_char.map(&:to_i).reverse
end

# ...
def digitize(n)
    array = n.to_s.split(//)
    new_array = []
    array.each do |number|
        new_array << number.to_i
    end
    new_array.reverse
end

# ...
def digitize(n)
    (n.to_s.split('').map { |digit| digit.to_i }).reverse
end
   