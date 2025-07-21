# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: 53a50eb
- commit date: 2025-07-21
- overall geometric mean: 1.007x faster
- HPT reliability: 98.91%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none_tg        | 171 ms                                                                     | 165 ms: 1.03x faster                                                               |
| coroutines                | 14.7 ms                                                                    | 14.3 ms: 1.03x faster                                                              |
| async_tree_none           | 170 ms                                                                     | 167 ms: 1.02x faster                                                               |
| async_tree_io_tg          | 396 ms                                                                     | 389 ms: 1.02x faster                                                               |
| async_tree_memoization_tg | 213 ms                                                                     | 209 ms: 1.02x faster                                                               |
| async_tree_memoization    | 205 ms                                                                     | 202 ms: 1.02x faster                                                               |
| async_generators          | 247 ms                                                                     | 248 ms: 1.01x slower                                                               |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 54.4 ms                                                                    | 46.2 ms: 1.18x faster                                                              |
| float          | 43.8 ms                                                                    | 43.0 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.06x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 79.4 ms                                                                    | 78.9 ms: 1.01x faster                                                              |
| regex_dna      | 116 ms                                                                     | 119 ms: 1.02x slower                                                               |
| regex_effbot   | 1.49 ms                                                                    | 1.56 ms: 1.05x slower                                                              |
| regex_v8       | 13.4 ms                                                                    | 14.5 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pickle_pure_python   | 202 us                                                                     | 200 us: 1.01x faster                                                               |
| xml_etree_parse      | 86.3 ms                                                                    | 86.8 ms: 1.01x slower                                                              |
| xml_etree_process    | 35.1 ms                                                                    | 35.6 ms: 1.01x slower                                                              |
| unpickle_pure_python | 105 us                                                                     | 107 us: 1.02x slower                                                               |
| xml_etree_generate   | 49.5 ms                                                                    | 51.1 ms: 1.03x slower                                                              |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (4): xml_etree_iterparse, tomli_loads, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 24.7 ms                                                                    | 24.2 ms: 1.02x faster                                                              |
| genshi_text     | 15.5 ms                                                                    | 15.4 ms: 1.01x faster                                                              |
| genshi_xml      | 34.4 ms                                                                    | 34.1 ms: 1.01x faster                                                              |
| mako            | 5.27 ms                                                                    | 5.62 ms: 1.07x slower                                                              |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                       |

All benchmarks:
===============

