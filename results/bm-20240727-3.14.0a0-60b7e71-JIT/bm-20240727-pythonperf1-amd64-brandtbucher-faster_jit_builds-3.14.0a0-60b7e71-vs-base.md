# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: windows-amd64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.00x faster
- HPT reliability: 52.67%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_generators | 260 ms                                                                     | 252 ms: 1.03x faster                                                          |
| coroutines       | 13.2 ms                                                                    | 13.3 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl  | 1.38 sec                                                                   | 1.46 sec: 1.06x slower                                                        |
| Geometric mean   | (ref)                                                                      | 1.00x slower                                                                  |

Benchmark hidden because not significant (9): asyncio_tcp, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                     | 150 ms: 1.00x slower                                                          |
| float          | 43.6 ms                                                                    | 43.9 ms: 1.01x slower                                                         |
| nbody          | 49.8 ms                                                                    | 50.9 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 1.61 ms                                                                    | 1.60 ms: 1.01x faster                                                         |
| regex_compile  | 88.3 ms                                                                    | 89.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.02x faster                                                                  |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| json_dumps         | 5.86 ms                                                                    | 5.80 ms: 1.01x faster                                                         |
| tomli_loads        | 1.24 sec                                                                   | 1.25 sec: 1.01x slower                                                        |
| json_loads         | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                         |
| pickle_pure_python | 179 us                                                                     | 181 us: 1.01x slower                                                          |
| xml_etree_parse    | 90.8 ms                                                                    | 92.7 ms: 1.02x slower                                                         |
| Geometric mean     | (ref)                                                                      | 1.00x slower                                                                  |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_process, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml     | 44.1 ms                                                                    | 44.7 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                  |

Benchmark hidden because not significant (3): django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240725-pythonperf1-amd64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-pythonperf1-amd64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| scimark_sor              | 90.8 ms                                                                    | 86.1 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult  | 2.09 ms                                                                    | 2.01 ms: 1.04x faster                                                         |
| fannkuch                 | 227 ms                                                                     | 219 ms: 1.04x faster                                                          |
| coverage                 | 48.7 ms                                                                    | 47.0 ms: 1.03x faster                                                         |
| nqueens                  | 61.0 ms                                                                    | 59.0 ms: 1.03x faster                                                         |
| async_generators         | 260 ms                                                                     | 252 ms: 1.03x faster                                                          |
| logging_silent           | 57.0 ns                                                                    | 55.4 ns: 1.03x faster                                                         |
| telco                    | 4.59 ms                                                                    | 4.47 ms: 1.03x faster                                                         |
| mdp                      | 1.49 sec                                                                   | 1.45 sec: 1.02x faster                                                        |
| meteor_contest           | 73.2 ms                                                                    | 71.8 ms: 1.02x faster                                                         |
| thrift                   | 511 us                                                                     | 502 us: 1.02x faster                                                          |
| pprint_pformat           | 967 ms                                                                     | 950 ms: 1.02x faster                                                          |
| create_gc_cycles         | 924 us                                                                     | 910 us: 1.02x faster                                                          |
| generators               | 21.8 ms                                                                    | 21.6 ms: 1.01x faster                                                         |
| gc_traversal             | 1.59 ms                                                                    | 1.58 ms: 1.01x faster                                                         |
| raytrace                 | 177 ms                                                                     | 176 ms: 1.01x faster                                                          |
| regex_effbot             | 1.61 ms                                                                    | 1.60 ms: 1.01x faster                                                         |
| json_dumps               | 5.86 ms                                                                    | 5.80 ms: 1.01x faster                                                         |
| sympy_integrate          | 14.4 ms                                                                    | 14.2 ms: 1.01x faster                                                         |
| bench_mp_pool            | 73.2 ms                                                                    | 72.6 ms: 1.01x faster                                                         |
| deepcopy                 | 183 us                                                                     | 182 us: 1.01x faster                                                          |
| sqlglot_optimize         | 36.6 ms                                                                    | 36.4 ms: 1.01x faster                                                         |
| pathlib                  | 81.9 ms                                                                    | 81.4 ms: 1.01x faster                                                         |
| sympy_expand             | 316 ms                                                                     | 315 ms: 1.00x faster                                                          |
| pidigits                 | 150 ms                                                                     | 150 ms: 1.00x slower                                                          |
| sqlglot_normalize        | 191 ms                                                                     | 192 ms: 1.01x slower                                                          |
| coroutines               | 13.2 ms                                                                    | 13.3 ms: 1.01x slower                                                         |
| tomli_loads              | 1.24 sec                                                                   | 1.25 sec: 1.01x slower                                                        |
| float                    | 43.6 ms                                                                    | 43.9 ms: 1.01x slower                                                         |
| json_loads               | 14.1 us                                                                    | 14.2 us: 1.01x slower                                                         |
| deltablue                | 2.13 ms                                                                    | 2.14 ms: 1.01x slower                                                         |
| spectral_norm            | 45.6 ms                                                                    | 46.1 ms: 1.01x slower                                                         |
| regex_compile            | 88.3 ms                                                                    | 89.4 ms: 1.01x slower                                                         |
| go                       | 94.2 ms                                                                    | 95.4 ms: 1.01x slower                                                         |
| genshi_xml               | 44.1 ms                                                                    | 44.7 ms: 1.01x slower                                                         |
| hexiom                   | 4.59 ms                                                                    | 4.65 ms: 1.01x slower                                                         |
| pickle_pure_python       | 179 us                                                                     | 181 us: 1.01x slower                                                          |
| scimark_monte_carlo      | 36.8 ms                                                                    | 37.4 ms: 1.02x slower                                                         |
| crypto_pyaes             | 39.8 ms                                                                    | 40.5 ms: 1.02x slower                                                         |
| xml_etree_parse          | 90.8 ms                                                                    | 92.7 ms: 1.02x slower                                                         |
| nbody                    | 49.8 ms                                                                    | 50.9 ms: 1.02x slower                                                         |
| logging_format           | 6.10 us                                                                    | 6.24 us: 1.02x slower                                                         |
| scimark_lu               | 70.3 ms                                                                    | 72.0 ms: 1.02x slower                                                         |
| logging_simple           | 5.63 us                                                                    | 5.80 us: 1.03x slower                                                         |
| typing_runtime_protocols | 114 us                                                                     | 118 us: 1.03x slower                                                          |
| asyncio_tcp_ssl          | 1.38 sec                                                                   | 1.46 sec: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                  |

Benchmark hidden because not significant (42): regex_v8, asyncio_tcp, pyflate, pycparser, unpickle_pure_python, chaos, async_tree_memoization_tg, json, regex_dna, sympy_str, pylint, async_tree_none_tg, deepcopy_memo, async_tree_cpu_io_mixed, sympy_sum, sqlglot_transpile, async_tree_cpu_io_mixed_tg, pprint_safe_repr, richards_super, docutils, django_template, async_tree_none, scimark_fft, genshi_text, bench_thread_pool, html5lib, comprehensions, mako, xml_etree_process, sqlglot_parse, 2to3, xml_etree_generate, dulwich_log, richards, python_startup, async_tree_memoization, xml_etree_iterparse, async_tree_io_tg, tornado_http, deepcopy_reduce, python_startup_no_site, async_tree_io

# HPT report

- Reliability score: 52.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown