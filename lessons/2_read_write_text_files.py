import os
import datetime

def deleting_files():
    files_in_current_dir = os.listdir(os.getcwd())
    print('all the files in the current dir')
    print(files_in_current_dir)
    for f in files_in_current_dir:
        if f.endswith('.txt'):
            try:
                os.remove(os.path.join(os.getcwd(), f))
            except Exception as e:
                print('could not remove file')
                print(e)

def writing_file():
    right_now = datetime.datetime.now()
    print('right now it is', str(right_now))
    print('we will put this in a new text file')
    # this method makes a readable string that youc an format
    readable_now = right_now.strftime("%m_%d_%Y_%H:%M:%S")
    new_text_file_name = 'text_file_' + readable_now + '.txt'
    with open(new_text_file_name, 'w') as f:
        # note the inclusion of the new line character
        f.write('We are writing the current date and time\n')
        f.write(readable_now+'\n')
    print('done here')

def reading_file():
    current_location = os.getcwd()

    path_components = current_location.split('/')
    parent_directory = current_location.replace('/lessons','')
    material_directory = os.path.join(parent_directory, 'materials')
    all_materials = os.listdir(material_directory)

    file_for_this_lesson = None

    for each in all_materials:
        if 'generic' in each and each.endswith('.txt'):
            file_for_this_lesson = os.path.join(material_directory, each)

    if file_for_this_lesson:
        with open(file_for_this_lesson, 'r') as f:
            # with files it is often better to do readlines than just read, since read just returns one gig string
            lines = f.readlines()
            print('how many lines?', len(lines))
    for each_line in lines:
        # here we strip off the new line character at the end of each line
        # it ends up causing an extra blank line to be printed
        print(each_line.rstrip('\n'))
    print('done')

if __name__ == "__main__":
    writing_file()
    reading_file()
    # this next one deletes all the text files that the writing files part created
    deleting_files()
