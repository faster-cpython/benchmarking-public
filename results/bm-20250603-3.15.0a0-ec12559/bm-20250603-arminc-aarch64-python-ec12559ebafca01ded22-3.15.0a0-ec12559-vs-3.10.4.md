# Results vs. 3.10.4

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-aarch64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.225x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.8 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                    |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.8 ms: 1.55x faster                                                   |
| nbody          | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.80 ms: 1.12x faster                                                   |
| regex_v8       | 32.2 ms                                                               | 29.1 ms: 1.11x faster                                                   |
| regex_dna      | 257 ms                                                                | 235 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.50 sec: 1.34x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| django_template | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.37x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                    |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.01 ms: 2.23x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| go                       | 264 ms                                                                | 129 ms: 2.04x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                   |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                                   |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                    |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                   |
| scimark_sor              | 246 ms                                                                | 144 ms: 1.71x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.63x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 79.0 ms: 1.62x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 83.4 ms: 1.61x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 6.97 ms: 1.56x faster                                                   |
| float                    | 135 ms                                                                | 86.8 ms: 1.55x faster                                                   |
| deepcopy                 | 511 us                                                                | 330 us: 1.55x faster                                                    |
| pylint                   | 485 ms                                                                | 318 ms: 1.53x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.50x faster                                                    |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 550 ms: 1.44x faster                                                    |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.8 ms: 1.42x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 52.3 ms: 1.40x faster                                                   |
| nbody                    | 166 ms                                                                | 119 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.7 ms: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.50 sec: 1.34x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 20.2 ms: 1.32x faster                                                   |
| django_template          | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.0 ms: 1.30x faster                                                   |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.69 us: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| sympy_str                | 329 ms                                                                | 262 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.49 us: 1.25x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 465 ms: 1.17x faster                                                    |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.03 sec: 1.16x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                   |
| sympy_expand             | 543 ms                                                                | 469 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.00 sec: 1.15x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 3.80 ms: 1.12x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 29.1 ms: 1.11x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.95 ms: 1.10x faster                                                   |
| regex_dna                | 257 ms                                                                | 235 ms: 1.10x faster                                                    |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                                   |
| json                     | 5.88 ms                                                               | 5.79 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.0 us: 1.07x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.18 ms: 1.08x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.97 ms: 1.68x slower                                                   |
| logging_silent           | 222 ns                                                                | 639 ns: 2.88x slower                                                    |
| coverage                 | 83.6 ms                                                               | 555 ms: 6.64x slower                                                    |
| thrift                   | 1.26 ms                                                               | 197 ms: 156.27x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (2): pidigits, async_generators
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.225x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.35x