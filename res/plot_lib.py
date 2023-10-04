import matplotlib as mpl
import numpy as np
import torch
from IPython.display import clear_output
from matplotlib import pyplot as plt


def set_default(figsize=(10, 10), dpi=100):
    plt.style.use(['dark_background', 'bmh'])
    plt.rc('axes', facecolor='k')
    plt.rc('figure', facecolor='k')
    plt.rc('figure', figsize=figsize, dpi=dpi)


def plot_data(X, y, d=0, auto=False, zoom=1, title='Training data (x, y)'):
    X = X.cpu()
    y = y.cpu()
    s = plt.scatter(X.numpy()[:, 0], X.numpy()[:, 1], c=y, s=20, cmap=plt.cm.Spectral)
    plt.axis('square')
    plt.axis(np.array((-1.1, 1.1, -1.1, 1.1)) * zoom)
    if auto is True: plt.axis('equal')
    plt.axis('off')

    _m, _c = 0, '.35'
    plt.axvline(0, ymin=_m, color=_c, lw=1)
    plt.axhline(0, xmin=_m, color=_c, lw=1)
    plt.title(title)
    return s


def plot_model(X, y, model):
    model.cpu()
    mesh = torch.arange(-1.1, 1.11, 0.01)
    xx, yy = torch.meshgrid(mesh, mesh, indexing='xy')
    with torch.no_grad():
        data = torch.stack((xx.reshape(-1), yy.reshape(-1)), dim=1)
        Z = model(data)
    Z = Z.argmax(dim=1).reshape(xx.shape)
    plt.contourf(xx.numpy(), yy.numpy(), Z, cmap=plt.cm.Spectral, alpha=0.3)
    plot_data(X, y)
    plt.title('Model decision boundaries')


def plot_embeddings(X, y, model, zoom=10):
    # Use forward hook to get internal embeddings of the second last layer
    layer_outputs = {}

    def get_layer_outputs(name):
        def hook(model, input, output):
            layer_outputs[name] = output

        return hook

    layer = model[-2]

    if layer.__class__ == torch.nn.modules.linear.Linear and layer.out_features == 2:
        layer.register_forward_hook(get_layer_outputs("low_dim_embeddings"))
        with torch.no_grad():
            model(X)  # pass data through model to populate layer_outputs
        plot_data(
            layer_outputs["low_dim_embeddings"],
            y,
            zoom=zoom,
            title="Low dim embeddings",
        )
        last_layer = model[-1]
        mesh = torch.arange(-1.1, 1.1, 0.01) * zoom
        xx, yy = torch.meshgrid(mesh, mesh, indexing="ij")
        with torch.no_grad():
            data = torch.stack((xx.reshape(-1), yy.reshape(-1)), dim=1)
            Z = last_layer(data)
        Z = Z.argmax(dim=1).reshape(xx.shape)
        plt.contourf(xx.numpy(), yy.numpy(), Z, cmap=plt.cm.Spectral, alpha=0.3, levels=y.max().item())
    else:
        print(
            "Cannot plot: second-last layer is not a linear layer"
            f" with output in R^2 (it is {layer})"
        )


def acc(l, y):
    score, predicted = torch.max(l, 1)
    return (y == predicted).sum().float() / len(y)


def overwrite(string):
    print(string)
    clear_output(wait=True)


def plot_2d_energy_levels(X, y, energy, v=None, l=None):
    xx, yy, F, k, K = energy
    if not v: vmin = vmax = None
    else: vmin, vmax = v
    if not l: levels = None
    else: levels = torch.arange(l[0], l[1], l[2])
    plt.figure(figsize=(12, 10))
    plt.pcolormesh(xx.numpy(), yy.numpy(), F, vmin=vmin, vmax=vmax)
    plt.colorbar()
    cnt = plt.contour(xx.numpy(), yy.numpy(), F, colors='w', linewidths=1, levels=levels)
    plt.clabel(cnt, inline=True, fontsize=10, colors='w')
    s = plot_data(X, y)
    plt.legend(*s.legend_elements(), title='Classes', loc='lower right')
    plt.axvline(color='0.55', lw=1)
    plt.axhline(color='0.55', lw=1)
    plt.axis([-1.5, 1.5, -1.5, 1.5])
    ȳ = torch.zeros(K).int(); ȳ[k] = 1
    plt.title(f'Free energy F(x, y = {ȳ.tolist()})')


def plot_3d_energy_levels(X, y, energy, v=None, l=None, cbl=None):
    xx, yy, F, k, K = energy
    if not v: vmin = vmax = None
    else: vmin, vmax = v
    if not l: levels = None
    else: levels = torch.arange(l[0], l[1], l[2])
    fig = plt.figure(figsize=(9.5, 6), facecolor='k')
    ax = fig.add_subplot(projection='3d')
    cnt = ax.contour(xx.numpy(), yy.numpy(), F, levels=levels, vmin=vmin, vmax=vmax)
    ax.scatter(X[:,0], X[:,1], zs=0, c=y, cmap=plt.cm.Spectral)
    ax.xaxis.set_pane_color(color=(0,0,0))
    ax.yaxis.set_pane_color(color=(0,0,0))
    ax.zaxis.set_pane_color(color=(0,0,0))

    vmin, vmax = cnt.get_clim()
    ax.set_zlim3d(vmin, vmax)
    norm = mpl.colors.Normalize(vmin=vmin, vmax=vmax)
    if not cbl: cbl = l
    else: cbl = torch.arange(cbl[0], cbl[1], cbl[2])
    sm = plt.cm.ScalarMappable(norm=norm, cmap=cnt.cmap)
    sm.set_array([])
    fig.colorbar(sm, ticks=cbl, ax=ax)
    ȳ = torch.zeros(K).int(); ȳ[k] = 1
    plt.title(f'Free energy F(x, y = {ȳ.tolist()})')
    plt.tight_layout()
    return fig, ax
