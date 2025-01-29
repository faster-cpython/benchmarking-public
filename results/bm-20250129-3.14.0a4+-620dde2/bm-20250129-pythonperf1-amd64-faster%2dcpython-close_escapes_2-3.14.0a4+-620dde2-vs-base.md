# Results vs. base

- fork: faster-cpython
- ref: close_escapes_2
- machine: windows-amd64
- commit hash: 620dde2
- commit date: 2025-01-29
- overall geometric mean: 1.012x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 230 ms                                                                      | 233 ms: 1.01x slower                                                             |
| html5lib       | 39.1 ms                                                                     | 39.8 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 314 ms                                                                      | 310 ms: 1.01x faster                                                             |
| async_generators           | 227 ms                                                                      | 225 ms: 1.01x faster                                                             |
| coroutines                 | 14.8 ms                                                                     | 15.0 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 345 ms                                                                      | 349 ms: 1.01x slower                                                             |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                     |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 74.9 ms                                                                     | 77.1 ms: 1.03x slower                                                            |
| float          | 50.1 ms                                                                     | 52.6 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 1.51 ms                                                                     | 1.43 ms: 1.06x faster                                                            |
| regex_dna      | 117 ms                                                                      | 114 ms: 1.02x faster                                                             |
| regex_compile  | 88.2 ms                                                                     | 89.5 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 16.0 us                                                                     | 15.4 us: 1.04x faster                                                            |
| xml_etree_process    | 41.1 ms                                                                     | 41.3 ms: 1.00x slower                                                            |
| xml_etree_iterparse  | 64.3 ms                                                                     | 64.8 ms: 1.01x slower                                                            |
| xml_etree_generate   | 57.7 ms                                                                     | 58.6 ms: 1.02x slower                                                            |
| tomli_loads          | 1.40 sec                                                                    | 1.44 sec: 1.03x slower                                                           |
| pickle_pure_python   | 229 us                                                                      | 238 us: 1.04x slower                                                             |
| unpickle_pure_python | 153 us                                                                      | 164 us: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 24.7 ms                                                                     | 24.3 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text    | 16.5 ms                                                                     | 16.3 ms: 1.01x faster                                                            |
| genshi_xml     | 35.4 ms                                                                     | 36.0 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20250127-pythonperf1-amd64-python-75b49621578a45415bfe-3.14.0a4+-75b4962 | bm-20250129-pythonperf1-amd64-faster%2dcpython-close_escapes_2-3.14.0a4+-620dde2 |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot               | 1.51 ms                                                                     | 1.43 ms: 1.06x faster                                                            |
| json_loads                 | 16.0 us                                                                     | 15.4 us: 1.04x faster                                                            |
| regex_dna                  | 117 ms                                                                      | 114 ms: 1.02x faster                                                             |
| python_startup             | 24.7 ms                                                                     | 24.3 ms: 1.02x faster                                                            |
| asyncio_websockets         | 314 ms                                                                      | 310 ms: 1.01x faster                                                             |
| shortest_path              | 351 ms                                                                      | 347 ms: 1.01x faster                                                             |
| connected_components       | 318 ms                                                                      | 315 ms: 1.01x faster                                                             |
| async_generators           | 227 ms                                                                      | 225 ms: 1.01x faster                                                             |
| mdp                        | 1.63 sec                                                                    | 1.62 sec: 1.01x faster                                                           |
| genshi_text                | 16.5 ms                                                                     | 16.3 ms: 1.01x faster                                                            |
| bench_mp_pool              | 88.2 ms                                                                     | 87.7 ms: 1.01x faster                                                            |
| sqlite_synth               | 1.62 us                                                                     | 1.62 us: 1.00x faster                                                            |
| xml_etree_process          | 41.1 ms                                                                     | 41.3 ms: 1.00x slower                                                            |
| many_optionals             | 438 us                                                                      | 440 us: 1.00x slower                                                             |
| coverage                   | 48.9 ms                                                                     | 49.2 ms: 1.00x slower                                                            |
| bpe_tokeniser              | 3.00 sec                                                                    | 3.02 sec: 1.01x slower                                                           |
| meteor_contest             | 75.8 ms                                                                     | 76.2 ms: 1.01x slower                                                            |
| sympy_integrate            | 13.6 ms                                                                     | 13.7 ms: 1.01x slower                                                            |
| crypto_pyaes               | 49.2 ms                                                                     | 49.5 ms: 1.01x slower                                                            |
| raytrace                   | 202 ms                                                                      | 203 ms: 1.01x slower                                                             |
| deltablue                  | 2.36 ms                                                                     | 2.38 ms: 1.01x slower                                                            |
| logging_simple             | 6.25 us                                                                     | 6.29 us: 1.01x slower                                                            |
| sympy_expand               | 304 ms                                                                      | 306 ms: 1.01x slower                                                             |
| xml_etree_iterparse        | 64.3 ms                                                                     | 64.8 ms: 1.01x slower                                                            |
| sympy_str                  | 178 ms                                                                      | 180 ms: 1.01x slower                                                             |
| nqueens                    | 65.5 ms                                                                     | 66.2 ms: 1.01x slower                                                            |
| coroutines                 | 14.8 ms                                                                     | 15.0 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                      | 347 ms: 1.01x slower                                                             |
| 2to3                       | 230 ms                                                                      | 233 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed    | 345 ms                                                                      | 349 ms: 1.01x slower                                                             |
| sqlglot_optimize           | 36.2 ms                                                                     | 36.6 ms: 1.01x slower                                                            |
| subparsers                 | 15.9 ms                                                                     | 16.1 ms: 1.01x slower                                                            |
| regex_compile              | 88.2 ms                                                                     | 89.5 ms: 1.01x slower                                                            |
| sqlglot_transpile          | 1.10 ms                                                                     | 1.12 ms: 1.01x slower                                                            |
| sqlglot_normalize          | 197 ms                                                                      | 200 ms: 1.02x slower                                                             |
| sqlglot_parse              | 888 us                                                                      | 901 us: 1.02x slower                                                             |
| logging_format             | 6.66 us                                                                     | 6.76 us: 1.02x slower                                                            |
| logging_silent             | 68.1 ns                                                                     | 69.1 ns: 1.02x slower                                                            |
| xml_etree_generate         | 57.7 ms                                                                     | 58.6 ms: 1.02x slower                                                            |
| genshi_xml                 | 35.4 ms                                                                     | 36.0 ms: 1.02x slower                                                            |
| dulwich_log                | 42.5 ms                                                                     | 43.3 ms: 1.02x slower                                                            |
| html5lib                   | 39.1 ms                                                                     | 39.8 ms: 1.02x slower                                                            |
| pyflate                    | 308 ms                                                                      | 314 ms: 1.02x slower                                                             |
| chaos                      | 42.5 ms                                                                     | 43.4 ms: 1.02x slower                                                            |
| comprehensions             | 12.6 us                                                                     | 12.9 us: 1.02x slower                                                            |
| pycparser                  | 732 ms                                                                      | 750 ms: 1.02x slower                                                             |
| scimark_fft                | 195 ms                                                                      | 199 ms: 1.02x slower                                                             |
| deepcopy                   | 183 us                                                                      | 187 us: 1.02x slower                                                             |
| nbody                      | 74.9 ms                                                                     | 77.1 ms: 1.03x slower                                                            |
| deepcopy_reduce            | 1.84 us                                                                     | 1.90 us: 1.03x slower                                                            |
| pprint_pformat             | 1.08 sec                                                                    | 1.12 sec: 1.03x slower                                                           |
| go                         | 89.2 ms                                                                     | 92.0 ms: 1.03x slower                                                            |
| typing_runtime_protocols   | 112 us                                                                      | 116 us: 1.03x slower                                                             |
| tomli_loads                | 1.40 sec                                                                    | 1.44 sec: 1.03x slower                                                           |
| pprint_safe_repr           | 538 ms                                                                      | 556 ms: 1.03x slower                                                             |
| hexiom                     | 4.54 ms                                                                     | 4.70 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 48.0 ms                                                                     | 49.7 ms: 1.03x slower                                                            |
| richards_super             | 35.7 ms                                                                     | 37.0 ms: 1.04x slower                                                            |
| pickle_pure_python         | 229 us                                                                      | 238 us: 1.04x slower                                                             |
| scimark_sparse_mat_mult    | 2.58 ms                                                                     | 2.68 ms: 1.04x slower                                                            |
| richards                   | 31.5 ms                                                                     | 32.8 ms: 1.04x slower                                                            |
| scimark_lu                 | 67.1 ms                                                                     | 70.1 ms: 1.04x slower                                                            |
| deepcopy_memo              | 20.3 us                                                                     | 21.4 us: 1.05x slower                                                            |
| float                      | 50.1 ms                                                                     | 52.6 ms: 1.05x slower                                                            |
| scimark_sor                | 90.8 ms                                                                     | 95.4 ms: 1.05x slower                                                            |
| fannkuch                   | 272 ms                                                                      | 286 ms: 1.05x slower                                                             |
| unpickle_pure_python       | 153 us                                                                      | 164 us: 1.07x slower                                                             |
| spectral_norm              | 60.5 ms                                                                     | 66.3 ms: 1.10x slower                                                            |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                     |

Benchmark hidden because not significant (26): gc_traversal, json, django_template, thrift, sympy_sum, async_tree_memoization_tg, pidigits, xml_etree_parse, json_dumps, telco, create_gc_cycles, mako, async_tree_io_tg, async_tree_memoization, docutils, generators, async_tree_io, async_tree_none_tg, sphinx, async_tree_none, k_core, pathlib, python_startup_no_site, pylint, bench_thread_pool, regex_v8

- Geometric mean (including insignificant results): 1.012x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown