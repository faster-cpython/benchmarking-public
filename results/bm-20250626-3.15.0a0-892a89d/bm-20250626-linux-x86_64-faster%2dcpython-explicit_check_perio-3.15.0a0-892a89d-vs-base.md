# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.002x slower
- HPT reliability: 92.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| docutils       | 2.57 sec                                                              | 2.58 sec: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines             | 25.0 ms                                                               | 24.5 ms: 1.02x faster                                                           |
| async_tree_memoization | 311 ms                                                                | 315 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io, async_generators, async_tree_none_tg, async_tree_none, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 100 ms                                                                | 97.0 ms: 1.03x faster                                                           |
| pidigits       | 188 ms                                                                | 196 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps      | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| json_loads      | 28.5 us                                                               | 28.2 us: 1.01x faster                                                           |
| xml_etree_parse | 141 ms                                                                | 145 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, unpickle_pure_python, pickle_pure_python, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.90 ms                                                               | 6.93 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| genshi_text     | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                           |
| genshi_xml      | 49.2 ms                                                               | 50.1 ms: 1.02x slower                                                           |
| django_template | 32.1 ms                                                               | 33.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250626-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_lu              | 118 ms                                                                | 114 ms: 1.03x faster                                                            |
| nbody                   | 100 ms                                                                | 97.0 ms: 1.03x faster                                                           |
| coroutines              | 25.0 ms                                                               | 24.5 ms: 1.02x faster                                                           |
| pathlib                 | 17.4 ms                                                               | 17.0 ms: 1.02x faster                                                           |
| shortest_path           | 509 ms                                                                | 500 ms: 1.02x faster                                                            |
| connected_components    | 474 ms                                                                | 468 ms: 1.01x faster                                                            |
| sqlglot_v2_normalize    | 106 ms                                                                | 105 ms: 1.01x faster                                                            |
| scimark_fft             | 363 ms                                                                | 359 ms: 1.01x faster                                                            |
| json_dumps              | 11.1 ms                                                               | 11.0 ms: 1.01x faster                                                           |
| deltablue               | 3.51 ms                                                               | 3.47 ms: 1.01x faster                                                           |
| json                    | 5.32 ms                                                               | 5.27 ms: 1.01x faster                                                           |
| json_loads              | 28.5 us                                                               | 28.2 us: 1.01x faster                                                           |
| pprint_safe_repr        | 805 ms                                                                | 798 ms: 1.01x faster                                                            |
| sqlglot_v2_optimize     | 52.5 ms                                                               | 52.1 ms: 1.01x faster                                                           |
| scimark_sor             | 118 ms                                                                | 117 ms: 1.01x faster                                                            |
| fannkuch                | 408 ms                                                                | 404 ms: 1.01x faster                                                            |
| hexiom                  | 6.16 ms                                                               | 6.11 ms: 1.01x faster                                                           |
| raytrace                | 270 ms                                                                | 268 ms: 1.01x faster                                                            |
| sympy_sum               | 149 ms                                                                | 148 ms: 1.01x faster                                                            |
| meteor_contest          | 106 ms                                                                | 106 ms: 1.01x faster                                                            |
| crypto_pyaes            | 75.8 ms                                                               | 75.4 ms: 1.00x faster                                                           |
| go                      | 110 ms                                                                | 110 ms: 1.00x faster                                                            |
| mako                    | 11.3 ms                                                               | 11.3 ms: 1.00x faster                                                           |
| python_startup          | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| docutils                | 2.57 sec                                                              | 2.58 sec: 1.00x slower                                                          |
| sympy_integrate         | 18.9 ms                                                               | 19.0 ms: 1.00x slower                                                           |
| mdp                     | 1.22 sec                                                              | 1.22 sec: 1.00x slower                                                          |
| scimark_monte_carlo     | 66.9 ms                                                               | 67.2 ms: 1.00x slower                                                           |
| richards_super          | 49.3 ms                                                               | 49.5 ms: 1.00x slower                                                           |
| python_startup_no_site  | 6.90 ms                                                               | 6.93 ms: 1.00x slower                                                           |
| create_gc_cycles        | 2.57 ms                                                               | 2.59 ms: 1.00x slower                                                           |
| comprehensions          | 16.1 us                                                               | 16.1 us: 1.01x slower                                                           |
| 2to3                    | 254 ms                                                                | 256 ms: 1.01x slower                                                            |
| chaos                   | 59.6 ms                                                               | 60.0 ms: 1.01x slower                                                           |
| regex_v8                | 23.0 ms                                                               | 23.2 ms: 1.01x slower                                                           |
| nqueens                 | 81.1 ms                                                               | 81.8 ms: 1.01x slower                                                           |
| coverage                | 86.9 ms                                                               | 87.6 ms: 1.01x slower                                                           |
| many_optionals          | 957 us                                                                | 964 us: 1.01x slower                                                            |
| deepcopy_reduce         | 2.70 us                                                               | 2.72 us: 1.01x slower                                                           |
| richards                | 43.1 ms                                                               | 43.6 ms: 1.01x slower                                                           |
| genshi_text             | 21.3 ms                                                               | 21.5 ms: 1.01x slower                                                           |
| deepcopy                | 255 us                                                                | 258 us: 1.01x slower                                                            |
| pycparser               | 1.16 sec                                                              | 1.17 sec: 1.01x slower                                                          |
| async_tree_memoization  | 311 ms                                                                | 315 ms: 1.01x slower                                                            |
| subparsers              | 23.3 ms                                                               | 23.7 ms: 1.01x slower                                                           |
| telco                   | 7.93 ms                                                               | 8.04 ms: 1.01x slower                                                           |
| pyflate                 | 422 ms                                                                | 428 ms: 1.01x slower                                                            |
| generators              | 29.8 ms                                                               | 30.4 ms: 1.02x slower                                                           |
| genshi_xml              | 49.2 ms                                                               | 50.1 ms: 1.02x slower                                                           |
| logging_simple          | 6.15 us                                                               | 6.27 us: 1.02x slower                                                           |
| deepcopy_memo           | 29.1 us                                                               | 29.8 us: 1.02x slower                                                           |
| logging_silent          | 471 ns                                                                | 481 ns: 1.02x slower                                                            |
| xml_etree_parse         | 141 ms                                                                | 145 ms: 1.02x slower                                                            |
| logging_format          | 6.85 us                                                               | 7.06 us: 1.03x slower                                                           |
| thrift                  | 763 us                                                                | 785 us: 1.03x slower                                                            |
| django_template         | 32.1 ms                                                               | 33.1 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult | 4.90 ms                                                               | 5.08 ms: 1.04x slower                                                           |
| pidigits                | 188 ms                                                                | 196 ms: 1.04x slower                                                            |
| gc_traversal            | 4.85 ms                                                               | 5.13 ms: 1.06x slower                                                           |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (34): async_tree_cpu_io_mixed_tg, typing_runtime_protocols, xml_etree_generate, sqlite_synth, async_tree_cpu_io_mixed, bpe_tokeniser, asyncio_websockets, dulwich_log, xml_etree_process, regex_compile, sqlglot_v2_transpile, sqlglot_v2_parse, regex_dna, sphinx, regex_effbot, sympy_expand, async_tree_io, pprint_pformat, unpickle_pure_python, k_core, async_generators, pickle_pure_python, pylint, sympy_str, async_tree_none_tg, html5lib, async_tree_none, tomli_loads, float, xml_etree_iterparse, spectral_norm, async_tree_memoization_tg, async_tree_io_tg, djangocms

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 92.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x