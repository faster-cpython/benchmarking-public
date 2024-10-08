# Results vs. 3.10.4

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 296 ms: 1.29x faster                                             |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                           |
| html5lib       | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                            |
| tornado_http   | 178 ms                                                                | 126 ms: 1.42x faster                                             |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 429 ms: 2.21x faster                                             |
| async_tree_memoization  | 1.13 sec                                                              | 553 ms: 2.05x faster                                             |
| async_tree_io           | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 714 ms: 1.78x faster                                             |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.51x faster                                             |
| float          | 135 ms                                                                | 94.4 ms: 1.43x faster                                            |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                             |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                            |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                             |
| regex_effbot   | 4.25 ms                                                               | 4.99 ms: 1.17x slower                                            |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 366 us: 1.44x faster                                             |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.44x faster                                             |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                           |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                            |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                             |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                             |
| unpickle_list        | 6.99 us                                                               | 6.64 us: 1.05x faster                                            |
| pickle_dict          | 35.1 us                                                               | 38.1 us: 1.09x slower                                            |
| pickle               | 12.5 us                                                               | 13.9 us: 1.11x slower                                            |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                            |
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                            |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                            |
| django_template | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                            |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                            |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.40x faster                                             |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.28x faster                                            |
| async_tree_none          | 950 ms                                                                | 429 ms: 2.21x faster                                             |
| async_tree_memoization   | 1.13 sec                                                              | 553 ms: 2.05x faster                                             |
| async_tree_io            | 2.28 sec                                                              | 1.17 sec: 1.95x faster                                           |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.94x faster                                            |
| go                       | 264 ms                                                                | 138 ms: 1.91x faster                                             |
| raytrace                 | 573 ms                                                                | 304 ms: 1.88x faster                                             |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                            |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 714 ms: 1.78x faster                                             |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                            |
| chaos                    | 121 ms                                                                | 69.7 ms: 1.74x faster                                            |
| scimark_lu               | 227 ms                                                                | 132 ms: 1.72x faster                                             |
| logging_silent           | 222 ns                                                                | 132 ns: 1.69x faster                                             |
| asyncio_tcp              | 944 ms                                                                | 560 ms: 1.69x faster                                             |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                            |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                            |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                            |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                            |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                             |
| hexiom                   | 10.9 ms                                                               | 7.03 ms: 1.55x faster                                            |
| scimark_monte_carlo      | 128 ms                                                                | 82.4 ms: 1.55x faster                                            |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                             |
| nbody                    | 166 ms                                                                | 110 ms: 1.51x faster                                             |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                           |
| pickle_pure_python       | 529 us                                                                | 366 us: 1.44x faster                                             |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.44x faster                                             |
| float                    | 135 ms                                                                | 94.4 ms: 1.43x faster                                            |
| tornado_http             | 178 ms                                                                | 126 ms: 1.42x faster                                             |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                            |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                             |
| logging_simple           | 9.78 us                                                               | 7.11 us: 1.38x faster                                            |
| html5lib                 | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                            |
| pylint                   | 485 ms                                                                | 355 ms: 1.37x faster                                             |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                           |
| pyflate                  | 795 ms                                                                | 583 ms: 1.36x faster                                             |
| logging_format           | 10.6 us                                                               | 7.81 us: 1.36x faster                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.45 us: 1.33x faster                                            |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                             |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                             |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                             |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.29x faster                                            |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                            |
| 2to3                     | 381 ms                                                                | 296 ms: 1.29x faster                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 904 ms: 1.27x faster                                             |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                           |
| django_template          | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                            |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 58.6 ms: 1.25x faster                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                            |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                            |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                             |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                             |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                            |
| sqlglot_optimize         | 75.4 ms                                                               | 62.0 ms: 1.22x faster                                            |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.39 ms: 1.19x faster                                            |
| nqueens                  | 117 ms                                                                | 98.5 ms: 1.19x faster                                            |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                             |
| scimark_fft              | 500 ms                                                                | 426 ms: 1.17x faster                                             |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                           |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                             |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                            |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                             |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                           |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                             |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                             |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.07x faster                                            |
| json                     | 5.88 ms                                                               | 5.50 ms: 1.07x faster                                            |
| unpickle_list            | 6.99 us                                                               | 6.64 us: 1.05x faster                                            |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                            |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                             |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                            |
| async_generators         | 452 ms                                                                | 475 ms: 1.05x slower                                             |
| pickle_dict              | 35.1 us                                                               | 38.1 us: 1.09x slower                                            |
| telco                    | 8.49 ms                                                               | 9.25 ms: 1.09x slower                                            |
| pickle                   | 12.5 us                                                               | 13.9 us: 1.11x slower                                            |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                            |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                            |
| regex_effbot             | 4.25 ms                                                               | 4.99 ms: 1.17x slower                                            |
| coverage                 | 83.6 ms                                                               | 99.0 ms: 1.18x slower                                            |
| gc_traversal             | 4.15 ms                                                               | 5.07 ms: 1.22x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                            |
| bench_mp_pool            | 14.5 ms                                                               | 5.20 sec: 358.02x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.22x faster                                                     |

Benchmark hidden because not significant (5): xml_etree_iterparse, pidigits, pickle_list, asyncio_websockets, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.14x