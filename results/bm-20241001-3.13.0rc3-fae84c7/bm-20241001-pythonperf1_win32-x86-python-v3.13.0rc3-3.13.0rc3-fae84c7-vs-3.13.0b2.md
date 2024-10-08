# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc3
- machine: windows-x86
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 243 ms: 1.04x slower                                                  |
| chameleon      | 5.71 ms                                                             | 5.98 ms: 1.05x slower                                                 |
| docutils       | 1.81 sec                                                            | 1.77 sec: 1.02x faster                                                |
| tornado_http   | 94.3 ms                                                             | 102 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 482 ms: 1.10x faster                                                  |
| async_tree_io              | 530 ms                                                              | 508 ms: 1.04x faster                                                  |
| async_tree_none            | 228 ms                                                              | 231 ms: 1.01x slower                                                  |
| async_tree_none_tg         | 203 ms                                                              | 206 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                  |
| async_tree_memoization     | 275 ms                                                              | 281 ms: 1.02x slower                                                  |
| async_tree_memoization_tg  | 254 ms                                                              | 273 ms: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                          |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                  |
| nbody          | 76.9 ms                                                             | 78.0 ms: 1.02x slower                                                 |
| float          | 52.4 ms                                                             | 55.2 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                               | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 99.5 ms: 1.00x faster                                                 |
| regex_v8       | 15.7 ms                                                             | 15.8 ms: 1.01x slower                                                 |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                               | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.32 us: 1.07x faster                                                 |
| unpickle_list        | 2.93 us                                                             | 2.78 us: 1.06x faster                                                 |
| pickle               | 8.07 us                                                             | 7.79 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.2 ms: 1.03x faster                                                 |
| pickle_dict          | 20.8 us                                                             | 20.3 us: 1.02x faster                                                 |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.01x faster                                                  |
| json_loads           | 20.5 us                                                             | 20.6 us: 1.00x slower                                                 |
| tomli_loads          | 1.65 sec                                                            | 1.67 sec: 1.01x slower                                                |
| xml_etree_generate   | 59.6 ms                                                             | 62.6 ms: 1.05x slower                                                 |
| xml_etree_process    | 42.1 ms                                                             | 44.3 ms: 1.05x slower                                                 |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.06x slower                                                 |
| unpickle_pure_python | 147 us                                                              | 157 us: 1.06x slower                                                  |
| pickle_pure_python   | 213 us                                                              | 231 us: 1.08x slower                                                  |
| json_dumps           | 6.84 ms                                                             | 7.48 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.7 ms: 1.11x slower                                                 |
| python_startup_no_site | 18.2 ms                                                             | 20.6 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 29.3 ms: 1.02x faster                                                 |
| mako            | 6.94 ms                                                             | 7.06 ms: 1.02x slower                                                 |
| genshi_xml      | 44.3 ms                                                             | 45.1 ms: 1.02x slower                                                 |
| genshi_text     | 20.1 ms                                                             | 20.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 482 ms: 1.10x faster                                                  |
| create_gc_cycles           | 756 us                                                              | 699 us: 1.08x faster                                                  |
| pickle_list                | 3.57 us                                                             | 3.32 us: 1.07x faster                                                 |
| unpickle_list              | 2.93 us                                                             | 2.78 us: 1.06x faster                                                 |
| async_tree_io              | 530 ms                                                              | 508 ms: 1.04x faster                                                  |
| pickle                     | 8.07 us                                                             | 7.79 us: 1.04x faster                                                 |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.2 ms: 1.03x faster                                                 |
| docutils                   | 1.81 sec                                                            | 1.77 sec: 1.02x faster                                                |
| django_template            | 30.1 ms                                                             | 29.3 ms: 1.02x faster                                                 |
| pickle_dict                | 20.8 us                                                             | 20.3 us: 1.02x faster                                                 |
| xml_etree_parse            | 104 ms                                                              | 103 ms: 1.01x faster                                                  |
| async_generators           | 266 ms                                                              | 263 ms: 1.01x faster                                                  |
| sympy_expand               | 375 ms                                                              | 371 ms: 1.01x faster                                                  |
| sqlglot_parse              | 964 us                                                              | 956 us: 1.01x faster                                                  |
| regex_compile              | 99.9 ms                                                             | 99.5 ms: 1.00x faster                                                 |
| json_loads                 | 20.5 us                                                             | 20.6 us: 1.00x slower                                                 |
| sympy_str                  | 211 ms                                                              | 212 ms: 1.00x slower                                                  |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 607 ms                                                              | 610 ms: 1.01x slower                                                  |
| regex_v8                   | 15.7 ms                                                             | 15.8 ms: 1.01x slower                                                 |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                  |
| nqueens                    | 68.7 ms                                                             | 69.1 ms: 1.01x slower                                                 |
| chaos                      | 48.0 ms                                                             | 48.3 ms: 1.01x slower                                                 |
| coroutines                 | 15.5 ms                                                             | 15.6 ms: 1.01x slower                                                 |
| sqlite_synth               | 1.96 us                                                             | 1.98 us: 1.01x slower                                                 |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                 |
| pprint_pformat             | 1.24 sec                                                            | 1.25 sec: 1.01x slower                                                |
| typing_runtime_protocols   | 136 us                                                              | 137 us: 1.01x slower                                                  |
| tomli_loads                | 1.65 sec                                                            | 1.67 sec: 1.01x slower                                                |
| sqlglot_normalize          | 206 ms                                                              | 209 ms: 1.01x slower                                                  |
| raytrace                   | 189 ms                                                              | 191 ms: 1.01x slower                                                  |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                 |
| async_tree_none            | 228 ms                                                              | 231 ms: 1.01x slower                                                  |
| nbody                      | 76.9 ms                                                             | 78.0 ms: 1.02x slower                                                 |
| pyflate                    | 308 ms                                                              | 313 ms: 1.02x slower                                                  |
| mako                       | 6.94 ms                                                             | 7.06 ms: 1.02x slower                                                 |
| sympy_integrate            | 14.6 ms                                                             | 14.9 ms: 1.02x slower                                                 |
| async_tree_none_tg         | 203 ms                                                              | 206 ms: 1.02x slower                                                  |
| generators                 | 21.2 ms                                                             | 21.5 ms: 1.02x slower                                                 |
| deltablue                  | 2.23 ms                                                             | 2.27 ms: 1.02x slower                                                 |
| genshi_xml                 | 44.3 ms                                                             | 45.1 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 456 ms: 1.02x slower                                                  |
| sqlglot_optimize           | 39.7 ms                                                             | 40.5 ms: 1.02x slower                                                 |
| async_tree_memoization     | 275 ms                                                              | 281 ms: 1.02x slower                                                  |
| logging_format             | 8.13 us                                                             | 8.31 us: 1.02x slower                                                 |
| mdp                        | 1.60 sec                                                            | 1.64 sec: 1.02x slower                                                |
| logging_silent             | 57.9 ns                                                             | 59.5 ns: 1.03x slower                                                 |
| logging_simple             | 7.47 us                                                             | 7.68 us: 1.03x slower                                                 |
| crypto_pyaes               | 55.8 ms                                                             | 57.5 ms: 1.03x slower                                                 |
| meteor_contest             | 74.1 ms                                                             | 76.3 ms: 1.03x slower                                                 |
| scimark_fft                | 198 ms                                                              | 205 ms: 1.04x slower                                                  |
| genshi_text                | 20.1 ms                                                             | 20.9 ms: 1.04x slower                                                 |
| json                       | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                 |
| deepcopy                   | 280 us                                                              | 291 us: 1.04x slower                                                  |
| thrift                     | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                                 |
| 2to3                       | 233 ms                                                              | 243 ms: 1.04x slower                                                  |
| richards_super             | 35.5 ms                                                             | 37.0 ms: 1.04x slower                                                 |
| pycparser                  | 777 ms                                                              | 810 ms: 1.04x slower                                                  |
| comprehensions             | 11.9 us                                                             | 12.4 us: 1.04x slower                                                 |
| fannkuch                   | 270 ms                                                              | 282 ms: 1.05x slower                                                  |
| chameleon                  | 5.71 ms                                                             | 5.98 ms: 1.05x slower                                                 |
| scimark_lu                 | 59.4 ms                                                             | 62.1 ms: 1.05x slower                                                 |
| go                         | 101 ms                                                              | 105 ms: 1.05x slower                                                  |
| xml_etree_generate         | 59.6 ms                                                             | 62.6 ms: 1.05x slower                                                 |
| deepcopy_reduce            | 2.59 us                                                             | 2.72 us: 1.05x slower                                                 |
| pathlib                    | 83.9 ms                                                             | 88.3 ms: 1.05x slower                                                 |
| xml_etree_process          | 42.1 ms                                                             | 44.3 ms: 1.05x slower                                                 |
| telco                      | 6.03 ms                                                             | 6.35 ms: 1.05x slower                                                 |
| coverage                   | 307 ms                                                              | 324 ms: 1.05x slower                                                  |
| float                      | 52.4 ms                                                             | 55.2 ms: 1.05x slower                                                 |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.06x slower                                                 |
| scimark_monte_carlo        | 45.2 ms                                                             | 47.9 ms: 1.06x slower                                                 |
| hexiom                     | 4.23 ms                                                             | 4.50 ms: 1.06x slower                                                 |
| unpickle_pure_python       | 147 us                                                              | 157 us: 1.06x slower                                                  |
| richards                   | 31.2 ms                                                             | 33.5 ms: 1.07x slower                                                 |
| async_tree_memoization_tg  | 254 ms                                                              | 273 ms: 1.08x slower                                                  |
| spectral_norm              | 68.0 ms                                                             | 73.1 ms: 1.08x slower                                                 |
| pickle_pure_python         | 213 us                                                              | 231 us: 1.08x slower                                                  |
| tornado_http               | 94.3 ms                                                             | 102 ms: 1.08x slower                                                  |
| scimark_sor                | 81.0 ms                                                             | 88.0 ms: 1.09x slower                                                 |
| deepcopy_memo              | 23.5 us                                                             | 25.7 us: 1.09x slower                                                 |
| json_dumps                 | 6.84 ms                                                             | 7.48 ms: 1.09x slower                                                 |
| bench_mp_pool              | 69.4 ms                                                             | 76.8 ms: 1.11x slower                                                 |
| python_startup             | 22.2 ms                                                             | 24.7 ms: 1.11x slower                                                 |
| asyncio_tcp                | 662 ms                                                              | 739 ms: 1.12x slower                                                  |
| python_startup_no_site     | 18.2 ms                                                             | 20.6 ms: 1.13x slower                                                 |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                          |

Benchmark hidden because not significant (8): sqlglot_transpile, flaskblogging, bench_thread_pool, regex_dna, html5lib, async_tree_cpu_io_mixed, scimark_sparse_mat_mult, pylint
Ignored benchmarks (2) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown