import sys, getopt
from collections import OrderedDict

class Element:
  """ This class is for a css element style. It will also determine whether or
      not css properties are relevant. """

  KEYWORDS = ['left', 'right', 'margin', 'padding', 'border',
   'background:', 'position', 'float', 'shadow']

  def __init__(self, rule):
    for kw in Element.KEYWORDS: #Check if a keyword exists before continuing
      if kw in rule:
        self.selector = ""
        self.properties = OrderedDict()
        self.populate(rule)
        break #if a keyword exists, no need to loop through the rest

  def populate(self, rule):
    """ Populate the properties dict with the relevant properties """
    splittedRule = rule.strip('}').split('{')
    self.selector = splittedRule[0]
    propertiesList = splittedRule[1].split(';')
    for prop in propertiesList:
      for kw in Element.KEYWORDS:
        """ Checks if property and values are relevant by checking if it
            contains the following: left, right, margin, padding, background,
            border, float """
        if kw in prop:
          relevantProperty = prop.split(':')
          self.properties[relevantProperty[0].strip()] = relevantProperty[1].strip()

  def __str__(self):
    try:
      cssProperties = ''
      for cssProperty, value in iter(self.properties.items()):
        cssProperties += '  {0} : {1};\n'.format(cssProperty, value)
      return self.selector + ' {\n'+cssProperties+ '}\n'
    except:
      return ''


def main(argv):
  inputfile = ''
  outputfile = ''
  try:
     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
     print ('rtlhelper.py -i <inputfile> -o <outputfile>')
     sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('rtlhelper.py -i <inputfile> -o <outputfile>')
      sys.exit()
    elif arg =='-o' or arg == '' or arg == '-i' or opt == '':
        print ('rtlhelper.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    elif opt in ("-i", "--ifile"):
      inputfile = arg
    elif opt in ("-o", "--ofile"):
      outputfile = arg

  print ('Input file is: '+ inputfile)
  print ('Output file is: '+ outputfile)

  try:
    with open(inputfile, 'rt') as inFile:
      cssFile = inFile.read()
    try:
      outFile = open(outputfile, 'w')
      arr = cssFile.split('}')
      for rule in arr:
        el = Element(rule + '}')
        outFile.write(str(el))
      outFile.close()

    except:
      print('Error while trying to write to the file.')
  except:
    print('Error while opening the file.')

if __name__ == '__main__':
  main(sys.argv[1:])