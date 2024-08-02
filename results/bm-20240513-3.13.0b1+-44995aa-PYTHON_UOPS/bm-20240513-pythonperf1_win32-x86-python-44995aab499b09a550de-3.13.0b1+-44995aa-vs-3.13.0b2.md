# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 257 ms: 1.10x slower                                                            |
| chameleon      | 5.71 ms                                                             | 6.38 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                          |
| html5lib       | 45.4 ms                                                             | 50.8 ms: 1.12x slower                                                           |
| tornado_http   | 94.3 ms                                                             | 99.6 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 538 ms: 1.02x slower                                                            |
| async_tree_none            | 228 ms                                                              | 233 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                            |
| async_tree_memoization     | 275 ms                                                              | 282 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 202 ms: 1.02x slower                                                            |
| nbody          | 76.9 ms                                                             | 79.5 ms: 1.03x slower                                                           |
| float          | 52.4 ms                                                             | 57.2 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 126 ms: 1.27x slower                                                            |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list        | 2.93 us                                                             | 2.73 us: 1.07x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| tomli_loads          | 1.65 sec                                                            | 1.68 sec: 1.02x slower                                                          |
| pickle_list          | 3.57 us                                                             | 3.64 us: 1.02x slower                                                           |
| pickle               | 8.07 us                                                             | 8.24 us: 1.02x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 6.98 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.5 ms: 1.04x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 62.0 ms: 1.04x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 44.5 ms: 1.06x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 255 us: 1.20x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 181 us: 1.23x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 20.6 ms: 1.02x slower                                                           |
| django_template | 30.1 ms                                                             | 31.9 ms: 1.06x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                                           |
| mako            | 6.94 ms                                                             | 7.78 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list              | 2.93 us                                                             | 2.73 us: 1.07x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.91 us: 1.03x faster                                                           |
| flaskblogging              | 2.03 sec                                                            | 2.03 sec: 1.00x faster                                                          |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 538 ms: 1.02x slower                                                            |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                              | 202 ms: 1.02x slower                                                            |
| tomli_loads                | 1.65 sec                                                            | 1.68 sec: 1.02x slower                                                          |
| pickle_list                | 3.57 us                                                             | 3.64 us: 1.02x slower                                                           |
| pickle                     | 8.07 us                                                             | 8.24 us: 1.02x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 6.98 ms: 1.02x slower                                                           |
| async_tree_none            | 228 ms                                                              | 233 ms: 1.02x slower                                                            |
| genshi_text                | 20.1 ms                                                             | 20.6 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                            |
| async_tree_memoization     | 275 ms                                                              | 282 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                            |
| coroutines                 | 15.5 ms                                                             | 16.0 ms: 1.03x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.40 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                            |
| nbody                      | 76.9 ms                                                             | 79.5 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.5 ms: 1.04x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 62.0 ms: 1.04x slower                                                           |
| richards                   | 31.2 ms                                                             | 32.6 ms: 1.04x slower                                                           |
| richards_super             | 35.5 ms                                                             | 37.1 ms: 1.05x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.82 us: 1.05x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 72.8 ms: 1.05x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 88.3 ms: 1.05x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.04 ms: 1.05x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 99.6 ms: 1.06x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 44.5 ms: 1.06x slower                                                           |
| django_template            | 30.1 ms                                                             | 31.9 ms: 1.06x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.03 ms: 1.07x slower                                                           |
| pprint_safe_repr           | 607 ms                                                              | 648 ms: 1.07x slower                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 79.7 ms: 1.08x slower                                                           |
| coverage                   | 307 ms                                                              | 331 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.08x slower                                                            |
| crypto_pyaes               | 55.8 ms                                                             | 60.2 ms: 1.08x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.29 ms: 1.08x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 719 ms: 1.09x slower                                                            |
| deepcopy_reduce            | 2.59 us                                                             | 2.81 us: 1.09x slower                                                           |
| float                      | 52.4 ms                                                             | 57.2 ms: 1.09x slower                                                           |
| async_generators           | 266 ms                                                              | 290 ms: 1.09x slower                                                            |
| genshi_xml                 | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                                           |
| pycparser                  | 777 ms                                                              | 853 ms: 1.10x slower                                                            |
| sqlglot_normalize          | 206 ms                                                              | 227 ms: 1.10x slower                                                            |
| 2to3                       | 233 ms                                                              | 257 ms: 1.10x slower                                                            |
| generators                 | 21.2 ms                                                             | 23.4 ms: 1.11x slower                                                           |
| fannkuch                   | 270 ms                                                              | 299 ms: 1.11x slower                                                            |
| docutils                   | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.3 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.2 ms: 1.11x slower                                                           |
| scimark_fft                | 198 ms                                                              | 220 ms: 1.11x slower                                                            |
| chameleon                  | 5.71 ms                                                             | 6.38 ms: 1.12x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 76.8 ms: 1.12x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 50.8 ms: 1.12x slower                                                           |
| mako                       | 6.94 ms                                                             | 7.78 ms: 1.12x slower                                                           |
| sympy_str                  | 211 ms                                                              | 237 ms: 1.12x slower                                                            |
| sympy_expand               | 375 ms                                                              | 421 ms: 1.12x slower                                                            |
| pylint                     | 217 ms                                                              | 244 ms: 1.13x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 118 ms: 1.13x slower                                                            |
| raytrace                   | 189 ms                                                              | 214 ms: 1.13x slower                                                            |
| sympy_integrate            | 14.6 ms                                                             | 16.7 ms: 1.14x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.89 ms: 1.14x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.29 ms: 1.15x slower                                                           |
| deepcopy                   | 280 us                                                              | 321 us: 1.15x slower                                                            |
| spectral_norm              | 68.0 ms                                                             | 78.6 ms: 1.16x slower                                                           |
| go                         | 101 ms                                                              | 118 ms: 1.17x slower                                                            |
| pickle_pure_python         | 213 us                                                              | 255 us: 1.20x slower                                                            |
| scimark_sor                | 81.0 ms                                                             | 97.1 ms: 1.20x slower                                                           |
| thrift                     | 9.73 ms                                                             | 11.8 ms: 1.21x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.1 ms: 1.22x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 181 us: 1.23x slower                                                            |
| comprehensions             | 11.9 us                                                             | 14.7 us: 1.24x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 126 ms: 1.27x slower                                                            |
| pyflate                    | 308 ms                                                              | 397 ms: 1.29x slower                                                            |
| deepcopy_memo              | 23.5 us                                                             | 30.3 us: 1.29x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.90 ms: 1.30x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 81.3 ns: 1.41x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 84.5 ms: 1.42x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 6.16 ms: 1.46x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.09x slower                                                                    |

Benchmark hidden because not significant (7): pickle_dict, xml_etree_parse, regex_dna, asyncio_tcp_ssl, python_startup, async_tree_io, create_gc_cycles

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown