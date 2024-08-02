import pyperclip

def find_matching_brace(s, start):
    stack = []
    for i in range(start, len(s)):
        if s[i] == '{':
            stack.append('{')
        elif s[i] == '}':
            stack.pop()
            if not stack:
                return i
    return -1

def extract_braced_substrings(s):
    substrings = []
    i = 0
    while i < len(s):
        if s[i] == '{':
            end = find_matching_brace(s, i)
            if end != -1:
                substrings.append(s[i:end + 1])
                i = end
        i += 1
    return substrings

def main():
    # Get the string from the clipboard
    input_string = pyperclip.paste()
    # Extract substrings enclosed in braces
    substrings = extract_braced_substrings(input_string)
    # Combine substrings into a single string
    result_string = '\n'.join(substrings)
    # Copy the result to the clipboard
    pyperclip.copy(result_string)
    print("Extracted substrings have been copied to the clipboard.")

if __name__ == "__main__":
    main()
