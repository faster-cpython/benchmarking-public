# Results vs. base

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: windows-amd64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.005x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                     | 222 ms: 1.01x slower                                                              |
| sphinx         | 637 ms                                                                     | 661 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_memoization     | 210 ms                                                                     | 204 ms: 1.03x faster                                                              |
| async_tree_io              | 403 ms                                                                     | 397 ms: 1.02x faster                                                              |
| async_tree_none            | 172 ms                                                                     | 170 ms: 1.01x faster                                                              |
| async_tree_none_tg         | 170 ms                                                                     | 168 ms: 1.01x faster                                                              |
| async_generators           | 234 ms                                                                     | 231 ms: 1.01x faster                                                              |
| async_tree_memoization_tg  | 212 ms                                                                     | 210 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed    | 331 ms                                                                     | 327 ms: 1.01x faster                                                              |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                     | 341 ms: 1.01x faster                                                              |
| coroutines                 | 13.8 ms                                                                    | 14.1 ms: 1.02x slower                                                             |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                      |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 67.5 ms                                                                    | 62.0 ms: 1.09x faster                                                             |
| pidigits       | 149 ms                                                                     | 145 ms: 1.02x faster                                                              |
| float          | 44.5 ms                                                                    | 43.7 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                                      | 1.04x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 80.6 ms                                                                    | 79.3 ms: 1.02x faster                                                             |
| regex_effbot   | 1.47 ms                                                                    | 1.51 ms: 1.03x slower                                                             |
| regex_dna      | 117 ms                                                                     | 122 ms: 1.04x slower                                                              |
| regex_v8       | 13.5 ms                                                                    | 14.0 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 136 us                                                                     | 131 us: 1.04x faster                                                              |
| pickle_pure_python   | 216 us                                                                     | 208 us: 1.04x faster                                                              |
| json_loads           | 14.3 us                                                                    | 14.1 us: 1.01x faster                                                             |
| tomli_loads          | 1.39 sec                                                                   | 1.37 sec: 1.01x faster                                                            |
| xml_etree_generate   | 56.4 ms                                                                    | 55.7 ms: 1.01x faster                                                             |
| json_dumps           | 6.27 ms                                                                    | 6.36 ms: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                                      | 1.01x faster                                                                      |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 6.64 ms                                                                    | 6.54 ms: 1.02x faster                                                             |
| genshi_text    | 15.2 ms                                                                    | 15.1 ms: 1.01x faster                                                             |
| genshi_xml     | 33.9 ms                                                                    | 33.7 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20250613-pythonperf1-amd64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-pythonperf1-amd64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------|:--------------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody                      | 67.5 ms                                                                    | 62.0 ms: 1.09x faster                                                             |
| scimark_monte_carlo        | 42.1 ms                                                                    | 39.4 ms: 1.07x faster                                                             |
| unpickle_pure_python       | 136 us                                                                     | 131 us: 1.04x faster                                                              |
| telco                      | 4.67 ms                                                                    | 4.49 ms: 1.04x faster                                                             |
| richards_super             | 31.7 ms                                                                    | 30.5 ms: 1.04x faster                                                             |
| pickle_pure_python         | 216 us                                                                     | 208 us: 1.04x faster                                                              |
| pyflate                    | 290 ms                                                                     | 280 ms: 1.03x faster                                                              |
| scimark_fft                | 182 ms                                                                     | 176 ms: 1.03x faster                                                              |
| typing_runtime_protocols   | 104 us                                                                     | 101 us: 1.03x faster                                                              |
| pprint_safe_repr           | 553 ms                                                                     | 537 ms: 1.03x faster                                                              |
| richards                   | 27.9 ms                                                                    | 27.1 ms: 1.03x faster                                                             |
| pprint_pformat             | 1.13 sec                                                                   | 1.10 sec: 1.03x faster                                                            |
| async_tree_memoization     | 210 ms                                                                     | 204 ms: 1.03x faster                                                              |
| scimark_lu                 | 59.6 ms                                                                    | 58.1 ms: 1.03x faster                                                             |
| json                       | 3.08 ms                                                                    | 3.01 ms: 1.02x faster                                                             |
| pidigits                   | 149 ms                                                                     | 145 ms: 1.02x faster                                                              |
| scimark_sor                | 77.1 ms                                                                    | 75.5 ms: 1.02x faster                                                             |
| float                      | 44.5 ms                                                                    | 43.7 ms: 1.02x faster                                                             |
| deepcopy                   | 174 us                                                                     | 171 us: 1.02x faster                                                              |
| deepcopy_reduce            | 1.84 us                                                                    | 1.81 us: 1.02x faster                                                             |
| regex_compile              | 80.6 ms                                                                    | 79.3 ms: 1.02x faster                                                             |
| async_tree_io              | 403 ms                                                                     | 397 ms: 1.02x faster                                                              |
| mako                       | 6.64 ms                                                                    | 6.54 ms: 1.02x faster                                                             |
| deltablue                  | 2.22 ms                                                                    | 2.19 ms: 1.02x faster                                                             |
| async_tree_none            | 172 ms                                                                     | 170 ms: 1.01x faster                                                              |
| mdp                        | 805 ms                                                                     | 795 ms: 1.01x faster                                                              |
| subparsers                 | 17.2 ms                                                                    | 16.9 ms: 1.01x faster                                                             |
| json_loads                 | 14.3 us                                                                    | 14.1 us: 1.01x faster                                                             |
| async_tree_none_tg         | 170 ms                                                                     | 168 ms: 1.01x faster                                                              |
| tomli_loads                | 1.39 sec                                                                   | 1.37 sec: 1.01x faster                                                            |
| async_generators           | 234 ms                                                                     | 231 ms: 1.01x faster                                                              |
| go                         | 76.8 ms                                                                    | 75.8 ms: 1.01x faster                                                             |
| xml_etree_generate         | 56.4 ms                                                                    | 55.7 ms: 1.01x faster                                                             |
| hexiom                     | 4.08 ms                                                                    | 4.03 ms: 1.01x faster                                                             |
| async_tree_memoization_tg  | 212 ms                                                                     | 210 ms: 1.01x faster                                                              |
| crypto_pyaes               | 47.6 ms                                                                    | 47.0 ms: 1.01x faster                                                             |
| genshi_text                | 15.2 ms                                                                    | 15.1 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 331 ms                                                                     | 327 ms: 1.01x faster                                                              |
| genshi_xml                 | 33.9 ms                                                                    | 33.7 ms: 1.01x faster                                                             |
| sqlglot_v2_parse           | 825 us                                                                     | 818 us: 1.01x faster                                                              |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                     | 341 ms: 1.01x faster                                                              |
| sqlglot_v2_transpile       | 1.02 ms                                                                    | 1.01 ms: 1.01x faster                                                             |
| coverage                   | 296 ms                                                                     | 294 ms: 1.01x faster                                                              |
| many_optionals             | 440 us                                                                     | 437 us: 1.01x faster                                                              |
| sqlglot_v2_optimize        | 33.9 ms                                                                    | 33.7 ms: 1.01x faster                                                             |
| generators                 | 19.4 ms                                                                    | 19.3 ms: 1.01x faster                                                             |
| sympy_str                  | 169 ms                                                                     | 168 ms: 1.01x faster                                                              |
| bpe_tokeniser              | 2.96 sec                                                                   | 2.95 sec: 1.00x faster                                                            |
| 2to3                       | 221 ms                                                                     | 222 ms: 1.01x slower                                                              |
| dulwich_log                | 40.9 ms                                                                    | 41.2 ms: 1.01x slower                                                             |
| raytrace                   | 180 ms                                                                     | 182 ms: 1.01x slower                                                              |
| nqueens                    | 59.5 ms                                                                    | 60.2 ms: 1.01x slower                                                             |
| shortest_path              | 360 ms                                                                     | 365 ms: 1.01x slower                                                              |
| create_gc_cycles           | 1.32 ms                                                                    | 1.34 ms: 1.01x slower                                                             |
| json_dumps                 | 6.27 ms                                                                    | 6.36 ms: 1.01x slower                                                             |
| sympy_expand               | 285 ms                                                                     | 290 ms: 1.02x slower                                                              |
| chaos                      | 39.5 ms                                                                    | 40.2 ms: 1.02x slower                                                             |
| coroutines                 | 13.8 ms                                                                    | 14.1 ms: 1.02x slower                                                             |
| fannkuch                   | 253 ms                                                                     | 258 ms: 1.02x slower                                                              |
| pycparser                  | 709 ms                                                                     | 725 ms: 1.02x slower                                                              |
| regex_effbot               | 1.47 ms                                                                    | 1.51 ms: 1.03x slower                                                             |
| logging_simple             | 6.20 us                                                                    | 6.40 us: 1.03x slower                                                             |
| sphinx                     | 637 ms                                                                     | 661 ms: 1.04x slower                                                              |
| regex_dna                  | 117 ms                                                                     | 122 ms: 1.04x slower                                                              |
| regex_v8                   | 13.5 ms                                                                    | 14.0 ms: 1.04x slower                                                             |
| logging_format             | 6.60 us                                                                    | 6.92 us: 1.05x slower                                                             |
| deepcopy_memo              | 18.4 us                                                                    | 19.5 us: 1.06x slower                                                             |
| spectral_norm              | 58.1 ms                                                                    | 61.6 ms: 1.06x slower                                                             |
| Geometric mean             | (ref)                                                                      | 1.01x faster                                                                      |

Benchmark hidden because not significant (24): xml_etree_parse, python_startup_no_site, xml_etree_process, comprehensions, meteor_contest, xml_etree_iterparse, gc_traversal, scimark_sparse_mat_mult, docutils, django_template, logging_silent, python_startup, async_tree_io_tg, connected_components, sqlglot_v2_normalize, html5lib, sympy_sum, sympy_integrate, asyncio_websockets, sqlite_synth, k_core, thrift, pylint, pathlib

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown