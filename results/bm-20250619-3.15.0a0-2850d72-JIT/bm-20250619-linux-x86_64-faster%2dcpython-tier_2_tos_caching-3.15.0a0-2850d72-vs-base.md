# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.004x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                                | 260 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_generators           | 430 ms                                                                | 428 ms: 1.00x faster                                                          |
| async_tree_memoization     | 313 ms                                                                | 317 ms: 1.01x slower                                                          |
| async_tree_none            | 261 ms                                                                | 265 ms: 1.01x slower                                                          |
| async_tree_io              | 599 ms                                                                | 607 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                                | 506 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                | 498 ms: 1.03x slower                                                          |
| coroutines                 | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                         |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 93.7 ms                                                               | 82.8 ms: 1.13x faster                                                         |
| float          | 65.6 ms                                                               | 65.0 ms: 1.01x faster                                                         |
| pidigits       | 189 ms                                                                | 193 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 192 ms                                                                | 186 ms: 1.03x faster                                                          |
| regex_effbot   | 3.20 ms                                                               | 3.10 ms: 1.03x faster                                                         |
| regex_compile  | 127 ms                                                                | 127 ms: 1.00x slower                                                          |
| regex_v8       | 22.1 ms                                                               | 22.3 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 97.6 ms                                                               | 98.5 ms: 1.01x slower                                                         |
| json_dumps           | 10.9 ms                                                               | 11.0 ms: 1.01x slower                                                         |
| xml_etree_generate   | 79.9 ms                                                               | 81.1 ms: 1.02x slower                                                         |
| unpickle_pure_python | 201 us                                                                | 205 us: 1.02x slower                                                          |
| tomli_loads          | 1.83 sec                                                              | 1.86 sec: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (4): pickle_pure_python, xml_etree_parse, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 12.1 ms                                                               | 12.2 ms: 1.01x slower                                                         |
| python_startup_no_site | 6.91 ms                                                               | 6.98 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (3): django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250619-linux-x86_64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                      | 93.7 ms                                                               | 82.8 ms: 1.13x faster                                                         |
| regex_dna                  | 192 ms                                                                | 186 ms: 1.03x faster                                                          |
| regex_effbot               | 3.20 ms                                                               | 3.10 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 2.75 us                                                               | 2.69 us: 1.02x faster                                                         |
| pycparser                  | 1.12 sec                                                              | 1.11 sec: 1.01x faster                                                        |
| float                      | 65.6 ms                                                               | 65.0 ms: 1.01x faster                                                         |
| thrift                     | 788 us                                                                | 781 us: 1.01x faster                                                          |
| hexiom                     | 6.47 ms                                                               | 6.41 ms: 1.01x faster                                                         |
| nqueens                    | 82.6 ms                                                               | 82.0 ms: 1.01x faster                                                         |
| async_generators           | 430 ms                                                                | 428 ms: 1.00x faster                                                          |
| mako                       | 10.8 ms                                                               | 10.8 ms: 1.00x faster                                                         |
| regex_compile              | 127 ms                                                                | 127 ms: 1.00x slower                                                          |
| sympy_integrate            | 19.3 ms                                                               | 19.3 ms: 1.00x slower                                                         |
| create_gc_cycles           | 2.58 ms                                                               | 2.59 ms: 1.00x slower                                                         |
| sqlglot_v2_optimize        | 52.7 ms                                                               | 52.8 ms: 1.00x slower                                                         |
| 2to3                       | 259 ms                                                                | 260 ms: 1.00x slower                                                          |
| sympy_expand               | 466 ms                                                                | 468 ms: 1.00x slower                                                          |
| go                         | 121 ms                                                                | 121 ms: 1.00x slower                                                          |
| deltablue                  | 3.12 ms                                                               | 3.14 ms: 1.00x slower                                                         |
| logging_silent             | 474 ns                                                                | 477 ns: 1.01x slower                                                          |
| pathlib                    | 16.9 ms                                                               | 17.0 ms: 1.01x slower                                                         |
| regex_v8                   | 22.1 ms                                                               | 22.3 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.79 us                                                               | 2.81 us: 1.01x slower                                                         |
| xml_etree_iterparse        | 97.6 ms                                                               | 98.5 ms: 1.01x slower                                                         |
| python_startup             | 12.1 ms                                                               | 12.2 ms: 1.01x slower                                                         |
| connected_components       | 460 ms                                                                | 464 ms: 1.01x slower                                                          |
| python_startup_no_site     | 6.91 ms                                                               | 6.98 ms: 1.01x slower                                                         |
| raytrace                   | 271 ms                                                                | 274 ms: 1.01x slower                                                          |
| logging_format             | 6.77 us                                                               | 6.85 us: 1.01x slower                                                         |
| json_dumps                 | 10.9 ms                                                               | 11.0 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 169 us                                                                | 171 us: 1.01x slower                                                          |
| spectral_norm              | 93.6 ms                                                               | 94.7 ms: 1.01x slower                                                         |
| async_tree_memoization     | 313 ms                                                                | 317 ms: 1.01x slower                                                          |
| async_tree_none            | 261 ms                                                                | 265 ms: 1.01x slower                                                          |
| chaos                      | 60.7 ms                                                               | 61.5 ms: 1.01x slower                                                         |
| async_tree_io              | 599 ms                                                                | 607 ms: 1.01x slower                                                          |
| xml_etree_generate         | 79.9 ms                                                               | 81.1 ms: 1.02x slower                                                         |
| deepcopy                   | 258 us                                                                | 262 us: 1.02x slower                                                          |
| crypto_pyaes               | 75.6 ms                                                               | 76.8 ms: 1.02x slower                                                         |
| generators                 | 29.7 ms                                                               | 30.3 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 201 us                                                                | 205 us: 1.02x slower                                                          |
| pidigits                   | 189 ms                                                                | 193 ms: 1.02x slower                                                          |
| tomli_loads                | 1.83 sec                                                              | 1.86 sec: 1.02x slower                                                        |
| telco                      | 7.73 ms                                                               | 7.91 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                                | 506 ms: 1.02x slower                                                          |
| shortest_path              | 495 ms                                                                | 508 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 485 ms                                                                | 498 ms: 1.03x slower                                                          |
| scimark_fft                | 310 ms                                                                | 318 ms: 1.03x slower                                                          |
| deepcopy_memo              | 28.8 us                                                               | 29.5 us: 1.03x slower                                                         |
| coroutines                 | 24.3 ms                                                               | 25.1 ms: 1.03x slower                                                         |
| scimark_sparse_mat_mult    | 4.86 ms                                                               | 5.04 ms: 1.04x slower                                                         |
| pprint_safe_repr           | 819 ms                                                                | 855 ms: 1.04x slower                                                          |
| gc_traversal               | 4.85 ms                                                               | 5.07 ms: 1.04x slower                                                         |
| pprint_pformat             | 1.66 sec                                                              | 1.75 sec: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (39): richards_super, pickle_pure_python, django_template, asyncio_websockets, many_optionals, comprehensions, sympy_str, sqlglot_v2_normalize, subparsers, docutils, xml_etree_parse, dulwich_log, bpe_tokeniser, scimark_monte_carlo, sympy_sum, async_tree_memoization_tg, sqlglot_v2_parse, scimark_sor, json_loads, meteor_contest, sphinx, genshi_xml, coverage, mdp, richards, json, sqlglot_v2_transpile, async_tree_io_tg, pylint, genshi_text, pyflate, fannkuch, logging_simple, scimark_lu, xml_etree_process, async_tree_none_tg, html5lib, k_core, djangocms

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x