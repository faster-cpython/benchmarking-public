# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: linux-aarch64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                           |
| chameleon      | 10.8 ms                                                               | 9.16 ms: 1.18x faster                                          |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                         |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                          |
| tornado_http   | 178 ms                                                                | 128 ms: 1.40x faster                                           |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 494 ms: 1.92x faster                                           |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 649 ms: 1.75x faster                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 784 ms: 1.62x faster                                           |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.2 ms: 1.48x faster                                          |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                           |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                           |
| regex_v8       | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                          |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                           |
| regex_effbot   | 4.25 ms                                                               | 4.98 ms: 1.17x slower                                          |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 355 us: 1.49x faster                                           |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                           |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                         |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                          |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                          |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 198 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                           |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.01x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                          |
| python_startup_no_site | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                          |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                          |
| genshi_text     | 35.2 ms                                                               | 28.4 ms: 1.24x faster                                          |
| genshi_xml      | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                          |
| Geometric mean  | (ref)                                                                 | 1.25x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                           |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                          |
| bench_mp_pool            | 14.5 ms                                                               | 7.12 ms: 2.04x faster                                          |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                           |
| async_tree_none          | 950 ms                                                                | 494 ms: 1.92x faster                                           |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                         |
| generators               | 68.1 ms                                                               | 37.7 ms: 1.80x faster                                          |
| richards_super           | 107 ms                                                                | 59.9 ms: 1.79x faster                                          |
| chaos                    | 121 ms                                                                | 68.5 ms: 1.77x faster                                          |
| async_tree_memoization   | 1.13 sec                                                              | 649 ms: 1.75x faster                                           |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                          |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.73x faster                                          |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.66x faster                                          |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                           |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                           |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.64x faster                                          |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 784 ms: 1.62x faster                                           |
| asyncio_tcp              | 944 ms                                                                | 582 ms: 1.62x faster                                           |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                          |
| scimark_monte_carlo      | 128 ms                                                                | 82.5 ms: 1.55x faster                                          |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                           |
| hexiom                   | 10.9 ms                                                               | 7.12 ms: 1.53x faster                                          |
| pickle_pure_python       | 529 us                                                                | 355 us: 1.49x faster                                           |
| float                    | 135 ms                                                                | 91.2 ms: 1.48x faster                                          |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                         |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                           |
| pyflate                  | 795 ms                                                                | 560 ms: 1.42x faster                                           |
| tornado_http             | 178 ms                                                                | 128 ms: 1.40x faster                                           |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                         |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                          |
| logging_simple           | 9.78 us                                                               | 7.06 us: 1.39x faster                                          |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                           |
| logging_format           | 10.6 us                                                               | 7.83 us: 1.35x faster                                          |
| pylint                   | 485 ms                                                                | 362 ms: 1.34x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                         |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                           |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                           |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                          |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                          |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                           |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                          |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                           |
| sympy_integrate          | 26.5 ms                                                               | 21.4 ms: 1.24x faster                                          |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                          |
| genshi_text              | 35.2 ms                                                               | 28.4 ms: 1.24x faster                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                          |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                           |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                          |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                         |
| mypy2                    | 936 ms                                                                | 765 ms: 1.22x faster                                           |
| deepcopy_memo            | 61.7 us                                                               | 50.5 us: 1.22x faster                                          |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                           |
| pprint_safe_repr         | 1.15 sec                                                              | 948 ms: 1.21x faster                                           |
| fannkuch                 | 546 ms                                                                | 453 ms: 1.21x faster                                           |
| dask                     | 450 ms                                                                | 374 ms: 1.20x faster                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 62.8 ms: 1.20x faster                                          |
| nqueens                  | 117 ms                                                                | 98.6 ms: 1.19x faster                                          |
| chameleon                | 10.8 ms                                                               | 9.16 ms: 1.18x faster                                          |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.51 ms: 1.17x faster                                          |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                          |
| deepcopy_reduce          | 4.60 us                                                               | 4.01 us: 1.15x faster                                          |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                         |
| deepcopy                 | 511 us                                                                | 450 us: 1.14x faster                                           |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                           |
| genshi_xml               | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                          |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                           |
| mdp                      | 3.70 sec                                                              | 3.36 sec: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                           |
| json                     | 5.88 ms                                                               | 5.47 ms: 1.07x faster                                          |
| xml_etree_parse          | 212 ms                                                                | 198 ms: 1.07x faster                                           |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                           |
| regex_v8                 | 32.2 ms                                                               | 31.3 ms: 1.03x faster                                          |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                           |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.01x slower                                          |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.03x slower                                          |
| async_generators         | 452 ms                                                                | 492 ms: 1.09x slower                                           |
| telco                    | 8.49 ms                                                               | 9.54 ms: 1.12x slower                                          |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                          |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                          |
| regex_effbot             | 4.25 ms                                                               | 4.98 ms: 1.17x slower                                          |
| gc_traversal             | 4.15 ms                                                               | 5.07 ms: 1.22x slower                                          |
| python_startup_no_site   | 6.89 ms                                                               | 8.75 ms: 1.27x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                   |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, dulwich_log, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-arminc-aarch64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.305x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.14x