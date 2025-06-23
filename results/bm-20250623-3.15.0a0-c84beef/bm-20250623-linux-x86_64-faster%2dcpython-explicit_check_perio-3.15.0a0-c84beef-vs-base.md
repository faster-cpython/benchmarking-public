# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.003x faster
- HPT reliability: 57.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 255 ms: 1.01x faster                                                            |
| docutils       | 2.57 sec                                                              | 2.59 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 25.9 ms                                                               | 24.4 ms: 1.06x faster                                                           |
| async_generators           | 415 ms                                                                | 410 ms: 1.01x faster                                                            |
| async_tree_memoization     | 311 ms                                                                | 316 ms: 1.01x slower                                                            |
| async_tree_none_tg         | 249 ms                                                                | 253 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 625 ms                                                                | 638 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 310 ms                                                                | 316 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 492 ms                                                                | 508 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                | 501 ms: 1.04x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 101 ms                                                                | 95.5 ms: 1.06x faster                                                           |
| float          | 73.2 ms                                                               | 72.5 ms: 1.01x faster                                                           |
| pidigits       | 188 ms                                                                | 193 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 210 ms                                                                | 210 ms: 1.00x slower                                                            |
| regex_effbot   | 3.31 ms                                                               | 3.33 ms: 1.01x slower                                                           |
| regex_v8       | 23.1 ms                                                               | 23.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python | 323 us                                                                | 321 us: 1.01x faster                                                            |
| xml_etree_process  | 60.4 ms                                                               | 60.0 ms: 1.01x faster                                                           |
| json_loads         | 28.1 us                                                               | 28.3 us: 1.01x slower                                                           |
| tomli_loads        | 1.99 sec                                                              | 2.00 sec: 1.01x slower                                                          |
| xml_etree_parse    | 141 ms                                                                | 144 ms: 1.02x slower                                                            |
| json_dumps         | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                               | 6.95 ms: 1.00x slower                                                           |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                           |
| genshi_xml      | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                                           |
| django_template | 32.9 ms                                                               | 32.4 ms: 1.01x faster                                                           |
| mako            | 11.1 ms                                                               | 11.5 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 25.9 ms                                                               | 24.4 ms: 1.06x faster                                                           |
| nbody                      | 101 ms                                                                | 95.5 ms: 1.06x faster                                                           |
| scimark_sor                | 120 ms                                                                | 115 ms: 1.04x faster                                                            |
| deltablue                  | 3.59 ms                                                               | 3.45 ms: 1.04x faster                                                           |
| richards_super             | 50.5 ms                                                               | 48.8 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 68.0 ms                                                               | 65.7 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult    | 5.17 ms                                                               | 5.04 ms: 1.03x faster                                                           |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.24 ms: 1.03x faster                                                           |
| go                         | 114 ms                                                                | 111 ms: 1.03x faster                                                            |
| scimark_lu                 | 121 ms                                                                | 118 ms: 1.03x faster                                                            |
| scimark_fft                | 369 ms                                                                | 361 ms: 1.02x faster                                                            |
| spectral_norm              | 103 ms                                                                | 101 ms: 1.02x faster                                                            |
| richards                   | 44.0 ms                                                               | 43.2 ms: 1.02x faster                                                           |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.55 ms: 1.02x faster                                                           |
| genshi_text                | 21.6 ms                                                               | 21.2 ms: 1.02x faster                                                           |
| fannkuch                   | 416 ms                                                                | 408 ms: 1.02x faster                                                            |
| meteor_contest             | 107 ms                                                                | 105 ms: 1.02x faster                                                            |
| chaos                      | 61.2 ms                                                               | 60.2 ms: 1.02x faster                                                           |
| pyflate                    | 432 ms                                                                | 425 ms: 1.02x faster                                                            |
| raytrace                   | 273 ms                                                                | 268 ms: 1.02x faster                                                            |
| genshi_xml                 | 50.5 ms                                                               | 49.7 ms: 1.02x faster                                                           |
| comprehensions             | 16.3 us                                                               | 16.1 us: 1.02x faster                                                           |
| django_template            | 32.9 ms                                                               | 32.4 ms: 1.01x faster                                                           |
| generators                 | 30.1 ms                                                               | 29.7 ms: 1.01x faster                                                           |
| coverage                   | 88.5 ms                                                               | 87.3 ms: 1.01x faster                                                           |
| async_generators           | 415 ms                                                                | 410 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.66 sec                                                              | 1.65 sec: 1.01x faster                                                          |
| float                      | 73.2 ms                                                               | 72.5 ms: 1.01x faster                                                           |
| hexiom                     | 6.17 ms                                                               | 6.11 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 814 ms                                                                | 807 ms: 1.01x faster                                                            |
| dulwich_log                | 59.4 ms                                                               | 59.0 ms: 1.01x faster                                                           |
| pickle_pure_python         | 323 us                                                                | 321 us: 1.01x faster                                                            |
| telco                      | 7.96 ms                                                               | 7.90 ms: 1.01x faster                                                           |
| 2to3                       | 257 ms                                                                | 255 ms: 1.01x faster                                                            |
| xml_etree_process          | 60.4 ms                                                               | 60.0 ms: 1.01x faster                                                           |
| crypto_pyaes               | 76.1 ms                                                               | 75.7 ms: 1.01x faster                                                           |
| logging_silent             | 473 ns                                                                | 471 ns: 1.00x faster                                                            |
| sqlglot_v2_normalize       | 106 ms                                                                | 106 ms: 1.00x faster                                                            |
| sqlglot_v2_optimize        | 52.8 ms                                                               | 52.7 ms: 1.00x faster                                                           |
| python_startup_no_site     | 6.94 ms                                                               | 6.95 ms: 1.00x slower                                                           |
| regex_dna                  | 210 ms                                                                | 210 ms: 1.00x slower                                                            |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| sympy_integrate            | 19.0 ms                                                               | 19.0 ms: 1.00x slower                                                           |
| mdp                        | 1.22 sec                                                              | 1.23 sec: 1.00x slower                                                          |
| sympy_sum                  | 148 ms                                                                | 149 ms: 1.01x slower                                                            |
| json_loads                 | 28.1 us                                                               | 28.3 us: 1.01x slower                                                           |
| nqueens                    | 80.7 ms                                                               | 81.2 ms: 1.01x slower                                                           |
| regex_effbot               | 3.31 ms                                                               | 3.33 ms: 1.01x slower                                                           |
| sympy_str                  | 266 ms                                                                | 268 ms: 1.01x slower                                                            |
| sympy_expand               | 450 ms                                                                | 453 ms: 1.01x slower                                                            |
| create_gc_cycles           | 2.57 ms                                                               | 2.59 ms: 1.01x slower                                                           |
| shortest_path              | 503 ms                                                                | 507 ms: 1.01x slower                                                            |
| docutils                   | 2.57 sec                                                              | 2.59 sec: 1.01x slower                                                          |
| tomli_loads                | 1.99 sec                                                              | 2.00 sec: 1.01x slower                                                          |
| pathlib                    | 17.3 ms                                                               | 17.4 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 166 us                                                                | 167 us: 1.01x slower                                                            |
| regex_v8                   | 23.1 ms                                                               | 23.5 ms: 1.01x slower                                                           |
| many_optionals             | 953 us                                                                | 966 us: 1.01x slower                                                            |
| async_tree_memoization     | 311 ms                                                                | 316 ms: 1.01x slower                                                            |
| xml_etree_parse            | 141 ms                                                                | 144 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 249 ms                                                                | 253 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 625 ms                                                                | 638 ms: 1.02x slower                                                            |
| async_tree_memoization_tg  | 310 ms                                                                | 316 ms: 1.02x slower                                                            |
| json_dumps                 | 11.0 ms                                                               | 11.2 ms: 1.02x slower                                                           |
| pidigits                   | 188 ms                                                                | 193 ms: 1.02x slower                                                            |
| deepcopy                   | 254 us                                                                | 261 us: 1.03x slower                                                            |
| deepcopy_memo              | 29.4 us                                                               | 30.3 us: 1.03x slower                                                           |
| subparsers                 | 23.3 ms                                                               | 23.9 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 492 ms                                                                | 508 ms: 1.03x slower                                                            |
| mako                       | 11.1 ms                                                               | 11.5 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                | 501 ms: 1.04x slower                                                            |
| gc_traversal               | 4.72 ms                                                               | 5.02 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (21): xml_etree_generate, async_tree_io, unpickle_pure_python, regex_compile, bpe_tokeniser, logging_format, sphinx, xml_etree_iterparse, json, deepcopy_reduce, thrift, asyncio_websockets, k_core, djangocms, sqlite_synth, pylint, html5lib, logging_simple, pycparser, connected_components, async_tree_none

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 57.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x