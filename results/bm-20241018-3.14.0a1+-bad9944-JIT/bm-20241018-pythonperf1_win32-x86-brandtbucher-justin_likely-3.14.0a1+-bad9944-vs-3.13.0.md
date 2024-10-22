# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.06x faster
- HPT reliability: 75.82%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 266 ms: 1.05x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.05 sec: 1.13x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.0 ms: 1.05x faster                                                          |
| tornado_http   | 104 ms                                                          | 109 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none           | 246 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| async_tree_io             | 537 ms                                                          | 510 ms: 1.05x faster                                                           |
| async_tree_io_tg          | 509 ms                                                          | 547 ms: 1.07x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 322 ms: 1.18x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 59.6 ms: 1.37x faster                                                          |
| float          | 57.8 ms                                                         | 45.7 ms: 1.26x faster                                                          |
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.81 ms                                                         | 1.76 ms: 1.03x faster                                                          |
| regex_dna      | 117 ms                                                          | 118 ms: 1.02x slower                                                           |
| regex_compile  | 103 ms                                                          | 106 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 56.1 ms: 1.12x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.81 us: 1.10x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 42.3 ms: 1.06x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.03x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 21.2 us: 1.02x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 64.0 ms: 1.02x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.44 us: 1.01x slower                                                          |
| xml_etree_parse      | 109 ms                                                          | 110 ms: 1.01x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 164 us: 1.02x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 251 us: 1.05x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.74 ms: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| python_startup         | 24.3 ms                                                         | 26.9 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.78 ms: 1.26x faster                                                          |
| django_template | 32.7 ms                                                         | 33.1 ms: 1.01x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 53.7 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 790 us: 12.84x faster                                                          |
| coverage                  | 333 ms                                                          | 52.7 ms: 6.31x faster                                                          |
| deepcopy_memo             | 26.2 us                                                         | 16.7 us: 1.57x faster                                                          |
| nbody                     | 81.9 ms                                                         | 59.6 ms: 1.37x faster                                                          |
| deepcopy                  | 307 us                                                          | 231 us: 1.33x faster                                                           |
| scimark_sor               | 91.8 ms                                                         | 69.2 ms: 1.33x faster                                                          |
| scimark_monte_carlo       | 50.3 ms                                                         | 39.6 ms: 1.27x faster                                                          |
| float                     | 57.8 ms                                                         | 45.7 ms: 1.26x faster                                                          |
| mako                      | 7.31 ms                                                         | 5.78 ms: 1.26x faster                                                          |
| spectral_norm             | 71.3 ms                                                         | 57.8 ms: 1.23x faster                                                          |
| deepcopy_reduce           | 2.85 us                                                         | 2.38 us: 1.20x faster                                                          |
| go                        | 111 ms                                                          | 96.0 ms: 1.16x faster                                                          |
| crypto_pyaes              | 58.2 ms                                                         | 50.3 ms: 1.16x faster                                                          |
| fannkuch                  | 293 ms                                                          | 254 ms: 1.15x faster                                                           |
| tomli_loads               | 1.73 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| async_tree_none           | 246 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.55 ms: 1.14x faster                                                          |
| scimark_fft               | 206 ms                                                          | 184 ms: 1.12x faster                                                           |
| pprint_safe_repr          | 644 ms                                                          | 577 ms: 1.12x faster                                                           |
| xml_etree_generate        | 62.6 ms                                                         | 56.1 ms: 1.12x faster                                                          |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| logging_silent            | 61.6 ns                                                         | 55.7 ns: 1.11x faster                                                          |
| unpickle_list             | 3.09 us                                                         | 2.81 us: 1.10x faster                                                          |
| telco                     | 6.67 ms                                                         | 6.10 ms: 1.09x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.20 sec: 1.08x faster                                                         |
| meteor_contest            | 77.0 ms                                                         | 72.1 ms: 1.07x faster                                                          |
| xml_etree_process         | 45.0 ms                                                         | 42.3 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| scimark_lu                | 63.5 ms                                                         | 59.9 ms: 1.06x faster                                                          |
| pycparser                 | 869 ms                                                          | 824 ms: 1.06x faster                                                           |
| async_tree_io             | 537 ms                                                          | 510 ms: 1.05x faster                                                           |
| html5lib                  | 48.3 ms                                                         | 46.0 ms: 1.05x faster                                                          |
| unpack_sequence           | 42.9 ns                                                         | 41.2 ns: 1.04x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.24 us: 1.04x faster                                                          |
| logging_simple            | 7.87 us                                                         | 7.62 us: 1.03x faster                                                          |
| regex_effbot              | 1.81 ms                                                         | 1.76 ms: 1.03x faster                                                          |
| pyflate                   | 326 ms                                                          | 317 ms: 1.03x faster                                                           |
| unpickle                  | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| json_loads                | 21.0 us                                                         | 20.5 us: 1.03x faster                                                          |
| pickle_dict               | 21.7 us                                                         | 21.2 us: 1.02x faster                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 64.0 ms: 1.02x faster                                                          |
| pidigits                  | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| sqlglot_parse             | 1.05 ms                                                         | 1.04 ms: 1.01x faster                                                          |
| comprehensions            | 12.7 us                                                         | 12.8 us: 1.01x slower                                                          |
| pickle_list               | 3.40 us                                                         | 3.44 us: 1.01x slower                                                          |
| nqueens                   | 75.1 ms                                                         | 76.0 ms: 1.01x slower                                                          |
| django_template           | 32.7 ms                                                         | 33.1 ms: 1.01x slower                                                          |
| xml_etree_parse           | 109 ms                                                          | 110 ms: 1.01x slower                                                           |
| regex_dna                 | 117 ms                                                          | 118 ms: 1.02x slower                                                           |
| python_startup_no_site    | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| unpickle_pure_python      | 162 us                                                          | 164 us: 1.02x slower                                                           |
| genshi_text               | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| regex_compile             | 103 ms                                                          | 106 ms: 1.03x slower                                                           |
| sqlglot_transpile         | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 142 us: 1.04x slower                                                           |
| sympy_expand              | 375 ms                                                          | 392 ms: 1.05x slower                                                           |
| mdp                       | 1.67 sec                                                        | 1.75 sec: 1.05x slower                                                         |
| tornado_http              | 104 ms                                                          | 109 ms: 1.05x slower                                                           |
| sympy_str                 | 215 ms                                                          | 226 ms: 1.05x slower                                                           |
| 2to3                      | 253 ms                                                          | 266 ms: 1.05x slower                                                           |
| pickle_pure_python        | 238 us                                                          | 251 us: 1.05x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.58 ms: 1.07x slower                                                          |
| async_tree_io_tg          | 509 ms                                                          | 547 ms: 1.07x slower                                                           |
| chaos                     | 51.2 ms                                                         | 55.3 ms: 1.08x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.08x slower                                                           |
| genshi_xml                | 49.5 ms                                                         | 53.7 ms: 1.08x slower                                                          |
| generators                | 22.1 ms                                                         | 24.3 ms: 1.10x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 244 ms: 1.11x slower                                                           |
| python_startup            | 24.3 ms                                                         | 26.9 ms: 1.11x slower                                                          |
| json                      | 4.27 ms                                                         | 4.74 ms: 1.11x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| docutils                  | 1.82 sec                                                        | 2.05 sec: 1.13x slower                                                         |
| sympy_integrate           | 15.2 ms                                                         | 17.4 ms: 1.14x slower                                                          |
| richards                  | 33.8 ms                                                         | 38.8 ms: 1.15x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.42 ms: 1.17x slower                                                          |
| async_generators          | 274 ms                                                          | 322 ms: 1.18x slower                                                           |
| json_dumps                | 7.40 ms                                                         | 8.74 ms: 1.18x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 50.3 ms: 1.18x slower                                                          |
| richards_super            | 38.0 ms                                                         | 45.2 ms: 1.19x slower                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.83 ms: 1.26x slower                                                          |
| pylint                    | 225 ms                                                          | 284 ms: 1.27x slower                                                           |
| bench_mp_pool             | 74.3 ms                                                         | 94.1 ms: 1.27x slower                                                          |
| raytrace                  | 205 ms                                                          | 272 ms: 1.32x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 1.20 ms: 1.68x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (9): bench_thread_pool, pathlib, dulwich_log, pickle, sqlite_synth, async_tree_cpu_io_mixed_tg, regex_v8, asyncio_tcp_ssl, asyncio_tcp
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx

# HPT report

- Reliability score: 75.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown