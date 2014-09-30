class Element:
  """docstring for Element"""

  selector = ""
  properties = {}

  def __init__(self, cssLine):
    # .sd > ff {height: 40px; float: left; margin: 4px 4px 5px 10px; }
    seperate(cssLine)

  def seperate(cssLine):
    splittedLine = cssLine.strip('}').split('{')
    self.selector = splittedLine[0]
    propertiesSet = splittedLine[1]
    for prop in propertiesSet:
      relevantProperty = prop.split(';')
      self.properties[relevantProperty[0]] = relevantProperty[1]