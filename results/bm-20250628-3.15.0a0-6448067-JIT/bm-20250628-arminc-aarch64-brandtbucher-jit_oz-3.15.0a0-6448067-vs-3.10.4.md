# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_oz
- machine: linux-aarch64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 315 ms: 1.21x faster                                            |
| docutils       | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                          |
| html5lib       | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                           |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 905 ms: 2.52x faster                                            |
| async_tree_memoization  | 1.13 sec                                                              | 470 ms: 2.41x faster                                            |
| async_tree_none         | 950 ms                                                                | 396 ms: 2.40x faster                                            |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 664 ms: 1.92x faster                                            |
| Geometric mean          | (ref)                                                                 | 2.30x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.4 ms: 1.60x faster                                           |
| nbody          | 166 ms                                                                | 125 ms: 1.32x faster                                            |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                            |
| regex_v8       | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                           |
| regex_dna      | 257 ms                                                                | 220 ms: 1.17x faster                                            |
| regex_effbot   | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                                 | 1.21x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                          |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                            |
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                            |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                           |
| xml_etree_process    | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.19x faster                                            |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                            |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                           |
| python_startup         | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                           |
| mako            | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                           |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                           |
| genshi_xml      | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                           |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.13x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 905 ms: 2.52x faster                                            |
| async_tree_memoization   | 1.13 sec                                                              | 470 ms: 2.41x faster                                            |
| async_tree_none          | 950 ms                                                                | 396 ms: 2.40x faster                                            |
| deltablue                | 8.94 ms                                                               | 3.94 ms: 2.27x faster                                           |
| mdp                      | 3.70 sec                                                              | 1.70 sec: 2.17x faster                                          |
| richards_super           | 107 ms                                                                | 51.9 ms: 2.07x faster                                           |
| richards                 | 91.7 ms                                                               | 44.6 ms: 2.06x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 664 ms: 1.92x faster                                            |
| generators               | 68.1 ms                                                               | 36.2 ms: 1.88x faster                                           |
| chaos                    | 121 ms                                                                | 69.1 ms: 1.75x faster                                           |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.73x faster                                            |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                            |
| raytrace                 | 573 ms                                                                | 338 ms: 1.69x faster                                            |
| deepcopy_memo            | 61.7 us                                                               | 37.2 us: 1.66x faster                                           |
| go                       | 264 ms                                                                | 162 ms: 1.63x faster                                            |
| float                    | 135 ms                                                                | 84.4 ms: 1.60x faster                                           |
| scimark_monte_carlo      | 128 ms                                                                | 83.4 ms: 1.53x faster                                           |
| deepcopy                 | 511 us                                                                | 335 us: 1.53x faster                                            |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                            |
| pylint                   | 485 ms                                                                | 330 ms: 1.47x faster                                            |
| comprehensions           | 33.1 us                                                               | 22.5 us: 1.47x faster                                           |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                            |
| hexiom                   | 10.9 ms                                                               | 7.77 ms: 1.40x faster                                           |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                           |
| pyflate                  | 795 ms                                                                | 569 ms: 1.40x faster                                            |
| spectral_norm            | 186 ms                                                                | 134 ms: 1.40x faster                                            |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                          |
| crypto_pyaes             | 134 ms                                                                | 97.7 ms: 1.37x faster                                           |
| html5lib                 | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                            |
| logging_format           | 10.6 us                                                               | 7.83 us: 1.35x faster                                           |
| django_template          | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                           |
| mako                     | 18.9 ms                                                               | 14.2 ms: 1.33x faster                                           |
| nbody                    | 166 ms                                                                | 125 ms: 1.32x faster                                            |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                            |
| dulwich_log              | 73.5 ms                                                               | 56.2 ms: 1.31x faster                                           |
| thrift                   | 1.26 ms                                                               | 973 us: 1.29x faster                                            |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                           |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                           |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                            |
| sympy_integrate          | 26.5 ms                                                               | 21.6 ms: 1.23x faster                                           |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.75 us: 1.22x faster                                           |
| xml_etree_process        | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                           |
| 2to3                     | 381 ms                                                                | 315 ms: 1.21x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.40 sec: 1.21x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 27.0 ms: 1.19x faster                                           |
| sympy_str                | 329 ms                                                                | 276 ms: 1.19x faster                                            |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.19x faster                                            |
| regex_dna                | 257 ms                                                                | 220 ms: 1.17x faster                                            |
| genshi_xml               | 69.8 ms                                                               | 62.0 ms: 1.13x faster                                           |
| nqueens                  | 117 ms                                                                | 104 ms: 1.12x faster                                            |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                            |
| pathlib                  | 26.3 ms                                                               | 23.6 ms: 1.12x faster                                           |
| docutils                 | 3.53 sec                                                              | 3.16 sec: 1.12x faster                                          |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                            |
| sympy_expand             | 543 ms                                                                | 495 ms: 1.10x faster                                            |
| regex_effbot             | 4.25 ms                                                               | 3.91 ms: 1.09x faster                                           |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                            |
| meteor_contest           | 126 ms                                                                | 120 ms: 1.05x faster                                            |
| sqlite_synth             | 4.12 us                                                               | 3.95 us: 1.04x faster                                           |
| fannkuch                 | 546 ms                                                                | 527 ms: 1.03x faster                                            |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                            |
| async_generators         | 452 ms                                                                | 481 ms: 1.06x slower                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 1.23 sec: 1.07x slower                                          |
| pprint_pformat           | 2.36 sec                                                              | 2.54 sec: 1.08x slower                                          |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                           |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                           |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                           |
| python_startup           | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 6.84 ms: 1.65x slower                                           |
| create_gc_cycles         | 2.26 ms                                                               | 3.78 ms: 1.67x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.30x faster                                                    |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, json, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-arminc-aarch64-brandtbucher-jit_oz-3.15.0a0-6448067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.39x