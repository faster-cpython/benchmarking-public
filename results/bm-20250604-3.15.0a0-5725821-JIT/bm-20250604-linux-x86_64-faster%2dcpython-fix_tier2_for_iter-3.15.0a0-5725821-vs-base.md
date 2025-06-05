# Results vs. base

- fork: faster-cpython
- ref: fix_tier2_for_iter
- machine: linux-x86_64
- commit hash: 5725821
- commit date: 2025-06-04
- overall geometric mean: 1.273x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 638 ms                                                                | 617 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 497 ms                                                                | 488 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 506 ms                                                                | 498 ms: 1.02x faster                                                          |
| async_generators           | 430 ms                                                                | 427 ms: 1.01x faster                                                          |
| async_tree_io              | 598 ms                                                                | 603 ms: 1.01x slower                                                          |
| coroutines                 | 25.5 ms                                                               | 26.0 ms: 1.02x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_none, asyncio_websockets, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 187 ms: 1.02x faster                                                          |
| nbody          | 91.8 ms                                                               | 90.2 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.24 ms                                                               | 3.27 ms: 1.01x slower                                                         |
| regex_dna      | 197 ms                                                                | 207 ms: 1.05x slower                                                          |
| regex_v8       | 22.1 ms                                                               | 23.3 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads         | 1.89 sec                                                              | 1.91 sec: 1.01x slower                                                        |
| xml_etree_iterparse | 97.4 ms                                                               | 98.7 ms: 1.01x slower                                                         |
| xml_etree_generate  | 80.1 ms                                                               | 82.0 ms: 1.02x slower                                                         |
| json_loads          | 27.8 us                                                               | 28.5 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_process, json_dumps, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                         |
| python_startup_no_site | 6.98 ms                                                               | 6.98 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                         |
| genshi_xml      | 49.2 ms                                                               | 49.9 ms: 1.01x slower                                                         |
| django_template | 32.3 ms                                                               | 33.1 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 | bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 638 ms                                                                | 617 ms: 1.03x faster                                                          |
| telco                      | 7.88 ms                                                               | 7.70 ms: 1.02x faster                                                         |
| pidigits                   | 191 ms                                                                | 187 ms: 1.02x faster                                                          |
| fannkuch                   | 421 ms                                                                | 413 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 497 ms                                                                | 488 ms: 1.02x faster                                                          |
| nbody                      | 91.8 ms                                                               | 90.2 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 506 ms                                                                | 498 ms: 1.02x faster                                                          |
| mako                       | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 170 us                                                                | 168 us: 1.01x faster                                                          |
| pyflate                    | 413 ms                                                                | 410 ms: 1.01x faster                                                          |
| async_generators           | 430 ms                                                                | 427 ms: 1.01x faster                                                          |
| crypto_pyaes               | 76.3 ms                                                               | 75.9 ms: 1.01x faster                                                         |
| python_startup             | 12.2 ms                                                               | 12.2 ms: 1.00x faster                                                         |
| python_startup_no_site     | 6.98 ms                                                               | 6.98 ms: 1.00x faster                                                         |
| thrift                     | 148 ms                                                                | 148 ms: 1.00x slower                                                          |
| sqlglot_v2_transpile       | 1.58 ms                                                               | 1.59 ms: 1.00x slower                                                         |
| sympy_integrate            | 19.4 ms                                                               | 19.5 ms: 1.00x slower                                                         |
| dulwich_log                | 60.9 ms                                                               | 61.2 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.57 ms                                                               | 2.58 ms: 1.01x slower                                                         |
| many_optionals             | 973 us                                                                | 979 us: 1.01x slower                                                          |
| sqlglot_v2_parse           | 1.27 ms                                                               | 1.27 ms: 1.01x slower                                                         |
| shortest_path              | 494 ms                                                                | 497 ms: 1.01x slower                                                          |
| go                         | 123 ms                                                                | 123 ms: 1.01x slower                                                          |
| logging_silent             | 471 ns                                                                | 474 ns: 1.01x slower                                                          |
| meteor_contest             | 106 ms                                                                | 107 ms: 1.01x slower                                                          |
| sympy_str                  | 271 ms                                                                | 273 ms: 1.01x slower                                                          |
| scimark_fft                | 332 ms                                                                | 334 ms: 1.01x slower                                                          |
| docutils                   | 2.64 sec                                                              | 2.66 sec: 1.01x slower                                                        |
| regex_effbot               | 3.24 ms                                                               | 3.27 ms: 1.01x slower                                                         |
| logging_simple             | 6.09 us                                                               | 6.13 us: 1.01x slower                                                         |
| connected_components       | 453 ms                                                                | 457 ms: 1.01x slower                                                          |
| async_tree_io              | 598 ms                                                                | 603 ms: 1.01x slower                                                          |
| comprehensions             | 17.0 us                                                               | 17.1 us: 1.01x slower                                                         |
| tomli_loads                | 1.89 sec                                                              | 1.91 sec: 1.01x slower                                                        |
| sympy_expand               | 463 ms                                                                | 468 ms: 1.01x slower                                                          |
| generators                 | 30.0 ms                                                               | 30.3 ms: 1.01x slower                                                         |
| deepcopy_memo              | 29.6 us                                                               | 29.9 us: 1.01x slower                                                         |
| raytrace                   | 272 ms                                                                | 275 ms: 1.01x slower                                                          |
| bpe_tokeniser              | 4.37 sec                                                              | 4.42 sec: 1.01x slower                                                        |
| sqlglot_v2_optimize        | 52.1 ms                                                               | 52.8 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 97.4 ms                                                               | 98.7 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.80 us                                                               | 2.84 us: 1.01x slower                                                         |
| nqueens                    | 83.2 ms                                                               | 84.3 ms: 1.01x slower                                                         |
| genshi_xml                 | 49.2 ms                                                               | 49.9 ms: 1.01x slower                                                         |
| sympy_sum                  | 149 ms                                                                | 151 ms: 1.01x slower                                                          |
| richards_super             | 39.4 ms                                                               | 40.0 ms: 1.02x slower                                                         |
| pathlib                    | 16.9 ms                                                               | 17.2 ms: 1.02x slower                                                         |
| richards                   | 33.4 ms                                                               | 34.0 ms: 1.02x slower                                                         |
| coroutines                 | 25.5 ms                                                               | 26.0 ms: 1.02x slower                                                         |
| json                       | 5.10 ms                                                               | 5.21 ms: 1.02x slower                                                         |
| deltablue                  | 3.06 ms                                                               | 3.12 ms: 1.02x slower                                                         |
| xml_etree_generate         | 80.1 ms                                                               | 82.0 ms: 1.02x slower                                                         |
| mdp                        | 1.23 sec                                                              | 1.26 sec: 1.02x slower                                                        |
| json_loads                 | 27.8 us                                                               | 28.5 us: 1.02x slower                                                         |
| django_template            | 32.3 ms                                                               | 33.1 ms: 1.03x slower                                                         |
| scimark_lu                 | 116 ms                                                                | 119 ms: 1.03x slower                                                          |
| deepcopy                   | 253 us                                                                | 260 us: 1.03x slower                                                          |
| gc_traversal               | 4.91 ms                                                               | 5.08 ms: 1.03x slower                                                         |
| deepcopy_reduce            | 2.65 us                                                               | 2.74 us: 1.03x slower                                                         |
| coverage                   | 422 ms                                                                | 436 ms: 1.03x slower                                                          |
| spectral_norm              | 100 ms                                                                | 104 ms: 1.04x slower                                                          |
| pycparser                  | 1.11 sec                                                              | 1.16 sec: 1.04x slower                                                        |
| regex_dna                  | 197 ms                                                                | 207 ms: 1.05x slower                                                          |
| regex_v8                   | 22.1 ms                                                               | 23.3 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 829 ns                                                                | 818 ms: 986809.55x slower                                                     |
| pprint_pformat             | 1.45 us                                                               | 1.70 sec: 1172537.02x slower                                                  |
| Geometric mean             | (ref)                                                                 | 1.37x slower                                                                  |

Benchmark hidden because not significant (25): async_tree_none_tg, float, async_tree_none, scimark_sparse_mat_mult, hexiom, unpickle_pure_python, xml_etree_process, json_dumps, asyncio_websockets, subparsers, 2to3, scimark_monte_carlo, async_tree_memoization, chaos, genshi_text, async_tree_memoization_tg, pickle_pure_python, scimark_sor, html5lib, pylint, sqlglot_v2_normalize, xml_etree_parse, logging_format, k_core, sphinx
Ignored benchmarks (1) of results/bm-20250604-3.15.0a0-5725821-JIT/bm-20250604-linux-x86_64-faster%2dcpython-fix_tier2_for_iter-3.15.0a0-5725821.json: regex_compile

- Geometric mean (including insignificant results): 1.273x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x