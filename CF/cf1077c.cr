# require "benchmark"

# time = Benchmark.measure {
MAXSIZE = 10**6

t = STDIN.gets.to_s.to_i
a = Array(Int128).new
sum = uninitialized Int128

STDIN.gets.to_s.split.map { |x| a.push(x.to_i) }

sum = a.sum
count = Array(Int32).new(MAXSIZE + 1, 0)
solution = Array(Int32).new

a.each_index { |i| count[a[i]] += 1 }
i = 0
while i <= a.size - 1
  sum = sum - a[i]
  count[a[i]] -= 1
  if sum.even? && sum/2 <= MAXSIZE && count[sum//2] > 0
    solution.push(i + 1)
  end
  sum += a[i]
  count[a[i]] += 1
  i += 1
end

p solution.size
solution.map { |x| print "#{x} " }
# }
p time