| Benchmark                 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250721-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-53a50eb |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                     | 54.4 ms                                                                    | 46.2 ms: 1.18x faster                                                              |
| spectral_norm             | 68.1 ms                                                                    | 62.2 ms: 1.09x faster                                                              |
| scimark_monte_carlo       | 43.8 ms                                                                    | 40.4 ms: 1.08x faster                                                              |
| scimark_sor               | 79.5 ms                                                                    | 74.1 ms: 1.07x faster                                                              |
| deepcopy_reduce           | 1.92 us                                                                    | 1.81 us: 1.06x faster                                                              |
| coverage                  | 51.8 ms                                                                    | 49.1 ms: 1.06x faster                                                              |
| deltablue                 | 2.26 ms                                                                    | 2.16 ms: 1.05x faster                                                              |
| logging_simple            | 6.19 us                                                                    | 5.95 us: 1.04x faster                                                              |
| logging_format            | 6.68 us                                                                    | 6.44 us: 1.04x faster                                                              |
| go                        | 77.8 ms                                                                    | 75.3 ms: 1.03x faster                                                              |
| async_tree_none_tg        | 171 ms                                                                     | 165 ms: 1.03x faster                                                               |
| richards_super            | 31.0 ms                                                                    | 30.2 ms: 1.03x faster                                                              |
| chaos                     | 41.0 ms                                                                    | 39.9 ms: 1.03x faster                                                              |
| deepcopy_memo             | 18.4 us                                                                    | 17.9 us: 1.03x faster                                                              |
| coroutines                | 14.7 ms                                                                    | 14.3 ms: 1.03x faster                                                              |
| raytrace                  | 181 ms                                                                     | 177 ms: 1.02x faster                                                               |
| django_template           | 24.7 ms                                                                    | 24.2 ms: 1.02x faster                                                              |
| scimark_fft               | 150 ms                                                                     | 147 ms: 1.02x faster                                                               |
| scimark_lu                | 61.2 ms                                                                    | 60.0 ms: 1.02x faster                                                              |
| float                     | 43.8 ms                                                                    | 43.0 ms: 1.02x faster                                                              |
| async_tree_none           | 170 ms                                                                     | 167 ms: 1.02x faster                                                               |
| async_tree_io_tg          | 396 ms                                                                     | 389 ms: 1.02x faster                                                               |
| async_tree_memoization_tg | 213 ms                                                                     | 209 ms: 1.02x faster                                                               |
| telco                     | 4.31 ms                                                                    | 4.24 ms: 1.02x faster                                                              |
| async_tree_memoization    | 205 ms                                                                     | 202 ms: 1.02x faster                                                               |
| richards                  | 27.1 ms                                                                    | 26.6 ms: 1.02x faster                                                              |
| json                      | 3.07 ms                                                                    | 3.02 ms: 1.02x faster                                                              |
| sqlglot_v2_transpile      | 991 us                                                                     | 978 us: 1.01x faster                                                               |
| sqlglot_v2_normalize      | 71.3 ms                                                                    | 70.4 ms: 1.01x faster                                                              |
| dulwich_log               | 40.7 ms                                                                    | 40.1 ms: 1.01x faster                                                              |
| sqlglot_v2_parse          | 784 us                                                                     | 774 us: 1.01x faster                                                               |
| sqlglot_v2_optimize       | 34.6 ms                                                                    | 34.2 ms: 1.01x faster                                                              |
| genshi_text               | 15.5 ms                                                                    | 15.4 ms: 1.01x faster                                                              |
| pickle_pure_python        | 202 us                                                                     | 200 us: 1.01x faster                                                               |
| deepcopy                  | 172 us                                                                     | 170 us: 1.01x faster                                                               |
| comprehensions            | 10.4 us                                                                    | 10.3 us: 1.01x faster                                                              |
| mdp                       | 806 ms                                                                     | 798 ms: 1.01x faster                                                               |
| logging_silent            | 54.7 ns                                                                    | 54.2 ns: 1.01x faster                                                              |
| thrift                    | 497 us                                                                     | 493 us: 1.01x faster                                                               |
| regex_compile             | 79.4 ms                                                                    | 78.9 ms: 1.01x faster                                                              |
| genshi_xml                | 34.4 ms                                                                    | 34.1 ms: 1.01x faster                                                              |
| connected_components      | 323 ms                                                                     | 322 ms: 1.01x faster                                                               |
| hexiom                    | 4.10 ms                                                                    | 4.08 ms: 1.01x faster                                                              |
| generators                | 19.7 ms                                                                    | 19.6 ms: 1.01x faster                                                              |
| xml_etree_parse           | 86.3 ms                                                                    | 86.8 ms: 1.01x slower                                                              |
| async_generators          | 247 ms                                                                     | 248 ms: 1.01x slower                                                               |
| sqlite_synth              | 1.54 us                                                                    | 1.56 us: 1.01x slower                                                              |
| sympy_sum                 | 87.0 ms                                                                    | 87.6 ms: 1.01x slower                                                              |
| xml_etree_process         | 35.1 ms                                                                    | 35.6 ms: 1.01x slower                                                              |
| regex_dna                 | 116 ms                                                                     | 119 ms: 1.02x slower                                                               |
| scimark_sparse_mat_mult   | 2.26 ms                                                                    | 2.31 ms: 1.02x slower                                                              |
| create_gc_cycles          | 1.30 ms                                                                    | 1.33 ms: 1.02x slower                                                              |
| unpickle_pure_python      | 105 us                                                                     | 107 us: 1.02x slower                                                               |
| nqueens                   | 58.5 ms                                                                    | 60.0 ms: 1.02x slower                                                              |
| xml_etree_generate        | 49.5 ms                                                                    | 51.1 ms: 1.03x slower                                                              |
| bpe_tokeniser             | 2.49 sec                                                                   | 2.58 sec: 1.04x slower                                                             |
| regex_effbot              | 1.49 ms                                                                    | 1.56 ms: 1.05x slower                                                              |
| meteor_contest            | 69.7 ms                                                                    | 73.2 ms: 1.05x slower                                                              |
| mako                      | 5.27 ms                                                                    | 5.62 ms: 1.07x slower                                                              |
| fannkuch                  | 209 ms                                                                     | 224 ms: 1.07x slower                                                               |
| regex_v8                  | 13.4 ms                                                                    | 14.5 ms: 1.08x slower                                                              |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (31): pyflate, sympy_str, pprint_safe_repr, asyncio_websockets, xml_etree_iterparse, pylint, subparsers, tomli_loads, shortest_path, pidigits, html5lib, 2to3, python_startup, async_tree_cpu_io_mixed, sphinx, pycparser, typing_runtime_protocols, pprint_pformat, async_tree_io, pathlib, sympy_expand, k_core, many_optionals, docutils, sympy_integrate, crypto_pyaes, json_loads, json_dumps, python_startup_no_site, gc_traversal, async_tree_cpu_io_mixed_tg

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 98.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown