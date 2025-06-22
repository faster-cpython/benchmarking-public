# Results vs. base

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: be0ebdc
- commit date: 2025-06-20
- overall geometric mean: 1.005x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                                | 259 ms: 1.01x slower                                                            |
| docutils       | 2.60 sec                                                              | 2.61 sec: 1.01x slower                                                          |
| html5lib       | 62.8 ms                                                               | 62.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 25.9 ms                                                               | 24.7 ms: 1.05x faster                                                           |
| async_tree_io              | 608 ms                                                                | 602 ms: 1.01x faster                                                            |
| async_tree_memoization     | 314 ms                                                                | 317 ms: 1.01x slower                                                            |
| async_generators           | 411 ms                                                                | 418 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                | 500 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 495 ms                                                                | 510 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 102 ms                                                                | 100 ms: 1.02x faster                                                            |
| float          | 73.6 ms                                                               | 74.3 ms: 1.01x slower                                                           |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 216 ms: 1.01x faster                                                            |
| regex_effbot   | 3.37 ms                                                               | 3.33 ms: 1.01x faster                                                           |
| regex_v8       | 23.7 ms                                                               | 23.5 ms: 1.01x faster                                                           |
| regex_compile  | 127 ms                                                                | 130 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process   | 60.7 ms                                                               | 60.4 ms: 1.01x faster                                                           |
| xml_etree_iterparse | 98.3 ms                                                               | 99.1 ms: 1.01x slower                                                           |
| xml_etree_generate  | 85.4 ms                                                               | 86.2 ms: 1.01x slower                                                           |
| xml_etree_parse     | 140 ms                                                                | 142 ms: 1.01x slower                                                            |
| json_loads          | 28.4 us                                                               | 28.8 us: 1.01x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): pickle_pure_python, json_dumps, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.92 ms                                                               | 6.95 ms: 1.00x slower                                                           |
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                           |
| genshi_xml      | 50.1 ms                                                               | 51.2 ms: 1.02x slower                                                           |
| genshi_text     | 21.4 ms                                                               | 22.1 ms: 1.03x slower                                                           |
| mako            | 11.3 ms                                                               | 11.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.03x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20250619-linux-x86_64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 | bm-20250620-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-be0ebdc |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 25.9 ms                                                               | 24.7 ms: 1.05x faster                                                           |
| spectral_norm              | 107 ms                                                                | 102 ms: 1.04x faster                                                            |
| pyflate                    | 442 ms                                                                | 431 ms: 1.03x faster                                                            |
| scimark_sor                | 120 ms                                                                | 117 ms: 1.02x faster                                                            |
| nbody                      | 102 ms                                                                | 100 ms: 1.02x faster                                                            |
| scimark_lu                 | 121 ms                                                                | 119 ms: 1.02x faster                                                            |
| regex_dna                  | 219 ms                                                                | 216 ms: 1.01x faster                                                            |
| regex_effbot               | 3.37 ms                                                               | 3.33 ms: 1.01x faster                                                           |
| html5lib                   | 62.8 ms                                                               | 62.1 ms: 1.01x faster                                                           |
| regex_v8                   | 23.7 ms                                                               | 23.5 ms: 1.01x faster                                                           |
| async_tree_io              | 608 ms                                                                | 602 ms: 1.01x faster                                                            |
| scimark_fft                | 372 ms                                                                | 369 ms: 1.01x faster                                                            |
| generators                 | 30.1 ms                                                               | 29.9 ms: 1.01x faster                                                           |
| xml_etree_process          | 60.7 ms                                                               | 60.4 ms: 1.01x faster                                                           |
| comprehensions             | 16.3 us                                                               | 16.2 us: 1.01x faster                                                           |
| create_gc_cycles           | 2.59 ms                                                               | 2.59 ms: 1.00x faster                                                           |
| python_startup_no_site     | 6.92 ms                                                               | 6.95 ms: 1.00x slower                                                           |
| docutils                   | 2.60 sec                                                              | 2.61 sec: 1.01x slower                                                          |
| raytrace                   | 275 ms                                                                | 276 ms: 1.01x slower                                                            |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.01x slower                                                           |
| many_optionals             | 963 us                                                                | 968 us: 1.01x slower                                                            |
| dulwich_log                | 59.1 ms                                                               | 59.5 ms: 1.01x slower                                                           |
| sympy_str                  | 267 ms                                                                | 269 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 98.3 ms                                                               | 99.1 ms: 1.01x slower                                                           |
| 2to3                       | 257 ms                                                                | 259 ms: 1.01x slower                                                            |
| sympy_sum                  | 148 ms                                                                | 149 ms: 1.01x slower                                                            |
| bpe_tokeniser              | 4.53 sec                                                              | 4.57 sec: 1.01x slower                                                          |
| async_tree_memoization     | 314 ms                                                                | 317 ms: 1.01x slower                                                            |
| float                      | 73.6 ms                                                               | 74.3 ms: 1.01x slower                                                           |
| xml_etree_generate         | 85.4 ms                                                               | 86.2 ms: 1.01x slower                                                           |
| pprint_pformat             | 1.64 sec                                                              | 1.66 sec: 1.01x slower                                                          |
| richards_super             | 50.2 ms                                                               | 50.7 ms: 1.01x slower                                                           |
| sympy_integrate            | 19.0 ms                                                               | 19.2 ms: 1.01x slower                                                           |
| xml_etree_parse            | 140 ms                                                                | 142 ms: 1.01x slower                                                            |
| django_template            | 32.3 ms                                                               | 32.6 ms: 1.01x slower                                                           |
| telco                      | 7.94 ms                                                               | 8.02 ms: 1.01x slower                                                           |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                            |
| thrift                     | 771 us                                                                | 780 us: 1.01x slower                                                            |
| json                       | 5.28 ms                                                               | 5.34 ms: 1.01x slower                                                           |
| sympy_expand               | 452 ms                                                                | 457 ms: 1.01x slower                                                            |
| nqueens                    | 81.0 ms                                                               | 81.9 ms: 1.01x slower                                                           |
| json_loads                 | 28.4 us                                                               | 28.8 us: 1.01x slower                                                           |
| logging_silent             | 474 ns                                                                | 481 ns: 1.01x slower                                                            |
| sqlglot_v2_normalize       | 106 ms                                                                | 108 ms: 1.01x slower                                                            |
| async_generators           | 411 ms                                                                | 418 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 801 ms                                                                | 815 ms: 1.02x slower                                                            |
| gc_traversal               | 4.87 ms                                                               | 4.96 ms: 1.02x slower                                                           |
| deepcopy                   | 255 us                                                                | 260 us: 1.02x slower                                                            |
| richards                   | 43.7 ms                                                               | 44.6 ms: 1.02x slower                                                           |
| genshi_xml                 | 50.1 ms                                                               | 51.2 ms: 1.02x slower                                                           |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                | 500 ms: 1.02x slower                                                            |
| deepcopy_reduce            | 2.69 us                                                               | 2.75 us: 1.02x slower                                                           |
| regex_compile              | 127 ms                                                                | 130 ms: 1.03x slower                                                            |
| hexiom                     | 6.21 ms                                                               | 6.37 ms: 1.03x slower                                                           |
| logging_format             | 6.82 us                                                               | 7.02 us: 1.03x slower                                                           |
| logging_simple             | 6.15 us                                                               | 6.33 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 495 ms                                                                | 510 ms: 1.03x slower                                                            |
| genshi_text                | 21.4 ms                                                               | 22.1 ms: 1.03x slower                                                           |
| shortest_path              | 508 ms                                                                | 524 ms: 1.03x slower                                                            |
| deepcopy_memo              | 29.5 us                                                               | 30.5 us: 1.03x slower                                                           |
| mako                       | 11.3 ms                                                               | 11.8 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult    | 5.12 ms                                                               | 5.37 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (30): scimark_monte_carlo, sphinx, crypto_pyaes, deltablue, subparsers, chaos, sqlglot_v2_parse, go, sqlite_synth, asyncio_websockets, fannkuch, sqlglot_v2_transpile, typing_runtime_protocols, k_core, sqlglot_v2_optimize, async_tree_none_tg, pickle_pure_python, json_dumps, mdp, async_tree_io_tg, async_tree_none, pylint, unpickle_pure_python, tomli_loads, coverage, pathlib, async_tree_memoization_tg, connected_components, pycparser, djangocms

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x