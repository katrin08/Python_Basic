import zipfile
import collections


def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for i_sym in i_line:
            if i_sym.isalpha():
                if i_sym not in result:
                    result[i_sym] = 0
                result[i_sym] += 1
    text_file.close()
    return result


def print_stats(stats):
    print('+{:-^19}+'.format('+'))
    print('|{:-^9}|{:-^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    for sym, count in stats.items():
        print('|{:-^9}|{:-^9}|'.format(sym, count))
    print('+{:-^19}+'.format('+'))


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
sorted_stats = collections.OrderedDict(sorted(stats.items(), key=lambda val:  val[1]))
print_stats(sorted_stats)
