# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: windows-amd64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.016x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                      | 224 ms: 1.02x faster                                                        |
| docutils       | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 310 ms                                                                      | 304 ms: 1.02x faster                                                        |
| async_generators           | 221 ms                                                                      | 218 ms: 1.02x faster                                                        |
| async_tree_none_tg         | 176 ms                                                                      | 174 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 405 ms                                                                      | 401 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 342 ms: 1.01x faster                                                        |
| coroutines                 | 13.3 ms                                                                     | 13.6 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 47.9 ms                                                                     | 46.1 ms: 1.04x faster                                                       |
| nbody          | 75.3 ms                                                                     | 72.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 124 ms                                                                      | 117 ms: 1.06x faster                                                        |
| regex_compile  | 89.2 ms                                                                     | 86.4 ms: 1.03x faster                                                       |
| regex_v8       | 15.4 ms                                                                     | 14.9 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.46 sec                                                                    | 1.41 sec: 1.04x faster                                                      |
| unpickle_pure_python | 153 us                                                                      | 148 us: 1.04x faster                                                        |
| xml_etree_process    | 41.5 ms                                                                     | 40.4 ms: 1.03x faster                                                       |
| xml_etree_generate   | 58.2 ms                                                                     | 56.9 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 63.7 ms                                                                     | 62.7 ms: 1.02x faster                                                       |
| json_dumps           | 6.90 ms                                                                     | 6.83 ms: 1.01x faster                                                       |
| pickle_pure_python   | 228 us                                                                      | 226 us: 1.01x faster                                                        |
| json_loads           | 14.7 us                                                                     | 14.8 us: 1.01x slower                                                       |
| xml_etree_parse      | 89.8 ms                                                                     | 90.9 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20250226-pythonperf1-amd64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-pythonperf1-amd64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| scimark_lu                 | 68.7 ms                                                                     | 62.9 ms: 1.09x faster                                                       |
| scimark_sor                | 91.7 ms                                                                     | 84.2 ms: 1.09x faster                                                       |
| scimark_fft                | 194 ms                                                                      | 181 ms: 1.07x faster                                                        |
| deepcopy_memo              | 21.3 us                                                                     | 19.9 us: 1.07x faster                                                       |
| deltablue                  | 2.32 ms                                                                     | 2.19 ms: 1.06x faster                                                       |
| regex_dna                  | 124 ms                                                                      | 117 ms: 1.06x faster                                                        |
| fannkuch                   | 290 ms                                                                      | 274 ms: 1.06x faster                                                        |
| richards                   | 31.1 ms                                                                     | 29.5 ms: 1.05x faster                                                       |
| logging_silent             | 65.1 ns                                                                     | 61.7 ns: 1.05x faster                                                       |
| scimark_monte_carlo        | 46.7 ms                                                                     | 44.5 ms: 1.05x faster                                                       |
| pyflate                    | 319 ms                                                                      | 304 ms: 1.05x faster                                                        |
| richards_super             | 35.0 ms                                                                     | 33.5 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.70 ms                                                                     | 2.58 ms: 1.04x faster                                                       |
| float                      | 47.9 ms                                                                     | 46.1 ms: 1.04x faster                                                       |
| spectral_norm              | 60.7 ms                                                                     | 58.5 ms: 1.04x faster                                                       |
| tomli_loads                | 1.46 sec                                                                    | 1.41 sec: 1.04x faster                                                      |
| unpickle_pure_python       | 153 us                                                                      | 148 us: 1.04x faster                                                        |
| nbody                      | 75.3 ms                                                                     | 72.8 ms: 1.03x faster                                                       |
| raytrace                   | 198 ms                                                                      | 192 ms: 1.03x faster                                                        |
| regex_compile              | 89.2 ms                                                                     | 86.4 ms: 1.03x faster                                                       |
| chaos                      | 43.5 ms                                                                     | 42.2 ms: 1.03x faster                                                       |
| go                         | 89.2 ms                                                                     | 86.6 ms: 1.03x faster                                                       |
| regex_v8                   | 15.4 ms                                                                     | 14.9 ms: 1.03x faster                                                       |
| meteor_contest             | 77.0 ms                                                                     | 75.0 ms: 1.03x faster                                                       |
| xml_etree_process          | 41.5 ms                                                                     | 40.4 ms: 1.03x faster                                                       |
| hexiom                     | 4.46 ms                                                                     | 4.35 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.12 sec                                                                    | 1.09 sec: 1.03x faster                                                      |
| xml_etree_generate         | 58.2 ms                                                                     | 56.9 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 1.95 us                                                                     | 1.91 us: 1.02x faster                                                       |
| asyncio_websockets         | 310 ms                                                                      | 304 ms: 1.02x faster                                                        |
| bpe_tokeniser              | 2.94 sec                                                                    | 2.88 sec: 1.02x faster                                                      |
| pycparser                  | 749 ms                                                                      | 735 ms: 1.02x faster                                                        |
| deepcopy                   | 187 us                                                                      | 184 us: 1.02x faster                                                        |
| telco                      | 4.90 ms                                                                     | 4.81 ms: 1.02x faster                                                       |
| nqueens                    | 63.9 ms                                                                     | 62.8 ms: 1.02x faster                                                       |
| async_generators           | 221 ms                                                                      | 218 ms: 1.02x faster                                                        |
| coverage                   | 48.6 ms                                                                     | 47.8 ms: 1.02x faster                                                       |
| 2to3                       | 227 ms                                                                      | 224 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 63.7 ms                                                                     | 62.7 ms: 1.02x faster                                                       |
| comprehensions             | 11.6 us                                                                     | 11.4 us: 1.02x faster                                                       |
| crypto_pyaes               | 50.9 ms                                                                     | 50.1 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 35.4 ms                                                                     | 34.9 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 549 ms                                                                      | 542 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.11 ms                                                                     | 1.09 ms: 1.01x faster                                                       |
| docutils                   | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                      |
| logging_simple             | 6.47 us                                                                     | 6.40 us: 1.01x faster                                                       |
| dulwich_log                | 42.9 ms                                                                     | 42.5 ms: 1.01x faster                                                       |
| connected_components       | 322 ms                                                                      | 318 ms: 1.01x faster                                                        |
| json_dumps                 | 6.90 ms                                                                     | 6.83 ms: 1.01x faster                                                       |
| async_tree_none_tg         | 176 ms                                                                      | 174 ms: 1.01x faster                                                        |
| shortest_path              | 356 ms                                                                      | 352 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 405 ms                                                                      | 401 ms: 1.01x faster                                                        |
| pickle_pure_python         | 228 us                                                                      | 226 us: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 342 ms: 1.01x faster                                                        |
| sqlglot_parse              | 889 us                                                                      | 882 us: 1.01x faster                                                        |
| sympy_sum                  | 89.9 ms                                                                     | 89.4 ms: 1.01x faster                                                       |
| sympy_str                  | 175 ms                                                                      | 174 ms: 1.01x faster                                                        |
| sympy_integrate            | 13.4 ms                                                                     | 13.3 ms: 1.01x faster                                                       |
| subparsers                 | 16.1 ms                                                                     | 16.2 ms: 1.01x slower                                                       |
| json_loads                 | 14.7 us                                                                     | 14.8 us: 1.01x slower                                                       |
| xml_etree_parse            | 89.8 ms                                                                     | 90.9 ms: 1.01x slower                                                       |
| k_core                     | 1.72 sec                                                                    | 1.74 sec: 1.02x slower                                                      |
| json                       | 2.96 ms                                                                     | 3.01 ms: 1.02x slower                                                       |
| typing_runtime_protocols   | 107 us                                                                      | 109 us: 1.02x slower                                                        |
| coroutines                 | 13.3 ms                                                                     | 13.6 ms: 1.02x slower                                                       |
| mdp                        | 1.51 sec                                                                    | 1.61 sec: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (28): sphinx, async_tree_memoization_tg, logging_format, create_gc_cycles, pylint, bench_thread_pool, generators, async_tree_memoization, sqlite_synth, sqlglot_normalize, html5lib, regex_effbot, async_tree_io, async_tree_cpu_io_mixed, gc_traversal, async_tree_none, bench_mp_pool, thrift, sympy_expand, pidigits, mako, many_optionals, genshi_xml, pathlib, python_startup_no_site, python_startup, genshi_text, django_template

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown