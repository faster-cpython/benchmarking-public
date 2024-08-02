# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 513 ms: 1.35x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.11 sec: 1.17x slower                                                  |
| html5lib       | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| tornado_http   | 178 ms                                                                | 207 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                  |
| async_tree_none         | 950 ms                                                                | 604 ms: 1.57x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 739 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 912 ms: 1.39x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| nbody          | 166 ms                                                                | 290 ms: 1.75x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.40x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 32.6 ms: 1.01x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.43 ms: 1.04x slower                                                   |
| regex_compile  | 177 ms                                                                | 254 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 17.7 ms: 1.06x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| json_loads           | 30.9 us                                                               | 38.8 us: 1.25x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 157 ms: 1.28x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 130 ms: 1.30x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 773 us: 1.46x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 538 us: 1.47x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.20x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 17.6 ms: 1.57x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.8 ms: 1.72x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.65x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 52.2 ms: 1.48x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| django_template | 53.3 ms                                                               | 81.3 ms: 1.52x slower                                                   |
| mako            | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.50x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.23 ms: 2.33x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 332 us: 1.99x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.39 sec: 1.64x faster                                                  |
| async_tree_none          | 950 ms                                                                | 604 ms: 1.57x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 739 ms: 1.53x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.60 ms: 1.41x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 671 ms: 1.41x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 912 ms: 1.39x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.46 sec: 1.34x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.45 ms: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 57.7 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 32.6 ms: 1.01x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| pylint                   | 485 ms                                                                | 502 ms: 1.03x slower                                                    |
| coroutines               | 37.2 ms                                                               | 38.5 ms: 1.03x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.43 ms: 1.04x slower                                                   |
| crypto_pyaes             | 134 ms                                                                | 140 ms: 1.04x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 17.7 ms: 1.06x slower                                                   |
| deepcopy                 | 511 us                                                                | 553 us: 1.08x slower                                                    |
| tornado_http             | 178 ms                                                                | 207 ms: 1.16x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.11 sec: 1.17x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.92 ms: 1.17x slower                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.87 ms: 1.18x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 72.8 us: 1.18x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.38 sec: 1.18x slower                                                  |
| json                     | 5.88 ms                                                               | 6.97 ms: 1.19x slower                                                   |
| scimark_fft              | 500 ms                                                                | 599 ms: 1.20x slower                                                    |
| pycparser                | 1.69 sec                                                              | 2.06 sec: 1.22x slower                                                  |
| comprehensions           | 33.1 us                                                               | 40.5 us: 1.22x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| json_loads               | 30.9 us                                                               | 38.8 us: 1.25x slower                                                   |
| logging_silent           | 222 ns                                                                | 281 ns: 1.27x slower                                                    |
| nqueens                  | 117 ms                                                                | 149 ms: 1.27x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                  |
| richards                 | 91.7 ms                                                               | 117 ms: 1.27x slower                                                    |
| richards_super           | 107 ms                                                                | 137 ms: 1.28x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 157 ms: 1.28x slower                                                    |
| spectral_norm            | 186 ms                                                                | 239 ms: 1.28x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 5.99 us: 1.30x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 130 ms: 1.30x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.65 ms: 1.31x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 35.1 ms: 1.32x slower                                                   |
| chaos                    | 121 ms                                                                | 161 ms: 1.33x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 98.3 ms: 1.34x slower                                                   |
| 2to3                     | 381 ms                                                                | 513 ms: 1.35x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 172 ms: 1.35x slower                                                    |
| fannkuch                 | 546 ms                                                                | 740 ms: 1.36x slower                                                    |
| meteor_contest           | 126 ms                                                                | 172 ms: 1.36x slower                                                    |
| scimark_sor              | 246 ms                                                                | 341 ms: 1.39x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 121 ms: 1.40x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.7 ms: 1.42x slower                                                   |
| hexiom                   | 10.9 ms                                                               | 15.6 ms: 1.43x slower                                                   |
| regex_compile            | 177 ms                                                                | 254 ms: 1.44x slower                                                    |
| raytrace                 | 573 ms                                                                | 829 ms: 1.45x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 773 us: 1.46x slower                                                    |
| unpickle_pure_python     | 366 us                                                                | 538 us: 1.47x slower                                                    |
| telco                    | 8.49 ms                                                               | 12.5 ms: 1.47x slower                                                   |
| logging_format           | 10.6 us                                                               | 15.7 us: 1.48x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 231 ms: 1.48x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 52.2 ms: 1.48x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 104 ms: 1.48x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.7 us: 1.50x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.74 sec: 1.52x slower                                                  |
| async_generators         | 452 ms                                                                | 686 ms: 1.52x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.59 sec: 1.52x slower                                                  |
| django_template          | 53.3 ms                                                               | 81.3 ms: 1.52x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| scimark_lu               | 227 ms                                                                | 348 ms: 1.54x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.41 ms: 1.55x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 117 ms: 1.55x slower                                                    |
| float                    | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| python_startup           | 11.2 ms                                                               | 17.6 ms: 1.57x slower                                                   |
| coverage                 | 83.6 ms                                                               | 132 ms: 1.58x slower                                                    |
| sympy_str                | 329 ms                                                                | 520 ms: 1.58x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.83 ms: 1.59x slower                                                   |
| go                       | 264 ms                                                                | 446 ms: 1.69x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 11.8 ms: 1.72x slower                                                   |
| sympy_sum                | 184 ms                                                                | 317 ms: 1.72x slower                                                    |
| nbody                    | 166 ms                                                                | 290 ms: 1.75x slower                                                    |
| sympy_expand             | 543 ms                                                                | 953 ms: 1.76x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (4): regex_dna, pidigits, xml_etree_iterparse, pathlib
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 1.32x