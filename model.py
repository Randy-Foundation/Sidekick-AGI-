# Refactored model.py without TensorFlow
import numpy as np

def default_hparams():
    return {
        "n_vocab": 0,
        "n_ctx": 1024,
        "n_embd": 768,
        "n_head": 12,
        "n_layer": 12,
    }

def shape_list(x):
    """Return shape of a NumPy array."""
    return list(x.shape)

def softmax(x, axis=-1):
    """Numerically stable softmax using NumPy."""
    x = x - np.max(x, axis=axis, keepdims=True)
    ex = np.exp(x)
    return ex / np.sum(ex, axis=axis, keepdims=True)

def gelu(x):
    """Gaussian Error Linear Unit (GELU) approximation."""
    return 0.5 * x * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

def norm(x, axis=-1, epsilon=1e-5):
    """Normalize to mean = 0, std = 1, then do a diagonal affine transform."""
    u = np.mean(x, axis=axis, keepdims=True)
    s = np.mean(np.square(x - u), axis=axis, keepdims=True)
    x = (x - u) / np.sqrt(s + epsilon)
    return x

def split_states(x, n):
    """Reshape the last dimension of x into [n, x.shape[-1]/n]."""
    *start, m = shape_list(x)
    return x.reshape(start + [n, m // n])

def merge_states(x):
    """Smash the last two dimensions of x into a single dimension."""
    *start, a, b = shape_list(x)
    return x.reshape(start + [a * b])

def conv1d(x, w, b):
    """1D convolution implemented as a matrix multiplication."""
    return np.dot(x, w) + b

def attention_mask(nd, ns):
    """Lower triangular attention mask."""
    i = np.arange(nd)[:, None]
    j = np.arange(ns)
    return (i >= j - ns + nd).astype(np.float32)

def attn(x, w_q, w_k, w_v, w_proj, n_state, past=None):
    """Self-attention mechanism."""
    assert x.ndim == 3  # [batch, sequence, features]
    
    def split_heads(x, n_head):
        return np.transpose(split_states(x, n_head), [0, 2, 1, 3])

    def merge_heads(x):
        return merge_states(np.transpose(x, [0, 2, 1, 3]))

    q, k, v = split_heads(np.dot(x, w_q), 12), split_heads(np.dot(x, w_k), 12), split_heads(np.dot(x, w_v), 12)
    
    if past is not None:
        pk, pv = past
        k = np.concatenate([pk, k], axis=-2)
        v = np.concatenate([pv, v], axis=-2)
    
    w = np.matmul(q, np.transpose(k, [0, 1, 3, 2])) / np.sqrt(v.shape[-1])
    w = softmax(w)
    a = np.matmul(w, v)
    a = merge_heads(a)
    
    return np.dot(a, w_proj), (k, v)

def mlp(x, w_fc, b_fc, w_proj, b_proj):
    """Feedforward network."""
    h = gelu(np.dot(x, w_fc) + b_fc)
    return np.dot(h, w_proj) + b_proj

def block(x, w_q, w_k, w_v, w_proj, w_fc, b_fc, w_proj_fc, b_proj_fc, past=None):
    """Transformer block."""
    a, present = attn(norm(x), w_q, w_k, w_v, w_proj, x.shape[-1], past)
    x = x + a
    x = x + mlp(norm(x), w_fc, b_fc, w_proj_fc, b_proj_fc)
    return x, present

def model(hparams, X, w_q, w_k, w_v, w_proj, w_fc, b_fc, w_proj_fc, b_proj_fc, past=None):
    """Main Transformer model."""
    batch, sequence = X.shape

    presents = []
    pasts = past if past is not None else [None] * hparams["n_layer"]
    
    for layer in range(hparams["n_layer"]):
        X, present = block(X, w_q, w_k, w_v, w_proj, w_fc, b_fc, w_proj_fc, b_proj_fc, pasts[layer])
        presents.append(present)

    return {"logits": X, "present": presents}