class Element:
  """ This class is for a css element style, it will also determine whether or
      not css properties are relevant. """

  def __init__(self, cssLine):
    self.selector = ""
    self.properties = {}
    self.populate(cssLine)

  def populate(self, cssLine):
    """ Populate the properties dict with the relevant properties """
    splittedLine = cssLine.strip('}').split('{')
    self.selector = splittedLine[0]
    propertiesSet = splittedLine[1].split(';')
    keywords = ['left', 'right', 'margin', 'padding', 'border',
     'background', 'float']
    for prop in propertiesSet:
      print(prop)
      for kw in keywords:
        """ Checks if property is relevant by checking if it contains the
            following: left, right, margin, padding, background, border, float"""
        if kw in prop:
          relevantProperty = prop.split(':')
          self.properties[relevantProperty[0].strip()] = relevantProperty[1].strip()



def main():
  El = Element('.sd > ff {height: 40px; float: left; margin: 4px 4px 5px 10px; }')
  print(El.selector)
  print(El.properties)

if __name__ == '__main__':
  main()
