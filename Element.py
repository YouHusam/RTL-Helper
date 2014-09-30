class Element:
  """ This class is for a css element style. It will also determine whether or
      not css properties are relevant. """

  def __init__(self, rule):
    self.selector = ""
    self.properties = {}
    self.populate(rule)

  def populate(self, rule):
    """ Populate the properties dict with the relevant properties """
    splittedRule = rule.strip('}').split('{')
    self.selector = splittedRule[0]
    propertiesList = splittedRule[1].split(';')
    keywords = ['left', 'right', 'margin', 'padding', 'border',
     'background', 'float']
    for prop in propertiesList:
      for kw in keywords:
        """ Checks if property and values are relevant by checking if it
            contains the following: left, right, margin, padding, background,
            border, float """
        if kw in prop:
          relevantProperty = prop.split(':')
          self.properties[relevantProperty[0].strip()] = relevantProperty[1].strip()

  def __str__(self):
    cssProperties = ''
    for cssProperty, value in iter(self.properties.items()):
      cssProperties += '  ' + cssProperty + ':' + value + ';\n'
    return self.selector + '{\n' + cssProperties + '}'


def main():
  El = Element('.sd > ff {height: 40px; float: left; margin: 4px 4px 5px 10px; padding-left: 40px; position: right }')
  print(El)

if __name__ == '__main__':
  main()
