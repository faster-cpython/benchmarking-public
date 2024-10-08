# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.01x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 248 ms                                                                         | 253 ms: 1.02x slower                                                  |
| docutils       | 1.87 sec                                                                       | 1.86 sec: 1.00x faster                                                |
| html5lib       | 48.1 ms                                                                        | 46.9 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                                          | 1.00x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization | 271 ms                                                                         | 270 ms: 1.01x faster                                                  |
| async_generators       | 300 ms                                                                         | 307 ms: 1.02x slower                                                  |
| coroutines             | 18.0 ms                                                                        | 18.7 ms: 1.04x slower                                                 |
| Geometric mean         | (ref)                                                                          | 1.01x slower                                                          |

Benchmark hidden because not significant (9): async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 91.3 ms                                                                        | 90.2 ms: 1.01x faster                                                 |
| float          | 62.2 ms                                                                        | 63.2 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                          | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                                         | 119 ms: 1.01x slower                                                  |
| regex_effbot   | 1.88 ms                                                                        | 1.91 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                          |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|---------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads         | 1.93 sec                                                                       | 1.84 sec: 1.05x faster                                                |
| xml_etree_process   | 50.7 ms                                                                        | 48.6 ms: 1.04x faster                                                 |
| unpickle_list       | 2.96 us                                                                        | 2.85 us: 1.04x faster                                                 |
| xml_etree_generate  | 68.3 ms                                                                        | 67.0 ms: 1.02x faster                                                 |
| json_dumps          | 7.69 ms                                                                        | 7.57 ms: 1.02x faster                                                 |
| json_loads          | 20.8 us                                                                        | 20.6 us: 1.01x faster                                                 |
| unpickle            | 10.3 us                                                                        | 10.2 us: 1.01x faster                                                 |
| pickle_pure_python  | 257 us                                                                         | 260 us: 1.01x slower                                                  |
| xml_etree_parse     | 107 ms                                                                         | 108 ms: 1.01x slower                                                  |
| pickle_dict         | 20.3 us                                                                        | 20.6 us: 1.02x slower                                                 |
| xml_etree_iterparse | 66.8 ms                                                                        | 68.9 ms: 1.03x slower                                                 |
| pickle              | 7.77 us                                                                        | 8.03 us: 1.03x slower                                                 |
| Geometric mean      | (ref)                                                                          | 1.01x faster                                                          |

