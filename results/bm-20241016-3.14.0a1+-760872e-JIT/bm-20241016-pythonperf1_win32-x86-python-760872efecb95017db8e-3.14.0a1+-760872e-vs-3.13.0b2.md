# Results vs. 3.13.0b2

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-x86
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.00x faster
- HPT reliability: 99.41%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 265 ms: 1.14x slower                                                            |
| docutils       | 1.81 sec                                                            | 2.03 sec: 1.12x slower                                                          |
| html5lib       | 45.4 ms                                                             | 44.6 ms: 1.02x faster                                                           |
| tornado_http   | 94.3 ms                                                             | 108 ms: 1.15x slower                                                            |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                            |
| async_tree_io              | 530 ms                                                              | 514 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 203 ms                                                              | 199 ms: 1.02x faster                                                            |
| async_tree_io_tg           | 529 ms                                                              | 543 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 499 ms: 1.06x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 483 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 65.2 ms: 1.18x faster                                                           |
| float          | 52.4 ms                                                             | 46.1 ms: 1.14x faster                                                           |
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                               | 1.10x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 15.4 ms: 1.02x faster                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.86 ms: 1.01x faster                                                           |
| regex_compile  | 99.9 ms                                                             | 104 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.49 sec: 1.10x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 55.8 ms: 1.07x faster                                                           |
| pickle_list          | 3.57 us                                                             | 3.40 us: 1.05x faster                                                           |
| xml_etree_process    | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                                           |
| unpickle_list        | 2.93 us                                                             | 2.96 us: 1.01x slower                                                           |
| pickle_dict          | 20.8 us                                                             | 21.2 us: 1.02x slower                                                           |
| pickle               | 8.07 us                                                             | 8.44 us: 1.05x slower                                                           |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.05x slower                                                            |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 230 us: 1.08x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 161 us: 1.10x slower                                                            |
| json_dumps           | 6.84 ms                                                             | 8.31 ms: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                           |
| python_startup         | 22.2 ms                                                             | 26.7 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.16x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.75 ms: 1.21x faster                                                           |
| django_template | 30.1 ms                                                             | 32.1 ms: 1.07x slower                                                           |
| genshi_text     | 20.1 ms                                                             | 22.6 ms: 1.13x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 53.8 ms: 1.22x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 767 us: 12.68x faster                                                           |
| coverage                   | 307 ms                                                              | 53.5 ms: 5.74x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 17.0 us: 1.39x faster                                                           |
| mako                       | 6.94 ms                                                             | 5.75 ms: 1.21x faster                                                           |
| deepcopy                   | 280 us                                                              | 236 us: 1.19x faster                                                            |
| scimark_sor                | 81.0 ms                                                             | 68.5 ms: 1.18x faster                                                           |
| nbody                      | 76.9 ms                                                             | 65.2 ms: 1.18x faster                                                           |
| spectral_norm              | 68.0 ms                                                             | 57.8 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.50 ms: 1.15x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.6 ms: 1.14x faster                                                           |
| float                      | 52.4 ms                                                             | 46.1 ms: 1.14x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 50.2 ms: 1.11x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.49 sec: 1.10x faster                                                          |
| scimark_fft                | 198 ms                                                              | 180 ms: 1.10x faster                                                            |
| fannkuch                   | 270 ms                                                              | 248 ms: 1.09x faster                                                            |
| xml_etree_generate         | 59.6 ms                                                             | 55.8 ms: 1.07x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.43 us: 1.07x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.40 us: 1.05x faster                                                           |
| go                         | 101 ms                                                              | 96.6 ms: 1.04x faster                                                           |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                            |
| xml_etree_process          | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 585 ms: 1.04x faster                                                            |
| async_tree_io              | 530 ms                                                              | 514 ms: 1.03x faster                                                            |
| logging_silent             | 57.9 ns                                                             | 56.2 ns: 1.03x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.21 sec: 1.03x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 72.1 ms: 1.03x faster                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.4 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.92 us: 1.02x faster                                                           |
| html5lib                   | 45.4 ms                                                             | 44.6 ms: 1.02x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 199 ms: 1.02x faster                                                            |
| logging_simple             | 7.47 us                                                             | 7.36 us: 1.01x faster                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.86 ms: 1.01x faster                                                           |
| telco                      | 6.03 ms                                                             | 6.08 ms: 1.01x slower                                                           |
| unpickle_list              | 2.93 us                                                             | 2.96 us: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                            |
| pickle_dict                | 20.8 us                                                             | 21.2 us: 1.02x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 543 ms: 1.03x slower                                                            |
| pyflate                    | 308 ms                                                              | 316 ms: 1.03x slower                                                            |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 104 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 136 us                                                              | 141 us: 1.04x slower                                                            |
| pickle                     | 8.07 us                                                             | 8.44 us: 1.05x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.05x slower                                                            |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                           |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                            |
| pathlib                    | 83.9 ms                                                             | 88.5 ms: 1.06x slower                                                           |
| pycparser                  | 777 ms                                                              | 821 ms: 1.06x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 499 ms: 1.06x slower                                                            |
| django_template            | 30.1 ms                                                             | 32.1 ms: 1.07x slower                                                           |
| comprehensions             | 11.9 us                                                             | 12.7 us: 1.07x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 483 ms: 1.08x slower                                                            |
| pickle_pure_python         | 213 us                                                              | 230 us: 1.08x slower                                                            |
| sympy_str                  | 211 ms                                                              | 229 ms: 1.08x slower                                                            |
| nqueens                    | 68.7 ms                                                             | 74.6 ms: 1.09x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.74 sec: 1.09x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 161 us: 1.10x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 116 ms: 1.11x slower                                                            |
| docutils                   | 1.81 sec                                                            | 2.03 sec: 1.12x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.12x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.12x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.6 ms: 1.13x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.53 ms: 1.13x slower                                                           |
| 2to3                       | 233 ms                                                              | 265 ms: 1.14x slower                                                            |
| tornado_http               | 94.3 ms                                                             | 108 ms: 1.15x slower                                                            |
| chaos                      | 48.0 ms                                                             | 55.1 ms: 1.15x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 239 ms: 1.16x slower                                                            |
| generators                 | 21.2 ms                                                             | 24.9 ms: 1.18x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 17.4 ms: 1.19x slower                                                           |
| richards_super             | 35.5 ms                                                             | 42.3 ms: 1.19x slower                                                           |
| python_startup             | 22.2 ms                                                             | 26.7 ms: 1.20x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 8.31 ms: 1.22x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 53.8 ms: 1.22x slower                                                           |
| json                       | 4.10 ms                                                             | 4.99 ms: 1.22x slower                                                           |
| async_generators           | 266 ms                                                              | 324 ms: 1.22x slower                                                            |
| richards                   | 31.2 ms                                                             | 38.3 ms: 1.23x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 49.2 ms: 1.24x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 826 ms: 1.25x slower                                                            |
| gc_traversal               | 1.43 ms                                                             | 1.80 ms: 1.26x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.46 ms: 1.29x slower                                                           |
| pylint                     | 217 ms                                                              | 283 ms: 1.30x slower                                                            |
| bench_mp_pool              | 69.4 ms                                                             | 94.3 ms: 1.36x slower                                                           |
| raytrace                   | 189 ms                                                              | 271 ms: 1.44x slower                                                            |
| create_gc_cycles           | 756 us                                                              | 1.20 ms: 1.59x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (8): xml_etree_iterparse, async_tree_memoization, logging_format, scimark_lu, regex_dna, json_loads, async_tree_memoization_tg, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.41% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown