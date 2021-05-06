---
lang-ref: ch.08-3
title: Generative Models - Variational Autoencoders
lecturer: Alfredo Canziani
authors: Nandhitha Raghuram, Xinyi Zhao
date: 25 March 2021
---

### Summary (add to 08.md Practicum)

In this section, we introduced some other autoencoders including Denoising AE, Contractice AE and Variational AE. And compared the functionalities and advantages of  Variational AEs over Basic Autoencoders. We explored the objective function of VAE in detail, understanding how it enforced some structure in the latent space. 

### Recap: Autoencoder (AE)

// todo

### Denoising Autoencoder

// todo

### Contractive Autoencoder

A contractive autoencoder is an unsupervised deep learning technique that helps a neural network encode unlabeled training data. It makes this encoding less sensitive to small variations in its training dataset. This is accomplished by adding a regularizer, or penalty term, to whatever cost or objective function the algorithm is trying to minimize. The end result is to reduce the learned representation’s sensitivity towards the training input. 

<center>
<img src="{{site.baseurl}}/images/week08/08-3/contractiveAE.png" height="400px" /><br>
<b>Fig. 1</b>: Contactive autoencoder
</center>

As shown in *Fig. 1*, $C(y, \tilde y)$ penalises sensitivities to reconstructions along the manifold while $R(h)$ penalises how much the wiggling of $h$ comes from the wiggling of $y$. In this manner, you basically get to push up the energies only in the direction that are not used for the reconstruction.

### Variational Autoencoder (VAE)

**Intuition behind VAE and a comparison with classic autoencoders**

Next, we introduce Variational Autoencoders (or VAE), a type of generative models. But why do we even care about generative models? To answer the question, discriminative models learn to make predictions given some observations, but generative models aim to simulate the data generation process. One effect is that generative models can better understand the underlying causal relations which leads to better generalization.

Note that although VAE has "Autoencoders" (AE) in its name (because of structural or architectural similarity to auto-encoders), the formulations between VAEs and AEs are very different. See *Fig. 2* below.

<center>
<img src="{{site.baseurl}}/images/week08/08-3/VAE.png" height="400px" /><br>
<b>Fig. 2</b>: VAE vs. Basic AE
</center>

**What's the difference between variational autencoder (VAE) and basic autoencoder (AE)?**

For VAE:
- First, the encoder stage: we pass the input $\boldsymbol{x}$ to the encoder. Instead of generating a hidden representation $\boldsymbol{h}$ (the code) in AE, the code in VAE comprises two things: $\mathbb{U}(\boldsymbol{z})$ and $\mathbb{V}(\boldsymbol{z})$ where $\boldsymbol{z}$ is the latent random variable following a Gaussian distribution with mean $\mathbb{U}(\boldsymbol{z})$ and variance $\mathbb{V}(\boldsymbol{z})$. Note that people use Gaussian distributions as the encoded distribution in practice, but other distributions can be used as well.
    - The encoder will be a function from $\mathcal{Y}$ to $\mathbb{R}^{2d}$: $\boldsymbol{y} \mapsto \boldsymbol{h}$ (here we use $\boldsymbol{h}$ to represent the concatenation of $\mathbb{U}(\boldsymbol{z})$ and $\mathbb{V}(\boldsymbol{z})$).
- Next, we will sample $\boldsymbol{z}$ from the above distribution parametrized by the encoder; specifically, $\mathbb{U}(\boldsymbol{z})$ and $\mathbb{V}(\boldsymbol{z})$ are passed into a **sampler** to generate the latent variable $\boldsymbol{z}$.
- Finally, $\boldsymbol{z}$ is passed into the decoder to generate $\tilde{\boldsymbol{y}}$.
    - The decoder will be a function from $\mathcal{Z}$ to $\mathbb{R}^{n}$: $\boldsymbol{z} \mapsto \boldsymbol{\tilde{y}}$.

In fact, for basic autoencoder, we can think of $\boldsymbol{h}$ as just the vector $\mathbb{U}(\boldsymbol{z})$ in the VAE formulation. In short, the main difference between VAEs and AEs is that VAEs have a good latent space that enables generative process.


**The VAE objective (loss) function**

<center>
<img src="{{site.baseurl}}/images/week08/08-3/VAEloss.png" /><br>
<b>Fig. 3</b>: Mapping from input space to latent space
</center>

First, we encode from input space (left) to latent space (right), through encoder and noise. Next, we decode from latent space (right) to output space (left). To go from the latent to input space (the generative process) we will need to either learn the distribution (of the latent code) or enforce some structure. In our case, VAE enforces some structure to the latent space.

