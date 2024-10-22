# Results vs. base

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.00x slower
- HPT reliability: 55.06%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| docutils       | 1.88 sec                                                                       | 1.84 sec: 1.02x faster                                                                   |
| html5lib       | 47.3 ms                                                                        | 44.7 ms: 1.06x faster                                                                    |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                             |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_generators | 301 ms                                                                         | 303 ms: 1.01x slower                                                                     |
| async_tree_none  | 213 ms                                                                         | 218 ms: 1.02x slower                                                                     |
| Geometric mean   | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_cpu_io_mixed, coroutines, async_tree_io_tg, async_tree_memoization, asyncio_tcp_ssl, async_tree_io, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                                         | 201 ms: 1.01x slower                                                                     |
| nbody          | 86.7 ms                                                                        | 89.4 ms: 1.03x slower                                                                    |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                                         | 113 ms: 1.04x faster                                                                     |
| regex_effbot   | 1.84 ms                                                                        | 1.79 ms: 1.03x faster                                                                    |
| regex_v8       | 15.7 ms                                                                        | 15.3 ms: 1.02x faster                                                                    |
| Geometric mean | (ref)                                                                          | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| tomli_loads          | 1.87 sec                                                                       | 1.77 sec: 1.06x faster                                                                   |
| xml_etree_process    | 48.3 ms                                                                        | 47.4 ms: 1.02x faster                                                                    |
| xml_etree_generate   | 67.7 ms                                                                        | 66.6 ms: 1.02x faster                                                                    |
| json_loads           | 21.0 us                                                                        | 20.7 us: 1.01x faster                                                                    |
| xml_etree_iterparse  | 68.7 ms                                                                        | 68.1 ms: 1.01x faster                                                                    |
| pickle               | 8.55 us                                                                        | 8.48 us: 1.01x faster                                                                    |
| unpickle_pure_python | 177 us                                                                         | 180 us: 1.02x slower                                                                     |
| pickle_list          | 3.42 us                                                                        | 3.50 us: 1.02x slower                                                                    |
| pickle_pure_python   | 265 us                                                                         | 272 us: 1.03x slower                                                                     |
| unpickle             | 10.1 us                                                                        | 10.4 us: 1.03x slower                                                                    |
| unpickle_list        | 2.89 us                                                                        | 2.99 us: 1.03x slower                                                                    |
| Geometric mean       | (ref)                                                                          | 1.00x slower                                                                             |

Benchmark hidden because not significant (3): json_dumps, pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup_no_site | 20.7 ms                                                                        | 20.0 ms: 1.03x faster                                                                    |
| python_startup         | 24.9 ms                                                                        | 24.3 ms: 1.02x faster                                                                    |
| Geometric mean         | (ref)                                                                          | 1.03x faster                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template | 34.8 ms                                                                        | 32.8 ms: 1.06x faster                                                                    |
| genshi_text     | 21.5 ms                                                                        | 20.6 ms: 1.04x faster                                                                    |
| genshi_xml      | 47.0 ms                                                                        | 45.6 ms: 1.03x faster                                                                    |
| mako            | 7.76 ms                                                                        | 7.86 ms: 1.01x slower                                                                    |
| Geometric mean  | (ref)                                                                          | 1.03x faster                                                                             |

All benchmarks:
===============

