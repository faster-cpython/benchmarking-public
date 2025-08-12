# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.000x slower
- HPT reliability: 80.70%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 287 ms: 1.01x slower                                                                |
| docutils       | 2.90 sec                                                                    | 2.91 sec: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators           | 448 ms                                                                      | 442 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 271 ms                                                                      | 268 ms: 1.01x faster                                                                |
| async_tree_io_tg           | 637 ms                                                                      | 630 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                      | 504 ms: 1.01x faster                                                                |
| async_tree_io              | 623 ms                                                                      | 619 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed    | 504 ms                                                                      | 501 ms: 1.01x faster                                                                |
| coroutines                 | 22.5 ms                                                                     | 22.5 ms: 1.00x faster                                                               |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 99.6 ms                                                                     | 86.4 ms: 1.15x faster                                                               |
| float          | 64.2 ms                                                                     | 60.5 ms: 1.06x faster                                                               |
| pidigits       | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.07x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                                     | 23.5 ms: 1.03x faster                                                               |
| regex_dna      | 226 ms                                                                      | 226 ms: 1.00x faster                                                                |
| regex_compile  | 132 ms                                                                      | 134 ms: 1.01x slower                                                                |
| regex_effbot   | 3.60 ms                                                                     | 3.69 ms: 1.02x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_generate   | 80.8 ms                                                                     | 79.5 ms: 1.02x faster                                                               |
| xml_etree_process    | 55.8 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| xml_etree_iterparse  | 97.9 ms                                                                     | 98.2 ms: 1.00x slower                                                               |
| json_loads           | 25.2 us                                                                     | 25.3 us: 1.01x slower                                                               |
| json_dumps           | 10.1 ms                                                                     | 10.2 ms: 1.01x slower                                                               |
| tomli_loads          | 1.90 sec                                                                    | 1.92 sec: 1.01x slower                                                              |
| xml_etree_parse      | 139 ms                                                                      | 140 ms: 1.01x slower                                                                |
| pickle_pure_python   | 327 us                                                                      | 333 us: 1.02x slower                                                                |
| unpickle_pure_python | 193 us                                                                      | 199 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_xml      | 56.9 ms                                                                     | 54.6 ms: 1.04x faster                                                               |
| genshi_text     | 23.3 ms                                                                     | 23.1 ms: 1.01x faster                                                               |
| mako            | 9.72 ms                                                                     | 9.87 ms: 1.01x slower                                                               |
| django_template | 34.7 ms                                                                     | 35.5 ms: 1.02x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20250809-pythonperf2-x86_64-python-af15e1d13ea26575afbb-3.15.0a0-af15e1d | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                      | 99.6 ms                                                                     | 86.4 ms: 1.15x faster                                                               |
| float                      | 64.2 ms                                                                     | 60.5 ms: 1.06x faster                                                               |
| gc_traversal               | 6.79 ms                                                                     | 6.47 ms: 1.05x faster                                                               |
| genshi_xml                 | 56.9 ms                                                                     | 54.6 ms: 1.04x faster                                                               |
| regex_v8                   | 24.2 ms                                                                     | 23.5 ms: 1.03x faster                                                               |
| go                         | 126 ms                                                                      | 122 ms: 1.03x faster                                                                |
| create_gc_cycles           | 2.92 ms                                                                     | 2.87 ms: 1.02x faster                                                               |
| xml_etree_generate         | 80.8 ms                                                                     | 79.5 ms: 1.02x faster                                                               |
| async_generators           | 448 ms                                                                      | 442 ms: 1.01x faster                                                                |
| pprint_pformat             | 1.51 sec                                                                    | 1.49 sec: 1.01x faster                                                              |
| fannkuch                   | 371 ms                                                                      | 367 ms: 1.01x faster                                                                |
| async_tree_none_tg         | 271 ms                                                                      | 268 ms: 1.01x faster                                                                |
| pathlib                    | 16.7 ms                                                                     | 16.5 ms: 1.01x faster                                                               |
| async_tree_io_tg           | 637 ms                                                                      | 630 ms: 1.01x faster                                                                |
| thrift                     | 854 us                                                                      | 844 us: 1.01x faster                                                                |
| meteor_contest             | 122 ms                                                                      | 121 ms: 1.01x faster                                                                |
| xml_etree_process          | 55.8 ms                                                                     | 55.2 ms: 1.01x faster                                                               |
| pprint_safe_repr           | 749 ms                                                                      | 742 ms: 1.01x faster                                                                |
| logging_simple             | 6.09 us                                                                     | 6.04 us: 1.01x faster                                                               |
| deltablue                  | 2.89 ms                                                                     | 2.86 ms: 1.01x faster                                                               |
| genshi_text                | 23.3 ms                                                                     | 23.1 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                      | 504 ms: 1.01x faster                                                                |
| async_tree_io              | 623 ms                                                                      | 619 ms: 1.01x faster                                                                |
| generators                 | 29.7 ms                                                                     | 29.5 ms: 1.01x faster                                                               |
| async_tree_cpu_io_mixed    | 504 ms                                                                      | 501 ms: 1.01x faster                                                                |
| logging_silent             | 91.9 ns                                                                     | 91.5 ns: 1.00x faster                                                               |
| shortest_path              | 444 ms                                                                      | 442 ms: 1.00x faster                                                                |
| coroutines                 | 22.5 ms                                                                     | 22.5 ms: 1.00x faster                                                               |
| regex_dna                  | 226 ms                                                                      | 226 ms: 1.00x faster                                                                |
| pidigits                   | 255 ms                                                                      | 255 ms: 1.00x faster                                                                |
| python_startup             | 15.3 ms                                                                     | 15.4 ms: 1.00x slower                                                               |
| xml_etree_iterparse        | 97.9 ms                                                                     | 98.2 ms: 1.00x slower                                                               |
| sqlglot_v2_parse           | 1.29 ms                                                                     | 1.30 ms: 1.00x slower                                                               |
| hexiom                     | 6.10 ms                                                                     | 6.12 ms: 1.00x slower                                                               |
| docutils                   | 2.90 sec                                                                    | 2.91 sec: 1.01x slower                                                              |
| crypto_pyaes               | 76.9 ms                                                                     | 77.3 ms: 1.01x slower                                                               |
| json_loads                 | 25.2 us                                                                     | 25.3 us: 1.01x slower                                                               |
| json_dumps                 | 10.1 ms                                                                     | 10.2 ms: 1.01x slower                                                               |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                                |
| raytrace                   | 282 ms                                                                      | 283 ms: 1.01x slower                                                                |
| deepcopy_reduce            | 2.95 us                                                                     | 2.97 us: 1.01x slower                                                               |
| sqlite_synth               | 2.79 us                                                                     | 2.81 us: 1.01x slower                                                               |
| 2to3                       | 285 ms                                                                      | 287 ms: 1.01x slower                                                                |
| dulwich_log                | 59.4 ms                                                                     | 59.8 ms: 1.01x slower                                                               |
| comprehensions             | 17.3 us                                                                     | 17.4 us: 1.01x slower                                                               |
| sympy_str                  | 289 ms                                                                      | 291 ms: 1.01x slower                                                                |
| json                       | 5.43 ms                                                                     | 5.48 ms: 1.01x slower                                                               |
| scimark_sor                | 101 ms                                                                      | 102 ms: 1.01x slower                                                                |
| bpe_tokeniser              | 4.52 sec                                                                    | 4.57 sec: 1.01x slower                                                              |
| connected_components       | 403 ms                                                                      | 408 ms: 1.01x slower                                                                |
| sympy_integrate            | 22.2 ms                                                                     | 22.5 ms: 1.01x slower                                                               |
| tomli_loads                | 1.90 sec                                                                    | 1.92 sec: 1.01x slower                                                              |
| regex_compile              | 132 ms                                                                      | 134 ms: 1.01x slower                                                                |
| coverage                   | 77.9 ms                                                                     | 78.9 ms: 1.01x slower                                                               |
| deepcopy                   | 272 us                                                                      | 276 us: 1.01x slower                                                                |
| xml_etree_parse            | 139 ms                                                                      | 140 ms: 1.01x slower                                                                |
| mako                       | 9.72 ms                                                                     | 9.87 ms: 1.01x slower                                                               |
| scimark_lu                 | 93.9 ms                                                                     | 95.3 ms: 1.01x slower                                                               |
| telco                      | 158 ms                                                                      | 161 ms: 1.02x slower                                                                |
| pickle_pure_python         | 327 us                                                                      | 333 us: 1.02x slower                                                                |
| subparsers                 | 42.2 ms                                                                     | 42.9 ms: 1.02x slower                                                               |
| mdp                        | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                              |
| many_optionals             | 1.21 ms                                                                     | 1.23 ms: 1.02x slower                                                               |
| pyflate                    | 406 ms                                                                      | 414 ms: 1.02x slower                                                                |
| django_template            | 34.7 ms                                                                     | 35.5 ms: 1.02x slower                                                               |
| spectral_norm              | 78.8 ms                                                                     | 80.6 ms: 1.02x slower                                                               |
| regex_effbot               | 3.60 ms                                                                     | 3.69 ms: 1.02x slower                                                               |
| unpickle_pure_python       | 193 us                                                                      | 199 us: 1.03x slower                                                                |
| pycparser                  | 1.21 sec                                                                    | 1.25 sec: 1.03x slower                                                              |
| scimark_sparse_mat_mult    | 4.91 ms                                                                     | 5.09 ms: 1.04x slower                                                               |
| scimark_monte_carlo        | 62.1 ms                                                                     | 64.4 ms: 1.04x slower                                                               |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (22): richards_super, async_tree_memoization_tg, async_tree_none, async_tree_memoization, sqlglot_v2_transpile, sqlglot_v2_optimize, nqueens, python_startup_no_site, chaos, djangocms, logging_format, scimark_fft, deepcopy_memo, sympy_expand, sympy_sum, sqlglot_v2_normalize, k_core, typing_runtime_protocols, richards, html5lib, sphinx, pylint

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 80.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x