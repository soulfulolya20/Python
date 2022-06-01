import re


def main(example):
    exr = r'(var\s*\{([^}]*)\}\s*=>\s*\@\'([a-zA-Z0-9_]*)\'.)'
    d = {}
    matches = re.findall(exr, example)
    for match in matches:
        s = []
        for j in match[1].split(';'):
            j = int(j.strip())
            s.append(j)
        key = match[2]
        d[key] = s
    return d


print(main(
    "do var{ -5130 ; -5902 ; 4306; 3943 } => @'arzais_119'. done; do var {-4197; -4359; 6628 ; -8829 } => @'xexe'. done;"))
print(main(
    "do var { 8025 ; -9508 }=> @'dima_95'. done; do var { 2388 ; 8958;4434 ;-3053 }=> @'gebe_647'. done; do var { 2165 ; -5534 } =>@'endi_739'. done;"))

print(main(
    "do var {997 ; 6942; 2772; 9029 } => @'biriso'. done; do var { 9534 ;\n-8384 ; -1858 } =>@'inte'. done; do var{ -8647 ; 222} => @'rima'.\ndone;do var{ -7943;4546 ; 6896 } =>@'dianed'. done;"))