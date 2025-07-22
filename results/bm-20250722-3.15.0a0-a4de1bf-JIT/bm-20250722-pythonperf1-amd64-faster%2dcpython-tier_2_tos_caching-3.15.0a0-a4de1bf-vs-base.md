# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.004x faster
- HPT reliability: 98.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 219 ms                                                                     | 221 ms: 1.01x slower                                                               |
| docutils       | 1.64 sec                                                                   | 1.65 sec: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                       |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none_tg        | 171 ms                                                                     | 167 ms: 1.02x faster                                                               |
| async_tree_none           | 170 ms                                                                     | 167 ms: 1.02x faster                                                               |
| coroutines                | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                              |
| async_tree_memoization_tg | 213 ms                                                                     | 209 ms: 1.02x faster                                                               |
| async_tree_memoization    | 205 ms                                                                     | 203 ms: 1.01x faster                                                               |
| async_generators          | 247 ms                                                                     | 250 ms: 1.02x slower                                                               |
| Geometric mean            | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 54.4 ms                                                                    | 47.8 ms: 1.14x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                       |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 79.4 ms                                                                    | 78.7 ms: 1.01x faster                                                              |
| regex_dna      | 116 ms                                                                     | 121 ms: 1.04x slower                                                               |
| regex_v8       | 13.4 ms                                                                    | 14.0 ms: 1.05x slower                                                              |
| regex_effbot   | 1.49 ms                                                                    | 1.61 ms: 1.08x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.04x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.10 sec                                                                   | 1.08 sec: 1.02x faster                                                             |
| json_loads           | 14.5 us                                                                    | 14.2 us: 1.02x faster                                                              |
| json_dumps           | 6.21 ms                                                                    | 6.26 ms: 1.01x slower                                                              |
| unpickle_pure_python | 105 us                                                                     | 106 us: 1.01x slower                                                               |
| xml_etree_generate   | 49.5 ms                                                                    | 51.0 ms: 1.03x slower                                                              |
| xml_etree_parse      | 86.3 ms                                                                    | 89.5 ms: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup | 25.9 ms                                                                    | 25.7 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 24.7 ms                                                                    | 24.2 ms: 1.02x faster                                                              |
| mako            | 5.27 ms                                                                    | 5.58 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20250721-pythonperf1-amd64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|---------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody                     | 54.4 ms                                                                    | 47.8 ms: 1.14x faster                                                              |
| deepcopy_memo             | 18.4 us                                                                    | 17.3 us: 1.07x faster                                                              |
| spectral_norm             | 68.1 ms                                                                    | 63.9 ms: 1.07x faster                                                              |
| scimark_sor               | 79.5 ms                                                                    | 74.6 ms: 1.07x faster                                                              |
| deepcopy_reduce           | 1.92 us                                                                    | 1.81 us: 1.06x faster                                                              |
| deltablue                 | 2.26 ms                                                                    | 2.16 ms: 1.05x faster                                                              |
| go                        | 77.8 ms                                                                    | 75.2 ms: 1.03x faster                                                              |
| scimark_monte_carlo       | 43.8 ms                                                                    | 42.4 ms: 1.03x faster                                                              |
| sqlglot_v2_transpile      | 991 us                                                                     | 966 us: 1.03x faster                                                               |
| deepcopy                  | 172 us                                                                     | 168 us: 1.02x faster                                                               |
| pprint_safe_repr          | 445 ms                                                                     | 435 ms: 1.02x faster                                                               |
| json                      | 3.07 ms                                                                    | 3.00 ms: 1.02x faster                                                              |
| async_tree_none_tg        | 171 ms                                                                     | 167 ms: 1.02x faster                                                               |
| sqlglot_v2_parse          | 784 us                                                                     | 768 us: 1.02x faster                                                               |
| gc_traversal              | 2.12 ms                                                                    | 2.08 ms: 1.02x faster                                                              |
| generators                | 19.7 ms                                                                    | 19.3 ms: 1.02x faster                                                              |
| tomli_loads               | 1.10 sec                                                                   | 1.08 sec: 1.02x faster                                                             |
| django_template           | 24.7 ms                                                                    | 24.2 ms: 1.02x faster                                                              |
| richards_super            | 31.0 ms                                                                    | 30.4 ms: 1.02x faster                                                              |
| async_tree_none           | 170 ms                                                                     | 167 ms: 1.02x faster                                                               |
| coroutines                | 14.7 ms                                                                    | 14.4 ms: 1.02x faster                                                              |
| json_loads                | 14.5 us                                                                    | 14.2 us: 1.02x faster                                                              |
| pprint_pformat            | 902 ms                                                                     | 887 ms: 1.02x faster                                                               |
| logging_format            | 6.68 us                                                                    | 6.57 us: 1.02x faster                                                              |
| hexiom                    | 4.10 ms                                                                    | 4.04 ms: 1.02x faster                                                              |
| async_tree_memoization_tg | 213 ms                                                                     | 209 ms: 1.02x faster                                                               |
| scimark_fft               | 150 ms                                                                     | 148 ms: 1.01x faster                                                               |
| dulwich_log               | 40.7 ms                                                                    | 40.3 ms: 1.01x faster                                                              |
| python_startup            | 25.9 ms                                                                    | 25.7 ms: 1.01x faster                                                              |
| regex_compile             | 79.4 ms                                                                    | 78.7 ms: 1.01x faster                                                              |
| sqlglot_v2_optimize       | 34.6 ms                                                                    | 34.2 ms: 1.01x faster                                                              |
| logging_simple            | 6.19 us                                                                    | 6.14 us: 1.01x faster                                                              |
| async_tree_memoization    | 205 ms                                                                     | 203 ms: 1.01x faster                                                               |
| raytrace                  | 181 ms                                                                     | 180 ms: 1.01x faster                                                               |
| comprehensions            | 10.4 us                                                                    | 10.4 us: 1.01x faster                                                              |
| sqlglot_v2_normalize      | 71.3 ms                                                                    | 70.9 ms: 1.01x faster                                                              |
| richards                  | 27.1 ms                                                                    | 26.9 ms: 1.01x faster                                                              |
| coverage                  | 51.8 ms                                                                    | 52.2 ms: 1.01x slower                                                              |
| docutils                  | 1.64 sec                                                                   | 1.65 sec: 1.01x slower                                                             |
| many_optionals            | 567 us                                                                     | 572 us: 1.01x slower                                                               |
| json_dumps                | 6.21 ms                                                                    | 6.26 ms: 1.01x slower                                                              |
| 2to3                      | 219 ms                                                                     | 221 ms: 1.01x slower                                                               |
| typing_runtime_protocols  | 103 us                                                                     | 104 us: 1.01x slower                                                               |
| unpickle_pure_python      | 105 us                                                                     | 106 us: 1.01x slower                                                               |
| create_gc_cycles          | 1.30 ms                                                                    | 1.32 ms: 1.01x slower                                                              |
| async_generators          | 247 ms                                                                     | 250 ms: 1.02x slower                                                               |
| nqueens                   | 58.5 ms                                                                    | 59.9 ms: 1.02x slower                                                              |
| xml_etree_generate        | 49.5 ms                                                                    | 51.0 ms: 1.03x slower                                                              |
| meteor_contest            | 69.7 ms                                                                    | 71.9 ms: 1.03x slower                                                              |
| regex_dna                 | 116 ms                                                                     | 121 ms: 1.04x slower                                                               |
| bpe_tokeniser             | 2.49 sec                                                                   | 2.58 sec: 1.04x slower                                                             |
| xml_etree_parse           | 86.3 ms                                                                    | 89.5 ms: 1.04x slower                                                              |
| scimark_sparse_mat_mult   | 2.26 ms                                                                    | 2.35 ms: 1.04x slower                                                              |
| fannkuch                  | 209 ms                                                                     | 218 ms: 1.04x slower                                                               |
| regex_v8                  | 13.4 ms                                                                    | 14.0 ms: 1.05x slower                                                              |
| mako                      | 5.27 ms                                                                    | 5.58 ms: 1.06x slower                                                              |
| regex_effbot              | 1.49 ms                                                                    | 1.61 ms: 1.08x slower                                                              |
| Geometric mean            | (ref)                                                                      | 1.00x faster                                                                       |

Benchmark hidden because not significant (35): asyncio_websockets, html5lib, genshi_xml, k_core, telco, connected_components, python_startup_no_site, sympy_str, chaos, shortest_path, genshi_text, xml_etree_iterparse, sympy_integrate, pylint, async_tree_cpu_io_mixed, scimark_lu, pidigits, mdp, logging_silent, pickle_pure_python, async_tree_io_tg, subparsers, sympy_expand, crypto_pyaes, sympy_sum, pycparser, sphinx, xml_etree_process, float, async_tree_cpu_io_mixed_tg, sqlite_synth, pathlib, async_tree_io, pyflate, thrift

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 98.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown