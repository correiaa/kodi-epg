import io
class Merge:
    def merge(self, file_name_1, file_name_2):
        with open("output", 'wb') as outfile: # Python hack to stop automatic line ending processing under windows
            with open(file_name_1) as infile1:
                for line1 in infile1:
                    outfile.write(line1)
            with open(file_name_2) as infile2:
                for line2 in infile2:
                    outfile.write(line2)
