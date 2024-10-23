# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.10x faster
- HPT reliability: 99.47%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 255 ms: 1.01x slower                                                     |
| docutils       | 1.82 sec                                                        | 1.97 sec: 1.08x slower                                                   |
| html5lib       | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                    |
| tornado_http   | 104 ms                                                          | 109 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                           | 1.02x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                     |
| async_tree_none           | 246 ms                                                          | 217 ms: 1.14x faster                                                     |
| async_tree_none_tg        | 219 ms                                                          | 200 ms: 1.09x faster                                                     |
| async_tree_memoization    | 302 ms                                                          | 277 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                     |
| async_tree_io             | 537 ms                                                          | 522 ms: 1.03x faster                                                     |
| async_tree_io_tg          | 509 ms                                                          | 549 ms: 1.08x slower                                                     |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                    |
| async_generators          | 274 ms                                                          | 319 ms: 1.16x slower                                                     |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                             |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 57.9 ms: 1.41x faster                                                    |
| float          | 57.8 ms                                                         | 45.9 ms: 1.26x faster                                                    |
| pidigits       | 202 ms                                                          | 203 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                           | 1.21x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 97.7 ms: 1.06x faster                                                    |
| regex_dna      | 117 ms                                                          | 113 ms: 1.03x faster                                                     |
| regex_effbot   | 1.81 ms                                                         | 1.76 ms: 1.03x faster                                                    |
| regex_v8       | 15.6 ms                                                         | 15.2 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                           | 1.04x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                   |
| xml_etree_generate   | 62.6 ms                                                         | 54.9 ms: 1.14x faster                                                    |
| xml_etree_process    | 45.0 ms                                                         | 40.8 ms: 1.10x faster                                                    |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.5 ms: 1.02x faster                                                    |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                    |
| json_dumps           | 7.40 ms                                                         | 8.03 ms: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                             |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                                    |
| python_startup         | 24.3 ms                                                         | 27.0 ms: 1.11x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.68 ms: 1.29x faster                                                    |
| genshi_xml      | 49.5 ms                                                         | 48.9 ms: 1.01x faster                                                    |
| django_template | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                    |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 784 us: 12.94x faster                                                    |
| coverage                  | 333 ms                                                          | 53.3 ms: 6.24x faster                                                    |
| sqlglot_normalize         | 220 ms                                                          | 99.3 ms: 2.22x faster                                                    |
| deepcopy_memo             | 26.2 us                                                         | 15.8 us: 1.65x faster                                                    |
| nbody                     | 81.9 ms                                                         | 57.9 ms: 1.41x faster                                                    |
| scimark_sor               | 91.8 ms                                                         | 67.0 ms: 1.37x faster                                                    |
| scimark_monte_carlo       | 50.3 ms                                                         | 37.9 ms: 1.33x faster                                                    |
| deepcopy                  | 307 us                                                          | 233 us: 1.32x faster                                                     |
| mako                      | 7.31 ms                                                         | 5.68 ms: 1.29x faster                                                    |
| fannkuch                  | 293 ms                                                          | 232 ms: 1.27x faster                                                     |
| float                     | 57.8 ms                                                         | 45.9 ms: 1.26x faster                                                    |
| go                        | 111 ms                                                          | 89.2 ms: 1.25x faster                                                    |
| spectral_norm             | 71.3 ms                                                         | 58.7 ms: 1.21x faster                                                    |
| deepcopy_reduce           | 2.85 us                                                         | 2.36 us: 1.21x faster                                                    |
| crypto_pyaes              | 58.2 ms                                                         | 48.9 ms: 1.19x faster                                                    |
| scimark_fft               | 206 ms                                                          | 175 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.48 ms: 1.17x faster                                                    |
| pprint_safe_repr          | 644 ms                                                          | 556 ms: 1.16x faster                                                     |
| pprint_pformat            | 1.30 sec                                                        | 1.13 sec: 1.15x faster                                                   |
| tomli_loads               | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                   |
| xml_etree_generate        | 62.6 ms                                                         | 54.9 ms: 1.14x faster                                                    |
| async_tree_memoization_tg | 287 ms                                                          | 252 ms: 1.14x faster                                                     |
| async_tree_none           | 246 ms                                                          | 217 ms: 1.14x faster                                                     |
| logging_silent            | 61.6 ns                                                         | 55.1 ns: 1.12x faster                                                    |
| pycparser                 | 869 ms                                                          | 781 ms: 1.11x faster                                                     |
| xml_etree_process         | 45.0 ms                                                         | 40.8 ms: 1.10x faster                                                    |
| scimark_lu                | 63.5 ms                                                         | 57.7 ms: 1.10x faster                                                    |
| async_tree_none_tg        | 219 ms                                                          | 200 ms: 1.09x faster                                                     |
| async_tree_memoization    | 302 ms                                                          | 277 ms: 1.09x faster                                                     |
| meteor_contest            | 77.0 ms                                                         | 70.7 ms: 1.09x faster                                                    |
| pyflate                   | 326 ms                                                          | 300 ms: 1.09x faster                                                     |
| telco                     | 6.67 ms                                                         | 6.16 ms: 1.08x faster                                                    |
| regex_compile             | 103 ms                                                          | 97.7 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                     |
| logging_simple            | 7.87 us                                                         | 7.50 us: 1.05x faster                                                    |
| sqlglot_parse             | 1.05 ms                                                         | 1.01 ms: 1.04x faster                                                    |
| html5lib                  | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                    |
| logging_format            | 8.57 us                                                         | 8.23 us: 1.04x faster                                                    |
| unpickle_pure_python      | 162 us                                                          | 156 us: 1.04x faster                                                     |
| regex_dna                 | 117 ms                                                          | 113 ms: 1.03x faster                                                     |
| regex_effbot              | 1.81 ms                                                         | 1.76 ms: 1.03x faster                                                    |
| async_tree_io             | 537 ms                                                          | 522 ms: 1.03x faster                                                     |
| xml_etree_iterparse       | 65.1 ms                                                         | 63.5 ms: 1.02x faster                                                    |
| nqueens                   | 75.1 ms                                                         | 73.4 ms: 1.02x faster                                                    |
| regex_v8                  | 15.6 ms                                                         | 15.2 ms: 1.02x faster                                                    |
| dulwich_log               | 49.7 ms                                                         | 48.7 ms: 1.02x faster                                                    |
| comprehensions            | 12.7 us                                                         | 12.5 us: 1.02x faster                                                    |
| genshi_xml                | 49.5 ms                                                         | 48.9 ms: 1.01x faster                                                    |
| pathlib                   | 89.4 ms                                                         | 88.4 ms: 1.01x faster                                                    |
| django_template           | 32.7 ms                                                         | 32.4 ms: 1.01x faster                                                    |
| json_loads                | 21.0 us                                                         | 20.8 us: 1.01x faster                                                    |
| pidigits                  | 202 ms                                                          | 203 ms: 1.01x slower                                                     |
| 2to3                      | 253 ms                                                          | 255 ms: 1.01x slower                                                     |
| sqlglot_transpile         | 1.29 ms                                                         | 1.30 ms: 1.01x slower                                                    |
| hexiom                    | 4.64 ms                                                         | 4.70 ms: 1.01x slower                                                    |
| generators                | 22.1 ms                                                         | 22.4 ms: 1.01x slower                                                    |
| typing_runtime_protocols  | 136 us                                                          | 139 us: 1.02x slower                                                     |
| sympy_expand              | 375 ms                                                          | 382 ms: 1.02x slower                                                     |
| sympy_str                 | 215 ms                                                          | 219 ms: 1.02x slower                                                     |
| richards                  | 33.8 ms                                                         | 34.9 ms: 1.03x slower                                                    |
| chaos                     | 51.2 ms                                                         | 53.0 ms: 1.03x slower                                                    |
| python_startup_no_site    | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                                    |
| tornado_http              | 104 ms                                                          | 109 ms: 1.05x slower                                                     |
| deltablue                 | 2.41 ms                                                         | 2.52 ms: 1.05x slower                                                    |
| sympy_sum                 | 108 ms                                                          | 114 ms: 1.05x slower                                                     |
| richards_super            | 38.0 ms                                                         | 40.7 ms: 1.07x slower                                                    |
| async_tree_io_tg          | 509 ms                                                          | 549 ms: 1.08x slower                                                     |
| docutils                  | 1.82 sec                                                        | 1.97 sec: 1.08x slower                                                   |
| json_dumps                | 7.40 ms                                                         | 8.03 ms: 1.08x slower                                                    |
| coroutines                | 15.7 ms                                                         | 17.4 ms: 1.11x slower                                                    |
| python_startup            | 24.3 ms                                                         | 27.0 ms: 1.11x slower                                                    |
| sympy_integrate           | 15.2 ms                                                         | 17.0 ms: 1.12x slower                                                    |
| sqlglot_optimize          | 42.5 ms                                                         | 47.8 ms: 1.12x slower                                                    |
| async_generators          | 274 ms                                                          | 319 ms: 1.16x slower                                                     |
| json                      | 4.27 ms                                                         | 5.15 ms: 1.21x slower                                                    |
| pylint                    | 225 ms                                                          | 278 ms: 1.24x slower                                                     |
| gc_traversal              | 1.45 ms                                                         | 1.82 ms: 1.25x slower                                                    |
| bench_mp_pool             | 74.3 ms                                                         | 93.6 ms: 1.26x slower                                                    |
| raytrace                  | 205 ms                                                          | 263 ms: 1.28x slower                                                     |
| create_gc_cycles          | 713 us                                                          | 1.18 ms: 1.65x slower                                                    |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                             |

Benchmark hidden because not significant (6): bench_thread_pool, pickle_pure_python, mdp, async_tree_cpu_io_mixed_tg, genshi_text, xml_etree_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_tcp, asyncio_tcp_ssl, chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: sphinx

# HPT report

- Reliability score: 99.47% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown