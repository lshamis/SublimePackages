import sublime, sublime_plugin

# Command: replace_with_python_result
# Replaces all highlighted regions with the Python interpretation.
# A variable `i` is automatically defined to the region index.
#
# Example:
#   `40 + 2` -> `42`
#
#   `DBG i` something `DBG i` -> `DBG 0 something DBG 1`
class ReplaceWithPythonResultCommand(sublime_plugin.TextCommand):
  def eval(self, s, var):
    parts = ['%s=%s' % item for item in var.items()] + s.split(';')
    parts[-1] = 'global __return__; __return__ = ' + parts[-1]
    s = ';'.join(parts)
    exec(s)
    return __return__

  def run(self, edit):
    for i, region in enumerate(self.view.sel()):
      if not region.empty():
        txt = self.view.substr(region)
        try:
          new_txt = str(self.eval(txt, {'i': i}))
          self.view.replace(edit, region, new_txt)
        except Exception as e:
          print('Could not replace: %s' % e)
