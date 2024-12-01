# Results vs. 3.10.4

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.207x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 334 ms: 1.14x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.39 sec: 1.04x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 471 ms: 2.01x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 598 ms: 1.89x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 772 ms: 1.65x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| float          | 135 ms                                                                | 97.9 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 151 ms: 1.17x faster                                                     |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 410 us: 1.29x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.7 ms: 1.20x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.15x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| django_template | 53.3 ms                                                               | 47.5 ms: 1.12x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 32.3 ms: 1.09x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.10x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 228 us: 2.90x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.21 ms: 2.13x faster                                                    |
| async_tree_none          | 950 ms                                                                | 471 ms: 2.01x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 598 ms: 1.89x faster                                                     |
| richards_super           | 107 ms                                                                | 60.5 ms: 1.77x faster                                                    |
| richards                 | 91.7 ms                                                               | 55.1 ms: 1.67x faster                                                    |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 772 ms: 1.65x faster                                                     |
| raytrace                 | 573 ms                                                                | 358 ms: 1.60x faster                                                     |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                     |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 91.9 ms: 1.46x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.66 ms: 1.45x faster                                                    |
| chaos                    | 121 ms                                                                | 84.2 ms: 1.44x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 42.9 us: 1.44x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                     |
| nbody                    | 166 ms                                                                | 117 ms: 1.41x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 92.4 ms: 1.38x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.05 ms: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                    |
| float                    | 135 ms                                                                | 97.9 ms: 1.38x faster                                                    |
| generators               | 68.1 ms                                                               | 49.8 ms: 1.37x faster                                                    |
| go                       | 264 ms                                                                | 196 ms: 1.35x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.41 us: 1.32x faster                                                    |
| deepcopy                 | 511 us                                                                | 389 us: 1.31x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.14 us: 1.30x faster                                                    |
| comprehensions           | 33.1 us                                                               | 25.5 us: 1.30x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 410 us: 1.29x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                                   |
| pyflate                  | 795 ms                                                                | 625 ms: 1.27x faster                                                     |
| thrift                   | 1.26 ms                                                               | 997 us: 1.26x faster                                                     |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.22x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 163 ms: 1.21x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 82.7 ms: 1.20x faster                                                    |
| regex_compile            | 177 ms                                                                | 151 ms: 1.17x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.17x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.8 ms: 1.15x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| 2to3                     | 381 ms                                                                | 334 ms: 1.14x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.50 sec: 1.13x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.08 us: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 445 ms: 1.13x faster                                                     |
| django_template          | 53.3 ms                                                               | 47.5 ms: 1.12x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.84 ms: 1.11x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 24.1 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 32.3 ms: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 509 ms: 1.07x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 70.8 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.60 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.39 sec: 1.04x faster                                                   |
| sympy_str                | 329 ms                                                                | 317 ms: 1.04x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.60 sec: 1.03x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 75.1 ms: 1.02x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                                   |
| nqueens                  | 117 ms                                                                | 129 ms: 1.10x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.62 sec: 1.11x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 79.5 ms: 1.14x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.2 ms: 1.18x slower                                                    |
| async_generators         | 452 ms                                                                | 538 ms: 1.19x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.46x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.36 ms: 1.53x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.77 ms: 1.67x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.53 sec: 105.03x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                             |

Benchmark hidden because not significant (8): scimark_sparse_mat_mult, regex_effbot, sqlite_synth, meteor_contest, sympy_expand, sympy_sum, xml_etree_iterparse, pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.207x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.32x