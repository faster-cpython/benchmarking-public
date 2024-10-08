# Results vs. 3.10.4

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 521 ms: 1.37x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.04 sec: 1.14x slower                                                  |
| html5lib       | 86.5 ms                                                               | 122 ms: 1.41x slower                                                    |
| tornado_http   | 178 ms                                                                | 204 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.41 sec: 1.63x faster                                                  |
| async_tree_none         | 950 ms                                                                | 606 ms: 1.57x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 738 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 908 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.53x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| nbody          | 166 ms                                                                | 282 ms: 1.70x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.38x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.48 ms: 1.05x slower                                                   |
| regex_compile  | 177 ms                                                                | 260 ms: 1.47x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 18.3 ms: 1.10x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| json_loads           | 30.9 us                                                               | 39.5 us: 1.28x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 162 ms: 1.32x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 776 us: 1.47x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 548 us: 1.50x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.22x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.0 ms: 1.61x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.1 ms: 1.75x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.68x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 105 ms: 1.51x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 53.4 ms: 1.52x slower                                                   |
| mako            | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| django_template | 53.3 ms                                                               | 84.2 ms: 1.58x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.53x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.96 ms: 2.09x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 339 us: 1.95x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.41 sec: 1.63x faster                                                  |
| async_tree_none          | 950 ms                                                                | 606 ms: 1.57x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 738 ms: 1.54x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 642 ms: 1.47x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 908 ms: 1.40x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.64 ms: 1.38x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.46 sec: 1.34x faster                                                  |
| generators               | 68.1 ms                                                               | 57.4 ms: 1.19x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 3.50 ms: 1.19x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 26.8 ms: 1.02x slower                                                   |
| regex_v8                 | 32.2 ms                                                               | 32.8 ms: 1.02x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 137 ms: 1.03x slower                                                    |
| pylint                   | 485 ms                                                                | 509 ms: 1.05x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.48 ms: 1.05x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 18.3 ms: 1.10x slower                                                   |
| deepcopy                 | 511 us                                                                | 566 us: 1.11x slower                                                    |
| coroutines               | 37.2 ms                                                               | 41.3 ms: 1.11x slower                                                   |
| docutils                 | 3.53 sec                                                              | 4.04 sec: 1.14x slower                                                  |
| tornado_http             | 178 ms                                                                | 204 ms: 1.14x slower                                                    |
| scimark_fft              | 500 ms                                                                | 576 ms: 1.15x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 72.2 us: 1.17x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.34 sec: 1.17x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.03 ms: 1.18x slower                                                   |
| pycparser                | 1.69 sec                                                              | 2.03 sec: 1.20x slower                                                  |
| json                     | 5.88 ms                                                               | 7.12 ms: 1.21x slower                                                   |
| comprehensions           | 33.1 us                                                               | 40.7 us: 1.23x slower                                                   |
| spectral_norm            | 186 ms                                                                | 233 ms: 1.25x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 4.20 sec: 1.25x slower                                                  |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                  |
| json_loads               | 30.9 us                                                               | 39.5 us: 1.28x slower                                                   |
| richards                 | 91.7 ms                                                               | 118 ms: 1.28x slower                                                    |
| richards_super           | 107 ms                                                                | 138 ms: 1.28x slower                                                    |
| logging_silent           | 222 ns                                                                | 287 ns: 1.29x slower                                                    |
| nqueens                  | 117 ms                                                                | 153 ms: 1.30x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 34.7 ms: 1.31x slower                                                   |
| thrift                   | 1.26 ms                                                               | 1.66 ms: 1.31x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 162 ms: 1.32x slower                                                    |
| chaos                    | 121 ms                                                                | 159 ms: 1.32x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 2.10 ms: 1.32x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 6.08 us: 1.32x slower                                                   |
| meteor_contest           | 126 ms                                                                | 167 ms: 1.32x slower                                                    |
| fannkuch                 | 546 ms                                                                | 740 ms: 1.36x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 174 ms: 1.36x slower                                                    |
| 2to3                     | 381 ms                                                                | 521 ms: 1.37x slower                                                    |
| scimark_sor              | 246 ms                                                                | 342 ms: 1.39x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 122 ms: 1.41x slower                                                    |
| raytrace                 | 573 ms                                                                | 817 ms: 1.42x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.8 ms: 1.44x slower                                                   |
| hexiom                   | 10.9 ms                                                               | 15.9 ms: 1.46x slower                                                   |
| pickle_pure_python       | 529 us                                                                | 776 us: 1.47x slower                                                    |
| async_generators         | 452 ms                                                                | 665 ms: 1.47x slower                                                    |
| regex_compile            | 177 ms                                                                | 260 ms: 1.47x slower                                                    |
| logging_format           | 10.6 us                                                               | 15.7 us: 1.48x slower                                                   |
| logging_simple           | 9.78 us                                                               | 14.5 us: 1.48x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 548 us: 1.50x slower                                                    |
| sqlglot_normalize        | 156 ms                                                                | 234 ms: 1.50x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 105 ms: 1.51x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 4.30 ms: 1.51x slower                                                   |
| genshi_text              | 35.2 ms                                                               | 53.4 ms: 1.52x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.9 ms: 1.53x slower                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 3.70 ms: 1.54x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.78 sec: 1.55x slower                                                  |
| float                    | 135 ms                                                                | 209 ms: 1.55x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 117 ms: 1.55x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.66 sec: 1.55x slower                                                  |
| telco                    | 8.49 ms                                                               | 13.2 ms: 1.55x slower                                                   |
| scimark_lu               | 227 ms                                                                | 355 ms: 1.57x slower                                                    |
| sympy_str                | 329 ms                                                                | 514 ms: 1.57x slower                                                    |
| django_template          | 53.3 ms                                                               | 84.2 ms: 1.58x slower                                                   |
| python_startup           | 11.2 ms                                                               | 18.0 ms: 1.61x slower                                                   |
| coverage                 | 83.6 ms                                                               | 136 ms: 1.62x slower                                                    |
| go                       | 264 ms                                                                | 443 ms: 1.68x slower                                                    |
| nbody                    | 166 ms                                                                | 282 ms: 1.70x slower                                                    |
| sympy_sum                | 184 ms                                                                | 315 ms: 1.71x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.1 ms: 1.75x slower                                                   |
| sympy_expand             | 543 ms                                                                | 969 ms: 1.79x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (3): pidigits, regex_dna, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-52caaef-NOGIL/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.33x