from sampleData.employees import employees
from sampleData.discussions import discussions
from sources.utils import create_user, create_source

def run():
    new = {}
    for employee in employees:
        r = {}
        desc = employee['Role'] + ' '.join([ expertise for expertise in employee['Expertise']]) + ' '.join([ expertise for expertise in employee['Projects']])
        employee['desc'] = desc

    for employee in employees:
        id = create_user(employee['Name'], employee['desc'])
        employee['id'] = id

    for disc in discussions:
        replace = []
        for col in disc['collaborators']:
            for employee in employees:
                if col == employee['Name']:
                    replace.append(employee['id'])

        disc['collab'] = replace

        disc['message'] = '\n'.join(['\n'.join(['\n'.join([sender, text]) for sender, text in message.items()]) for message in disc['messages']])


    for disc in discussions:
        base = disc['collab'][0]
        disc['summary'] = '\n'.join([disc['title'], disc['message']])
        create_source(disc['summary'], base, collaborators=disc['collab'])


