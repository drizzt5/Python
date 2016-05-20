class MyTokenizer:

    def __init__(self, source_text):
        self._source_text = source_text


    def next_comment(self, start_loc):
        '''
        Starting from start_loc return the start location
        and end location of the next comment. If there's
        no next comment, return len(source_txt) for both values
        :param start_loc: loc to start looking for next comment
        :return: (s, e) where s is the start of comment and e
                        the end of comment
        '''
        start = start_loc
        end   = start_loc  ### MODIFY THIS ###


        return (start, end)


if __name__ == '__main__':

    source = input("Source Filename: ")
    source_file = open(source, "r")
    source_text = source_file.read()

    tokenizer = MyTokenizer(source_text)

    stop_loc = len(source_text)

    start_loc = 0
    end_loc = 0

    while True:

        start_loc, end_loc = tokenizer.next_comment(start_loc)

        if start_loc >= stop_loc: break

        print(source_text[start_loc:end_loc+1])

        start_loc = end_loc + 1


