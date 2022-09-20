# frozen_string_literal: true

@cache= [ 0, 1 ]
def fib(number)
  (0..number).each do |i|
    @cache[i] = i < 2 ? i : @cache[i - 1] + @cache[i - 2]
  end
  @cache.map { |el| puts el }
end

fib(10)
