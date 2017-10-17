import sys
import os
import re
import pprint

def process_file(name, f):
    """ 
    Takes in a filename along with the file object and scans its contents against regex patterns. 
    Returns a list of (filename, type, value) tuples where type is either an 'e' or a 'p'
    for e-mail or phone, and value is the formatted phone number or e-mail.

    The canonical formats are:
        (name, 'p', '###-###-#####')
        (name, 'e', 'someone@something')

    If the numbers you submit are formatted differently they will not match the gold answers.

    XXX: DO NOT change the inputs and outputs of process_file
    NOTE: Debug info should be printed to stderr
    `sys.stderr.write('[process_file]\tprocessing file: %s\n' % (path))`

    TODO: Change only the internals of this function. The assigment is modify and add lines.
    """
    
    #dummy_pattern = '(\w+)@(\w+).edu' # TODO: Create your own patterns for email & phone
    #test_patternemail_1 ='([\w%]+\.[\w%]+|[\w%]+|[\w%]+)[\s]?@[\s]?(([\w%]+\.[\w%]+\.[\w%]+)|([\w%]+\.[\w%]+))'  # This will match the characters at the end (for the domain) sdf@sdf.com will match
    test_patternemail_1='([\w%]+\.[\w%]+|[\w%]+|[\w%]+)\s?@\s?([\w%]+\.[\w%]+\.[\w%]+|[\w%]+\.[\w%]+)'

    test_patternemail_2 ='(\w+)\s\w{2}\s(\w+)\s(?:dot)\s(\w+)\s(?:dot)\s(\w+)' # captures test name dot name at something
    test_patternemail_3 = '(\w+)\s(?:WHERE)\s([s]\w+)\s(?:DOM)\s(\w{3})' #engler where stanford DOM edu
    test_patternemail_4 = '([\w.]+)(?:\s\()(?:\w)+(?:\s)(?:\w)+(?:\s).(?:@)([\w.]+)' #ouster (followed by “@cs.stanford.edu”)
    test_patternemail_5 = '([\w]+)(?:\s)[at]+(?:\s)([cs]+)(?:\s)([standford]+)(?:\s)([edu]+)'#pal at cs stanford edu
    test_patternemail_6 ='(?:[mailto"=href\sa<]+):([\w]+)%(?:[%at20]+)([standford]+)(?:[20dot=%<)]+)([edu]+)'#<a href="mailto:vladlen%20at%20stanford%20dot%20edu">
    test_patternemail_7='(?:[\w]+);E-mail:\s([\w]+)\s[at]+\s([cs.standford.edu]+)'#&nbsp;&nbsp;&nbsp;E-mail: lam at cs.stanford.edu
    test_patternemail_8='([\w])-([\w])-([\w])-([\w])-@-([s])-([t])-([\w])-([\w])-([\w])-([\w])-([\w])-([\w])-.-([\w])-([\w])-([\w])' #d-l-w-h-@-s-t-a-n-f-o-r-d-.-e-d-u
    test_patternemail_9 ='([\w]+)&(?:[#x40;]+)([\w.]+)</em>'
    #([\w]+\.[\w]+|[\w]+|[\w]+ )@(( [\w]+\.[\w]+)|([\w]+\.[\w]+\.[\w]+)|([\w]+\.[\w]+))  - 90 correct
    test_patternphone_1 = '([\d]{3}|\([\d]{3}\))[-\. ]?([\d]{3})[-\. ]([\d]{4})[^\d]' # Will match asdf.adsf@asdf.asdf.com

    

    #pattern = test_pattern_1
    #print(pattern,'pattern')
    # A little bit of meta-programming (strings all the way down!)
    # sub_pattern = '[ae]'
    #emailpattern_twogroup = "|".join([test_patternemail_1 ,test_patternemail_4])

    # # Does our test still pass?
    # assert sorted(re.findall(pattern2, string)) != sorted(chink)
    # assert sorted(re.findall(pattern2, string)) == sorted(chunk)

    #total_patterns_two = [dummy_pattern,test_pattern_1,test_pattern_2,test_pattern_3,test_pattern_4]

    results = []
    for line in f:
        matches = re.findall(test_patternemail_1,line)
        matches_phone = re.findall(test_patternphone_1, line)
        matches_email_longform = re.findall(test_patternemail_2,line)
        matches_email_longform2 = re.findall(test_patternemail_3 ,line)
        matches_email_longform3 = re.findall(test_patternemail_4,line)
        matches_email_longform4 = re.findall(test_patternemail_5,line)
        matches_email_longform5 = re.findall(test_patternemail_6,line)
        matches_email_longform6 = re.findall(test_patternemail_7,line)
        matches_email_longform7=re.findall(test_patternemail_8,line)
        matches_email_longform8=re.findall(test_patternemail_9,line)
       
        #print(matches, ' matches)')
        for match in matches_email_longform8:
             print(match,'match --- longform 8')
             email= '{}@{}'.format(*match)
             results.append((name,'e',email))

        for match in matches_email_longform7:
             print(match,'match --- longform 7')
             email= '{}{}{}{}@{}{}{}{}{}{}{}{}.{}{}{}'.format(*match)
             results.append((name,'e',email))

        for match in matches_email_longform6:
             print(match,'match --- longform 6')
             email= '{}@{}'.format(*match)
             results.append((name,'e',email))

        for match in matches_email_longform5:
             print(match,'match --- longform 5')
             email= '{}@{}.{}'.format(*match)
             results.append((name,'e',email))


        for match in matches_email_longform4:
             print(match,'match --- longform 4')
             email= '{}@{}.{}.{}'.format(*match)
             results.append((name,'e',email))

        for match in matches_email_longform3:
             print(match,'match --- longform 3')
             email= '{}@{}'.format(*match)
             results.append((name,'e',email))

        for match in matches_email_longform2:
            print(match,'match ---2')
            email= '{}@{}.{}'.format(*match)
            results.append((name,'e',email))

        for match in matches_email_longform:
            print(match,'match ---')
            email= '{}@{}.{}.{}'.format(*match)
            results.append((name,'e',email))


        for match in matches:
            print(match,'email match ----- group two')
            # email_length = len(match)
            #if email_length==2:
            email= '{}@{}'.format(*match)
            results.append((name,'e',email))
            # elif email_length == 4:
            #     email = '{}@{}.{}.{}'.format(*match)
            #     results.append((name,'e',email))


     

        for match in matches_phone:
            print(match,'match  phone-------')
            if match[0][0]=="(":
                area_code = match[0][1:4]
            else:
                area_code = match[0]

            try:
                phone= '{}-{}-{}'.format(area_code,match[1],match[2])
                results.append((name,'p',phone))
            except:
                print('failed')


                # email= '{}@{}.{}.{}'.format(*match)
                # results.append((name,'e',email))
            
        
            # for count,character in enumerate(match):

            #     if character != '':
            #         print(character,'character')

                    
            #         match_length = len(match[count:])

            #         #email_1 = '{}@{}.edu'.format(*match)
            #         if match_length ==5:
            #             email_2 = '{}{}{}{}{}'.format(*match[count:])
            #             print(email_2,'email 2')
            #             results.append((name,'e',email_2))
            #             break
            #         elif match_length ==7:
            #             email_3='{}{}{}{}{}{}{}'.format(*match[count:])
            #             print(email_3,'email 3')
            #             results.append((name,'e',email_3))
            #             break


            #         else:

            #             email_5 ='{}{}{}{}{}'.format(*match)
            #             results.append((name,'e',email_5))
            #             break
                    #print(email_4,'email 4')
                # else:
                #     pass

        # TODO: Create a section for phone matches
        
    return results

def process_dir(data_path):
    "XXX: DO NOT MODIFY THIS FUNCTION"

    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r', encoding="latin-1")
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

def get_gold(gold_path):
    """XXX: DO NOT MODIFY THIS FUNCTION
    
    Given a path to a tsv file of gold e-mails and phone numbers
    this function returns a list of tuples of the canonical form:
    (filename, type, value)
    """
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

def score(guess_list, gold_list):
    """ XXX: DO NOT MODIFY THIS FUNCTION
    
    Given a list of guessed contacts and gold contacts, this function
    computes the intersection and set differences, to compute the true
    positives, false positives and false negatives.  Importantly, it
    converts all of the values to lower case before comparing
    """

    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))


def main(data_path, gold_path):
    """ XXX: DO NOT MODIFY THIS FUNCTION

    Takes in the string path to the data directory and the gold file
    """
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

if __name__ == '__main__':
    """ The commandline interface takes a directory name and gold file.
    $ python spam_lord.py data/dev/ data/devGOLD

    It then processes each file within that directory and extracts any
    matching e-mails or phone numbers and compares them to the gold file
    """
    if (len(sys.argv) != 3):
        print('usage:\tSpamLord.py <data_dir> <gold_file>')
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
