
t = gets.to_i

t.times do
    right, left, j = gets.split.map(&:to_i)
    jumps = j/2
    result = j.even? ? right*jumps-left*jumps : right*(jumps+1)-left*jumps
    p result
end

