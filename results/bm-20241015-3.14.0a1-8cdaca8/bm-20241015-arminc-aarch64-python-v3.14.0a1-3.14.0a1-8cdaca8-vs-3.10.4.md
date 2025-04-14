# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 293 ms: 1.30x faster                                         |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                       |
| html5lib       | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                        |
| tornado_http   | 178 ms                                                                | 125 ms: 1.42x faster                                         |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 438 ms: 2.17x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 563 ms: 2.01x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 743 ms: 1.71x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.95x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                         |
| float          | 135 ms                                                                | 95.4 ms: 1.41x faster                                        |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| regex_dna      | 257 ms                                                                | 243 ms: 1.06x faster                                         |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                        |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 365 us: 1.45x faster                                         |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                       |
| xml_etree_process    | 99.5 ms                                                               | 80.6 ms: 1.24x faster                                        |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| unpickle_list        | 6.99 us                                                               | 6.60 us: 1.06x faster                                        |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.22 us: 1.00x faster                                        |
| json_loads           | 30.9 us                                                               | 31.2 us: 1.01x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                        |
| unpickle             | 17.5 us                                                               | 19.1 us: 1.09x slower                                        |
| pickle               | 12.5 us                                                               | 13.9 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                        |
| python_startup         | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.28x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.39x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                        |
| django_template | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.95 ms: 2.27x faster                                        |
| async_tree_none          | 950 ms                                                                | 438 ms: 2.17x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 563 ms: 2.01x faster                                         |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.95x faster                                        |
| go                       | 264 ms                                                                | 136 ms: 1.95x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.93x faster                                       |
| raytrace                 | 573 ms                                                                | 311 ms: 1.84x faster                                         |
| richards_super           | 107 ms                                                                | 60.0 ms: 1.79x faster                                        |
| chaos                    | 121 ms                                                                | 69.3 ms: 1.75x faster                                        |
| richards                 | 91.7 ms                                                               | 53.4 ms: 1.72x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 743 ms: 1.71x faster                                         |
| scimark_lu               | 227 ms                                                                | 133 ms: 1.71x faster                                         |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 554 ms: 1.70x faster                                         |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 80.9 ms: 1.66x faster                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.62x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                        |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                        |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                         |
| hexiom                   | 10.9 ms                                                               | 6.97 ms: 1.57x faster                                        |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                         |
| scimark_monte_carlo      | 128 ms                                                                | 83.7 ms: 1.53x faster                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                       |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                         |
| pickle_pure_python       | 529 us                                                                | 365 us: 1.45x faster                                         |
| logging_simple           | 9.78 us                                                               | 6.82 us: 1.43x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                         |
| tornado_http             | 178 ms                                                                | 125 ms: 1.42x faster                                         |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                         |
| logging_format           | 10.6 us                                                               | 7.51 us: 1.41x faster                                        |
| float                    | 135 ms                                                                | 95.4 ms: 1.41x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.40x faster                                       |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.39x faster                                        |
| pylint                   | 485 ms                                                                | 354 ms: 1.37x faster                                         |
| pyflate                  | 795 ms                                                                | 585 ms: 1.36x faster                                         |
| thrift                   | 1.26 ms                                                               | 929 us: 1.36x faster                                         |
| html5lib                 | 86.5 ms                                                               | 64.6 ms: 1.34x faster                                        |
| sympy_sum                | 184 ms                                                                | 138 ms: 1.33x faster                                         |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                         |
| 2to3                     | 381 ms                                                                | 293 ms: 1.30x faster                                         |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 57.0 ms: 1.29x faster                                        |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                       |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                        |
| django_template          | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 909 ms: 1.26x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.87 sec: 1.26x faster                                       |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                         |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 80.6 ms: 1.24x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 61.8 ms: 1.22x faster                                        |
| nqueens                  | 117 ms                                                                | 98.4 ms: 1.19x faster                                        |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                         |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.46 ms: 1.18x faster                                        |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                       |
| fannkuch                 | 546 ms                                                                | 469 ms: 1.16x faster                                         |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.16x faster                                         |
| meteor_contest           | 126 ms                                                                | 110 ms: 1.14x faster                                         |
| genshi_xml               | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                       |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| json                     | 5.88 ms                                                               | 5.46 ms: 1.08x faster                                        |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                        |
| unpickle_list            | 6.99 us                                                               | 6.60 us: 1.06x faster                                        |
| regex_dna                | 257 ms                                                                | 243 ms: 1.06x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                        |
| pickle_list              | 5.24 us                                                               | 5.22 us: 1.00x faster                                        |
| json_loads               | 30.9 us                                                               | 31.2 us: 1.01x slower                                        |
| async_generators         | 452 ms                                                                | 479 ms: 1.06x slower                                         |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.1 us: 1.09x slower                                        |
| pickle                   | 12.5 us                                                               | 13.9 us: 1.11x slower                                        |
| telco                    | 8.49 ms                                                               | 9.54 ms: 1.12x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                        |
| coverage                 | 83.6 ms                                                               | 97.6 ms: 1.17x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                        |
| python_startup           | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 6.25 ms: 1.50x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.67 ms: 1.63x slower                                        |
| bench_mp_pool            | 14.5 ms                                                               | 4.94 sec: 340.02x slower                                     |
| Geometric mean           | (ref)                                                                 | 1.21x faster                                                 |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx, unpack_sequence

- Geometric mean (including insignificant results): 1.319x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.29x