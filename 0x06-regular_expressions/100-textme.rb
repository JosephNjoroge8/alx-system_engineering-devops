#!/usr/bin/env ruby

pattern = /\[from:(?<sender>.*?)\] \[to:(?<receiver>.*?)\] \[flags:(?<flags>.*?)\]/

ARGV.each do |line|
  match = line.match(pattern)
  if match
    puts "#{match[:sender]},#{match[:receiver]},#{match[:flags]}"
  end
end
