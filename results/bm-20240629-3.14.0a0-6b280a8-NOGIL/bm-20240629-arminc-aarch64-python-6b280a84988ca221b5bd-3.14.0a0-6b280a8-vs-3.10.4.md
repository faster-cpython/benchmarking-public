# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.21x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 523 ms: 1.37x slower                                                    |
| docutils       | 3.53 sec                                                              | 4.12 sec: 1.17x slower                                                  |
| html5lib       | 86.5 ms                                                               | 120 ms: 1.39x slower                                                    |
| tornado_http   | 178 ms                                                                | 202 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.42 sec: 1.61x faster                                                  |
| async_tree_none         | 950 ms                                                                | 625 ms: 1.52x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 762 ms: 1.49x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 925 ms: 1.38x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.50x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 211 ms: 1.57x slower                                                    |
| nbody          | 166 ms                                                                | 293 ms: 1.77x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.40x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 241 ms: 1.07x faster                                                    |
| regex_compile  | 177 ms                                                                | 258 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 18.1 ms: 1.08x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.4 us: 1.24x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.29 sec: 1.28x slower                                                  |
| xml_etree_process    | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 164 ms: 1.33x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 778 us: 1.47x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 546 us: 1.49x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 17.7 ms: 1.58x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.9 ms: 1.72x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.65x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 52.5 ms: 1.49x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 105 ms: 1.50x slower                                                    |
| mako            | 18.9 ms                                                               | 28.7 ms: 1.52x slower                                                   |
| django_template | 53.3 ms                                                               | 82.4 ms: 1.54x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.51x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.25 ms: 2.32x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 338 us: 1.96x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.42 sec: 1.61x faster                                                  |
| async_tree_none          | 950 ms                                                                | 625 ms: 1.52x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 762 ms: 1.49x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.59 ms: 1.42x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 681 ms: 1.39x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 925 ms: 1.38x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.48 sec: 1.32x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.43 ms: 1.21x faster                                                   |
| generators               | 68.1 ms                                                               | 57.2 ms: 1.19x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| regex_dna                | 257 ms                                                                | 241 ms: 1.07x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 668 ms: 1.02x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 26.9 ms: 1.02x slower                                                   |
| pylint                   | 485 ms                                                                | 507 ms: 1.04x slower                                                    |
| crypto_pyaes             | 134 ms                                                                | 142 ms: 1.06x slower                                                    |
| coroutines               | 37.2 ms                                                               | 39.9 ms: 1.07x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 18.1 ms: 1.08x slower                                                   |
| deepcopy                 | 511 us                                                                | 562 us: 1.10x slower                                                    |
| tornado_http             | 178 ms                                                                | 202 ms: 1.13x slower                                                    |
| docutils                 | 3.53 sec                                                              | 4.12 sec: 1.17x slower                                                  |
| json                     | 5.88 ms                                                               | 6.89 ms: 1.17x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 72.6 us: 1.18x slower                                                   |
| scimark_fft              | 500 ms                                                                | 589 ms: 1.18x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.87 ms: 1.18x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.42 sec: 1.19x slower                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 9.16 ms: 1.20x slower                                                   |
| pycparser                | 1.69 sec                                                              | 2.06 sec: 1.22x slower                                                  |
| comprehensions           | 33.1 us                                                               | 40.8 us: 1.23x slower                                                   |
| logging_silent           | 222 ns                                                                | 276 ns: 1.24x slower                                                    |
| json_loads               | 30.9 us                                                               | 38.4 us: 1.24x slower                                                   |
| spectral_norm            | 186 ms                                                                | 235 ms: 1.26x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.01 sec: 1.27x slower                                                  |
| tomli_loads              | 3.36 sec                                                              | 4.29 sec: 1.28x slower                                                  |
| richards                 | 91.7 ms                                                               | 119 ms: 1.30x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 95.9 ms: 1.30x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 131 ms: 1.32x slower                                                    |
| richards_super           | 107 ms                                                                | 142 ms: 1.32x slower                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 6.11 us: 1.33x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 35.3 ms: 1.33x slower                                                   |
| nqueens                  | 117 ms                                                                | 156 ms: 1.33x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 164 ms: 1.33x slower                                                    |
| chaos                    | 121 ms                                                                | 163 ms: 1.34x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 172 ms: 1.35x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.72 ms: 1.36x slower                                                   |
| 2to3                     | 381 ms                                                                | 523 ms: 1.37x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.3 ms: 1.38x slower                                                   |
| scimark_sor              | 246 ms                                                                | 340 ms: 1.38x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 120 ms: 1.39x slower                                                    |
| meteor_contest           | 126 ms                                                                | 176 ms: 1.39x slower                                                    |
| fannkuch                 | 546 ms                                                                | 769 ms: 1.41x slower                                                    |
| raytrace                 | 573 ms                                                                | 824 ms: 1.44x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.9 ms: 1.46x slower                                                   |
| regex_compile            | 177 ms                                                                | 258 ms: 1.46x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 778 us: 1.47x slower                                                    |
| async_generators         | 452 ms                                                                | 667 ms: 1.47x slower                                                    |
| telco                    | 8.49 ms                                                               | 12.6 ms: 1.49x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 232 ms: 1.49x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 52.5 ms: 1.49x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 546 us: 1.49x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.6 us: 1.50x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 105 ms: 1.50x slower                                                    |
| logging_format           | 10.6 us                                                               | 16.0 us: 1.51x slower                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 4.28 ms: 1.51x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.7 ms: 1.52x slower                                                   |
| scimark_lu               | 227 ms                                                                | 345 ms: 1.52x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.69 ms: 1.54x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 116 ms: 1.54x slower                                                    |
| django_template          | 53.3 ms                                                               | 82.4 ms: 1.54x slower                                                   |
| float                    | 135 ms                                                                | 211 ms: 1.57x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.81 sec: 1.57x slower                                                  |
| python_startup           | 11.2 ms                                                               | 17.7 ms: 1.58x slower                                                   |
| sympy_str                | 329 ms                                                                | 519 ms: 1.58x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.73 sec: 1.58x slower                                                  |
| go                       | 264 ms                                                                | 449 ms: 1.70x slower                                                    |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.70x slower                                                    |
| sympy_sum                | 184 ms                                                                | 314 ms: 1.71x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 11.9 ms: 1.72x slower                                                   |
| sympy_expand             | 543 ms                                                                | 956 ms: 1.76x slower                                                    |
| nbody                    | 166 ms                                                                | 293 ms: 1.77x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.21x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_iterparse, pidigits, regex_v8, regex_effbot
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8-NOGIL/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.22x
- 95% likely to have a slowdown of 1.20x
- 99% likely to have a slowdown of 1.17x

# Memory
- memory change: 1.31x