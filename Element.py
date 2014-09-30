class Element:
  """docstring for Element"""

  selector = ""
  properties = {}

  def __init__(self, cssLine):
    # .sd > ff {height: 40px; float: left; margin: 4px 4px 5px 10px; }
    populate(cssLine)

  #TODO: find if property is relevant and populate the dictionary
  def populate(cssLine):
    splittedLine = cssLine.strip('}').split('{')
    self.selector = splittedLine[0]
    propertiesSet = splittedLine[1]
    for prop in propertiesSet:
      relevantProperty = prop.split(';')
      self.properties[relevantProperty[0]] = relevantProperty[1]

  #TODO
  def checkValues(cssProperty):
    """Checks if property is relevant by checking if it contains the following:
       left, right, margin, padding, background, border, float"""
    pass
