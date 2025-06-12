# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.040x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 312 ms                                                  | 320 ms: 1.03x slower                                                |
| docutils       | 3.09 sec                                                | 3.15 sec: 1.02x slower                                              |
| sphinx         | 1.15 sec                                                | 1.19 sec: 1.03x slower                                              |
| Geometric mean | (ref)                                                   | 1.02x slower                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|---------------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 476 ms                                                  | 482 ms: 1.01x slower                                                |
| async_tree_none           | 400 ms                                                  | 406 ms: 1.01x slower                                                |
| async_tree_none_tg        | 385 ms                                                  | 393 ms: 1.02x slower                                                |
| async_tree_io_tg          | 925 ms                                                  | 945 ms: 1.02x slower                                                |
| async_tree_io             | 897 ms                                                  | 929 ms: 1.04x slower                                                |
| Geometric mean            | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (6): coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 82.8 ms                                                 | 89.6 ms: 1.08x slower                                               |
| nbody          | 119 ms                                                  | 145 ms: 1.22x slower                                                |
| Geometric mean | (ref)                                                   | 1.10x slower                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                  | 224 ms: 1.01x slower                                                |
| regex_compile  | 122 ms                                                  | 125 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 13.9 ms                                                 | 13.3 ms: 1.04x faster                                               |
| xml_etree_process    | 79.2 ms                                                 | 83.0 ms: 1.05x slower                                               |
| pickle_pure_python   | 388 us                                                  | 407 us: 1.05x slower                                                |
| xml_etree_generate   | 110 ms                                                  | 116 ms: 1.05x slower                                                |
| tomli_loads          | 2.37 sec                                                | 2.54 sec: 1.08x slower                                              |
| unpickle_pure_python | 248 us                                                  | 289 us: 1.17x slower                                                |
| Geometric mean       | (ref)                                                   | 1.04x slower                                                        |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 41.7 ms                                                 | 40.0 ms: 1.04x faster                                               |
| mako            | 13.6 ms                                                 | 15.2 ms: 1.12x slower                                               |
| Geometric mean  | (ref)                                                   | 1.01x slower                                                        |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20250610-arminc-aarch64-python-main-3.15.0a0-0f866cb | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|---------------------------|:-------------------------------------------------------:|:-------------------------------------------------------------------:|
| gc_traversal              | 7.06 ms                                                 | 6.75 ms: 1.05x faster                                               |
| django_template           | 41.7 ms                                                 | 40.0 ms: 1.04x faster                                               |
| json_dumps                | 13.9 ms                                                 | 13.3 ms: 1.04x faster                                               |
| regex_dna                 | 223 ms                                                  | 224 ms: 1.01x slower                                                |
| logging_format            | 8.34 us                                                 | 8.41 us: 1.01x slower                                               |
| logging_simple            | 7.57 us                                                 | 7.66 us: 1.01x slower                                               |
| thrift                    | 191 ms                                                  | 193 ms: 1.01x slower                                                |
| async_tree_memoization_tg | 476 ms                                                  | 482 ms: 1.01x slower                                                |
| async_tree_none           | 400 ms                                                  | 406 ms: 1.01x slower                                                |
| mdp                       | 1.68 sec                                                | 1.71 sec: 1.02x slower                                              |
| docutils                  | 3.09 sec                                                | 3.15 sec: 1.02x slower                                              |
| async_tree_none_tg        | 385 ms                                                  | 393 ms: 1.02x slower                                                |
| k_core                    | 2.82 sec                                                | 2.88 sec: 1.02x slower                                              |
| scimark_sparse_mat_mult   | 6.93 ms                                                 | 7.08 ms: 1.02x slower                                               |
| async_tree_io_tg          | 925 ms                                                  | 945 ms: 1.02x slower                                                |
| regex_compile             | 122 ms                                                  | 125 ms: 1.02x slower                                                |
| 2to3                      | 312 ms                                                  | 320 ms: 1.03x slower                                                |
| sphinx                    | 1.15 sec                                                | 1.19 sec: 1.03x slower                                              |
| many_optionals            | 803 us                                                  | 830 us: 1.03x slower                                                |
| pycparser                 | 1.40 sec                                                | 1.44 sec: 1.03x slower                                              |
| sympy_expand              | 490 ms                                                  | 507 ms: 1.03x slower                                                |
| async_tree_io             | 897 ms                                                  | 929 ms: 1.04x slower                                                |
| sqlite_synth              | 3.71 us                                                 | 3.87 us: 1.04x slower                                               |
| scimark_monte_carlo       | 82.9 ms                                                 | 86.5 ms: 1.04x slower                                               |
| coverage                  | 554 ms                                                  | 578 ms: 1.04x slower                                                |
| xml_etree_process         | 79.2 ms                                                 | 83.0 ms: 1.05x slower                                               |
| pickle_pure_python        | 388 us                                                  | 407 us: 1.05x slower                                                |
| xml_etree_generate        | 110 ms                                                  | 116 ms: 1.05x slower                                                |
| nqueens                   | 101 ms                                                  | 107 ms: 1.05x slower                                                |
| dulwich_log               | 55.8 ms                                                 | 59.1 ms: 1.06x slower                                               |
| sqlglot_v2_transpile      | 1.87 ms                                                 | 1.98 ms: 1.06x slower                                               |
| pyflate                   | 549 ms                                                  | 587 ms: 1.07x slower                                                |
| tomli_loads               | 2.37 sec                                                | 2.54 sec: 1.08x slower                                              |
| bpe_tokeniser             | 5.45 sec                                                | 5.88 sec: 1.08x slower                                              |
| telco                     | 9.45 ms                                                 | 10.2 ms: 1.08x slower                                               |
| float                     | 82.8 ms                                                 | 89.6 ms: 1.08x slower                                               |
| sqlglot_v2_parse          | 1.54 ms                                                 | 1.69 ms: 1.09x slower                                               |
| scimark_fft               | 424 ms                                                  | 464 ms: 1.09x slower                                                |
| richards_super            | 51.1 ms                                                 | 56.2 ms: 1.10x slower                                               |
| crypto_pyaes              | 92.8 ms                                                 | 103 ms: 1.10x slower                                                |
| comprehensions            | 22.7 us                                                 | 25.1 us: 1.11x slower                                               |
| meteor_contest            | 116 ms                                                  | 129 ms: 1.11x slower                                                |
| mako                      | 13.6 ms                                                 | 15.2 ms: 1.12x slower                                               |
| spectral_norm             | 134 ms                                                  | 152 ms: 1.14x slower                                                |
| richards                  | 44.7 ms                                                 | 51.7 ms: 1.16x slower                                               |
| deltablue                 | 3.97 ms                                                 | 4.59 ms: 1.16x slower                                               |
| unpickle_pure_python      | 248 us                                                  | 289 us: 1.17x slower                                                |
| hexiom                    | 7.49 ms                                                 | 8.98 ms: 1.20x slower                                               |
| fannkuch                  | 483 ms                                                  | 582 ms: 1.21x slower                                                |
| nbody                     | 119 ms                                                  | 145 ms: 1.22x slower                                                |
| go                        | 159 ms                                                  | 195 ms: 1.23x slower                                                |
| pprint_safe_repr          | 1.25 sec                                                | 1.55 sec: 1.24x slower                                              |
| pprint_pformat            | 2.58 sec                                                | 3.30 sec: 1.28x slower                                              |
| Geometric mean            | (ref)                                                   | 1.04x slower                                                        |

Benchmark hidden because not significant (39): regex_effbot, deepcopy, deepcopy_memo, sympy_sum, json_loads, sympy_str, html5lib, scimark_lu, sqlglot_v2_normalize, pathlib, genshi_text, generators, genshi_xml, create_gc_cycles, json, coroutines, async_tree_cpu_io_mixed_tg, python_startup_no_site, xml_etree_iterparse, shortest_path, xml_etree_parse, python_startup, pidigits, scimark_sor, async_tree_memoization, asyncio_websockets, connected_components, chaos, async_tree_cpu_io_mixed, deepcopy_reduce, logging_silent, pylint, async_generators, raytrace, sympy_integrate, subparsers, regex_v8, sqlglot_v2_optimize, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.040x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x