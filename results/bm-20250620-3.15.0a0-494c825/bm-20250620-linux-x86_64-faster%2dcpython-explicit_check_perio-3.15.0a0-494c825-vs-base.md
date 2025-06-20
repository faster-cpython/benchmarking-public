# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: 494c825
- commit date: 2025-06-20
- overall geometric mean: 1.004x slower
- HPT reliability: 94.24%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                | 257 ms: 1.01x slower                                                            |
| docutils       | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                | 25.0 ms                                                               | 24.7 ms: 1.01x faster                                                           |
| async_generators          | 409 ms                                                                | 412 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed   | 497 ms                                                                | 502 ms: 1.01x slower                                                            |
| async_tree_io             | 598 ms                                                                | 604 ms: 1.01x slower                                                            |
| async_tree_memoization_tg | 307 ms                                                                | 314 ms: 1.02x slower                                                            |
| async_tree_none_tg        | 247 ms                                                                | 253 ms: 1.02x slower                                                            |
| async_tree_none           | 260 ms                                                                | 267 ms: 1.02x slower                                                            |
| async_tree_memoization    | 312 ms                                                                | 321 ms: 1.03x slower                                                            |
| Geometric mean            | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 73.3 ms                                                               | 72.3 ms: 1.01x faster                                                           |
| pidigits       | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| nbody          | 96.6 ms                                                               | 99.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 215 ms                                                                | 199 ms: 1.08x faster                                                            |
| regex_effbot   | 3.35 ms                                                               | 3.22 ms: 1.04x faster                                                           |
| regex_compile  | 128 ms                                                                | 130 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 85.7 ms                                                               | 84.8 ms: 1.01x faster                                                           |
| json_loads           | 28.1 us                                                               | 28.3 us: 1.01x slower                                                           |
| pickle_pure_python   | 322 us                                                                | 327 us: 1.02x slower                                                            |
| xml_etree_parse      | 140 ms                                                                | 143 ms: 1.02x slower                                                            |
| json_dumps           | 10.9 ms                                                               | 11.2 ms: 1.02x slower                                                           |
| unpickle_pure_python | 217 us                                                                | 222 us: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_process, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| python_startup_no_site | 6.93 ms                                                               | 6.94 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.8 ms                                                               | 50.0 ms: 1.02x faster                                                           |
| mako            | 11.5 ms                                                               | 11.6 ms: 1.00x slower                                                           |
| genshi_text     | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                                           |
| django_template | 32.1 ms                                                               | 32.8 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-494c825 |
|---------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna                 | 215 ms                                                                | 199 ms: 1.08x faster                                                            |
| regex_effbot              | 3.35 ms                                                               | 3.22 ms: 1.04x faster                                                           |
| scimark_sparse_mat_mult   | 5.22 ms                                                               | 5.09 ms: 1.02x faster                                                           |
| djangocms                 | 22.0 us                                                               | 21.6 us: 1.02x faster                                                           |
| scimark_monte_carlo       | 68.3 ms                                                               | 67.1 ms: 1.02x faster                                                           |
| scimark_lu                | 120 ms                                                                | 118 ms: 1.02x faster                                                            |
| genshi_xml                | 50.8 ms                                                               | 50.0 ms: 1.02x faster                                                           |
| pyflate                   | 433 ms                                                                | 427 ms: 1.01x faster                                                            |
| float                     | 73.3 ms                                                               | 72.3 ms: 1.01x faster                                                           |
| coroutines                | 25.0 ms                                                               | 24.7 ms: 1.01x faster                                                           |
| xml_etree_generate        | 85.7 ms                                                               | 84.8 ms: 1.01x faster                                                           |
| generators                | 29.7 ms                                                               | 29.4 ms: 1.01x faster                                                           |
| pprint_safe_repr          | 819 ms                                                                | 812 ms: 1.01x faster                                                            |
| meteor_contest            | 106 ms                                                                | 106 ms: 1.00x faster                                                            |
| chaos                     | 60.8 ms                                                               | 60.5 ms: 1.00x faster                                                           |
| richards_super            | 49.5 ms                                                               | 49.4 ms: 1.00x faster                                                           |
| pidigits                  | 189 ms                                                                | 189 ms: 1.00x slower                                                            |
| python_startup            | 12.2 ms                                                               | 12.2 ms: 1.00x slower                                                           |
| python_startup_no_site    | 6.93 ms                                                               | 6.94 ms: 1.00x slower                                                           |
| raytrace                  | 272 ms                                                                | 272 ms: 1.00x slower                                                            |
| sqlglot_v2_optimize       | 52.7 ms                                                               | 52.8 ms: 1.00x slower                                                           |
| mako                      | 11.5 ms                                                               | 11.6 ms: 1.00x slower                                                           |
| richards                  | 43.0 ms                                                               | 43.2 ms: 1.00x slower                                                           |
| create_gc_cycles          | 2.58 ms                                                               | 2.59 ms: 1.00x slower                                                           |
| sympy_sum                 | 148 ms                                                                | 149 ms: 1.00x slower                                                            |
| json_loads                | 28.1 us                                                               | 28.3 us: 1.01x slower                                                           |
| fannkuch                  | 414 ms                                                                | 416 ms: 1.01x slower                                                            |
| deepcopy                  | 256 us                                                                | 257 us: 1.01x slower                                                            |
| docutils                  | 2.59 sec                                                              | 2.61 sec: 1.01x slower                                                          |
| crypto_pyaes              | 76.3 ms                                                               | 76.8 ms: 1.01x slower                                                           |
| async_generators          | 409 ms                                                                | 412 ms: 1.01x slower                                                            |
| 2to3                      | 255 ms                                                                | 257 ms: 1.01x slower                                                            |
| sympy_expand              | 453 ms                                                                | 456 ms: 1.01x slower                                                            |
| scimark_fft               | 372 ms                                                                | 374 ms: 1.01x slower                                                            |
| comprehensions            | 15.9 us                                                               | 16.0 us: 1.01x slower                                                           |
| sympy_integrate           | 19.0 ms                                                               | 19.2 ms: 1.01x slower                                                           |
| thrift                    | 773 us                                                                | 779 us: 1.01x slower                                                            |
| sqlglot_v2_parse          | 1.24 ms                                                               | 1.25 ms: 1.01x slower                                                           |
| sqlglot_v2_transpile      | 1.55 ms                                                               | 1.56 ms: 1.01x slower                                                           |
| pathlib                   | 17.0 ms                                                               | 17.2 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed   | 497 ms                                                                | 502 ms: 1.01x slower                                                            |
| async_tree_io             | 598 ms                                                                | 604 ms: 1.01x slower                                                            |
| genshi_text               | 21.4 ms                                                               | 21.6 ms: 1.01x slower                                                           |
| dulwich_log               | 59.3 ms                                                               | 60.0 ms: 1.01x slower                                                           |
| many_optionals            | 957 us                                                                | 969 us: 1.01x slower                                                            |
| sqlglot_v2_normalize      | 106 ms                                                                | 108 ms: 1.01x slower                                                            |
| connected_components      | 476 ms                                                                | 482 ms: 1.01x slower                                                            |
| regex_compile             | 128 ms                                                                | 130 ms: 1.02x slower                                                            |
| logging_silent            | 472 ns                                                                | 480 ns: 1.02x slower                                                            |
| json                      | 5.20 ms                                                               | 5.28 ms: 1.02x slower                                                           |
| pickle_pure_python        | 322 us                                                                | 327 us: 1.02x slower                                                            |
| xml_etree_parse           | 140 ms                                                                | 143 ms: 1.02x slower                                                            |
| shortest_path             | 511 ms                                                                | 521 ms: 1.02x slower                                                            |
| deepcopy_memo             | 29.6 us                                                               | 30.1 us: 1.02x slower                                                           |
| django_template           | 32.1 ms                                                               | 32.8 ms: 1.02x slower                                                           |
| json_dumps                | 10.9 ms                                                               | 11.2 ms: 1.02x slower                                                           |
| async_tree_memoization_tg | 307 ms                                                                | 314 ms: 1.02x slower                                                            |
| async_tree_none_tg        | 247 ms                                                                | 253 ms: 1.02x slower                                                            |
| async_tree_none           | 260 ms                                                                | 267 ms: 1.02x slower                                                            |
| nbody                     | 96.6 ms                                                               | 99.1 ms: 1.03x slower                                                           |
| unpickle_pure_python      | 217 us                                                                | 222 us: 1.03x slower                                                            |
| hexiom                    | 6.04 ms                                                               | 6.22 ms: 1.03x slower                                                           |
| async_tree_memoization    | 312 ms                                                                | 321 ms: 1.03x slower                                                            |
| logging_simple            | 6.15 us                                                               | 6.33 us: 1.03x slower                                                           |
| logging_format            | 6.81 us                                                               | 7.11 us: 1.04x slower                                                           |
| gc_traversal              | 4.78 ms                                                               | 5.17 ms: 1.08x slower                                                           |
| Geometric mean            | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (27): async_tree_io_tg, k_core, pycparser, subparsers, scimark_sor, typing_runtime_protocols, telco, asyncio_websockets, async_tree_cpu_io_mixed_tg, bpe_tokeniser, go, deepcopy_reduce, pprint_pformat, xml_etree_iterparse, mdp, sympy_str, nqueens, xml_etree_process, regex_v8, sqlite_synth, coverage, pylint, deltablue, html5lib, tomli_loads, sphinx, spectral_norm

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 94.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x