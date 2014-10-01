import sys, getopt
from collections import OrderedDict

class Element:
  """ This class is for a css element style. It will also determine whether or
      not css properties are relevant. """

  KEYWORDS = ['left', 'right', 'margin', 'padding',
   'background:', 'position', 'float', 'shadow']

  def __init__(self, rule, rep):
    for kw in Element.KEYWORDS: #Check if a keyword exists before continuing
      if kw in rule:
        self.selector = ""
        self.properties = OrderedDict()
        self.populate(rule, rep)
        break #if a keyword exists, no need to loop through the rest

  def populate(self, rule, rep):
    """ Populate the properties dict with the relevant properties """
    splittedRule = rule.strip('}').split('{')
    self.selector = splittedRule[0].strip()
    propertiesList = splittedRule[1].split(';')
    for prop in propertiesList:
      for kw in Element.KEYWORDS:
        """ Checks if property and values are relevant by checking if it
            contains the following: left, right, margin, padding, background,
            border, float """
        if kw in prop:
          relevantProperty = prop.split(':')
          cssProperty= relevantProperty[0].strip()
          value = relevantProperty[1].strip()
          if 'bottom' in cssProperty or 'top' in cssProperty: break
          if cssProperty == 'padding' or cssProperty == 'margin':
            valueArray = value.split(' ')
            if len(valueArray) == 4:
              if valueArray[1] and valueArray[3] == 0:
                break
              elif rep:
                valueArray[1], valueArray[3] = valueArray[3], valueArray[1]
                value = ' '.join(valueArray)
            else: break
          elif rep: #replace left with right
            cssProperty = cssProperty.replace('left', 'l-ft')
            cssProperty = cssProperty.replace('right', 'left')
            cssProperty = cssProperty.replace('l-ft', 'right')
            value = value.replace('left', 'l-ft')
            value = value.replace('right', 'left')
            value = value.replace('l-ft', 'right')

          self.properties[cssProperty] = value
          break

  def __str__(self):
    try:
      cssProperties = ''
      for cssProperty, value in iter(self.properties.items()):
        cssProperties += '  {0}: {1};\n'.format(cssProperty, value)
      return self.selector + ' {\n'+cssProperties+ '}\n' if not cssProperties == '' else ''
    except:
      return ''

def main(argv):
  inputfile = ''
  outputfile = ''
  rep = False
  try:
     opts, args = getopt.getopt(argv,"rhi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
     print ('rtlhelper.py -i <inputfile> -o <outputfile> -r')
     sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print ('rtlhelper.py -i <inputfile> -o <outputfile> -r')
      sys.exit()
    elif opt == '-r':
      rep = True
    elif arg =='-o' or arg == '' or arg == '-i' or opt == '':
        print ('rtlhelper.py -i <inputfile> -o <outputfile> -r')
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
  except:
    print('Error while opening the file. Make sure the file exists and that you have permissions to read it.')
    sys.exit(2)

  try:
    outFile = open(outputfile, 'w')
    print('Processing...')
    elements = cssFile.split('}')
    for element in elements:
      el = Element(element + '}', rep)
      outFile.write(str(el))
    outFile.close()
    print('Done!')
  except:
    print('Error while writing to file. Make sure you have write permissions.')


if __name__ == '__main__':
  main(sys.argv[1:])
