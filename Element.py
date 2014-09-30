class Element:
  """docstring for Element"""

  selector = ""
  properties = {}

  def __init__(self, cssLine):
    # .sd > ff {height: 40px; float: left; margin: 4px 4px 5px 10px; }
    seperate(cssLine)

  def seperate(cssLine):
    splittedLine = cssLine.strip('}').split('{')
    selector = splittedLine[0]
