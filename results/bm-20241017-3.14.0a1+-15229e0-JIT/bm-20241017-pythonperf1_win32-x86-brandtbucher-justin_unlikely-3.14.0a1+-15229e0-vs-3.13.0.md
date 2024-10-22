# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_unlikely
- machine: windows-x86
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.07x faster
- HPT reliability: 84.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 264 ms: 1.04x slower                                                             |
| docutils       | 1.82 sec                                                        | 2.05 sec: 1.12x slower                                                           |
| html5lib       | 48.3 ms                                                         | 46.6 ms: 1.04x faster                                                            |
| tornado_http   | 104 ms                                                          | 110 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none           | 246 ms                                                          | 218 ms: 1.13x faster                                                             |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                             |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                             |
| async_tree_none_tg        | 219 ms                                                          | 204 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 462 ms: 1.07x faster                                                             |
| async_tree_io             | 537 ms                                                          | 527 ms: 1.02x faster                                                             |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                           |
| async_tree_io_tg          | 509 ms                                                          | 555 ms: 1.09x slower                                                             |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                            |
| async_generators          | 274 ms                                                          | 314 ms: 1.15x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 57.1 ms: 1.43x faster                                                            |
| float          | 57.8 ms                                                         | 46.5 ms: 1.24x faster                                                            |
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                           | 1.22x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.0 ms: 1.04x faster                                                            |
| regex_dna      | 117 ms                                                          | 113 ms: 1.03x faster                                                             |
| regex_effbot   | 1.81 ms                                                         | 1.80 ms: 1.01x faster                                                            |
| regex_compile  | 103 ms                                                          | 105 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 55.0 ms: 1.14x faster                                                            |
| xml_etree_process    | 45.0 ms                                                         | 41.5 ms: 1.09x faster                                                            |
| unpickle_list        | 3.09 us                                                         | 2.98 us: 1.04x faster                                                            |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                             |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.0 ms: 1.03x faster                                                            |
| pickle_dict          | 21.7 us                                                         | 21.2 us: 1.02x faster                                                            |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.02x faster                                                            |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.01x faster                                                            |
| pickle               | 8.42 us                                                         | 8.55 us: 1.02x slower                                                            |
| pickle_pure_python   | 238 us                                                          | 244 us: 1.02x slower                                                             |
| json_dumps           | 7.40 ms                                                         | 7.95 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                     |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                            |
| python_startup         | 24.3 ms                                                         | 26.8 ms: 1.11x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.82 ms: 1.26x faster                                                            |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                            |
| genshi_text     | 22.4 ms                                                         | 24.6 ms: 1.10x slower                                                            |
| genshi_xml      | 49.5 ms                                                         | 55.2 ms: 1.11x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 794 us: 12.78x faster                                                            |
| coverage                  | 333 ms                                                          | 53.8 ms: 6.19x faster                                                            |
| sqlglot_normalize         | 220 ms                                                          | 103 ms: 2.14x faster                                                             |
| deepcopy_memo             | 26.2 us                                                         | 15.9 us: 1.64x faster                                                            |
| nbody                     | 81.9 ms                                                         | 57.1 ms: 1.43x faster                                                            |
| deepcopy                  | 307 us                                                          | 225 us: 1.36x faster                                                             |
| scimark_sor               | 91.8 ms                                                         | 68.1 ms: 1.35x faster                                                            |
| scimark_monte_carlo       | 50.3 ms                                                         | 39.6 ms: 1.27x faster                                                            |
| mako                      | 7.31 ms                                                         | 5.82 ms: 1.26x faster                                                            |
| deepcopy_reduce           | 2.85 us                                                         | 2.28 us: 1.25x faster                                                            |
| float                     | 57.8 ms                                                         | 46.5 ms: 1.24x faster                                                            |
| spectral_norm             | 71.3 ms                                                         | 58.3 ms: 1.22x faster                                                            |
| fannkuch                  | 293 ms                                                          | 244 ms: 1.20x faster                                                             |
| go                        | 111 ms                                                          | 94.8 ms: 1.18x faster                                                            |
| tomli_loads               | 1.73 sec                                                        | 1.49 sec: 1.16x faster                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 50.0 ms: 1.16x faster                                                            |
| pprint_safe_repr          | 644 ms                                                          | 564 ms: 1.14x faster                                                             |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.55 ms: 1.14x faster                                                            |
| xml_etree_generate        | 62.6 ms                                                         | 55.0 ms: 1.14x faster                                                            |
| scimark_fft               | 206 ms                                                          | 183 ms: 1.13x faster                                                             |
| logging_silent            | 61.6 ns                                                         | 54.6 ns: 1.13x faster                                                            |
| async_tree_none           | 246 ms                                                          | 218 ms: 1.13x faster                                                             |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                             |
| telco                     | 6.67 ms                                                         | 5.95 ms: 1.12x faster                                                            |
| pprint_pformat            | 1.30 sec                                                        | 1.17 sec: 1.11x faster                                                           |
| unpack_sequence           | 42.9 ns                                                         | 39.5 ns: 1.09x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                             |
| xml_etree_process         | 45.0 ms                                                         | 41.5 ms: 1.09x faster                                                            |
| async_tree_none_tg        | 219 ms                                                          | 204 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 462 ms: 1.07x faster                                                             |
| meteor_contest            | 77.0 ms                                                         | 73.1 ms: 1.05x faster                                                            |
| scimark_lu                | 63.5 ms                                                         | 60.6 ms: 1.05x faster                                                            |
| pyflate                   | 326 ms                                                          | 311 ms: 1.05x faster                                                             |
| pycparser                 | 869 ms                                                          | 833 ms: 1.04x faster                                                             |
| html5lib                  | 48.3 ms                                                         | 46.6 ms: 1.04x faster                                                            |
| unpickle_list             | 3.09 us                                                         | 2.98 us: 1.04x faster                                                            |
| regex_v8                  | 15.6 ms                                                         | 15.0 ms: 1.04x faster                                                            |
| unpickle_pure_python      | 162 us                                                          | 156 us: 1.04x faster                                                             |
| xml_etree_iterparse       | 65.1 ms                                                         | 63.0 ms: 1.03x faster                                                            |
| logging_simple            | 7.87 us                                                         | 7.65 us: 1.03x faster                                                            |
| regex_dna                 | 117 ms                                                          | 113 ms: 1.03x faster                                                             |
| logging_format            | 8.57 us                                                         | 8.37 us: 1.02x faster                                                            |
| pickle_dict               | 21.7 us                                                         | 21.2 us: 1.02x faster                                                            |
| json_loads                | 21.0 us                                                         | 20.5 us: 1.02x faster                                                            |
| pathlib                   | 89.4 ms                                                         | 87.7 ms: 1.02x faster                                                            |
| async_tree_io             | 537 ms                                                          | 527 ms: 1.02x faster                                                             |
| pidigits                  | 202 ms                                                          | 200 ms: 1.01x faster                                                             |
| unpickle                  | 10.5 us                                                         | 10.4 us: 1.01x faster                                                            |
| regex_effbot              | 1.81 ms                                                         | 1.80 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.5 sec: 1.01x slower                                                           |
| pickle                    | 8.42 us                                                         | 8.55 us: 1.02x slower                                                            |
| python_startup_no_site    | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                            |
| regex_compile             | 103 ms                                                          | 105 ms: 1.02x slower                                                             |
| django_template           | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                            |
| typing_runtime_protocols  | 136 us                                                          | 139 us: 1.02x slower                                                             |
| pickle_pure_python        | 238 us                                                          | 244 us: 1.02x slower                                                             |
| nqueens                   | 75.1 ms                                                         | 77.4 ms: 1.03x slower                                                            |
| comprehensions            | 12.7 us                                                         | 13.2 us: 1.03x slower                                                            |
| 2to3                      | 253 ms                                                          | 264 ms: 1.04x slower                                                             |
| tornado_http              | 104 ms                                                          | 110 ms: 1.05x slower                                                             |
| sqlglot_transpile         | 1.29 ms                                                         | 1.37 ms: 1.06x slower                                                            |
| sympy_expand              | 375 ms                                                          | 397 ms: 1.06x slower                                                             |
| deltablue                 | 2.41 ms                                                         | 2.57 ms: 1.07x slower                                                            |
| json_dumps                | 7.40 ms                                                         | 7.95 ms: 1.07x slower                                                            |
| sympy_str                 | 215 ms                                                          | 231 ms: 1.07x slower                                                             |
| mdp                       | 1.67 sec                                                        | 1.80 sec: 1.08x slower                                                           |
| chaos                     | 51.2 ms                                                         | 55.2 ms: 1.08x slower                                                            |
| async_tree_io_tg          | 509 ms                                                          | 555 ms: 1.09x slower                                                             |
| genshi_text               | 22.4 ms                                                         | 24.6 ms: 1.10x slower                                                            |
| sympy_sum                 | 108 ms                                                          | 119 ms: 1.10x slower                                                             |
| generators                | 22.1 ms                                                         | 24.3 ms: 1.10x slower                                                            |
| python_startup            | 24.3 ms                                                         | 26.8 ms: 1.11x slower                                                            |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                            |
| genshi_xml                | 49.5 ms                                                         | 55.2 ms: 1.11x slower                                                            |
| docutils                  | 1.82 sec                                                        | 2.05 sec: 1.12x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 17.4 ms: 1.15x slower                                                            |
| async_generators          | 274 ms                                                          | 314 ms: 1.15x slower                                                             |
| hexiom                    | 4.64 ms                                                         | 5.39 ms: 1.16x slower                                                            |
| richards                  | 33.8 ms                                                         | 39.3 ms: 1.16x slower                                                            |
| sqlglot_optimize          | 42.5 ms                                                         | 50.3 ms: 1.18x slower                                                            |
| json                      | 4.27 ms                                                         | 5.06 ms: 1.19x slower                                                            |
| richards_super            | 38.0 ms                                                         | 46.2 ms: 1.22x slower                                                            |
| gc_traversal              | 1.45 ms                                                         | 1.83 ms: 1.26x slower                                                            |
| pylint                    | 225 ms                                                          | 286 ms: 1.27x slower                                                             |
| bench_mp_pool             | 74.3 ms                                                         | 95.5 ms: 1.28x slower                                                            |
| raytrace                  | 205 ms                                                          | 273 ms: 1.33x slower                                                             |
| create_gc_cycles          | 713 us                                                          | 1.19 ms: 1.67x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.07x faster                                                                     |

Benchmark hidden because not significant (8): asyncio_tcp, bench_thread_pool, dulwich_log, async_tree_cpu_io_mixed_tg, pickle_list, sqlite_synth, sqlglot_parse, xml_etree_parse
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-pythonperf1_win32-x86-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx

# HPT report

- Reliability score: 84.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown