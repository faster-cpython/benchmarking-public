# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.297x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.0 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 445 ms: 2.13x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 573 ms: 1.98x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.96x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 751 ms: 1.69x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| float          | 135 ms                                                                | 99.0 ms: 1.36x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 411 us: 1.29x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.74 sec: 1.22x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 83.6 ms: 1.19x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| django_template | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 29.2 ms: 1.21x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.9 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.20x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.09 ms: 2.18x faster                                                    |
| async_tree_none          | 950 ms                                                                | 445 ms: 2.13x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 573 ms: 1.98x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.96x faster                                                   |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                    |
| go                       | 264 ms                                                                | 142 ms: 1.86x faster                                                     |
| raytrace                 | 573 ms                                                                | 323 ms: 1.78x faster                                                     |
| richards_super           | 107 ms                                                                | 62.3 ms: 1.72x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 751 ms: 1.69x faster                                                     |
| chaos                    | 121 ms                                                                | 72.0 ms: 1.68x faster                                                    |
| scimark_lu               | 227 ms                                                                | 138 ms: 1.64x faster                                                     |
| pylint                   | 485 ms                                                                | 297 ms: 1.64x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.63x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.4 ms: 1.62x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.5 ms: 1.59x faster                                                    |
| logging_silent           | 222 ns                                                                | 143 ns: 1.56x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.84 ms: 1.54x faster                                                    |
| comprehensions           | 33.1 us                                                               | 21.8 us: 1.52x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.0 us: 1.50x faster                                                    |
| scimark_sor              | 246 ms                                                                | 165 ms: 1.49x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.34 ms: 1.49x faster                                                    |
| deepcopy                 | 511 us                                                                | 354 us: 1.44x faster                                                     |
| logging_simple           | 9.78 us                                                               | 6.99 us: 1.40x faster                                                    |
| nbody                    | 166 ms                                                                | 119 ms: 1.40x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 92.9 ms: 1.38x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.78 us: 1.36x faster                                                    |
| float                    | 135 ms                                                                | 99.0 ms: 1.36x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 65.0 ms: 1.33x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| pyflate                  | 795 ms                                                                | 601 ms: 1.32x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.6 ms: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 968 us: 1.30x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 411 us: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.28x faster                                                    |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                     |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.7 ms: 1.23x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.74 sec: 1.22x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 947 ms: 1.21x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 29.2 ms: 1.21x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.96 sec: 1.20x faster                                                   |
| sympy_sum                | 184 ms                                                                | 153 ms: 1.20x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 22.1 ms: 1.20x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 63.0 ms: 1.20x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.6 ms: 1.19x faster                                                    |
| sympy_str                | 329 ms                                                                | 283 ms: 1.16x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 63.6 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.15x faster                                                    |
| sympy_expand             | 543 ms                                                                | 480 ms: 1.13x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 138 ms: 1.13x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.75 ms: 1.13x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                                   |
| fannkuch                 | 546 ms                                                                | 486 ms: 1.12x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 62.9 ms: 1.11x faster                                                    |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 197 ms: 1.08x faster                                                     |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.38 ms: 1.11x slower                                                    |
| async_generators         | 452 ms                                                                | 509 ms: 1.12x slower                                                     |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.25x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.05 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.36 ms: 1.53x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.89 sec: 405.18x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (5): xml_etree_iterparse, sqlite_synth, regex_v8, pidigits, regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.297x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.30x