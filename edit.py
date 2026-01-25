def part(self, space:str = '') -> str:
    result = ''
    for char in self:
        result += char + space
    return result

str.part = part

'abc'.part()
