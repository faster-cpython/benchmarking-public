# Results vs. base

- fork: kumaraditya303
- ref: freelist_async
- machine: linux-x86_64
- commit hash: cfae815
- commit date: 2025-04-03
- overall geometric mean: 1.003x faster
- HPT reliability: 98.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 249 ms                                                                 | 247 ms: 1.01x faster                                                     |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                   |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_generators           | 391 ms                                                                 | 394 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 479 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 485 ms: 1.01x slower                                                     |
| async_tree_io              | 613 ms                                                                 | 621 ms: 1.01x slower                                                     |
| coroutines                 | 23.0 ms                                                                | 23.8 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization, asyncio_websockets, async_tree_none_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 70.2 ms                                                                | 67.0 ms: 1.05x faster                                                    |
| nbody          | 91.3 ms                                                                | 90.1 ms: 1.01x faster                                                    |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                                    |
| regex_compile  | 124 ms                                                                 | 123 ms: 1.01x faster                                                     |
| regex_dna      | 214 ms                                                                 | 219 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.94 sec                                                               | 1.90 sec: 1.02x faster                                                   |
| unpickle_pure_python | 217 us                                                                 | 215 us: 1.01x faster                                                     |
| xml_etree_process    | 58.9 ms                                                                | 58.5 ms: 1.01x faster                                                    |
| pickle_pure_python   | 313 us                                                                 | 311 us: 1.01x faster                                                     |
| xml_etree_generate   | 83.8 ms                                                                | 84.1 ms: 1.00x slower                                                    |
| json_loads           | 29.8 us                                                                | 30.0 us: 1.01x slower                                                    |
| json_dumps           | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.17 ms                                                                | 8.17 ms: 1.00x faster                                                    |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|-----------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 21.2 ms                                                                | 21.4 ms: 1.01x slower                                                    |
| django_template | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                    |
| genshi_xml      | 48.7 ms                                                                | 49.5 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250403-linux-x86_64-kumaraditya303-freelist_async-3.14.0a6+-cfae815 |
|----------------------------|:----------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float                      | 70.2 ms                                                                | 67.0 ms: 1.05x faster                                                    |
| generators                 | 29.9 ms                                                                | 28.7 ms: 1.04x faster                                                    |
| regex_v8                   | 24.0 ms                                                                | 23.1 ms: 1.04x faster                                                    |
| scimark_monte_carlo        | 66.2 ms                                                                | 63.9 ms: 1.04x faster                                                    |
| go                         | 111 ms                                                                 | 108 ms: 1.03x faster                                                     |
| deepcopy_reduce            | 2.76 us                                                                | 2.69 us: 1.02x faster                                                    |
| logging_silent             | 94.4 ns                                                                | 92.2 ns: 1.02x faster                                                    |
| pyflate                    | 445 ms                                                                 | 435 ms: 1.02x faster                                                     |
| deltablue                  | 3.31 ms                                                                | 3.24 ms: 1.02x faster                                                    |
| richards_super             | 49.3 ms                                                                | 48.3 ms: 1.02x faster                                                    |
| tomli_loads                | 1.94 sec                                                               | 1.90 sec: 1.02x faster                                                   |
| richards                   | 43.0 ms                                                                | 42.3 ms: 1.02x faster                                                    |
| deepcopy_memo              | 29.3 us                                                                | 28.9 us: 1.02x faster                                                    |
| sqlglot_v2_parse           | 1.24 ms                                                                | 1.22 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.48 sec                                                               | 1.45 sec: 1.02x faster                                                   |
| comprehensions             | 16.9 us                                                                | 16.6 us: 1.02x faster                                                    |
| pprint_safe_repr           | 724 ms                                                                 | 713 ms: 1.02x faster                                                     |
| sqlglot_v2_transpile       | 1.56 ms                                                                | 1.53 ms: 1.01x faster                                                    |
| gc_traversal               | 5.02 ms                                                                | 4.95 ms: 1.01x faster                                                    |
| raytrace                   | 258 ms                                                                 | 254 ms: 1.01x faster                                                     |
| nbody                      | 91.3 ms                                                                | 90.1 ms: 1.01x faster                                                    |
| nqueens                    | 81.7 ms                                                                | 80.7 ms: 1.01x faster                                                    |
| connected_components       | 453 ms                                                                 | 448 ms: 1.01x faster                                                     |
| regex_compile              | 124 ms                                                                 | 123 ms: 1.01x faster                                                     |
| dulwich_log                | 59.5 ms                                                                | 59.0 ms: 1.01x faster                                                    |
| unpickle_pure_python       | 217 us                                                                 | 215 us: 1.01x faster                                                     |
| json                       | 5.33 ms                                                                | 5.29 ms: 1.01x faster                                                    |
| xml_etree_process          | 58.9 ms                                                                | 58.5 ms: 1.01x faster                                                    |
| deepcopy                   | 253 us                                                                 | 252 us: 1.01x faster                                                     |
| pickle_pure_python         | 313 us                                                                 | 311 us: 1.01x faster                                                     |
| 2to3                       | 249 ms                                                                 | 247 ms: 1.01x faster                                                     |
| chaos                      | 56.5 ms                                                                | 56.2 ms: 1.00x faster                                                    |
| create_gc_cycles           | 2.46 ms                                                                | 2.45 ms: 1.00x faster                                                    |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                   |
| many_optionals             | 933 us                                                                 | 929 us: 1.00x faster                                                     |
| mdp                        | 1.22 sec                                                               | 1.22 sec: 1.00x faster                                                   |
| bench_thread_pool          | 877 us                                                                 | 875 us: 1.00x faster                                                     |
| python_startup_no_site     | 8.17 ms                                                                | 8.17 ms: 1.00x faster                                                    |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x slower                                                     |
| xml_etree_generate         | 83.8 ms                                                                | 84.1 ms: 1.00x slower                                                    |
| bpe_tokeniser              | 4.51 sec                                                               | 4.53 sec: 1.01x slower                                                   |
| async_generators           | 391 ms                                                                 | 394 ms: 1.01x slower                                                     |
| scimark_sor                | 115 ms                                                                 | 115 ms: 1.01x slower                                                     |
| genshi_text                | 21.2 ms                                                                | 21.4 ms: 1.01x slower                                                    |
| hexiom                     | 6.14 ms                                                                | 6.19 ms: 1.01x slower                                                    |
| json_loads                 | 29.8 us                                                                | 30.0 us: 1.01x slower                                                    |
| sqlalchemy_imperative      | 16.9 ms                                                                | 17.0 ms: 1.01x slower                                                    |
| async_tree_cpu_io_mixed_tg | 474 ms                                                                 | 479 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed    | 480 ms                                                                 | 485 ms: 1.01x slower                                                     |
| async_tree_io              | 613 ms                                                                 | 621 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 4.64 ms                                                                | 4.70 ms: 1.01x slower                                                    |
| coverage                   | 84.4 ms                                                                | 85.5 ms: 1.01x slower                                                    |
| django_template            | 32.0 ms                                                                | 32.4 ms: 1.01x slower                                                    |
| genshi_xml                 | 48.7 ms                                                                | 49.5 ms: 1.02x slower                                                    |
| pathlib                    | 16.5 ms                                                                | 16.7 ms: 1.02x slower                                                    |
| regex_dna                  | 214 ms                                                                 | 219 ms: 1.02x slower                                                     |
| json_dumps                 | 11.3 ms                                                                | 11.5 ms: 1.02x slower                                                    |
| spectral_norm              | 101 ms                                                                 | 104 ms: 1.03x slower                                                     |
| pycparser                  | 1.12 sec                                                               | 1.16 sec: 1.03x slower                                                   |
| coroutines                 | 23.0 ms                                                                | 23.8 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (35): async_tree_io_tg, logging_format, regex_effbot, xml_etree_iterparse, html5lib, k_core, shortest_path, async_tree_memoization, fannkuch, typing_runtime_protocols, telco, sphinx, sympy_expand, sympy_str, asyncio_websockets, sympy_sum, logging_simple, async_tree_none_tg, sqlglot_v2_optimize, python_startup, sqlalchemy_declarative, meteor_contest, xml_etree_parse, sqlglot_v2_normalize, mako, sympy_integrate, scimark_fft, async_tree_memoization_tg, crypto_pyaes, subparsers, bench_mp_pool, pylint, sqlite_synth, scimark_lu, async_tree_none

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 98.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x