| Benchmark                | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| django_template          | 34.8 ms                                                                        | 32.8 ms: 1.06x faster                                                                    |
| html5lib                 | 47.3 ms                                                                        | 44.7 ms: 1.06x faster                                                                    |
| tomli_loads              | 1.87 sec                                                                       | 1.77 sec: 1.06x faster                                                                   |
| genshi_text              | 21.5 ms                                                                        | 20.6 ms: 1.04x faster                                                                    |
| regex_dna                | 117 ms                                                                         | 113 ms: 1.04x faster                                                                     |
| python_startup_no_site   | 20.7 ms                                                                        | 20.0 ms: 1.03x faster                                                                    |
| crypto_pyaes             | 61.1 ms                                                                        | 59.2 ms: 1.03x faster                                                                    |
| genshi_xml               | 47.0 ms                                                                        | 45.6 ms: 1.03x faster                                                                    |
| regex_effbot             | 1.84 ms                                                                        | 1.79 ms: 1.03x faster                                                                    |
| regex_v8                 | 15.7 ms                                                                        | 15.3 ms: 1.02x faster                                                                    |
| python_startup           | 24.9 ms                                                                        | 24.3 ms: 1.02x faster                                                                    |
| sqlglot_normalize        | 229 ms                                                                         | 224 ms: 1.02x faster                                                                     |
| sympy_sum                | 108 ms                                                                         | 106 ms: 1.02x faster                                                                     |
| xml_etree_process        | 48.3 ms                                                                        | 47.4 ms: 1.02x faster                                                                    |
| telco                    | 6.98 ms                                                                        | 6.86 ms: 1.02x faster                                                                    |
| docutils                 | 1.88 sec                                                                       | 1.84 sec: 1.02x faster                                                                   |
| deepcopy                 | 245 us                                                                         | 241 us: 1.02x faster                                                                     |
| xml_etree_generate       | 67.7 ms                                                                        | 66.6 ms: 1.02x faster                                                                    |
| nqueens                  | 74.7 ms                                                                        | 73.5 ms: 1.02x faster                                                                    |
| sqlite_synth             | 1.97 us                                                                        | 1.94 us: 1.02x faster                                                                    |
| json_loads               | 21.0 us                                                                        | 20.7 us: 1.01x faster                                                                    |
| bench_thread_pool        | 1.01 ms                                                                        | 997 us: 1.01x faster                                                                     |
| sqlglot_optimize         | 44.0 ms                                                                        | 43.5 ms: 1.01x faster                                                                    |
| sympy_integrate          | 15.6 ms                                                                        | 15.4 ms: 1.01x faster                                                                    |
| sympy_str                | 219 ms                                                                         | 216 ms: 1.01x faster                                                                     |
| create_gc_cycles         | 783 us                                                                         | 774 us: 1.01x faster                                                                     |
| dulwich_log              | 51.7 ms                                                                        | 51.2 ms: 1.01x faster                                                                    |
| scimark_lu               | 68.5 ms                                                                        | 67.8 ms: 1.01x faster                                                                    |
| logging_simple           | 7.84 us                                                                        | 7.77 us: 1.01x faster                                                                    |
| xml_etree_iterparse      | 68.7 ms                                                                        | 68.1 ms: 1.01x faster                                                                    |
| pickle                   | 8.55 us                                                                        | 8.48 us: 1.01x faster                                                                    |
| sympy_expand             | 386 ms                                                                         | 384 ms: 1.01x faster                                                                     |
| pprint_pformat           | 1.32 sec                                                                       | 1.31 sec: 1.01x faster                                                                   |
| bench_mp_pool            | 74.0 ms                                                                        | 73.6 ms: 1.01x faster                                                                    |
| generators               | 23.5 ms                                                                        | 23.6 ms: 1.00x slower                                                                    |
| async_generators         | 301 ms                                                                         | 303 ms: 1.01x slower                                                                     |
| json                     | 4.27 ms                                                                        | 4.30 ms: 1.01x slower                                                                    |
| pidigits                 | 199 ms                                                                         | 201 ms: 1.01x slower                                                                     |
| mdp                      | 1.71 sec                                                                       | 1.72 sec: 1.01x slower                                                                   |
| comprehensions           | 13.1 us                                                                        | 13.3 us: 1.01x slower                                                                    |
| scimark_monte_carlo      | 55.9 ms                                                                        | 56.7 ms: 1.01x slower                                                                    |
| mako                     | 7.76 ms                                                                        | 7.86 ms: 1.01x slower                                                                    |
| deepcopy_reduce          | 2.49 us                                                                        | 2.53 us: 1.02x slower                                                                    |
| richards_super           | 45.3 ms                                                                        | 46.0 ms: 1.02x slower                                                                    |
| pyflate                  | 356 ms                                                                         | 362 ms: 1.02x slower                                                                     |
| chaos                    | 55.0 ms                                                                        | 55.9 ms: 1.02x slower                                                                    |
| unpickle_pure_python     | 177 us                                                                         | 180 us: 1.02x slower                                                                     |
| async_tree_none          | 213 ms                                                                         | 218 ms: 1.02x slower                                                                     |
| sqlglot_transpile        | 1.30 ms                                                                        | 1.33 ms: 1.02x slower                                                                    |
| raytrace                 | 243 ms                                                                         | 249 ms: 1.02x slower                                                                     |
| pickle_list              | 3.42 us                                                                        | 3.50 us: 1.02x slower                                                                    |
| spectral_norm            | 74.0 ms                                                                        | 75.9 ms: 1.03x slower                                                                    |
| scimark_sor              | 99.4 ms                                                                        | 102 ms: 1.03x slower                                                                     |
| pickle_pure_python       | 265 us                                                                         | 272 us: 1.03x slower                                                                     |
| unpickle                 | 10.1 us                                                                        | 10.4 us: 1.03x slower                                                                    |
| nbody                    | 86.7 ms                                                                        | 89.4 ms: 1.03x slower                                                                    |
| go                       | 99.3 ms                                                                        | 103 ms: 1.03x slower                                                                     |
| unpickle_list            | 2.89 us                                                                        | 2.99 us: 1.03x slower                                                                    |
| sqlglot_parse            | 1.06 ms                                                                        | 1.09 ms: 1.03x slower                                                                    |
| deepcopy_memo            | 21.3 us                                                                        | 22.1 us: 1.04x slower                                                                    |
| typing_runtime_protocols | 139 us                                                                         | 145 us: 1.05x slower                                                                     |
| fannkuch                 | 308 ms                                                                         | 324 ms: 1.05x slower                                                                     |
| logging_silent           | 67.4 ns                                                                        | 73.2 ns: 1.09x slower                                                                    |
| unpack_sequence          | 43.4 ns                                                                        | 52.3 ns: 1.20x slower                                                                    |
| Geometric mean           | (ref)                                                                          | 1.00x slower                                                                             |

Benchmark hidden because not significant (31): async_tree_cpu_io_mixed_tg, regex_compile, gc_traversal, scimark_sparse_mat_mult, hexiom, pathlib, meteor_contest, scimark_fft, asyncio_tcp, coverage, tornado_http, async_tree_cpu_io_mixed, pycparser, coroutines, logging_format, json_dumps, thrift, pickle_dict, pprint_safe_repr, async_tree_io_tg, async_tree_memoization, 2to3, float, xml_etree_parse, asyncio_tcp_ssl, pylint, deltablue, async_tree_io, async_tree_memoization_tg, richards, async_tree_none_tg

# HPT report

- Reliability score: 55.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown