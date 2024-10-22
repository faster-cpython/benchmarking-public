# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                                            |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                          |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.6 ms: 1.50x faster                                                           |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 427 ms: 2.04x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 906 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                           |
| float          | 117 ms                                                 | 76.4 ms: 1.53x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                           |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                            |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                           |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 427 ms: 2.04x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 906 ms: 1.95x faster                                                            |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                           |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                            |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.79x faster                                                           |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                           |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.72x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 74.8 ms: 1.71x faster                                                           |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.71x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 69.4 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                           |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                            |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                           |
| float                    | 117 ms                                                 | 76.4 ms: 1.53x faster                                                           |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                            |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.52x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                           |
| tornado_http             | 136 ms                                                 | 90.6 ms: 1.50x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.63 us: 1.47x faster                                                           |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                           |
| pyflate                  | 716 ms                                                 | 490 ms: 1.46x faster                                                            |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                          |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                          |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                           |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                            |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                           |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                           |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                            |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.8 ms: 1.29x faster                                                           |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                            |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 787 us: 1.25x faster                                                            |
| dask                     | 441 ms                                                 | 357 ms: 1.23x faster                                                            |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                          |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                           |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                            |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                           |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.13x