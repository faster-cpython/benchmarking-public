# Results vs. 3.13.0b2

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.89 sec: 1.04x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 556 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 471 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| float          | 52.4 ms                                                             | 62.1 ms: 1.19x slower                                                          |
| nbody          | 76.9 ms                                                             | 97.8 ms: 1.27x slower                                                          |
| Geometric mean | (ref)                                                               | 1.15x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 121 ms: 1.03x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 110 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.1 ms: 1.06x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.52 ms: 1.10x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 67.8 ms: 1.14x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 258 us: 1.21x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 180 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 45.9 ms: 1.04x slower                                                          |
| django_template | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 8.45 ms: 1.22x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 752 us: 12.94x faster                                                          |
| coverage                   | 307 ms                                                              | 52.8 ms: 5.81x faster                                                          |
| deepcopy                   | 280 us                                                              | 249 us: 1.12x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.2 us: 1.06x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.48 us: 1.04x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 747 us: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| regex_dna                  | 118 ms                                                              | 121 ms: 1.03x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                              | 386 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.03x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 45.9 ms: 1.04x slower                                                          |
| sympy_str                  | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.04x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.4 ms: 1.04x slower                                                          |
| go                         | 101 ms                                                              | 105 ms: 1.04x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.89 sec: 1.04x slower                                                         |
| async_tree_io              | 530 ms                                                              | 556 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 471 ms: 1.05x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 73.1 ms: 1.05x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.9 ms: 1.06x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.1 ms: 1.06x slower                                                          |
| json                       | 4.10 ms                                                             | 4.36 ms: 1.06x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.7 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                         |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 658 ms: 1.09x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.35 sec: 1.09x slower                                                         |
| logging_simple             | 7.47 us                                                             | 8.15 us: 1.09x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 110 ms: 1.10x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.94 us: 1.10x slower                                                          |
| pylint                     | 217 ms                                                              | 239 ms: 1.10x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.52 ms: 1.10x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                          |
| async_generators           | 266 ms                                                              | 294 ms: 1.10x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.2 ms: 1.11x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 736 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.11x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 82.7 ms: 1.12x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 76.2 ms: 1.12x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| pycparser                  | 777 ms                                                              | 873 ms: 1.12x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.23 ms: 1.12x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 78.0 ms: 1.14x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 67.8 ms: 1.14x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.7 ms: 1.15x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.38 ms: 1.15x slower                                                          |
| chaos                      | 48.0 ms                                                             | 55.5 ms: 1.16x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.99 ms: 1.16x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| sqlglot_parse              | 964 us                                                              | 1.12 ms: 1.16x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 158 us: 1.17x slower                                                           |
| pyflate                    | 308 ms                                                              | 360 ms: 1.17x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 69.6 ms: 1.17x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.0 us: 1.18x slower                                                          |
| float                      | 52.4 ms                                                             | 62.1 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 239 ms: 1.21x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 258 us: 1.21x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.45 ms: 1.22x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 180 us: 1.22x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.74 ms: 1.22x slower                                                          |
| fannkuch                   | 270 ms                                                              | 334 ms: 1.24x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.0 ms: 1.24x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.27 ms: 1.25x slower                                                          |
| nbody                      | 76.9 ms                                                             | 97.8 ms: 1.27x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 104 ms: 1.28x slower                                                           |
| richards_super             | 35.5 ms                                                             | 45.7 ms: 1.29x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 74.6 ns: 1.29x slower                                                          |
| raytrace                   | 189 ms                                                              | 245 ms: 1.30x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.5 ms: 1.30x slower                                                          |
| richards                   | 31.2 ms                                                             | 40.8 ms: 1.31x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_none, gc_traversal, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown