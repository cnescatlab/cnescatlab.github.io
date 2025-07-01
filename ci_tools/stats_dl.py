import requests
from tabulate import tabulate

REPO = "cnescatlab/sonar-cnes-report"


if __name__ == "__main__":
    releases = requests.get(url = "https://api.github.com/repos/%s/releases"%REPO)
    releases_list = releases.json()

    dl_count = 0
    downloads = []
    
    for rel in releases_list:
        assets = rel["assets"]
        for asset in assets:
            if asset['name'][-3:] == "jar":
                downloads.append(
                    [
                        "[%s](%s)"%(rel["tag_name"], asset["url"]), 
                        asset["name"], 
                        asset["download_count"]
                    ]
                )
                dl_count += asset["download_count"]


    print(tabulate(downloads, ["Tag", "File", "Downloads"], tablefmt="github"))
    print("TOTAL: %d" % dl_count)