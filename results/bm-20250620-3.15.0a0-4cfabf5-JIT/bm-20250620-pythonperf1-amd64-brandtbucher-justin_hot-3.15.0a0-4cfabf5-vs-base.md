# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.001x slower
- HPT reliability: 94.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 222 ms: 1.01x slower                                                   |
| html5lib       | 39.2 ms                                                                    | 38.7 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 168 ms                                                                     | 169 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 332 ms                                                                     | 334 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 347 ms: 1.01x slower                                                   |
| async_tree_io_tg           | 388 ms                                                                     | 394 ms: 1.01x slower                                                   |
| async_generators           | 243 ms                                                                     | 248 ms: 1.02x slower                                                   |
| async_tree_memoization     | 206 ms                                                                     | 210 ms: 1.02x slower                                                   |
| async_tree_none            | 168 ms                                                                     | 172 ms: 1.02x slower                                                   |
| coroutines                 | 13.9 ms                                                                    | 14.5 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 62.8 ms                                                                    | 56.4 ms: 1.11x faster                                                  |
| float          | 43.3 ms                                                                    | 44.2 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.03x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                                    | 79.5 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|--------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_loads         | 14.4 us                                                                    | 14.3 us: 1.01x faster                                                  |
| xml_etree_process  | 36.4 ms                                                                    | 36.6 ms: 1.01x slower                                                  |
| pickle_pure_python | 205 us                                                                     | 207 us: 1.01x slower                                                   |
| xml_etree_parse    | 86.6 ms                                                                    | 87.9 ms: 1.01x slower                                                  |
| xml_etree_generate | 51.0 ms                                                                    | 52.2 ms: 1.02x slower                                                  |
| Geometric mean     | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 23.9 ms                                                                    | 24.1 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:--------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody                      | 62.8 ms                                                                    | 56.4 ms: 1.11x faster                                                  |
| dulwich_log                | 43.8 ms                                                                    | 41.3 ms: 1.06x faster                                                  |
| fannkuch                   | 250 ms                                                                     | 236 ms: 1.06x faster                                                   |
| crypto_pyaes               | 48.4 ms                                                                    | 45.9 ms: 1.05x faster                                                  |
| scimark_fft                | 162 ms                                                                     | 156 ms: 1.04x faster                                                   |
| json                       | 3.07 ms                                                                    | 3.00 ms: 1.02x faster                                                  |
| coverage                   | 50.1 ms                                                                    | 49.0 ms: 1.02x faster                                                  |
| meteor_contest             | 74.8 ms                                                                    | 73.3 ms: 1.02x faster                                                  |
| pyflate                    | 268 ms                                                                     | 263 ms: 1.02x faster                                                   |
| hexiom                     | 4.21 ms                                                                    | 4.13 ms: 1.02x faster                                                  |
| nqueens                    | 60.4 ms                                                                    | 59.4 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.06 sec                                                                   | 1.05 sec: 1.02x faster                                                 |
| html5lib                   | 39.2 ms                                                                    | 38.7 ms: 1.01x faster                                                  |
| telco                      | 4.41 ms                                                                    | 4.35 ms: 1.01x faster                                                  |
| create_gc_cycles           | 1.34 ms                                                                    | 1.32 ms: 1.01x faster                                                  |
| scimark_monte_carlo        | 40.4 ms                                                                    | 39.9 ms: 1.01x faster                                                  |
| sympy_integrate            | 12.8 ms                                                                    | 12.7 ms: 1.01x faster                                                  |
| scimark_lu                 | 59.5 ms                                                                    | 58.9 ms: 1.01x faster                                                  |
| spectral_norm              | 60.0 ms                                                                    | 59.3 ms: 1.01x faster                                                  |
| json_loads                 | 14.4 us                                                                    | 14.3 us: 1.01x faster                                                  |
| logging_silent             | 322 ns                                                                     | 319 ns: 1.01x faster                                                   |
| shortest_path              | 359 ms                                                                     | 357 ms: 1.01x faster                                                   |
| connected_components       | 328 ms                                                                     | 329 ms: 1.01x slower                                                   |
| sqlglot_v2_normalize       | 70.6 ms                                                                    | 71.1 ms: 1.01x slower                                                  |
| xml_etree_process          | 36.4 ms                                                                    | 36.6 ms: 1.01x slower                                                  |
| async_tree_none_tg         | 168 ms                                                                     | 169 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 332 ms                                                                     | 334 ms: 1.01x slower                                                   |
| pathlib                    | 31.6 ms                                                                    | 31.8 ms: 1.01x slower                                                  |
| django_template            | 23.9 ms                                                                    | 24.1 ms: 1.01x slower                                                  |
| sqlglot_v2_optimize        | 34.5 ms                                                                    | 34.8 ms: 1.01x slower                                                  |
| sqlglot_v2_transpile       | 1.00 ms                                                                    | 1.01 ms: 1.01x slower                                                  |
| pickle_pure_python         | 205 us                                                                     | 207 us: 1.01x slower                                                   |
| 2to3                       | 220 ms                                                                     | 222 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                     | 347 ms: 1.01x slower                                                   |
| subparsers                 | 17.0 ms                                                                    | 17.2 ms: 1.01x slower                                                  |
| regex_compile              | 78.6 ms                                                                    | 79.5 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult    | 2.31 ms                                                                    | 2.34 ms: 1.01x slower                                                  |
| richards_super             | 31.1 ms                                                                    | 31.5 ms: 1.01x slower                                                  |
| async_tree_io_tg           | 388 ms                                                                     | 394 ms: 1.01x slower                                                   |
| xml_etree_parse            | 86.6 ms                                                                    | 87.9 ms: 1.01x slower                                                  |
| sympy_str                  | 170 ms                                                                     | 172 ms: 1.02x slower                                                   |
| scimark_sor                | 74.7 ms                                                                    | 75.9 ms: 1.02x slower                                                  |
| deepcopy                   | 168 us                                                                     | 171 us: 1.02x slower                                                   |
| mdp                        | 805 ms                                                                     | 820 ms: 1.02x slower                                                   |
| sympy_expand               | 291 ms                                                                     | 297 ms: 1.02x slower                                                   |
| async_generators           | 243 ms                                                                     | 248 ms: 1.02x slower                                                   |
| logging_simple             | 6.36 us                                                                    | 6.49 us: 1.02x slower                                                  |
| async_tree_memoization     | 206 ms                                                                     | 210 ms: 1.02x slower                                                   |
| go                         | 77.0 ms                                                                    | 78.5 ms: 1.02x slower                                                  |
| raytrace                   | 178 ms                                                                     | 181 ms: 1.02x slower                                                   |
| float                      | 43.3 ms                                                                    | 44.2 ms: 1.02x slower                                                  |
| bpe_tokeniser              | 2.64 sec                                                                   | 2.69 sec: 1.02x slower                                                 |
| xml_etree_generate         | 51.0 ms                                                                    | 52.2 ms: 1.02x slower                                                  |
| async_tree_none            | 168 ms                                                                     | 172 ms: 1.02x slower                                                   |
| richards                   | 27.2 ms                                                                    | 27.8 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 104 us                                                                     | 107 us: 1.03x slower                                                   |
| comprehensions             | 10.9 us                                                                    | 11.2 us: 1.03x slower                                                  |
| deepcopy_memo              | 17.8 us                                                                    | 18.4 us: 1.03x slower                                                  |
| coroutines                 | 13.9 ms                                                                    | 14.5 ms: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (33): json_dumps, asyncio_websockets, k_core, docutils, pycparser, sqlite_synth, genshi_xml, deepcopy_reduce, pprint_safe_repr, many_optionals, regex_dna, pidigits, thrift, sympy_sum, generators, gc_traversal, unpickle_pure_python, python_startup, regex_effbot, deltablue, logging_format, sphinx, sqlglot_v2_parse, genshi_text, python_startup_no_site, pylint, chaos, xml_etree_iterparse, async_tree_memoization_tg, tomli_loads, async_tree_io, regex_v8, mako

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 94.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown