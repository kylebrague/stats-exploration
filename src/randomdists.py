import numpy as np
import matplotlib.axes as axes
import matplotlib.pyplot as plt


def plot_random_distributions(
    lower_bound,
    upper_bound,
    n_samples=10000,
    save_path="../plots/random_distributions.png",
):
    mu = (lower_bound + upper_bound) / 2
    # Generate random samples
    uniform_samples = np.random.uniform(lower_bound, upper_bound, n_samples)

    # For beta distribution, assume lower_bound and upper_bound are shape parameters alpha and beta
    # Ensure lower_bound and upper_bound are > 0 to be valid shape parameters
    alpha = 10
    beta = alpha * (1 - mu) / mu
    beta_samples = np.random.beta(alpha, beta, n_samples)
    # For binomial distribution, assume lower_bound = n (trials) and upper_bound = p (probability of success)
    # Ensure 0 < upper_bound <= 1 to be a valid probability
    binom_n = 100
    binomial_samples = (
        np.random.binomial(binom_n, mu, n_samples) / 100
    )  # Normalize to get probabilities
    # Create histograms
    fig, ax = plt.subplots(3, 1, figsize=(10, 12))
    bins = 100
    c_alpha = 0.75
    ax: list[axes.Axes] = ax
    for plot_axis in ax:
        plot_axis.set_xlabel("Value")
        plot_axis.set_ylabel("Frequency")
        plot_axis.set_xlim([0, 1])

    ax[0].hist(uniform_samples, bins=bins, alpha=c_alpha, color="blue")
    ax[0].set_title("Uniform Distribution")
    ax[1].hist(beta_samples, bins=bins, alpha=c_alpha, color="green")
    ax[1].set_title("Beta Distribution")
    ax[1].set_xlim([0, 1])
    ax[1].text(
        0.2,
        300,
        "Mean: "
        + str(np.mean(beta_samples))
        + "\nAlpha: "
        + str(alpha)
        + "\nBeta: "
        + str(beta),
    )
    ax[2].hist(binomial_samples, bins=bins, alpha=c_alpha, color="red")
    ax[2].set_title("Binomial Distribution (Normalized)")
    ax[2].text(0.2, 300, "Mean: " + str(mu))

    plt.tight_layout()
    plt.savefig(save_path)  # Save the figure to a file
    plt.close(fig)