As usual, to train VAE, we minimize a loss function. The loss function is therefore composed of a reconstruction term as well as a regularization term.
- The reconstruction term is on the final layer (left side of the figure). This corresponds to $C(\boldsymbol{y}, \tilde{\boldsymbol{y}})$ in the figure.
- The regularization term is on the latent layer, to enforce some specific Gaussian structure on the latent space (right side of the figure). We do so by using a penalty term $D_{KL}(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{v}) || \mathcal{N}(\boldsymbol{0}, \boldsymbol{1}))$. Without this term, VAE will act like a basic autoencoder, which may lead to overfitting, and we won't have the generative properties that we desire.

**Discussion on sampling $\boldsymbol{z}$ (reparameterisation trick)**

How do we sample from the distribution returned by the encoder in VAE? According to above, we sample from the Gaussian distribution, in order to obtain $\boldsymbol{z}$. However, this is problematic, because when we do gradient descent to train the VAE model, we don't know how to do backpropagation through the sampling module.

Instead, we use the *reparameterization trick* to "sample" $\boldsymbol{z}$. We use $\boldsymbol{z} = \mathbb{U}(\boldsymbol{z}) + \boldsymbol{\epsilon} \odot \sqrt{\mathbb{V}(\boldsymbol{z})}$ where $\epsilon\sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{I}_d)$. In this case, backpropagation in training is possible. Specifically, the gradients will go through the (element-wise) multiplication and addition in the above equation.

**Visualizing Latent Variable Estimates and Reconstruction Loss**

As stated above, the Free Energy for the VAE contains two parts: a reconstruction term and a regularization term.  We can write this as

$$
\tilde{F}(\boldsymbol{y}) = C(\boldsymbol{y}, \tilde{\boldsymbol{y}}) + \beta D_{\text{KL}}(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{v}) || \mathcal{N}(\boldsymbol{0}, \boldsymbol{1}))
$$

To visualize the purpose of each term in the free energy, we can think of each estimated $\boldsymbol{z}$ value as a circle in $2d$ space, where the centre of the circle is $\mathbb{U}(\boldsymbol{z})$ and the surrounding area are the possible values of $\boldsymbol{z}$ determined by $\mathbb{V}(\boldsymbol{z}).$

<center>
<img src="{{site.baseurl}}/images/week08/08-3/bubbles_z.png" height="350px" /><br>
<b>Fig. 4</b>: Visualizing vector z as bubbles in the latent space
</center>

*In Fig. 4 above, each bubble represents an estimated region of $\boldsymbol{z}$, and the arrows represent how the reconstruction term pushes each estimated value away from the others, which is explained more below.*

If there is overlap between any two estimates of $z$, (visually, if two bubbles overlap) this creates ambiguity for reconstruction because the points in the overlap can be mapped to both original inputs. Therefore the reconstruction loss will push the points away from one another.

However, if we use just the reconstruction loss, the estimates will continue to be pushed away from each other and the system could blow up.  This is where the penalty term comes in.

**The penalty term**

The second term is the relative entropy (a measure of the distance between two distributions) between $\boldsymbol{z}$ which comes from a Gaussian with mean $\mathbb{U}(\boldsymbol{z})$ referring to $\mu$, variance $\mathbb{V}(\boldsymbol{z})$ referring to $v$ and the standard normal distribution. If we expand this second term in the VAE loss function we get:

$$
\beta D_{\text{KL}}(\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{v}) || \mathcal{N}(\boldsymbol{0}, \boldsymbol{1})) = \frac{\beta}{2} \sum\limits_{i=1}^d(v_i - \log{(v_i)} - 1 + \mu_i^2)
$$

Where each expression in the summation has four terms. Below we write out and graph the first three terms in *Fig. 5*.

$$
\mathbb{V} = v_i - \log{(v_i)} - 1
$$

<center>
<img src="{{site.baseurl}}/images/week08/08-3/relative_entropy.png" /><br>
<b>Fig. 5</b>: Plot showing how relative entropy forces the bubbles to have variance = 1
</center>

So we can see that this expression is minimized when $z_i$ has variance 1.  Therefore our penalty loss will keep the variance of our estimated latent variables at around 1.  Visually, this means our "bubbles" from above will have a radius of around 1.

The last term, $\mu_i^2$, minimizes the distance between the $z_i$ and therefore prevents the "exploding" encouraged by the reconstruction term.

<center>
<img src="{{site.baseurl}}/images/week08/08-3/bubble-of-bubble.png" height="400px"/><br>
<b>Fig. 6</b>: The "bubble-of-bubble" interpretation of VAE
</center>

*Fig. 6 above shows how VAE loss pushed the estimated latent variables as close together as possible without any overlap while keeping the estimated variance of each point around one.*

**Note:** The $\beta$ in the VAE loss function is a hyperparameter that dictates how to weight the reconstruction and penalty terms.

