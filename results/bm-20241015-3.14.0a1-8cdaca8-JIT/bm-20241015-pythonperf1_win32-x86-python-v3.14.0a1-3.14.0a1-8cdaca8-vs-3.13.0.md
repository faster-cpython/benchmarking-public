# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.05x faster
- HPT reliability: 74.05%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 264 ms: 1.04x slower                                                |
| docutils       | 1.82 sec                                                        | 2.07 sec: 1.14x slower                                              |
| html5lib       | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                               |
| tornado_http   | 104 ms                                                          | 109 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                |
| async_tree_none_tg        | 219 ms                                                          | 204 ms: 1.07x faster                                                |
| asyncio_tcp               | 842 ms                                                          | 789 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                |
| async_tree_io             | 537 ms                                                          | 523 ms: 1.03x faster                                                |
| async_tree_io_tg          | 509 ms                                                          | 551 ms: 1.08x slower                                                |
| coroutines                | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                               |
| async_generators          | 274 ms                                                          | 325 ms: 1.19x slower                                                |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 63.2 ms: 1.30x faster                                               |
| float          | 57.8 ms                                                         | 47.0 ms: 1.23x faster                                               |
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                           | 1.17x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                               |
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| regex_compile  | 103 ms                                                          | 104 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                           | 1.00x slower                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list       | 3.09 us                                                         | 2.71 us: 1.14x faster                                               |
| xml_etree_generate  | 62.6 ms                                                         | 55.7 ms: 1.12x faster                                               |
| tomli_loads         | 1.73 sec                                                        | 1.56 sec: 1.11x faster                                              |
| xml_etree_process   | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                               |
| unpickle            | 10.5 us                                                         | 10.4 us: 1.02x faster                                               |
| xml_etree_iterparse | 65.1 ms                                                         | 64.3 ms: 1.01x faster                                               |
| pickle_dict         | 21.7 us                                                         | 21.5 us: 1.01x faster                                               |
| json_loads          | 21.0 us                                                         | 20.8 us: 1.01x faster                                               |
| pickle              | 8.42 us                                                         | 8.60 us: 1.02x slower                                               |
| pickle_list         | 3.40 us                                                         | 3.48 us: 1.02x slower                                               |
| pickle_pure_python  | 238 us                                                          | 246 us: 1.03x slower                                                |
| json_dumps          | 7.40 ms                                                         | 8.11 ms: 1.09x slower                                               |
| Geometric mean      | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                               |
| python_startup         | 24.3 ms                                                         | 27.1 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.70 ms: 1.28x faster                                               |
| django_template | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                               |
| genshi_text     | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                               |
| genshi_xml      | 49.5 ms                                                         | 54.0 ms: 1.09x slower                                               |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 770 us: 13.17x faster                                               |
| coverage                  | 333 ms                                                          | 53.8 ms: 6.19x faster                                               |
| deepcopy_memo             | 26.2 us                                                         | 16.2 us: 1.62x faster                                               |
| scimark_sor               | 91.8 ms                                                         | 70.1 ms: 1.31x faster                                               |
| nbody                     | 81.9 ms                                                         | 63.2 ms: 1.30x faster                                               |
| deepcopy                  | 307 us                                                          | 238 us: 1.29x faster                                                |
| mako                      | 7.31 ms                                                         | 5.70 ms: 1.28x faster                                               |
| spectral_norm             | 71.3 ms                                                         | 57.2 ms: 1.25x faster                                               |
| float                     | 57.8 ms                                                         | 47.0 ms: 1.23x faster                                               |
| scimark_monte_carlo       | 50.3 ms                                                         | 41.6 ms: 1.21x faster                                               |
| pprint_safe_repr          | 644 ms                                                          | 546 ms: 1.18x faster                                                |
| fannkuch                  | 293 ms                                                          | 249 ms: 1.17x faster                                                |
| deepcopy_reduce           | 2.85 us                                                         | 2.44 us: 1.17x faster                                               |
| pprint_pformat            | 1.30 sec                                                        | 1.12 sec: 1.16x faster                                              |
| go                        | 111 ms                                                          | 97.2 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.54 ms: 1.14x faster                                               |
| unpickle_list             | 3.09 us                                                         | 2.71 us: 1.14x faster                                               |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                |
| xml_etree_generate        | 62.6 ms                                                         | 55.7 ms: 1.12x faster                                               |
| crypto_pyaes              | 58.2 ms                                                         | 51.9 ms: 1.12x faster                                               |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                |
| tomli_loads               | 1.73 sec                                                        | 1.56 sec: 1.11x faster                                              |
| scimark_fft               | 206 ms                                                          | 187 ms: 1.11x faster                                                |
| logging_silent            | 61.6 ns                                                         | 56.0 ns: 1.10x faster                                               |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.09x faster                                                |
| async_tree_none_tg        | 219 ms                                                          | 204 ms: 1.07x faster                                                |
| asyncio_tcp               | 842 ms                                                          | 789 ms: 1.07x faster                                                |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                |
| xml_etree_process         | 45.0 ms                                                         | 42.8 ms: 1.05x faster                                               |
| meteor_contest            | 77.0 ms                                                         | 73.3 ms: 1.05x faster                                               |
| scimark_lu                | 63.5 ms                                                         | 60.6 ms: 1.05x faster                                               |
| telco                     | 6.67 ms                                                         | 6.36 ms: 1.05x faster                                               |
| logging_simple            | 7.87 us                                                         | 7.54 us: 1.04x faster                                               |
| pyflate                   | 326 ms                                                          | 312 ms: 1.04x faster                                                |
| pycparser                 | 869 ms                                                          | 834 ms: 1.04x faster                                                |
| logging_format            | 8.57 us                                                         | 8.27 us: 1.04x faster                                               |
| unpack_sequence           | 42.9 ns                                                         | 41.7 ns: 1.03x faster                                               |
| sqlite_synth              | 1.97 us                                                         | 1.91 us: 1.03x faster                                               |
| async_tree_io             | 537 ms                                                          | 523 ms: 1.03x faster                                                |
| html5lib                  | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                               |
| unpickle                  | 10.5 us                                                         | 10.4 us: 1.02x faster                                               |
| pathlib                   | 89.4 ms                                                         | 88.4 ms: 1.01x faster                                               |
| regex_v8                  | 15.6 ms                                                         | 15.4 ms: 1.01x faster                                               |
| xml_etree_iterparse       | 65.1 ms                                                         | 64.3 ms: 1.01x faster                                               |
| pickle_dict               | 21.7 us                                                         | 21.5 us: 1.01x faster                                               |
| pidigits                  | 202 ms                                                          | 200 ms: 1.01x faster                                                |
| dulwich_log               | 49.7 ms                                                         | 49.3 ms: 1.01x faster                                               |
| json_loads                | 21.0 us                                                         | 20.8 us: 1.01x faster                                               |
| regex_dna                 | 117 ms                                                          | 118 ms: 1.01x slower                                                |
| regex_compile             | 103 ms                                                          | 104 ms: 1.01x slower                                                |
| nqueens                   | 75.1 ms                                                         | 76.2 ms: 1.01x slower                                               |
| python_startup_no_site    | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                               |
| pickle                    | 8.42 us                                                         | 8.60 us: 1.02x slower                                               |
| pickle_list               | 3.40 us                                                         | 3.48 us: 1.02x slower                                               |
| comprehensions            | 12.7 us                                                         | 13.0 us: 1.02x slower                                               |
| django_template           | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                               |
| pickle_pure_python        | 238 us                                                          | 246 us: 1.03x slower                                                |
| mdp                       | 1.67 sec                                                        | 1.73 sec: 1.03x slower                                              |
| 2to3                      | 253 ms                                                          | 264 ms: 1.04x slower                                                |
| tornado_http              | 104 ms                                                          | 109 ms: 1.05x slower                                                |
| sympy_expand              | 375 ms                                                          | 394 ms: 1.05x slower                                                |
| sympy_str                 | 215 ms                                                          | 227 ms: 1.06x slower                                                |
| sqlglot_transpile         | 1.29 ms                                                         | 1.37 ms: 1.06x slower                                               |
| genshi_text               | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                               |
| async_tree_io_tg          | 509 ms                                                          | 551 ms: 1.08x slower                                                |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.08x slower                                                |
| typing_runtime_protocols  | 136 us                                                          | 148 us: 1.09x slower                                                |
| genshi_xml                | 49.5 ms                                                         | 54.0 ms: 1.09x slower                                               |
| chaos                     | 51.2 ms                                                         | 55.8 ms: 1.09x slower                                               |
| json_dumps                | 7.40 ms                                                         | 8.11 ms: 1.09x slower                                               |
| deltablue                 | 2.41 ms                                                         | 2.64 ms: 1.10x slower                                               |
| sqlglot_normalize         | 220 ms                                                          | 244 ms: 1.11x slower                                                |
| python_startup            | 24.3 ms                                                         | 27.1 ms: 1.12x slower                                               |
| coroutines                | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                               |
| generators                | 22.1 ms                                                         | 25.1 ms: 1.13x slower                                               |
| docutils                  | 1.82 sec                                                        | 2.07 sec: 1.14x slower                                              |
| sympy_integrate           | 15.2 ms                                                         | 17.5 ms: 1.15x slower                                               |
| hexiom                    | 4.64 ms                                                         | 5.38 ms: 1.16x slower                                               |
| json                      | 4.27 ms                                                         | 5.03 ms: 1.18x slower                                               |
| sqlglot_optimize          | 42.5 ms                                                         | 50.3 ms: 1.18x slower                                               |
| async_generators          | 274 ms                                                          | 325 ms: 1.19x slower                                                |
| richards                  | 33.8 ms                                                         | 40.2 ms: 1.19x slower                                               |
| richards_super            | 38.0 ms                                                         | 45.6 ms: 1.20x slower                                               |
| gc_traversal              | 1.45 ms                                                         | 1.81 ms: 1.25x slower                                               |
| pylint                    | 225 ms                                                          | 283 ms: 1.26x slower                                                |
| bench_mp_pool             | 74.3 ms                                                         | 94.5 ms: 1.27x slower                                               |
| raytrace                  | 205 ms                                                          | 269 ms: 1.31x slower                                                |
| create_gc_cycles          | 713 us                                                          | 1.20 ms: 1.68x slower                                               |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                        |

Benchmark hidden because not significant (7): bench_thread_pool, xml_etree_parse, sqlglot_parse, unpickle_pure_python, regex_effbot, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 74.05% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown