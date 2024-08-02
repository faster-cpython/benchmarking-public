# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 255 ms: 1.09x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.18 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                         |
| html5lib       | 45.4 ms                                                             | 50.5 ms: 1.11x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 99.3 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg          | 529 ms                                                              | 540 ms: 1.02x slower                                                           |
| async_tree_none           | 228 ms                                                              | 234 ms: 1.03x slower                                                           |
| async_tree_memoization    | 275 ms                                                              | 283 ms: 1.03x slower                                                           |
| async_tree_none_tg        | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| Geometric mean            | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 75.9 ms: 1.01x faster                                                          |
| float          | 52.4 ms                                                             | 51.9 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.01x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 123 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.61 sec: 1.03x faster                                                         |
| pickle_list          | 3.57 us                                                             | 3.58 us: 1.00x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 64.7 ms: 1.01x slower                                                          |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 6.92 ms: 1.01x slower                                                          |
| pickle               | 8.07 us                                                             | 8.17 us: 1.01x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 60.3 ms: 1.01x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.02 us: 1.03x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 243 us: 1.14x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 168 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.0 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 7.08 ms: 1.02x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.2 ms: 1.05x slower                                                          |
| django_template | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 47.7 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.73 ms                                                             | 723 us: 13.46x faster                                                          |
| coverage                  | 307 ms                                                              | 49.7 ms: 6.18x faster                                                          |
| tomli_loads               | 1.65 sec                                                            | 1.61 sec: 1.03x faster                                                         |
| sqlite_synth              | 1.96 us                                                             | 1.92 us: 1.02x faster                                                          |
| nbody                     | 76.9 ms                                                             | 75.9 ms: 1.01x faster                                                          |
| float                     | 52.4 ms                                                             | 51.9 ms: 1.01x faster                                                          |
| richards                  | 31.2 ms                                                             | 31.0 ms: 1.01x faster                                                          |
| pickle_list               | 3.57 us                                                             | 3.58 us: 1.00x slower                                                          |
| xml_etree_iterparse       | 64.2 ms                                                             | 64.7 ms: 1.01x slower                                                          |
| telco                     | 6.03 ms                                                             | 6.08 ms: 1.01x slower                                                          |
| json_loads                | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| regex_effbot              | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                          |
| json_dumps                | 6.84 ms                                                             | 6.92 ms: 1.01x slower                                                          |
| pickle                    | 8.07 us                                                             | 8.17 us: 1.01x slower                                                          |
| xml_etree_generate        | 59.6 ms                                                             | 60.3 ms: 1.01x slower                                                          |
| mdp                       | 1.60 sec                                                            | 1.62 sec: 1.01x slower                                                         |
| regex_dna                 | 118 ms                                                              | 120 ms: 1.01x slower                                                           |
| mako                      | 6.94 ms                                                             | 7.08 ms: 1.02x slower                                                          |
| regex_v8                  | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| async_tree_io_tg          | 529 ms                                                              | 540 ms: 1.02x slower                                                           |
| scimark_fft               | 198 ms                                                              | 202 ms: 1.02x slower                                                           |
| logging_format            | 8.13 us                                                             | 8.32 us: 1.02x slower                                                          |
| fannkuch                  | 270 ms                                                              | 276 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult   | 2.87 ms                                                             | 2.94 ms: 1.02x slower                                                          |
| xml_etree_process         | 42.1 ms                                                             | 43.2 ms: 1.03x slower                                                          |
| async_tree_none           | 228 ms                                                              | 234 ms: 1.03x slower                                                           |
| async_tree_memoization    | 275 ms                                                              | 283 ms: 1.03x slower                                                           |
| logging_simple            | 7.47 us                                                             | 7.70 us: 1.03x slower                                                          |
| unpickle_list             | 2.93 us                                                             | 3.02 us: 1.03x slower                                                          |
| json                      | 4.10 ms                                                             | 4.23 ms: 1.03x slower                                                          |
| sqlglot_parse             | 964 us                                                              | 997 us: 1.03x slower                                                           |
| async_tree_none_tg        | 203 ms                                                              | 210 ms: 1.04x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| python_startup            | 22.2 ms                                                             | 23.0 ms: 1.04x slower                                                          |
| pprint_safe_repr          | 607 ms                                                              | 630 ms: 1.04x slower                                                           |
| pathlib                   | 83.9 ms                                                             | 87.3 ms: 1.04x slower                                                          |
| pprint_pformat            | 1.24 sec                                                            | 1.29 sec: 1.04x slower                                                         |
| sqlglot_transpile         | 1.19 ms                                                             | 1.24 ms: 1.04x slower                                                          |
| bench_mp_pool             | 69.4 ms                                                             | 72.7 ms: 1.05x slower                                                          |
| python_startup_no_site    | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| crypto_pyaes              | 55.8 ms                                                             | 58.5 ms: 1.05x slower                                                          |
| unpickle                  | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| meteor_contest            | 74.1 ms                                                             | 77.7 ms: 1.05x slower                                                          |
| tornado_http              | 94.3 ms                                                             | 99.3 ms: 1.05x slower                                                          |
| genshi_text               | 20.1 ms                                                             | 21.2 ms: 1.05x slower                                                          |
| deepcopy_reduce           | 2.59 us                                                             | 2.73 us: 1.06x slower                                                          |
| coroutines                | 15.5 ms                                                             | 16.4 ms: 1.06x slower                                                          |
| spectral_norm             | 68.0 ms                                                             | 72.3 ms: 1.06x slower                                                          |
| bench_thread_pool         | 985 us                                                              | 1.05 ms: 1.06x slower                                                          |
| django_template           | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                          |
| asyncio_tcp               | 662 ms                                                              | 711 ms: 1.07x slower                                                           |
| deepcopy                  | 280 us                                                              | 301 us: 1.08x slower                                                           |
| genshi_xml                | 44.3 ms                                                             | 47.7 ms: 1.08x slower                                                          |
| chameleon                 | 5.71 ms                                                             | 6.18 ms: 1.08x slower                                                          |
| 2to3                      | 233 ms                                                              | 255 ms: 1.09x slower                                                           |
| typing_runtime_protocols  | 136 us                                                              | 149 us: 1.10x slower                                                           |
| sqlglot_normalize         | 206 ms                                                              | 226 ms: 1.10x slower                                                           |
| sqlglot_optimize          | 39.7 ms                                                             | 43.6 ms: 1.10x slower                                                          |
| generators                | 21.2 ms                                                             | 23.2 ms: 1.10x slower                                                          |
| pycparser                 | 777 ms                                                              | 854 ms: 1.10x slower                                                           |
| docutils                  | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                         |
| raytrace                  | 189 ms                                                              | 209 ms: 1.11x slower                                                           |
| async_generators          | 266 ms                                                              | 295 ms: 1.11x slower                                                           |
| html5lib                  | 45.4 ms                                                             | 50.5 ms: 1.11x slower                                                          |
| chaos                     | 48.0 ms                                                             | 53.4 ms: 1.11x slower                                                          |
| sympy_sum                 | 105 ms                                                              | 118 ms: 1.12x slower                                                           |
| pylint                    | 217 ms                                                              | 244 ms: 1.12x slower                                                           |
| go                        | 101 ms                                                              | 113 ms: 1.12x slower                                                           |
| scimark_monte_carlo       | 45.2 ms                                                             | 50.8 ms: 1.12x slower                                                          |
| sympy_integrate           | 14.6 ms                                                             | 16.5 ms: 1.12x slower                                                          |
| comprehensions            | 11.9 us                                                             | 13.3 us: 1.13x slower                                                          |
| sympy_expand              | 375 ms                                                              | 423 ms: 1.13x slower                                                           |
| sympy_str                 | 211 ms                                                              | 238 ms: 1.13x slower                                                           |
| pickle_pure_python        | 213 us                                                              | 243 us: 1.14x slower                                                           |
| unpickle_pure_python      | 147 us                                                              | 168 us: 1.14x slower                                                           |
| nqueens                   | 68.7 ms                                                             | 79.0 ms: 1.15x slower                                                          |
| scimark_sor               | 81.0 ms                                                             | 93.5 ms: 1.16x slower                                                          |
| pyflate                   | 308 ms                                                              | 360 ms: 1.17x slower                                                           |
| deepcopy_memo             | 23.5 us                                                             | 27.6 us: 1.17x slower                                                          |
| regex_compile             | 99.9 ms                                                             | 123 ms: 1.24x slower                                                           |
| deltablue                 | 2.23 ms                                                             | 2.84 ms: 1.27x slower                                                          |
| logging_silent            | 57.9 ns                                                             | 74.1 ns: 1.28x slower                                                          |
| scimark_lu                | 59.4 ms                                                             | 77.3 ms: 1.30x slower                                                          |
| hexiom                    | 4.23 ms                                                             | 5.72 ms: 1.35x slower                                                          |
| Geometric mean            | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, xml_etree_parse, pickle_dict, pidigits, flaskblogging, richards_super, async_tree_cpu_io_mixed, create_gc_cycles, asyncio_tcp_ssl, gc_traversal, async_tree_io

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown