# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.001x slower
- HPT reliability: 72.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                      | 285 ms: 1.00x faster                                                                |
| docutils       | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                              |
| html5lib       | 67.5 ms                                                                     | 67.0 ms: 1.01x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators           | 448 ms                                                                      | 443 ms: 1.01x faster                                                                |
| async_tree_memoization     | 329 ms                                                                      | 327 ms: 1.01x faster                                                                |
| async_tree_none            | 274 ms                                                                      | 272 ms: 1.00x faster                                                                |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed    | 500 ms                                                                      | 504 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                      | 511 ms: 1.01x slower                                                                |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, coroutines, async_tree_io_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 98.4 ms                                                                     | 84.4 ms: 1.17x faster                                                               |
| float          | 64.2 ms                                                                     | 61.7 ms: 1.04x faster                                                               |
| pidigits       | 256 ms                                                                      | 256 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.07x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_effbot   | 3.71 ms                                                                     | 3.60 ms: 1.03x faster                                                               |
| regex_dna      | 228 ms                                                                      | 223 ms: 1.02x faster                                                                |
| regex_compile  | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| regex_v8       | 22.9 ms                                                                     | 23.8 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| xml_etree_generate   | 81.6 ms                                                                     | 80.2 ms: 1.02x faster                                                               |
| json_dumps           | 11.3 ms                                                                     | 11.1 ms: 1.01x faster                                                               |
| pickle_pure_python   | 334 us                                                                      | 335 us: 1.00x slower                                                                |
| xml_etree_iterparse  | 96.9 ms                                                                     | 97.9 ms: 1.01x slower                                                               |
| tomli_loads          | 1.92 sec                                                                    | 1.94 sec: 1.01x slower                                                              |
| unpickle_pure_python | 197 us                                                                      | 199 us: 1.01x slower                                                                |
| xml_etree_parse      | 138 ms                                                                      | 140 ms: 1.02x slower                                                                |
| json_loads           | 24.9 us                                                                     | 25.5 us: 1.02x slower                                                               |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 35.5 ms                                                                     | 35.0 ms: 1.01x faster                                                               |
| genshi_text     | 23.0 ms                                                                     | 23.6 ms: 1.03x slower                                                               |
| mako            | 9.65 ms                                                                     | 10.3 ms: 1.06x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.02x slower                                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250721-pythonperf2-x86_64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody                      | 98.4 ms                                                                     | 84.4 ms: 1.17x faster                                                               |
| coverage                   | 81.7 ms                                                                     | 77.9 ms: 1.05x faster                                                               |
| float                      | 64.2 ms                                                                     | 61.7 ms: 1.04x faster                                                               |
| go                         | 128 ms                                                                      | 124 ms: 1.03x faster                                                                |
| regex_effbot               | 3.71 ms                                                                     | 3.60 ms: 1.03x faster                                                               |
| pycparser                  | 1.26 sec                                                                    | 1.23 sec: 1.02x faster                                                              |
| regex_dna                  | 228 ms                                                                      | 223 ms: 1.02x faster                                                                |
| xml_etree_generate         | 81.6 ms                                                                     | 80.2 ms: 1.02x faster                                                               |
| chaos                      | 59.9 ms                                                                     | 59.1 ms: 1.01x faster                                                               |
| json_dumps                 | 11.3 ms                                                                     | 11.1 ms: 1.01x faster                                                               |
| django_template            | 35.5 ms                                                                     | 35.0 ms: 1.01x faster                                                               |
| async_generators           | 448 ms                                                                      | 443 ms: 1.01x faster                                                                |
| sympy_expand               | 498 ms                                                                      | 493 ms: 1.01x faster                                                                |
| raytrace                   | 291 ms                                                                      | 288 ms: 1.01x faster                                                                |
| json                       | 5.40 ms                                                                     | 5.34 ms: 1.01x faster                                                               |
| pyflate                    | 421 ms                                                                      | 417 ms: 1.01x faster                                                                |
| deepcopy_memo              | 28.3 us                                                                     | 28.1 us: 1.01x faster                                                               |
| sqlglot_v2_transpile       | 1.71 ms                                                                     | 1.69 ms: 1.01x faster                                                               |
| sqlglot_v2_normalize       | 114 ms                                                                      | 113 ms: 1.01x faster                                                                |
| html5lib                   | 67.5 ms                                                                     | 67.0 ms: 1.01x faster                                                               |
| async_tree_memoization     | 329 ms                                                                      | 327 ms: 1.01x faster                                                                |
| many_optionals             | 1.23 ms                                                                     | 1.22 ms: 1.01x faster                                                               |
| sympy_str                  | 291 ms                                                                      | 289 ms: 1.00x faster                                                                |
| deepcopy                   | 280 us                                                                      | 279 us: 1.00x faster                                                                |
| async_tree_none            | 274 ms                                                                      | 272 ms: 1.00x faster                                                                |
| logging_silent             | 93.8 ns                                                                     | 93.4 ns: 1.00x faster                                                               |
| 2to3                       | 286 ms                                                                      | 285 ms: 1.00x faster                                                                |
| hexiom                     | 6.20 ms                                                                     | 6.18 ms: 1.00x faster                                                               |
| connected_components       | 408 ms                                                                      | 407 ms: 1.00x faster                                                                |
| scimark_monte_carlo        | 62.5 ms                                                                     | 62.4 ms: 1.00x faster                                                               |
| pidigits                   | 256 ms                                                                      | 256 ms: 1.00x faster                                                                |
| shortest_path              | 442 ms                                                                      | 443 ms: 1.00x slower                                                                |
| pickle_pure_python         | 334 us                                                                      | 335 us: 1.00x slower                                                                |
| docutils                   | 2.92 sec                                                                    | 2.93 sec: 1.01x slower                                                              |
| meteor_contest             | 121 ms                                                                      | 122 ms: 1.01x slower                                                                |
| asyncio_websockets         | 381 ms                                                                      | 384 ms: 1.01x slower                                                                |
| scimark_sor                | 103 ms                                                                      | 104 ms: 1.01x slower                                                                |
| subparsers                 | 42.9 ms                                                                     | 43.2 ms: 1.01x slower                                                               |
| gc_traversal               | 6.53 ms                                                                     | 6.58 ms: 1.01x slower                                                               |
| async_tree_cpu_io_mixed    | 500 ms                                                                      | 504 ms: 1.01x slower                                                                |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                      | 511 ms: 1.01x slower                                                                |
| mdp                        | 1.28 sec                                                                    | 1.29 sec: 1.01x slower                                                              |
| fannkuch                   | 369 ms                                                                      | 372 ms: 1.01x slower                                                                |
| sqlite_synth               | 2.80 us                                                                     | 2.82 us: 1.01x slower                                                               |
| xml_etree_iterparse        | 96.9 ms                                                                     | 97.9 ms: 1.01x slower                                                               |
| logging_simple             | 6.06 us                                                                     | 6.12 us: 1.01x slower                                                               |
| deltablue                  | 2.90 ms                                                                     | 2.93 ms: 1.01x slower                                                               |
| pprint_pformat             | 1.50 sec                                                                    | 1.52 sec: 1.01x slower                                                              |
| tomli_loads                | 1.92 sec                                                                    | 1.94 sec: 1.01x slower                                                              |
| regex_compile              | 132 ms                                                                      | 133 ms: 1.01x slower                                                                |
| comprehensions             | 17.3 us                                                                     | 17.5 us: 1.01x slower                                                               |
| unpickle_pure_python       | 197 us                                                                      | 199 us: 1.01x slower                                                                |
| nqueens                    | 93.2 ms                                                                     | 94.4 ms: 1.01x slower                                                               |
| pprint_safe_repr           | 741 ms                                                                      | 753 ms: 1.02x slower                                                                |
| scimark_lu                 | 95.0 ms                                                                     | 96.6 ms: 1.02x slower                                                               |
| xml_etree_parse            | 138 ms                                                                      | 140 ms: 1.02x slower                                                                |
| richards_super             | 40.8 ms                                                                     | 41.6 ms: 1.02x slower                                                               |
| spectral_norm              | 79.2 ms                                                                     | 80.9 ms: 1.02x slower                                                               |
| json_loads                 | 24.9 us                                                                     | 25.5 us: 1.02x slower                                                               |
| bpe_tokeniser              | 4.56 sec                                                                    | 4.66 sec: 1.02x slower                                                              |
| telco                      | 159 ms                                                                      | 163 ms: 1.03x slower                                                                |
| genshi_text                | 23.0 ms                                                                     | 23.6 ms: 1.03x slower                                                               |
| typing_runtime_protocols   | 171 us                                                                      | 175 us: 1.03x slower                                                                |
| generators                 | 29.0 ms                                                                     | 30.2 ms: 1.04x slower                                                               |
| regex_v8                   | 22.9 ms                                                                     | 23.8 ms: 1.04x slower                                                               |
| scimark_fft                | 300 ms                                                                      | 314 ms: 1.05x slower                                                                |
| scimark_sparse_mat_mult    | 4.81 ms                                                                     | 5.07 ms: 1.05x slower                                                               |
| mako                       | 9.65 ms                                                                     | 10.3 ms: 1.06x slower                                                               |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (25): k_core, async_tree_io, dulwich_log, xml_etree_process, sympy_sum, sqlglot_v2_parse, sqlglot_v2_optimize, async_tree_memoization_tg, crypto_pyaes, sympy_integrate, coroutines, djangocms, python_startup, async_tree_io_tg, logging_format, python_startup_no_site, deepcopy_reduce, pathlib, thrift, create_gc_cycles, pylint, genshi_xml, async_tree_none_tg, sphinx, richards

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 72.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x