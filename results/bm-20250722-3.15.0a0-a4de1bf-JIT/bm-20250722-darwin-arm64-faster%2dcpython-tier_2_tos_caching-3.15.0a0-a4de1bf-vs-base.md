# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.011x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                                | 167 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 63.9 ms                                                               | 63.2 ms: 1.01x faster                                                         |
| async_tree_memoization        | 194 ms                                                                | 193 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                | 359 ms: 1.00x faster                                                          |
| async_generators              | 284 ms                                                                | 286 ms: 1.01x slower                                                          |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (15): async_tree_none, async_tree_eager_io, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_memoization, async_tree_eager_tg, asyncio_websockets, async_tree_io_tg, async_tree_io, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coroutines, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 72.4 ms                                                               | 60.3 ms: 1.20x faster                                                         |
| float          | 51.2 ms                                                               | 51.5 ms: 1.01x slower                                                         |
| pidigits       | 280 ms                                                                | 284 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.16 ms                                                               | 2.13 ms: 1.02x faster                                                         |
| regex_compile  | 72.3 ms                                                               | 71.6 ms: 1.01x faster                                                         |
| regex_v8       | 15.3 ms                                                               | 15.5 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 127 us                                                                | 118 us: 1.08x faster                                                          |
| tomli_loads          | 1.22 sec                                                              | 1.15 sec: 1.06x faster                                                        |
| xml_etree_generate   | 49.3 ms                                                               | 48.2 ms: 1.02x faster                                                         |
| xml_etree_process    | 34.3 ms                                                               | 33.6 ms: 1.02x faster                                                         |
| pickle_pure_python   | 206 us                                                                | 202 us: 1.02x faster                                                          |
| xml_etree_iterparse  | 72.6 ms                                                               | 72.2 ms: 1.01x faster                                                         |
| json_dumps           | 6.55 ms                                                               | 6.60 ms: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 12.9 ms                                                               | 12.4 ms: 1.05x faster                                                         |
| python_startup         | 17.2 ms                                                               | 16.5 ms: 1.04x faster                                                         |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako           | 6.57 ms                                                               | 6.44 ms: 1.02x faster                                                         |
| genshi_xml     | 33.0 ms                                                               | 32.7 ms: 1.01x faster                                                         |
| genshi_text    | 15.3 ms                                                               | 15.2 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                     | bm-20250721-darwin-arm64-python-9c7b2af73dee2b997936-3.15.0a0-9c7b2af | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody                         | 72.4 ms                                                               | 60.3 ms: 1.20x faster                                                         |
| hexiom                        | 4.53 ms                                                               | 4.15 ms: 1.09x faster                                                         |
| spectral_norm                 | 63.4 ms                                                               | 58.8 ms: 1.08x faster                                                         |
| unpickle_pure_python          | 127 us                                                                | 118 us: 1.08x faster                                                          |
| tomli_loads                   | 1.22 sec                                                              | 1.15 sec: 1.06x faster                                                        |
| pyflate                       | 283 ms                                                                | 270 ms: 1.05x faster                                                          |
| python_startup_no_site        | 12.9 ms                                                               | 12.4 ms: 1.05x faster                                                         |
| scimark_fft                   | 188 ms                                                                | 180 ms: 1.04x faster                                                          |
| python_startup                | 17.2 ms                                                               | 16.5 ms: 1.04x faster                                                         |
| bpe_tokeniser                 | 2.90 sec                                                              | 2.80 sec: 1.04x faster                                                        |
| k_core                        | 1.59 sec                                                              | 1.53 sec: 1.04x faster                                                        |
| shortest_path                 | 351 ms                                                                | 341 ms: 1.03x faster                                                          |
| sqlglot_v2_parse              | 779 us                                                                | 756 us: 1.03x faster                                                          |
| sqlglot_v2_transpile          | 947 us                                                                | 920 us: 1.03x faster                                                          |
| connected_components          | 322 ms                                                                | 313 ms: 1.03x faster                                                          |
| fannkuch                      | 249 ms                                                                | 243 ms: 1.02x faster                                                          |
| nqueens                       | 61.0 ms                                                               | 59.6 ms: 1.02x faster                                                         |
| meteor_contest                | 71.8 ms                                                               | 70.1 ms: 1.02x faster                                                         |
| xml_etree_generate            | 49.3 ms                                                               | 48.2 ms: 1.02x faster                                                         |
| xml_etree_process             | 34.3 ms                                                               | 33.6 ms: 1.02x faster                                                         |
| pprint_safe_repr              | 457 ms                                                                | 447 ms: 1.02x faster                                                          |
| pickle_pure_python            | 206 us                                                                | 202 us: 1.02x faster                                                          |
| mako                          | 6.57 ms                                                               | 6.44 ms: 1.02x faster                                                         |
| regex_effbot                  | 2.16 ms                                                               | 2.13 ms: 1.02x faster                                                         |
| pprint_pformat                | 931 ms                                                                | 921 ms: 1.01x faster                                                          |
| genshi_xml                    | 33.0 ms                                                               | 32.7 ms: 1.01x faster                                                         |
| async_tree_eager              | 63.9 ms                                                               | 63.2 ms: 1.01x faster                                                         |
| scimark_monte_carlo           | 45.2 ms                                                               | 44.7 ms: 1.01x faster                                                         |
| regex_compile                 | 72.3 ms                                                               | 71.6 ms: 1.01x faster                                                         |
| genshi_text                   | 15.3 ms                                                               | 15.2 ms: 1.01x faster                                                         |
| scimark_lu                    | 74.9 ms                                                               | 74.2 ms: 1.01x faster                                                         |
| crypto_pyaes                  | 49.6 ms                                                               | 49.2 ms: 1.01x faster                                                         |
| 2to3                          | 169 ms                                                                | 167 ms: 1.01x faster                                                          |
| json                          | 3.00 ms                                                               | 2.98 ms: 1.01x faster                                                         |
| generators                    | 24.5 ms                                                               | 24.3 ms: 1.01x faster                                                         |
| sympy_sum                     | 76.6 ms                                                               | 76.1 ms: 1.01x faster                                                         |
| go                            | 86.0 ms                                                               | 85.4 ms: 1.01x faster                                                         |
| sympy_integrate               | 10.9 ms                                                               | 10.9 ms: 1.01x faster                                                         |
| subparsers                    | 25.4 ms                                                               | 25.2 ms: 1.01x faster                                                         |
| xml_etree_iterparse           | 72.6 ms                                                               | 72.2 ms: 1.01x faster                                                         |
| async_tree_memoization        | 194 ms                                                                | 193 ms: 1.01x faster                                                          |
| scimark_sparse_mat_mult       | 3.30 ms                                                               | 3.28 ms: 1.01x faster                                                         |
| coverage                      | 47.4 ms                                                               | 47.1 ms: 1.00x faster                                                         |
| async_tree_eager_cpu_io_mixed | 360 ms                                                                | 359 ms: 1.00x faster                                                          |
| chaos                         | 38.4 ms                                                               | 38.3 ms: 1.00x faster                                                         |
| raytrace                      | 172 ms                                                                | 172 ms: 1.00x faster                                                          |
| comprehensions                | 11.2 us                                                               | 11.2 us: 1.00x slower                                                         |
| many_optionals                | 593 us                                                                | 595 us: 1.00x slower                                                          |
| richards                      | 33.3 ms                                                               | 33.4 ms: 1.00x slower                                                         |
| create_gc_cycles              | 1.36 ms                                                               | 1.36 ms: 1.00x slower                                                         |
| deepcopy_memo                 | 21.5 us                                                               | 21.6 us: 1.00x slower                                                         |
| logging_silent                | 73.3 ns                                                               | 73.6 ns: 1.00x slower                                                         |
| sqlglot_v2_normalize          | 68.5 ms                                                               | 68.8 ms: 1.00x slower                                                         |
| float                         | 51.2 ms                                                               | 51.5 ms: 1.01x slower                                                         |
| async_generators              | 284 ms                                                                | 286 ms: 1.01x slower                                                          |
| deepcopy                      | 172 us                                                                | 173 us: 1.01x slower                                                          |
| telco                         | 4.39 ms                                                               | 4.42 ms: 1.01x slower                                                         |
| scimark_sor                   | 83.2 ms                                                               | 83.8 ms: 1.01x slower                                                         |
| json_dumps                    | 6.55 ms                                                               | 6.60 ms: 1.01x slower                                                         |
| deltablue                     | 2.40 ms                                                               | 2.42 ms: 1.01x slower                                                         |
| sqlglot_v2_optimize           | 33.4 ms                                                               | 33.7 ms: 1.01x slower                                                         |
| gc_traversal                  | 3.19 ms                                                               | 3.21 ms: 1.01x slower                                                         |
| richards_super                | 37.4 ms                                                               | 37.8 ms: 1.01x slower                                                         |
| regex_v8                      | 15.3 ms                                                               | 15.5 ms: 1.01x slower                                                         |
| pidigits                      | 280 ms                                                                | 284 ms: 1.02x slower                                                          |
| thrift                        | 448 us                                                                | 456 us: 1.02x slower                                                          |
| typing_runtime_protocols      | 94.1 us                                                               | 95.9 us: 1.02x slower                                                         |
| Geometric mean                | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (34): async_tree_none, async_tree_eager_io, async_tree_eager_io_tg, async_tree_none_tg, async_tree_memoization_tg, sympy_str, async_tree_eager_memoization, async_tree_eager_tg, xml_etree_parse, pycparser, json_loads, logging_format, regex_dna, asyncio_websockets, async_tree_io_tg, sqlite_synth, pylint, dask, sympy_expand, async_tree_io, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, logging_simple, deepcopy_reduce, coroutines, async_tree_eager_memoization_tg, django_template, mdp, dulwich_log, sphinx, docutils, html5lib, pathlib

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x