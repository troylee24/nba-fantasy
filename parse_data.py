import xml.etree.ElementTree as et
import json

def xml_to_json(file_rank, file_proj):
    # rankings
    xtree = et.parse(file_rank)
    xroot = xtree.getroot()
    ranks = {}
    for player in xroot:
        id = rank = None
        for stat in player:
            if stat.tag == 'playerId':
                id = stat.text
            elif stat.tag == 'rankOverall':
                rank = stat.text
        ranks[id] = rank

    # projections
    xtree = et.parse(file_proj)
    xroot = xtree.getroot()
    rows = []
    for player in xroot:
        stats = {}
        for stat in player:
            if stat.tag == 'playerId':
                if stat.text in ranks:
                    stats['rank'] = ranks[stat.text]
                else:
                    break
            else:
                stats[stat.tag] = stat.text
        
        if 'rank' in stats:
            rows.append(stats)

    print(rows)

    with open('data/stats.json', 'w') as f:
        json.dump(rows, f)

def get_stats():
    with open('data/stats.json', 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    xml_to_json('data/rankings.xml', 'data/projections.xml')