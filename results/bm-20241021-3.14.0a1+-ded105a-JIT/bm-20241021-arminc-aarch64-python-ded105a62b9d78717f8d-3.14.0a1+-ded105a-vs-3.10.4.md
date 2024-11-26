# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-aarch64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.161x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 385 ms: 1.01x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.64 sec: 1.03x slower                                                   |
| html5lib       | 86.5 ms                                                               | 72.4 ms: 1.19x faster                                                    |
| tornado_http   | 178 ms                                                                | 148 ms: 1.21x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 607 ms: 1.87x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 765 ms: 1.66x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.86x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| float          | 135 ms                                                                | 96.8 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                    |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 272 us: 1.34x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.8 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.70 ms: 1.26x slower                                                    |
| python_startup         | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                    |
| genshi_text    | 35.2 ms                                                               | 34.9 ms: 1.01x faster                                                    |
| genshi_xml     | 69.8 ms                                                               | 85.7 ms: 1.23x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                     |
| async_tree_none          | 950 ms                                                                | 475 ms: 2.00x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.53 ms: 1.97x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 607 ms: 1.87x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 765 ms: 1.66x faster                                                     |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                     |
| raytrace                 | 573 ms                                                                | 351 ms: 1.63x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 39.0 us: 1.58x faster                                                    |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                     |
| richards_super           | 107 ms                                                                | 68.5 ms: 1.56x faster                                                    |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.51x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.0 ms: 1.49x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| richards                 | 91.7 ms                                                               | 63.2 ms: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 89.1 ms: 1.43x faster                                                    |
| go                       | 264 ms                                                                | 185 ms: 1.43x faster                                                     |
| chaos                    | 121 ms                                                                | 85.0 ms: 1.42x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.70 ms: 1.41x faster                                                    |
| float                    | 135 ms                                                                | 96.8 ms: 1.39x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 272 us: 1.34x faster                                                     |
| deepcopy                 | 511 us                                                                | 382 us: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.19 ms: 1.30x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.22 us: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.68 us: 1.27x faster                                                    |
| pyflate                  | 795 ms                                                                | 638 ms: 1.25x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                    |
| tornado_http             | 178 ms                                                                | 148 ms: 1.21x faster                                                     |
| spectral_norm            | 186 ms                                                                | 155 ms: 1.20x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 72.4 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.4 ms: 1.16x faster                                                    |
| generators               | 68.1 ms                                                               | 58.8 ms: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.06 us: 1.13x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.53 sec: 1.10x faster                                                   |
| scimark_fft              | 500 ms                                                                | 453 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.18 ms: 1.06x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.49 sec: 1.06x faster                                                   |
| fannkuch                 | 546 ms                                                                | 519 ms: 1.05x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 10.4 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                    |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.02x faster                                                     |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 34.9 ms: 1.01x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 157 ms: 1.00x slower                                                     |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                     |
| 2to3                     | 381 ms                                                                | 385 ms: 1.01x slower                                                     |
| json_loads               | 30.9 us                                                               | 31.8 us: 1.03x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.64 sec: 1.03x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.20 sec: 1.05x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.51 sec: 1.07x slower                                                   |
| nqueens                  | 117 ms                                                                | 127 ms: 1.08x slower                                                     |
| sympy_expand             | 543 ms                                                                | 595 ms: 1.10x slower                                                     |
| sympy_str                | 329 ms                                                                | 361 ms: 1.10x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 83.1 ms: 1.10x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 81.5 ms: 1.11x slower                                                    |
| async_generators         | 452 ms                                                                | 511 ms: 1.13x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.63 ms: 1.13x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 30.2 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                                    |
| sympy_sum                | 184 ms                                                                | 219 ms: 1.19x slower                                                     |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 85.7 ms: 1.23x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.70 ms: 1.26x slower                                                    |
| python_startup           | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.34 ms: 1.53x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.61 ms: 1.60x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.71 sec: 186.72x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (6): pylint, xml_etree_iterparse, json, django_template, pidigits, regex_compile
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.161x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.37x