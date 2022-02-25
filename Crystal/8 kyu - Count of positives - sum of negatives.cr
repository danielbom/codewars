# https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives/train/crystal
# My solution
def count_positives_sum_negatives(lst)
    if lst.size == 0
        return lst
    end
    count = 0
    sum = 0
    lst.each do |i|
        if i > 0
            count += 1
        else
            sum += i
        end
    end
    return [count, sum]
end

# ...
def count_positives_sum_negatives(lst)
  return [] of typeof(lst) if lst.empty?
  groups = lst.group_by{|i| i > 0}
  [
    groups.fetch(true,  [] of Int32).size,
    groups.fetch(false, [] of Int32).sum
  ]
end

# ...
def count_positives_sum_negatives(lst)
    return [] of Int32 if lst.empty?
    [lst.select{ |nb| nb > 0 }.size, lst.select{ |nb| nb < 0 }.sum]
end

# ...
def count_positives_sum_negatives(x)
  return [x.select{|i|i>0}.size,x.select{|i|i<0}.sum] unless x.size == 0
  x
end