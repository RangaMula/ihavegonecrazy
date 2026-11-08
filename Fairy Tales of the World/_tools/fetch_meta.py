"""Fetch metadata.yaml for every GITenberg repo listed in repos.tsv (or given on argv)."""
import concurrent.futures as cf, os, sys, json, urllib.request, yaml

BASE = "https://raw.githubusercontent.com/GITenberg/{repo}/master/{path}"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "meta")
os.makedirs(OUT, exist_ok=True)


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor("!", lambda l, s, n: l.construct_scalar(n))


def get(url, timeout=30):
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read()


def fetch(repo):
    dst = os.path.join(OUT, repo + ".json")
    if os.path.exists(dst):
        return repo, "cached"
    try:
        y = yaml.load(get(BASE.format(repo=repo, path="metadata.yaml")), Loader=Loader)
        json.dump(y, open(dst, "w"), default=str)
        return repo, "ok"
    except Exception as e:  # noqa
        return repo, f"err {e}"


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "repos.tsv"
    repos = sorted({l.split("\t")[0].split("/")[-1].strip() for l in open(src) if l.strip()})
    with cf.ThreadPoolExecutor(16) as ex:
        res = list(ex.map(fetch, repos))
    print(sum(1 for _, s in res if s != "cached" and s != "ok"), "errors of", len(res))
