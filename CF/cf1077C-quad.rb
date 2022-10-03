require 'pry-byebug'
require 'benchmark'

time = Benchmark.measure{
    t = gets.to_i
    array = gets.split.map(&:to_i)

    @solution = []
    for i in 1..t do
        catch :goodArrayFound do
            tmp_arr = array.reject.each_with_index{ |_,v| v==i-1 }
            tmp_idx = i-1
            for j in 1..t-1
                ith_sum = (
                        deleted = tmp_arr.delete_at(j-1)
                        sum = tmp_arr.sum
                        )
                tmp_arr.insert(j-1, deleted)
                if sum==deleted
                    @solution.insert(0, i)
                    throw :goodArrayFound
                end
            end
        end
    end
    if  @solution.length == 0
        p 0
    else
        puts @solution.length
        @solution.map{|x| print "#{x} "}
    end

}
p time
