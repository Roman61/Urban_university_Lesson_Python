import xml.etree.ElementTree as ET
import os


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")
    else:
        print(f"File {file_path} does not exist.")


def xml_to_fsm(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    states = []
    transitions = []

    for node in root.findall('.//node'):
        states.append({'name': node.attrib['TEXT']})

    for node in root.findall('.//node'):
        for arrowlink in node.findall('arrowlink'):
            trigger = arrowlink.get('MIDDLE_LABEL')
            source = node.attrib['TEXT']
            dest_id = arrowlink.get('DESTINATION')
            dest_node = None
            for elem in root.findall('.//node'):
                if elem.get('ID') == dest_id:
                    dest_node = elem
                    break
            if dest_node is not None:
                dest = dest_node.attrib['TEXT']
                transitions.append({'trigger': trigger, 'source': source, 'dest': dest})

    fsm_dict = {
        'states': states,
        'transitions': transitions
    }

    return fsm_dict


xml_file = 'screen.mm'  # Замените на имя вашего файла XML
delete_file("state_map.py")
fsm_dict = xml_to_fsm(xml_file)

with open('state_map.py', 'w', encoding='utf-8') as f:
    f.write('states = [\n')
    for state in fsm_dict['states']:
        f.write(f"    {{'name': '{state['name']}'}},\n")
    f.write(']\n\n')

    f.write('transitions = [\n')
    for transition in fsm_dict['transitions']:
        f.write(
            f"    {{'trigger': '{transition['trigger']}', 'source': '{transition['source']}', 'dest': '{transition['dest']}'}},\n")
    f.write(']')

print("State map saved to state_map.py")
