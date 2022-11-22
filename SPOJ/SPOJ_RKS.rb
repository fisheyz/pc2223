arr = []
hash=Hash.new(0)
t = gets.split.map(&:to_i)
c = gets.split.map(&:to_i).tally

# TODO MAYBE??
# delete keys higher than t[1]
c.values.each{|el| arr.append(el)}

arr = arr.sort.reverse!
(0..arr.size-1).each{|i|
    tmp = c.key(arr[i])
    arr[i].times {print "#{tmp} "}
    c.delete(tmp)
}

