# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: windows-amd64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.91 sec                                                                    | 1.93 sec: 1.01x slower                                                         |
| html5lib       | 38.9 ms                                                                     | 39.8 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg | 631 ms                                                                      | 640 ms: 1.01x slower                                                           |
| async_tree_io    | 542 ms                                                                      | 553 ms: 1.02x slower                                                           |
| async_generators | 263 ms                                                                      | 270 ms: 1.03x slower                                                           |
| coroutines       | 13.6 ms                                                                     | 14.0 ms: 1.03x slower                                                          |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 46.9 ms                                                                     | 48.3 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                      | 115 ms: 1.01x faster                                                           |
| regex_compile  | 91.2 ms                                                                     | 92.5 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 14.4 us                                                                     | 14.6 us: 1.02x slower                                                          |
| tomli_loads          | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                         |
| unpickle_pure_python | 144 us                                                                      | 147 us: 1.02x slower                                                           |
| xml_etree_generate   | 50.5 ms                                                                     | 51.7 ms: 1.02x slower                                                          |
| xml_etree_process    | 35.8 ms                                                                     | 36.7 ms: 1.03x slower                                                          |
| pickle_pure_python   | 199 us                                                                      | 204 us: 1.03x slower                                                           |
| json_dumps           | 6.22 ms                                                                     | 6.62 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 28.0 ms                                                                     | 27.0 ms: 1.04x faster                                                          |
| genshi_xml      | 47.2 ms                                                                     | 46.8 ms: 1.01x faster                                                          |
| genshi_text     | 19.2 ms                                                                     | 19.6 ms: 1.02x slower                                                          |
| mako            | 4.96 ms                                                                     | 5.14 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20241022-pythonperf1-amd64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241025-pythonperf1-amd64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template          | 28.0 ms                                                                     | 27.0 ms: 1.04x faster                                                          |
| raytrace                 | 214 ms                                                                      | 207 ms: 1.04x faster                                                           |
| pycparser                | 730 ms                                                                      | 722 ms: 1.01x faster                                                           |
| create_gc_cycles         | 1.40 ms                                                                     | 1.39 ms: 1.01x faster                                                          |
| generators               | 23.2 ms                                                                     | 23.0 ms: 1.01x faster                                                          |
| regex_dna                | 116 ms                                                                      | 115 ms: 1.01x faster                                                           |
| genshi_xml               | 47.2 ms                                                                     | 46.8 ms: 1.01x faster                                                          |
| spectral_norm            | 54.0 ms                                                                     | 53.6 ms: 1.01x faster                                                          |
| sympy_expand             | 324 ms                                                                      | 325 ms: 1.00x slower                                                           |
| bench_mp_pool            | 89.1 ms                                                                     | 89.6 ms: 1.01x slower                                                          |
| pprint_safe_repr         | 450 ms                                                                      | 453 ms: 1.01x slower                                                           |
| sympy_str                | 192 ms                                                                      | 194 ms: 1.01x slower                                                           |
| sqlglot_optimize         | 43.3 ms                                                                     | 43.7 ms: 1.01x slower                                                          |
| docutils                 | 1.91 sec                                                                    | 1.93 sec: 1.01x slower                                                         |
| sympy_sum                | 103 ms                                                                      | 104 ms: 1.01x slower                                                           |
| sympy_integrate          | 15.5 ms                                                                     | 15.7 ms: 1.01x slower                                                          |
| scimark_sparse_mat_mult  | 2.17 ms                                                                     | 2.20 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 208 ms                                                                      | 211 ms: 1.01x slower                                                           |
| deepcopy                 | 193 us                                                                      | 196 us: 1.01x slower                                                           |
| regex_compile            | 91.2 ms                                                                     | 92.5 ms: 1.01x slower                                                          |
| async_tree_io_tg         | 631 ms                                                                      | 640 ms: 1.01x slower                                                           |
| coverage                 | 46.6 ms                                                                     | 47.2 ms: 1.01x slower                                                          |
| deltablue                | 2.32 ms                                                                     | 2.35 ms: 1.01x slower                                                          |
| richards                 | 33.7 ms                                                                     | 34.2 ms: 1.02x slower                                                          |
| meteor_contest           | 74.5 ms                                                                     | 75.7 ms: 1.02x slower                                                          |
| sqlglot_transpile        | 1.18 ms                                                                     | 1.20 ms: 1.02x slower                                                          |
| json_loads               | 14.4 us                                                                     | 14.6 us: 1.02x slower                                                          |
| pprint_pformat           | 928 ms                                                                      | 945 ms: 1.02x slower                                                           |
| tomli_loads              | 1.28 sec                                                                    | 1.30 sec: 1.02x slower                                                         |
| genshi_text              | 19.2 ms                                                                     | 19.6 ms: 1.02x slower                                                          |
| async_tree_io            | 542 ms                                                                      | 553 ms: 1.02x slower                                                           |
| unpickle_pure_python     | 144 us                                                                      | 147 us: 1.02x slower                                                           |
| telco                    | 4.67 ms                                                                     | 4.77 ms: 1.02x slower                                                          |
| html5lib                 | 38.9 ms                                                                     | 39.8 ms: 1.02x slower                                                          |
| json                     | 2.94 ms                                                                     | 3.01 ms: 1.02x slower                                                          |
| thrift                   | 513 us                                                                      | 525 us: 1.02x slower                                                           |
| deepcopy_reduce          | 1.88 us                                                                     | 1.92 us: 1.02x slower                                                          |
| xml_etree_generate       | 50.5 ms                                                                     | 51.7 ms: 1.02x slower                                                          |
| xml_etree_process        | 35.8 ms                                                                     | 36.7 ms: 1.03x slower                                                          |
| async_generators         | 263 ms                                                                      | 270 ms: 1.03x slower                                                           |
| pickle_pure_python       | 199 us                                                                      | 204 us: 1.03x slower                                                           |
| deepcopy_memo            | 16.5 us                                                                     | 17.0 us: 1.03x slower                                                          |
| mdp                      | 1.58 sec                                                                    | 1.62 sec: 1.03x slower                                                         |
| float                    | 46.9 ms                                                                     | 48.3 ms: 1.03x slower                                                          |
| coroutines               | 13.6 ms                                                                     | 14.0 ms: 1.03x slower                                                          |
| hexiom                   | 5.15 ms                                                                     | 5.33 ms: 1.04x slower                                                          |
| mako                     | 4.96 ms                                                                     | 5.14 ms: 1.04x slower                                                          |
| go                       | 90.0 ms                                                                     | 94.0 ms: 1.04x slower                                                          |
| typing_runtime_protocols | 114 us                                                                      | 119 us: 1.05x slower                                                           |
| chaos                    | 41.2 ms                                                                     | 43.2 ms: 1.05x slower                                                          |
| scimark_fft              | 156 ms                                                                      | 163 ms: 1.05x slower                                                           |
| pyflate                  | 285 ms                                                                      | 300 ms: 1.05x slower                                                           |
| crypto_pyaes             | 40.7 ms                                                                     | 42.8 ms: 1.05x slower                                                          |
| scimark_monte_carlo      | 37.3 ms                                                                     | 39.4 ms: 1.06x slower                                                          |
| json_dumps               | 6.22 ms                                                                     | 6.62 ms: 1.06x slower                                                          |
| scimark_sor              | 62.9 ms                                                                     | 67.9 ms: 1.08x slower                                                          |
| logging_silent           | 52.3 ns                                                                     | 57.6 ns: 1.10x slower                                                          |
| scimark_lu               | 52.8 ms                                                                     | 58.4 ms: 1.11x slower                                                          |
| Geometric mean           | (ref)                                                                       | 1.02x slower                                                                   |

Benchmark hidden because not significant (29): async_tree_cpu_io_mixed, python_startup_no_site, tornado_http, xml_etree_parse, async_tree_none_tg, logging_format, pidigits, dulwich_log, richards_super, fannkuch, regex_v8, nbody, async_tree_cpu_io_mixed_tg, python_startup, pathlib, nqueens, comprehensions, async_tree_memoization_tg, async_tree_none, regex_effbot, 2to3, gc_traversal, pylint, logging_simple, sqlglot_parse, sphinx, xml_etree_iterparse, async_tree_memoization, bench_thread_pool

- Geometric mean (including insignificant results): 1.013x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown