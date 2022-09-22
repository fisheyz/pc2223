require 'benchmark'
MAXSIZE = 10**6

t = gets.to_i
a = gets.split.map(&:to_i)

time = Benchmark.measure{
sum = a.sum
count = Array.new(MAXSIZE+1, 0)
solution = []
# for i in 0..a.length-1
#     @count[a[i]]+=1
# end

a.each_index {|i| count[a[i]]+=1}

for i in 0..a.length-1
    sum = sum - a[i]
    count[a[i]]-=1
    if sum.even? && sum/2 <=MAXSIZE && count[sum/2] > 0
        solution.push(i+1)
    end
    sum+=a[i]
    count[a[i]]+=1
end

p solution.size
solution.map{|x| print "#{x} "}
}
p time
