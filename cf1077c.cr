require "benchmark"

MAXSIZE = 10**6


# STDIN.raw do |stdin|
#     stdin.each_line do |line|
#       puts line
#     end
#   end


t = STDIN.gets.to_s.to_i
a = Array(Int128).new()
STDIN.gets.to_s.split.map{|x| a.push(x.to_i)}

time = Benchmark.measure{
    sum = uninitialized Int128
    sum = a.sum
    count = Array(Int32).new(MAXSIZE+1, 0)
    solution = Array(Int32).new()

    a.each_index {|i| count[a[i]]+=1}
    i=0
    while i <= a.size-1
        sum = sum - a[i]
        count[a[i]]-=1
        if sum.even? && sum/2 <=MAXSIZE && count[sum//2] > 0
            solution.push(i+1)
        end
        sum+=a[i]
        count[a[i]]+=1
        i+=1
    end
    # for i in 0..a.length-1
    #     sum = sum - a[i]
    #     count[a[i]]-=1
    #     if sum.even? && sum/2 <=MAXSIZE && count[sum/2] > 0
    #         solution.push(i+1)
    #     end
    #     sum+=a[i]
    #     count[a[i]]+=1
    # end

    p solution.size
    solution.map{|x| print "#{x} "}
}
p time
