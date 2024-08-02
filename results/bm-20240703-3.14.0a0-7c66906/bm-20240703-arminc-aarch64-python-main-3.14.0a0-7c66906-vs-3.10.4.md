# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-aarch64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                    |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.14x faster                                  |
| html5lib       | 86.5 ms                                                               | 68.8 ms: 1.26x faster                                   |
| tornado_http   | 178 ms                                                                | 132 ms: 1.35x faster                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 437 ms: 2.18x faster                                    |
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.15x faster                                  |
| async_tree_memoization  | 1.13 sec                                                              | 556 ms: 2.04x faster                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 725 ms: 1.75x faster                                    |
| Geometric mean          | (ref)                                                                 | 2.02x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| float          | 135 ms                                                                | 92.9 ms: 1.45x faster                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.45x faster                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                    |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.47x faster                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                    |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                    |
| json_loads           | 30.9 us                                                               | 33.2 us: 1.07x slower                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                   |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                   |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                   |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 199 us: 3.32x faster                                    |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                   |
| async_tree_none          | 950 ms                                                                | 437 ms: 2.18x faster                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.15x faster                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.06 ms: 2.06x faster                                   |
| async_tree_memoization   | 1.13 sec                                                              | 556 ms: 2.04x faster                                    |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                    |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                   |
| generators               | 68.1 ms                                                               | 38.0 ms: 1.79x faster                                   |
| chaos                    | 121 ms                                                                | 68.0 ms: 1.78x faster                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 725 ms: 1.75x faster                                    |
| richards                 | 91.7 ms                                                               | 53.2 ms: 1.72x faster                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                   |
| asyncio_tcp              | 944 ms                                                                | 565 ms: 1.67x faster                                    |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.66x faster                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.66x faster                                   |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                    |
| crypto_pyaes             | 134 ms                                                                | 81.7 ms: 1.64x faster                                   |
| comprehensions           | 33.1 us                                                               | 20.9 us: 1.59x faster                                   |
| deepcopy_memo            | 61.7 us                                                               | 39.1 us: 1.58x faster                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                    |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                   |
| scimark_monte_carlo      | 128 ms                                                                | 83.8 ms: 1.53x faster                                   |
| deepcopy                 | 511 us                                                                | 335 us: 1.52x faster                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                  |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.47x faster                                    |
| float                    | 135 ms                                                                | 92.9 ms: 1.45x faster                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.45x faster                                    |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                    |
| pylint                   | 485 ms                                                                | 344 ms: 1.41x faster                                    |
| logging_simple           | 9.78 us                                                               | 6.92 us: 1.41x faster                                   |
| logging_format           | 10.6 us                                                               | 7.61 us: 1.39x faster                                   |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                  |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                    |
| pyflate                  | 795 ms                                                                | 586 ms: 1.36x faster                                    |
| tornado_http             | 178 ms                                                                | 132 ms: 1.35x faster                                    |
| thrift                   | 1.26 ms                                                               | 943 us: 1.34x faster                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.47 us: 1.33x faster                                   |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.29x faster                                   |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                   |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                   |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                    |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                   |
| html5lib                 | 86.5 ms                                                               | 68.8 ms: 1.26x faster                                   |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.3 ms: 1.24x faster                                   |
| dulwich_log              | 73.5 ms                                                               | 59.3 ms: 1.24x faster                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                   |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                   |
| dask                     | 450 ms                                                                | 367 ms: 1.23x faster                                    |
| sympy_str                | 329 ms                                                                | 269 ms: 1.22x faster                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.22x faster                                   |
| sqlglot_normalize        | 156 ms                                                                | 130 ms: 1.20x faster                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 63.0 ms: 1.20x faster                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.99 sec: 1.19x faster                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 970 ms: 1.18x faster                                    |
| nqueens                  | 117 ms                                                                | 99.9 ms: 1.18x faster                                   |
| fannkuch                 | 546 ms                                                                | 466 ms: 1.17x faster                                    |
| sympy_expand             | 543 ms                                                                | 466 ms: 1.16x faster                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.55 ms: 1.16x faster                                   |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                   |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.14x faster                                  |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                    |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                    |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                   |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                    |
| json_loads               | 30.9 us                                                               | 33.2 us: 1.07x slower                                   |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                   |
| gc_traversal             | 4.15 ms                                                               | 4.86 ms: 1.17x slower                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                   |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                   |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-arminc-aarch64-python-main-3.14.0a0-7c66906.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.13x