Benchmark hidden because not significant (2): pickle_list, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 19.8 ms                                                                        | 19.6 ms: 1.01x faster                                                 |
| python_startup         | 23.8 ms                                                                        | 23.7 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                          | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 33.7 ms                                                                        | 32.1 ms: 1.05x faster                                                 |
| genshi_xml      | 48.7 ms                                                                        | 47.6 ms: 1.02x faster                                                 |
| mako            | 7.99 ms                                                                        | 8.30 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                                          | 1.01x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:------------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_reduce          | 2.60 us                                                                        | 2.42 us: 1.08x faster                                                 |
| pprint_pformat           | 1.39 sec                                                                       | 1.32 sec: 1.05x faster                                                |
| django_template          | 33.7 ms                                                                        | 32.1 ms: 1.05x faster                                                 |
| tomli_loads              | 1.93 sec                                                                       | 1.84 sec: 1.05x faster                                                |
| pprint_safe_repr         | 665 ms                                                                         | 636 ms: 1.05x faster                                                  |
| xml_etree_process        | 50.7 ms                                                                        | 48.6 ms: 1.04x faster                                                 |
| unpickle_list            | 2.96 us                                                                        | 2.85 us: 1.04x faster                                                 |
| pycparser                | 884 ms                                                                         | 854 ms: 1.03x faster                                                  |
| json                     | 4.28 ms                                                                        | 4.16 ms: 1.03x faster                                                 |
| html5lib                 | 48.1 ms                                                                        | 46.9 ms: 1.03x faster                                                 |
| genshi_xml               | 48.7 ms                                                                        | 47.6 ms: 1.02x faster                                                 |
| unpack_sequence          | 47.1 ns                                                                        | 46.1 ns: 1.02x faster                                                 |
| xml_etree_generate       | 68.3 ms                                                                        | 67.0 ms: 1.02x faster                                                 |
| json_dumps               | 7.69 ms                                                                        | 7.57 ms: 1.02x faster                                                 |
| nbody                    | 91.3 ms                                                                        | 90.2 ms: 1.01x faster                                                 |
| sympy_expand             | 383 ms                                                                         | 380 ms: 1.01x faster                                                  |
| json_loads               | 20.8 us                                                                        | 20.6 us: 1.01x faster                                                 |
| python_startup_no_site   | 19.8 ms                                                                        | 19.6 ms: 1.01x faster                                                 |
| python_startup           | 23.8 ms                                                                        | 23.7 ms: 1.01x faster                                                 |
| unpickle                 | 10.3 us                                                                        | 10.2 us: 1.01x faster                                                 |
| deepcopy                 | 250 us                                                                         | 249 us: 1.01x faster                                                  |
| async_tree_memoization   | 271 ms                                                                         | 270 ms: 1.01x faster                                                  |
| docutils                 | 1.87 sec                                                                       | 1.86 sec: 1.00x faster                                                |
| raytrace                 | 236 ms                                                                         | 237 ms: 1.00x slower                                                  |
| logging_format           | 8.71 us                                                                        | 8.76 us: 1.01x slower                                                 |
| pathlib                  | 83.3 ms                                                                        | 83.8 ms: 1.01x slower                                                 |
| logging_silent           | 74.5 ns                                                                        | 75.2 ns: 1.01x slower                                                 |
| sqlglot_optimize         | 43.0 ms                                                                        | 43.4 ms: 1.01x slower                                                 |
| pickle_pure_python       | 257 us                                                                         | 260 us: 1.01x slower                                                  |
| coverage                 | 52.7 ms                                                                        | 53.2 ms: 1.01x slower                                                 |
| bench_mp_pool            | 71.5 ms                                                                        | 72.2 ms: 1.01x slower                                                 |
| xml_etree_parse          | 107 ms                                                                         | 108 ms: 1.01x slower                                                  |
| crypto_pyaes             | 57.3 ms                                                                        | 57.9 ms: 1.01x slower                                                 |
| logging_simple           | 8.00 us                                                                        | 8.09 us: 1.01x slower                                                 |
| regex_dna                | 118 ms                                                                         | 119 ms: 1.01x slower                                                  |
| sqlite_synth             | 1.93 us                                                                        | 1.95 us: 1.01x slower                                                 |
| regex_effbot             | 1.88 ms                                                                        | 1.91 ms: 1.01x slower                                                 |
| scimark_fft              | 233 ms                                                                         | 236 ms: 1.01x slower                                                  |
| float                    | 62.2 ms                                                                        | 63.2 ms: 1.02x slower                                                 |
| pickle_dict              | 20.3 us                                                                        | 20.6 us: 1.02x slower                                                 |
| sympy_sum                | 106 ms                                                                         | 108 ms: 1.02x slower                                                  |
| 2to3                     | 248 ms                                                                         | 253 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 3.07 ms                                                                        | 3.13 ms: 1.02x slower                                                 |
| dulwich_log              | 49.9 ms                                                                        | 50.8 ms: 1.02x slower                                                 |
| chaos                    | 53.4 ms                                                                        | 54.6 ms: 1.02x slower                                                 |
| async_generators         | 300 ms                                                                         | 307 ms: 1.02x slower                                                  |
| meteor_contest           | 79.8 ms                                                                        | 81.8 ms: 1.03x slower                                                 |
| telco                    | 6.37 ms                                                                        | 6.54 ms: 1.03x slower                                                 |
| sqlglot_normalize        | 223 ms                                                                         | 230 ms: 1.03x slower                                                  |
| xml_etree_iterparse      | 66.8 ms                                                                        | 68.9 ms: 1.03x slower                                                 |
| typing_runtime_protocols | 137 us                                                                         | 142 us: 1.03x slower                                                  |
| pyflate                  | 352 ms                                                                         | 364 ms: 1.03x slower                                                  |
| thrift                   | 742 us                                                                         | 766 us: 1.03x slower                                                  |
| pickle                   | 7.77 us                                                                        | 8.03 us: 1.03x slower                                                 |
| generators               | 26.2 ms                                                                        | 27.2 ms: 1.04x slower                                                 |
| mako                     | 7.99 ms                                                                        | 8.30 ms: 1.04x slower                                                 |
| coroutines               | 18.0 ms                                                                        | 18.7 ms: 1.04x slower                                                 |
| mdp                      | 1.70 sec                                                                       | 1.77 sec: 1.04x slower                                                |
| sqlglot_transpile        | 1.30 ms                                                                        | 1.36 ms: 1.04x slower                                                 |
| nqueens                  | 74.9 ms                                                                        | 78.2 ms: 1.04x slower                                                 |
| hexiom                   | 5.10 ms                                                                        | 5.33 ms: 1.04x slower                                                 |
| sqlglot_parse            | 1.05 ms                                                                        | 1.10 ms: 1.04x slower                                                 |
| richards_super           | 43.5 ms                                                                        | 45.6 ms: 1.05x slower                                                 |
| deltablue                | 2.68 ms                                                                        | 2.82 ms: 1.05x slower                                                 |
| go                       | 103 ms                                                                         | 109 ms: 1.05x slower                                                  |
| scimark_lu               | 68.1 ms                                                                        | 71.7 ms: 1.05x slower                                                 |
| deepcopy_memo            | 21.9 us                                                                        | 23.1 us: 1.05x slower                                                 |
| scimark_monte_carlo      | 55.4 ms                                                                        | 58.6 ms: 1.06x slower                                                 |
| comprehensions           | 13.8 us                                                                        | 14.6 us: 1.06x slower                                                 |
| scimark_sor              | 98.3 ms                                                                        | 105 ms: 1.06x slower                                                  |
| richards                 | 37.9 ms                                                                        | 40.5 ms: 1.07x slower                                                 |
| fannkuch                 | 314 ms                                                                         | 341 ms: 1.09x slower                                                  |
| spectral_norm            | 75.2 ms                                                                        | 82.1 ms: 1.09x slower                                                 |
| Geometric mean           | (ref)                                                                          | 1.01x slower                                                          |

Benchmark hidden because not significant (22): genshi_text, sympy_integrate, pylint, pidigits, async_tree_memoization_tg, tornado_http, regex_compile, asyncio_tcp_ssl, pickle_list, async_tree_none, gc_traversal, sympy_str, create_gc_cycles, bench_thread_pool, async_tree_cpu_io_mixed_tg, regex_v8, unpickle_pure_python, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, asyncio_tcp

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown