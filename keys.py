from collections import defaultdict
from shodan.helpers import iterate_files


# Configuration
TOP_RESULTS = 20


def main(args):
    # Basic input validation
    if len(args) <= 1:
        print('Usage: {} <data.json.gz> [list of data files...]'.args[0])
        return 1

    # Keep track of the frequency of each key
    tracker = defaultdict(int)

    # Loop over all the banners in the provided Shodan data files
    for banner in iterate_files(args[1:]):
        # Find "Keys" section of the banner text
        start = banner['data'].find('# Keys\r\n')
        if start < 0:
            continue
        start += len('# Keys\r\n')

        # Find the start of the next section
        end = banner['data'].find('\r\n\r\n', start)

        # Grab the text in between
        keys = banner['data'][start:end]

        # Parse the keys line by line
        keys = keys.split('\r\n')
        for key in keys:
            # Skip comments or empty keys
            if key.startswith('#') or key.strip() == '':
                continue

            # Increment the frequency counter for this key
            tracker[key] += 1

    # Lets print the results
    print('Top {} Redis Keys\n'.format(TOP_RESULTS))

    # Turn the defaultdict into a list of items (iteritems())
    # Sort it in reverse (i.e. most common value will be at the start of the list)
    # And sort it based on the value instead of the key name (lambda ...)
    sorted_items = sorted(tracker.iteritems(), reverse=True, key=lambda (k, v): v)

    # Use the enumerate() method to give us a counter and start the counter at 1
    for i, item in enumerate(sorted_items, start=1):
        # The key names are padded to a length of 30 characters so the output aligns better
        print('#{}\t{:30s}\t{}'.format(i, item[0], item[1]))

        # Stop looping over results once we've printed the top X values
        if i >= TOP_RESULTS:
            break

if __name__ == '__main__':
    from sys import argv, exit
    exit(main(argv))