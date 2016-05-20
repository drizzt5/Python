

def remove_comments(source, destination):
    '''
    Remove all comments from source and save the resulting Jack program
    with no comments in destination file.
    :param source: name of the Jack source file
    :param destination: name of the destination file for storing source file
                        all comments removed
    :return: None
    '''

    source_file = open(source, "r")
    dest_file = open(destination, "w")

    source_text = source_file.read()
    source_file.close()

    no_commment_source = ""

    ## Go through source_text one char at a time
    ## if this char is not a beginning of a comment marker
    ## add this char to no_comment_source
    ## if it is the beginning, skip to the end of comment marker
    ## Repeat until no more char left in source_text

    ## Make sure you output whitespaces in source to destination


    dest_file = open(destination, "w")
    dest_file.write(no_comment_source)
    dest_file.close()