from configparser import ConfigParser


# filename = 
# section
def config(filename:str='database.ini', section:str='postgresql'):
    '''

    - filename: file where db's host, user, password and database are defined
    - section: database used in the project
    '''
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section(in use in the project) default to postgres
    db={}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db