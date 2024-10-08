# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.04x faster
- HPT reliability: 93.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.97 sec: 1.09x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.8 ms: 1.03x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 100 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 50.5 ms: 1.52x faster                                                          |
| float          | 52.4 ms                                                             | 43.5 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 15.8 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 102 ms: 1.02x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.97 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 53.5 ms: 1.12x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| pickle_list          | 3.57 us                                                             | 3.31 us: 1.08x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 39.7 ms: 1.06x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.78 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 60.9 ms: 1.05x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| pickle               | 8.07 us                                                             | 7.93 us: 1.02x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.02x faster                                                           |
| json_dumps           | 6.84 ms                                                             | 7.03 ms: 1.03x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.4 us: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 163 us: 1.11x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 242 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.47 ms: 1.27x faster                                                          |
| django_template | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.1 ms: 1.20x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.8 ms: 1.22x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 790 us: 12.32x faster                                                          |
| coverage                   | 307 ms                                                              | 53.8 ms: 5.71x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.2 us: 1.55x faster                                                          |
| nbody                      | 76.9 ms                                                             | 50.5 ms: 1.52x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 46.6 ms: 1.46x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.47 ms: 1.27x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.36 ms: 1.22x faster                                                          |
| float                      | 52.4 ms                                                             | 43.5 ms: 1.20x faster                                                          |
| deepcopy                   | 280 us                                                              | 233 us: 1.20x faster                                                           |
| scimark_sor                | 81.0 ms                                                             | 68.0 ms: 1.19x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.4 ms: 1.15x faster                                                          |
| fannkuch                   | 270 ms                                                              | 237 ms: 1.14x faster                                                           |
| scimark_fft                | 198 ms                                                              | 175 ms: 1.13x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 53.5 ms: 1.12x faster                                                          |
| deltablue                  | 2.23 ms                                                             | 2.02 ms: 1.10x faster                                                          |
| pyflate                    | 308 ms                                                              | 282 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 607 ms: 1.09x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| pickle_list                | 3.57 us                                                             | 3.31 us: 1.08x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 39.7 ms: 1.06x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.78 us: 1.06x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 60.9 ms: 1.05x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 19.9 us: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 221 ms: 1.03x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.90 us: 1.03x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 71.8 ms: 1.03x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.6 us: 1.02x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.53 us: 1.02x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.93 us: 1.02x faster                                                          |
| xml_etree_parse            | 104 ms                                                              | 103 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 745 us: 1.02x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 598 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 83.1 ms: 1.01x faster                                                          |
| telco                      | 6.03 ms                                                             | 6.00 ms: 1.01x faster                                                          |
| regex_v8                   | 15.7 ms                                                             | 15.8 ms: 1.01x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.25 sec: 1.01x slower                                                         |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                          |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| go                         | 101 ms                                                              | 102 ms: 1.01x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 60.0 ms: 1.01x slower                                                          |
| richards_super             | 35.5 ms                                                             | 35.9 ms: 1.01x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 102 ms: 1.02x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.34 us: 1.02x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.03 ms: 1.03x slower                                                          |
| json                       | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.8 ms: 1.03x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 59.7 ns: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.72 us: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 220 ms: 1.04x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.4 us: 1.04x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.97 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.69 sec: 1.05x slower                                                         |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                           |
| richards                   | 31.2 ms                                                             | 32.8 ms: 1.05x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| pycparser                  | 777 ms                                                              | 825 ms: 1.06x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 100 ms: 1.07x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 74.2 ms: 1.07x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.07x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 113 ms: 1.08x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.08x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.97 sec: 1.09x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 163 us: 1.11x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 76.2 ms: 1.11x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.3 ms: 1.11x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 50.4 ms: 1.11x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 231 ms: 1.12x slower                                                           |
| generators                 | 21.2 ms                                                             | 23.8 ms: 1.12x slower                                                          |
| django_template            | 30.1 ms                                                             | 34.0 ms: 1.13x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 242 us: 1.14x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.7 ms: 1.14x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.86 ms: 1.15x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 46.0 ms: 1.16x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.1 ms: 1.17x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 24.1 ms: 1.20x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 53.8 ms: 1.22x slower                                                          |
| pylint                     | 217 ms                                                              | 268 ms: 1.23x slower                                                           |
| async_generators           | 266 ms                                                              | 335 ms: 1.26x slower                                                           |
| raytrace                   | 189 ms                                                              | 244 ms: 1.29x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, pidigits, async_tree_memoization_tg, bench_thread_pool, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 93.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown