# frozen_string_literal: true

first = ARGV[0].to_i
last = ARGV[1].to_i


@cache = Hash.new

def count_cycles(num)
  length = 1
  while num != 1 do
    return length + @cache[num] if @cache.include?(num)
    num = num.even? ? (num / 2) : (3 * num + 1)
    length +=1
  end
  return length
end

def max_length(i, j)
  first,last   = [i, j].minmax()
  # j.downto(i) do |i|
  (first..last).each do |x|
    @cache[x]=count_cycles(x)
  end


  puts "#{ARGV[0].to_i} #{ARGV[1].to_i} #{@cache.values.max}"
  p @a
end
max_length(first, last)
