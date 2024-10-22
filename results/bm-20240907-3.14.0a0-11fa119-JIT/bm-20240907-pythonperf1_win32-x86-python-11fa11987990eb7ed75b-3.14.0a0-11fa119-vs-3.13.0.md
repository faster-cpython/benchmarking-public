# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.10x faster
- HPT reliability: 97.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 264 ms: 1.04x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.01 sec: 1.11x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.3 ms: 1.04x faster                                                          |
| tornado_http   | 104 ms                                                          | 110 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 678 ms: 1.24x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| async_tree_none           | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 524 ms: 1.03x slower                                                           |
| async_generators          | 274 ms                                                          | 322 ms: 1.18x slower                                                           |
| coroutines                | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 50.1 ms: 1.63x faster                                                          |
| float          | 57.8 ms                                                         | 44.5 ms: 1.30x faster                                                          |
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 101 ms: 1.03x faster                                                           |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| regex_dna      | 117 ms                                                          | 129 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate  | 62.6 ms                                                         | 53.3 ms: 1.17x faster                                                          |
| tomli_loads         | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| xml_etree_process   | 45.0 ms                                                         | 40.1 ms: 1.12x faster                                                          |
| unpickle_list       | 3.09 us                                                         | 2.79 us: 1.11x faster                                                          |
| pickle              | 8.42 us                                                         | 7.84 us: 1.07x faster                                                          |
| pickle_dict         | 21.7 us                                                         | 20.2 us: 1.07x faster                                                          |
| json_dumps          | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| xml_etree_iterparse | 65.1 ms                                                         | 62.4 ms: 1.04x faster                                                          |
| xml_etree_parse     | 109 ms                                                          | 105 ms: 1.04x faster                                                           |
| json_loads          | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| pickle_pure_python  | 238 us                                                          | 241 us: 1.01x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (3): unpickle_pure_python, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 25.0 ms: 1.03x slower                                                          |
| python_startup_no_site | 19.9 ms                                                         | 20.9 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.57 ms: 1.31x faster                                                          |
| django_template | 32.7 ms                                                         | 33.5 ms: 1.03x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 55.6 ms: 1.12x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 756 us: 13.42x faster                                                          |
| coverage                  | 333 ms                                                          | 54.7 ms: 6.09x faster                                                          |
| sqlglot_normalize         | 220 ms                                                          | 100 ms: 2.19x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 15.7 us: 1.67x faster                                                          |
| nbody                     | 81.9 ms                                                         | 50.1 ms: 1.63x faster                                                          |
| spectral_norm             | 71.3 ms                                                         | 49.2 ms: 1.45x faster                                                          |
| scimark_sor               | 91.8 ms                                                         | 68.1 ms: 1.35x faster                                                          |
| deepcopy                  | 307 us                                                          | 232 us: 1.32x faster                                                           |
| mako                      | 7.31 ms                                                         | 5.57 ms: 1.31x faster                                                          |
| float                     | 57.8 ms                                                         | 44.5 ms: 1.30x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 678 ms: 1.24x faster                                                           |
| fannkuch                  | 293 ms                                                          | 237 ms: 1.24x faster                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.40 ms: 1.21x faster                                                          |
| scimark_fft               | 206 ms                                                          | 172 ms: 1.20x faster                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 48.4 ms: 1.20x faster                                                          |
| pyflate                   | 326 ms                                                          | 275 ms: 1.18x faster                                                           |
| deltablue                 | 2.41 ms                                                         | 2.04 ms: 1.18x faster                                                          |
| xml_etree_generate        | 62.6 ms                                                         | 53.3 ms: 1.17x faster                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| deepcopy_reduce           | 2.85 us                                                         | 2.52 us: 1.13x faster                                                          |
| go                        | 111 ms                                                          | 98.9 ms: 1.13x faster                                                          |
| telco                     | 6.67 ms                                                         | 5.93 ms: 1.12x faster                                                          |
| pprint_safe_repr          | 644 ms                                                          | 574 ms: 1.12x faster                                                           |
| xml_etree_process         | 45.0 ms                                                         | 40.1 ms: 1.12x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| async_tree_none           | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| unpickle_list             | 3.09 us                                                         | 2.79 us: 1.11x faster                                                          |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.20 sec: 1.08x faster                                                         |
| pickle                    | 8.42 us                                                         | 7.84 us: 1.07x faster                                                          |
| pickle_dict               | 21.7 us                                                         | 20.2 us: 1.07x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 6.92 ms: 1.07x faster                                                          |
| comprehensions            | 12.7 us                                                         | 12.0 us: 1.06x faster                                                          |
| pycparser                 | 869 ms                                                          | 821 ms: 1.06x faster                                                           |
| json                      | 4.27 ms                                                         | 4.03 ms: 1.06x faster                                                          |
| sqlite_synth              | 1.97 us                                                         | 1.86 us: 1.06x faster                                                          |
| scimark_lu                | 63.5 ms                                                         | 60.3 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                           |
| richards_super            | 38.0 ms                                                         | 36.2 ms: 1.05x faster                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 62.4 ms: 1.04x faster                                                          |
| html5lib                  | 48.3 ms                                                         | 46.3 ms: 1.04x faster                                                          |
| xml_etree_parse           | 109 ms                                                          | 105 ms: 1.04x faster                                                           |
| meteor_contest            | 77.0 ms                                                         | 74.5 ms: 1.03x faster                                                          |
| richards                  | 33.8 ms                                                         | 32.9 ms: 1.03x faster                                                          |
| regex_compile             | 103 ms                                                          | 101 ms: 1.03x faster                                                           |
| pathlib                   | 89.4 ms                                                         | 87.4 ms: 1.02x faster                                                          |
| pidigits                  | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| json_loads                | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| logging_simple            | 7.87 us                                                         | 7.75 us: 1.02x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| scimark_monte_carlo       | 50.3 ms                                                         | 49.6 ms: 1.01x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.46 us: 1.01x faster                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| sqlglot_parse             | 1.05 ms                                                         | 1.04 ms: 1.01x faster                                                          |
| mdp                       | 1.67 sec                                                        | 1.68 sec: 1.00x slower                                                         |
| pickle_pure_python        | 238 us                                                          | 241 us: 1.01x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| django_template           | 32.7 ms                                                         | 33.5 ms: 1.03x slower                                                          |
| async_tree_io_tg          | 509 ms                                                          | 524 ms: 1.03x slower                                                           |
| unpack_sequence           | 42.9 ns                                                         | 44.2 ns: 1.03x slower                                                          |
| python_startup            | 24.3 ms                                                         | 25.0 ms: 1.03x slower                                                          |
| sympy_str                 | 215 ms                                                          | 224 ms: 1.04x slower                                                           |
| 2to3                      | 253 ms                                                          | 264 ms: 1.04x slower                                                           |
| sqlglot_transpile         | 1.29 ms                                                         | 1.35 ms: 1.04x slower                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 20.9 ms: 1.05x slower                                                          |
| tornado_http              | 104 ms                                                          | 110 ms: 1.05x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 752 us: 1.06x slower                                                           |
| genshi_text               | 22.4 ms                                                         | 23.7 ms: 1.06x slower                                                          |
| nqueens                   | 75.1 ms                                                         | 79.3 ms: 1.06x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 145 us: 1.06x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 115 ms: 1.07x slower                                                           |
| generators                | 22.1 ms                                                         | 23.6 ms: 1.07x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 4.96 ms: 1.07x slower                                                          |
| sympy_expand              | 375 ms                                                          | 402 ms: 1.07x slower                                                           |
| chaos                     | 51.2 ms                                                         | 55.0 ms: 1.07x slower                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 80.2 ms: 1.08x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 46.8 ms: 1.10x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 16.8 ms: 1.11x slower                                                          |
| regex_dna                 | 117 ms                                                          | 129 ms: 1.11x slower                                                           |
| docutils                  | 1.82 sec                                                        | 2.01 sec: 1.11x slower                                                         |
| genshi_xml                | 49.5 ms                                                         | 55.6 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 322 ms: 1.18x slower                                                           |
| coroutines                | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| pylint                    | 225 ms                                                          | 270 ms: 1.20x slower                                                           |
| raytrace                  | 205 ms                                                          | 248 ms: 1.21x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (8): bench_thread_pool, logging_silent, unpickle_pure_python, dulwich_log, async_tree_cpu_io_mixed_tg, unpickle, pickle_list, async_tree_io
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 97.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown