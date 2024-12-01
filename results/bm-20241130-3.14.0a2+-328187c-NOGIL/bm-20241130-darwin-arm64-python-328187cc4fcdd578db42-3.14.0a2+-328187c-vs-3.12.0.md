# Results vs. 3.12.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: darwin-arm64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.170x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 221 ms: 1.30x slower                                                   |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 459 ms: 1.46x faster                                                   |
| async_tree_io              | 668 ms                                                 | 481 ms: 1.39x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                                   |
| async_tree_none            | 266 ms                                                 | 216 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 450 ms: 1.18x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 280 ms: 1.00x faster                                                   |
| nbody          | 68.8 ms                                                | 94.7 ms: 1.38x slower                                                  |
| float          | 55.8 ms                                                | 86.5 ms: 1.55x slower                                                  |
| Geometric mean | (ref)                                                  | 1.29x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.07 ms: 1.27x faster                                                  |
| regex_dna      | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| regex_v8       | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                  |
| regex_compile  | 77.9 ms                                                | 97.1 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.0 ms                                                | 69.0 ms: 1.07x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| json_loads           | 17.2 us                                                | 17.6 us: 1.02x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 60.3 ms: 1.08x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 48.1 ms: 1.21x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.75 sec: 1.26x slower                                                 |
| json_dumps           | 6.22 ms                                                | 8.39 ms: 1.35x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 230 us: 1.53x slower                                                   |
| pickle_pure_python   | 200 us                                                 | 312 us: 1.56x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 17.8 ms: 1.90x slower                                                  |
| python_startup         | 11.4 ms                                                | 22.8 ms: 2.00x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.95x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 30.6 ms: 1.37x slower                                                  |
| mako            | 7.71 ms                                                | 12.6 ms: 1.63x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.49x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 459 ms: 1.46x faster                                                   |
| async_tree_io              | 668 ms                                                 | 481 ms: 1.39x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 246 ms: 1.31x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.07 ms: 1.27x faster                                                  |
| async_tree_none            | 266 ms                                                 | 216 ms: 1.23x faster                                                   |
| deepcopy                   | 235 us                                                 | 196 us: 1.20x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 450 ms: 1.18x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 266 ms: 1.17x faster                                                   |
| regex_dna                  | 154 ms                                                 | 136 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.45 us: 1.09x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 69.0 ms: 1.07x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 99.7 ms: 1.07x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 26.2 us: 1.06x faster                                                  |
| generators                 | 31.1 ms                                                | 30.0 ms: 1.04x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 2.01 us: 1.03x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                  |
| json                       | 3.09 ms                                                | 3.05 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_v8                   | 16.0 ms                                                | 16.0 ms: 1.00x slower                                                  |
| coroutines                 | 19.2 ms                                                | 19.3 ms: 1.00x slower                                                  |
| async_generators           | 304 ms                                                 | 309 ms: 1.02x slower                                                   |
| nqueens                    | 62.4 ms                                                | 63.8 ms: 1.02x slower                                                  |
| json_loads                 | 17.2 us                                                | 17.6 us: 1.02x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.04x slower                                                 |
| spectral_norm              | 76.4 ms                                                | 80.1 ms: 1.05x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.68 sec: 1.06x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 60.3 ms: 1.08x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.64 ms: 1.10x slower                                                  |
| meteor_contest             | 71.7 ms                                                | 83.5 ms: 1.16x slower                                                  |
| scimark_fft                | 195 ms                                                 | 228 ms: 1.17x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.74 ms: 1.19x slower                                                  |
| sqlglot_normalize          | 186 ms                                                 | 224 ms: 1.21x slower                                                   |
| xml_etree_process          | 39.7 ms                                                | 48.1 ms: 1.21x slower                                                  |
| pycparser                  | 677 ms                                                 | 830 ms: 1.23x slower                                                   |
| comprehensions             | 14.5 us                                                | 17.9 us: 1.23x slower                                                  |
| dulwich_log                | 29.8 ms                                                | 36.7 ms: 1.23x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 41.9 ms: 1.23x slower                                                  |
| regex_compile              | 77.9 ms                                                | 97.1 ms: 1.25x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 1.75 sec: 1.26x slower                                                 |
| fannkuch                   | 248 ms                                                 | 315 ms: 1.27x slower                                                   |
| sympy_integrate            | 11.4 ms                                                | 14.6 ms: 1.29x slower                                                  |
| 2to3                       | 169 ms                                                 | 221 ms: 1.30x slower                                                   |
| crypto_pyaes               | 51.9 ms                                                | 68.0 ms: 1.31x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 123 us: 1.32x slower                                                   |
| json_dumps                 | 6.22 ms                                                | 8.39 ms: 1.35x slower                                                  |
| sqlalchemy_declarative     | 62.3 ms                                                | 84.2 ms: 1.35x slower                                                  |
| telco                      | 3.68 ms                                                | 5.03 ms: 1.37x slower                                                  |
| sympy_str                  | 148 ms                                                 | 202 ms: 1.37x slower                                                   |
| django_template            | 22.3 ms                                                | 30.6 ms: 1.37x slower                                                  |
| nbody                      | 68.8 ms                                                | 94.7 ms: 1.38x slower                                                  |
| sqlalchemy_imperative      | 6.68 ms                                                | 9.20 ms: 1.38x slower                                                  |
| pyflate                    | 316 ms                                                 | 435 ms: 1.38x slower                                                   |
| coverage                   | 38.9 ms                                                | 53.8 ms: 1.38x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 698 ms: 1.40x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.42 sec: 1.41x slower                                                 |
| logging_simple             | 3.69 us                                                | 5.22 us: 1.42x slower                                                  |
| logging_format             | 3.98 us                                                | 5.67 us: 1.42x slower                                                  |
| hexiom                     | 4.54 ms                                                | 6.72 ms: 1.48x slower                                                  |
| raytrace                   | 212 ms                                                 | 316 ms: 1.49x slower                                                   |
| chaos                      | 42.5 ms                                                | 64.1 ms: 1.51x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 133 ms: 1.52x slower                                                   |
| unpickle_pure_python       | 151 us                                                 | 230 us: 1.53x slower                                                   |
| float                      | 55.8 ms                                                | 86.5 ms: 1.55x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 312 us: 1.56x slower                                                   |
| scimark_monte_carlo        | 45.0 ms                                                | 70.8 ms: 1.57x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 793 us: 1.57x slower                                                   |
| sympy_expand               | 241 ms                                                 | 379 ms: 1.57x slower                                                   |
| richards                   | 32.1 ms                                                | 50.8 ms: 1.58x slower                                                  |
| go                         | 102 ms                                                 | 161 ms: 1.58x slower                                                   |
| logging_silent             | 76.4 ns                                                | 122 ns: 1.60x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 125 ms: 1.61x slower                                                   |
| scimark_lu                 | 76.0 ms                                                | 122 ms: 1.61x slower                                                   |
| mako                       | 7.71 ms                                                | 12.6 ms: 1.63x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.15 ms: 1.64x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 74.1 ms: 1.65x slower                                                  |
| richards_super             | 36.0 ms                                                | 59.5 ms: 1.65x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.70 ms: 1.66x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.50 ms: 1.77x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.07 ms: 1.87x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 17.8 ms: 1.90x slower                                                  |
| python_startup             | 11.4 ms                                                | 22.8 ms: 2.00x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                           |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (20) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-darwin-arm64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.170x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.34x