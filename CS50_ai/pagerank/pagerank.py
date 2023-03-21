import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 100000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # Creating the dictionary
    trans_dict = {}

    # If page has no links, giving all the pages equal probability.
    if len(corpus[page]) == 0:
        trans_dict = {key: (1 / len(corpus)) for key in corpus}

    else:
        # Storing damped score
        damped_score = damping_factor / len(corpus[page])
        for key in corpus:
            # Assigning every page a base value
            trans_dict[key] = (1 - damping_factor) / len(corpus)
            if key in corpus[page]:
                # Adding the damped_score to each page found in page
                trans_dict[key] += damped_score

    return trans_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Making a new dictionary with the keys from corpus
    rank_dict = {key: 0 for key in corpus}

    # Getting random page to start
    page = random.choice(list(corpus.keys()))

    # Sample loop
    for i in range(n):
        # Getting dictionary with transition model
        trans_dict = transition_model(corpus, page, damping_factor)

        # Getting a random page using the transition model
        page = random_page(trans_dict)

        # Adding a counter for each page selected
        rank_dict[page] += 1

    # Normalizing values
    rank_dict = {key: value / n for key, value in rank_dict.items()}
    return rank_dict


def random_page(trans_dict):
    """
    Takes the dictionary from transition model and uses it to return
    a weighted random page.
    """
    keys = list(trans_dict.keys())
    values = list(trans_dict.values())
    return random.choices(keys, weights=values)[0]


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    # Getting variable and dictionary ready
    N = len(corpus)
    rank_dict = {key: 1 / N for key in corpus}

    # Define convergence threshold
    threshold = 0.001

    # While loop until values converge
    while True:
        # Counter to check convergence for each item in corpus
        count = 0
        
        # Create a new dictionary to store the updated pagerank values
        new_rank_dict = {}

        for key in corpus:
            # First part of the equation
            new_rank = (1 - damping_factor) / N

            # Initializing sigma
            sigma = 0

            # For each page in the corpus, if the page links to another
            for page in corpus:
                if key in corpus[page]:
                    
                    # get number of links
                    link_number = len(corpus[page])

                    # adding the pagerank from linking pages divided by link number
                    # and applying the damping factor
                    sigma += damping_factor * rank_dict[page] / link_number

            # closing up the equation
            new_rank += sigma

            # update the page rank for current page
            new_rank_dict[key] = new_rank

            # checking for convergence
            if abs(rank_dict[key] - new_rank) < threshold:
                count += 1

        # if we have N convergences, time to break
        if count == N:
            break
        
        # update the rank_dict to new_rank_dict
        rank_dict = new_rank_dict

    # normalize pageranks to ensure they sum to 1
    total = sum(rank_dict.values())
    rank_dict = {key: value / total for key, value in rank_dict.items()}

    return rank_dict


if __name__ == "__main__":
    main()
