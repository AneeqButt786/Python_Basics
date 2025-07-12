# 🧵 Basic String Operations
#Strings are text inside quotes:

astring = "Hello world!"
astring2 = 'Hello world!'


### **1. Get Length**
astring = "Hello world!"
print(len(astring))
#💡 Shows how many characters (including spaces and punctuation).
#**Output: 12**

### **2. Find First Occurrence**
astring = "Hello world!"
print(astring.index("o"))
#Finds where the first "o" is.
#Starts counting from 0, so "o" is at position 4, not 5.

### **3. Count Letters**
astring = "Hello world!"
print(astring.count("l"))
#Counts how many times "l" appears.
#**Output: 3** (that's lowercase L, not the number 1). 

### **4. Simple Slicing**
astring = "Hello world!"
print(astring[3:7])
#Shows letters from index 3 to 6 (7 is not included).
#Python uses start-inclusive, end-exclusive slicing.

### **5. Extended Slicing**
astring = "Hello world!"
print(astring[3:7:2])
#Same as above, but skips every second character — it shows index 3 and 5.
#This is an extended slice syntax. The general form is [start:stop:step].

### **6. Reverse a String**
astring = "Hello world!"
print(astring[::-1])
#A cool trick to reverse text: step through the string backwards. 

### **7. Change Case**
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
#.upper() makes all letters uppercase.
#.lower() makes them lowercase.

### **8. Check Start or End**
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdf"))
#Tells if the string starts with or ends with the given text.
#**Returns True or False.**

### **9. Split a String**
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
#Breaks the string into words where there’s a space.
#**Result: ["Hello", "world!"]**

### **Exercise**
#Try to fix the code to print out the correct information by changing the string.

s = "Hey there! what should this string be?"

# Length should be 20
print(f"Length of s = {len(s)}")

# First occurrence of "a" should be at index 8
print(f"The first occurrence of the letter a = {s.index('a')}")

# Number of a's should be 2
print(f"a occurs {s.count('a')} times")

# Slicing the string into bits
print(f"The first five characters are '{s[:5]}'")         # Start to 5
print(f"The next five characters are '{s[5:10]}'")        # 5 to 10
print(f"The thirteenth character is '{s[12]}'")           # Just number 12
print(f"The characters with odd index are '{s[1::2]}'")   # (0-based indexing)
print(f"The last five characters are '{s[-5:]}'")         # 5th-from-last to end

# Convert everything to uppercase
print(f"String in uppercase: {s.upper()}")

# Convert everything to lowercase
print(f"String in lowercase: {s.lower()}")

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print(f"Split the words of the string: {s.split(' ')}")
