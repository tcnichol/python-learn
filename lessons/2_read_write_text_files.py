import os

def main():
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
    main()