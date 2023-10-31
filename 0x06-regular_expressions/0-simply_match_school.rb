#!/usr/bin/env ruby

# Use ARGV to access command-line arguments. ARGV[0] is the first argument.
# Scan the argument for the regular expression /School/.
# The scan method returns an array of matched substrings.
# Join the matched substrings together into a single string.
puts ARGV[0].scan(/School/).join
