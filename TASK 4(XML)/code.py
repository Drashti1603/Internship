import xml.etree.ElementTree as ET
import csv
import html

def process_testcase(testcase, csv_writer, parent_test_name=''):
    test_name = testcase.get('name')
    status = 'unknown'
    execution_time = testcase.get('time', '') if 'time' in testcase.attrib else ''
    system_out_element = testcase.find('./system-out')
    failure_element = testcase.find('./failure')

    if system_out_element is not None:
        system_out = system_out_element.text.strip()
    else:
        system_out = testcase.text.strip() if testcase.text else ''

    # Count the occurrences of "passed," "failed," and "skipped" in the system out
    passed_count = system_out.lower().count('passed')
    failed_count = system_out.lower().count('failed')
    skipped_count = system_out.lower().count('skipped')

    # Determine the overall status based on the counts
    if failed_count > 0 or (failure_element is not None and 'IndexOutOfBoundsException' in failure_element.get('message', '')):
        status = 'failed'
    elif skipped_count > 0:
        status = 'skipped'
    elif passed_count > 0:
        status = 'passed'

    # Extract only the content within the <failure> element's message attribute
    failure_message = failure_element.get('message', '') if failure_element is not None else ''

    # Decode HTML entities in the failure message
    failure_message = html.unescape(failure_message)

    # Extract CDATA content if present
    cdata_element = testcase.find('.//system-out')  # Use the correct path to find CDATA
    cdata_content = cdata_element.text.strip() if cdata_element is not None else ''

    # Count the occurrences of "passed," "failed," and "skipped" in CDATA content
    cdata_passed_count = cdata_content.lower().count('passed')
    cdata_failed_count = cdata_content.lower().count('failed')
    cdata_skipped_count = cdata_content.lower().count('skipped')

    row_data = {
        'Test Name': test_name,
        'Status': status,
        'Execution Time': execution_time,
        'Sys_Out': system_out,
        'Passed Count': passed_count + cdata_passed_count,
        'Failed Count': failed_count + cdata_failed_count,
        'Skipped Count': skipped_count + cdata_skipped_count,
        'Exception Message': failure_message,
    }

    # Include the parent test name if available
    if parent_test_name:
        row_data['Sub-Test Name'] = test_name
        row_data['Test Name'] = parent_test_name

    csv_writer.writerow(row_data)

    subtests = testcase.findall('.//testcase')
    for subtest in subtests:
        process_testcase(subtest, csv_writer, parent_test_name=test_name)

xml_file_path = '/home/drashti/Documents/Python/TASK 4(XML)/cucumber.xml'
csv_filename = '/home/drashti/Documents/Python/TASK 4(XML)/final_.csv'

tree = ET.parse(xml_file_path)
root = tree.getroot()

with open(csv_filename, mode='w', newline='') as csv_file:
    field_names = ['Test Name', 'Sub-Test Name', 'Status', 'Execution Time', 'Sys_Out', 'Passed Count', 'Failed Count', 'Skipped Count', 'Exception Message']
    csv_writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=';')
    csv_writer.writeheader()  # Write header row

    testsuite_name = root.get('name', '')  # Extract testsuite name if available
    for testcase in root.findall('.//testcase'):
        process_testcase(testcase, csv_writer, parent_test_name=testsuite_name)

print(f'Data has been written to {csv_filename}')
