# Results vs. 3.13.0b2

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.04x faster
- HPT reliability: 78.55%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.95 sec: 1.07x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 98.2 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 503 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 247 ms: 1.03x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 268 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 55.2 ms: 1.39x faster                                                          |
| float          | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                          |
| Geometric mean | (ref)                                                               | 1.18x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 95.5 ms: 1.05x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_dna      | 118 ms                                                              | 127 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 150 us: 1.02x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 218 us: 1.02x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 43.6 ms: 1.04x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.6 us: 1.05x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.25 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.46 ms: 1.27x faster                                                          |
| django_template | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 23.4 ms: 1.16x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.6 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 772 us: 12.60x faster                                                          |
| coverage                   | 307 ms                                                              | 52.1 ms: 5.89x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.8 us: 1.49x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.7 ms: 1.42x faster                                                          |
| nbody                      | 76.9 ms                                                             | 55.2 ms: 1.39x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.46 ms: 1.27x faster                                                          |
| float                      | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.41 ms: 1.19x faster                                                          |
| scimark_fft                | 198 ms                                                              | 167 ms: 1.19x faster                                                           |
| fannkuch                   | 270 ms                                                              | 228 ms: 1.18x faster                                                           |
| deepcopy                   | 280 us                                                              | 238 us: 1.18x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 48.9 ms: 1.14x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.48 sec: 1.11x faster                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.36 us: 1.10x faster                                                          |
| pyflate                    | 308 ms                                                              | 285 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.9 ms: 1.08x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 565 ms: 1.07x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.07x faster                                                         |
| telco                      | 6.03 ms                                                             | 5.70 ms: 1.06x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 503 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 95.5 ms: 1.05x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 635 ms: 1.04x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.5 us: 1.03x faster                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 247 ms: 1.03x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 268 ms: 1.03x faster                                                           |
| logging_simple             | 7.47 us                                                             | 7.31 us: 1.02x faster                                                          |
| pathlib                    | 83.9 ms                                                             | 82.2 ms: 1.02x faster                                                          |
| logging_format             | 8.13 us                                                             | 7.99 us: 1.02x faster                                                          |
| bench_thread_pool          | 985 us                                                              | 970 us: 1.02x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 949 us: 1.02x faster                                                           |
| logging_silent             | 57.9 ns                                                             | 58.5 ns: 1.01x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 150 us: 1.02x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 218 us: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                           |
| sympy_expand               | 375 ms                                                              | 386 ms: 1.03x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 76.3 ms: 1.03x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 109 ms: 1.03x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.66 sec: 1.04x slower                                                         |
| xml_etree_process          | 42.1 ms                                                             | 43.6 ms: 1.04x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 98.2 ms: 1.04x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.6 us: 1.05x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.25 ms: 1.06x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.06x slower                                                          |
| richards                   | 31.2 ms                                                             | 33.4 ms: 1.07x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.95 sec: 1.07x slower                                                         |
| pycparser                  | 777 ms                                                              | 836 ms: 1.08x slower                                                           |
| regex_dna                  | 118 ms                                                              | 127 ms: 1.08x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 74.0 ms: 1.08x slower                                                          |
| json                       | 4.10 ms                                                             | 4.43 ms: 1.08x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                                          |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| chaos                      | 48.0 ms                                                             | 52.4 ms: 1.09x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.5 ms: 1.09x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.69 ms: 1.11x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 77.1 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 241 ms: 1.11x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 151 us: 1.11x slower                                                           |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 235 ms: 1.14x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.7 ms: 1.14x slower                                                          |
| richards_super             | 35.5 ms                                                             | 40.7 ms: 1.15x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.4 ms: 1.16x slower                                                          |
| raytrace                   | 189 ms                                                              | 227 ms: 1.20x slower                                                           |
| async_generators           | 266 ms                                                              | 320 ms: 1.20x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 53.6 ms: 1.21x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.76 ms: 1.23x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 101 ms: 1.24x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.9 ms: 1.32x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 79.7 ms: 1.34x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, xml_etree_parse, asyncio_tcp_ssl, create_gc_cycles, xml_etree_generate, gc_traversal, regex_effbot, async_tree_io, pidigits
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 78.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown