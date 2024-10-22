# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 362 ms: 1.05x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 451 ms: 2.10x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.11 sec: 2.05x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 573 ms: 1.98x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 742 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.96x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.5 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 385 us: 1.37x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 272 us: 1.34x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 195 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.85 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 50.3 ms: 1.06x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.5 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 81.2 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                    |
| async_tree_none          | 950 ms                                                                | 451 ms: 2.10x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.11 sec: 2.05x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.40 ms: 2.03x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 573 ms: 1.98x faster                                                    |
| generators               | 68.1 ms                                                               | 36.5 ms: 1.86x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.86 ms: 1.85x faster                                                   |
| raytrace                 | 573 ms                                                                | 323 ms: 1.78x faster                                                    |
| richards_super           | 107 ms                                                                | 60.7 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 742 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.8 ms: 1.70x faster                                                   |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.8 us: 1.63x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 612 ms: 1.54x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                   |
| float                    | 135 ms                                                                | 90.5 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 177 ms: 1.49x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 90.3 ms: 1.48x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.4 ms: 1.43x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.3 us: 1.42x faster                                                   |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.05 ms: 1.39x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 385 us: 1.37x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.12 us: 1.37x faster                                                   |
| deepcopy                 | 511 us                                                                | 376 us: 1.36x faster                                                    |
| chaos                    | 121 ms                                                                | 89.1 ms: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.84 us: 1.35x faster                                                   |
| pyflate                  | 795 ms                                                                | 589 ms: 1.35x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 272 us: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 963 us: 1.31x faster                                                    |
| tornado_http             | 178 ms                                                                | 136 ms: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| scimark_lu               | 227 ms                                                                | 181 ms: 1.26x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.23x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| pylint                   | 485 ms                                                                | 403 ms: 1.21x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.12 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.02 us: 1.14x faster                                                   |
| dask                     | 450 ms                                                                | 396 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.74 ms: 1.13x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 195 ms: 1.09x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 70.0 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                                  |
| django_template          | 53.3 ms                                                               | 50.3 ms: 1.06x faster                                                   |
| 2to3                     | 381 ms                                                                | 362 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 34.5 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.13 sec: 1.02x faster                                                  |
| nqueens                  | 117 ms                                                                | 116 ms: 1.01x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.33 sec: 1.01x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                   |
| sympy_str                | 329 ms                                                                | 343 ms: 1.04x slower                                                    |
| sympy_expand             | 543 ms                                                                | 569 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| sympy_sum                | 184 ms                                                                | 197 ms: 1.07x slower                                                    |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 81.2 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.23x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.85 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (7): xml_etree_iterparse, dulwich_log, json, regex_dna, regex_compile, pidigits, sympy_integrate
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.24x