import sublime, sublime_plugin
import re

# Command: natural_sort
# Sorts a selected list of lines in a "natural way".
# Numeric segments of a string are compared by value,
# rather of lexicographically.
#
# Example:
#
#   Before:
#     file1.txt
#     file10.txt
#     file2.txt
#     file20.txt
#
#   After:
#     file1.txt
#     file2.txt
#     file10.txt
#     file20.txt
class NaturalSortCommand(sublime_plugin.TextCommand):
  def run(self, edit, reverse=False):
    for region in self.view.sel():
      if region.empty():
        continue
      sorted_list = sorted(
          self.view.substr(region).splitlines(),
          key=lambda line: [int(part) if part.isdigit() else part
                            for part in re.split(r'(\d+)', line.lower())],
          reverse=reverse)
      self.view.replace(edit, region, '\n'.join(sorted_list))
