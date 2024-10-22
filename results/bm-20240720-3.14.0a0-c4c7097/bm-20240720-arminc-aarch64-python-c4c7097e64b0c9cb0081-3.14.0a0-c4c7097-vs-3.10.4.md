# Results vs. 3.10.4

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 68.0 ms: 1.27x faster                                                   |
| tornado_http   | 178 ms                                                                | 130 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 446 ms: 2.13x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.12 sec: 2.05x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 574 ms: 1.97x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 732 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 364 us: 1.45x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.5 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.87 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 41.8 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.83 ms: 2.33x faster                                                   |
| async_tree_none          | 950 ms                                                                | 446 ms: 2.13x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.09 ms: 2.05x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.12 sec: 2.05x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 574 ms: 1.97x faster                                                    |
| generators               | 68.1 ms                                                               | 34.9 ms: 1.95x faster                                                   |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                                    |
| richards_super           | 107 ms                                                                | 59.2 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 68.5 ms: 1.77x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 732 ms: 1.74x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                                   |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 572 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.7 us: 1.60x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.5 ms: 1.57x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.99 ms: 1.56x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 332 us: 1.54x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 364 us: 1.45x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.45x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                    |
| pylint                   | 485 ms                                                                | 335 ms: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| pyflate                  | 795 ms                                                                | 574 ms: 1.39x faster                                                    |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| tornado_http             | 178 ms                                                                | 130 ms: 1.38x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.18 us: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.84 us: 1.35x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 961 us: 1.31x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.28x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.8 ms: 1.27x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 68.0 ms: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                                   |
| dask                     | 450 ms                                                                | 364 ms: 1.23x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.23x faster                                                  |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 940 ms: 1.22x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.9 ms: 1.22x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                   |
| fannkuch                 | 546 ms                                                                | 458 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.43 ms: 1.19x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 60.9 ms: 1.15x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 5.81 ms: 1.01x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.5 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 494 ms: 1.09x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.93 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.4 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.99 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.87 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240720-3.14.0a0-c4c7097/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.15x