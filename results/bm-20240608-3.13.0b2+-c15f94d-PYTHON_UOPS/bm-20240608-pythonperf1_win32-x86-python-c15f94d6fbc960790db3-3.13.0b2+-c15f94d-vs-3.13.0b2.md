# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                            |
| chameleon      | 5.71 ms                                                             | 6.31 ms: 1.10x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                          |
| html5lib       | 45.4 ms                                                             | 50.9 ms: 1.12x slower                                                           |
| tornado_http   | 94.3 ms                                                             | 100 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                            |
| async_tree_io_tg           | 529 ms                                                              | 557 ms: 1.05x slower                                                            |
| async_tree_io              | 530 ms                                                              | 567 ms: 1.07x slower                                                            |
| async_tree_none            | 228 ms                                                              | 244 ms: 1.07x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 274 ms: 1.08x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 219 ms: 1.08x slower                                                            |
| async_tree_memoization     | 275 ms                                                              | 304 ms: 1.10x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                                           |
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                            |
| float          | 52.4 ms                                                             | 53.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 125 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| pickle               | 8.07 us                                                             | 7.94 us: 1.02x faster                                                           |
| unpickle_list        | 2.93 us                                                             | 2.90 us: 1.01x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 64.6 ms: 1.01x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.1 us: 1.03x slower                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 61.5 ms: 1.03x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.13 ms: 1.04x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 44.3 ms: 1.05x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 241 us: 1.13x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 171 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                                           |
| python_startup         | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                           |
| genshi_text     | 20.1 ms                                                             | 21.8 ms: 1.08x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 48.8 ms: 1.10x slower                                                           |
| django_template | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| telco                      | 6.03 ms                                                             | 5.62 ms: 1.07x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 619 ms: 1.07x faster                                                            |
| tomli_loads                | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                          |
| nbody                      | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| pickle                     | 8.07 us                                                             | 7.94 us: 1.02x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.95 us: 1.01x faster                                                           |
| unpickle_list              | 2.93 us                                                             | 2.90 us: 1.01x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 16.8 sec: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| xml_etree_iterparse        | 64.2 ms                                                             | 64.6 ms: 1.01x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 56.4 ms: 1.01x slower                                                           |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                            |
| python_startup_no_site     | 18.2 ms                                                             | 18.5 ms: 1.01x slower                                                           |
| scimark_fft                | 198 ms                                                              | 201 ms: 1.01x slower                                                            |
| float                      | 52.4 ms                                                             | 53.1 ms: 1.01x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                           |
| fannkuch                   | 270 ms                                                              | 275 ms: 1.02x slower                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.27 sec: 1.02x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 620 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                            |
| pickle_list                | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.47 ms: 1.02x slower                                                           |
| mako                       | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.95 ms: 1.03x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.1 us: 1.03x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 71.5 ms: 1.03x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.38 us: 1.03x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 61.5 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                            |
| logging_simple             | 7.47 us                                                             | 7.72 us: 1.03x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.00 ms: 1.04x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.13 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.30 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 557 ms: 1.05x slower                                                            |
| xml_etree_process          | 42.1 ms                                                             | 44.3 ms: 1.05x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 71.7 ms: 1.05x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.26 ms: 1.06x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 78.7 ms: 1.06x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 100 ms: 1.06x slower                                                            |
| nqueens                    | 68.7 ms                                                             | 73.1 ms: 1.06x slower                                                           |
| async_tree_io              | 530 ms                                                              | 567 ms: 1.07x slower                                                            |
| async_tree_none            | 228 ms                                                              | 244 ms: 1.07x slower                                                            |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                          |
| chaos                      | 48.0 ms                                                             | 51.5 ms: 1.07x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 274 ms: 1.08x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 219 ms: 1.08x slower                                                            |
| deepcopy_reduce            | 2.59 us                                                             | 2.80 us: 1.08x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 21.8 ms: 1.08x slower                                                           |
| coverage                   | 307 ms                                                              | 333 ms: 1.08x slower                                                            |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                            |
| typing_runtime_protocols   | 136 us                                                              | 149 us: 1.10x slower                                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 49.8 ms: 1.10x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 48.8 ms: 1.10x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 304 ms: 1.10x slower                                                            |
| deepcopy                   | 280 us                                                              | 309 us: 1.10x slower                                                            |
| chameleon                  | 5.71 ms                                                             | 6.31 ms: 1.10x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 116 ms: 1.11x slower                                                            |
| async_generators           | 266 ms                                                              | 294 ms: 1.11x slower                                                            |
| sqlglot_optimize           | 39.7 ms                                                             | 44.1 ms: 1.11x slower                                                           |
| docutils                   | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 242 ms: 1.11x slower                                                            |
| pycparser                  | 777 ms                                                              | 866 ms: 1.11x slower                                                            |
| raytrace                   | 189 ms                                                              | 211 ms: 1.12x slower                                                            |
| html5lib                   | 45.4 ms                                                             | 50.9 ms: 1.12x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.4 ms: 1.12x slower                                                           |
| sympy_str                  | 211 ms                                                              | 237 ms: 1.12x slower                                                            |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.12x slower                                                            |
| sympy_expand               | 375 ms                                                              | 422 ms: 1.12x slower                                                            |
| generators                 | 21.2 ms                                                             | 23.8 ms: 1.13x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 241 us: 1.13x slower                                                            |
| go                         | 101 ms                                                              | 115 ms: 1.14x slower                                                            |
| comprehensions             | 11.9 us                                                             | 13.6 us: 1.15x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 171 us: 1.16x slower                                                            |
| thrift                     | 9.73 ms                                                             | 11.5 ms: 1.18x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 27.8 us: 1.18x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 97.1 ms: 1.20x slower                                                           |
| pyflate                    | 308 ms                                                              | 375 ms: 1.22x slower                                                            |
| regex_compile              | 99.9 ms                                                             | 125 ms: 1.25x slower                                                            |
| deltablue                  | 2.23 ms                                                             | 2.84 ms: 1.27x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 73.8 ns: 1.27x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 79.0 ms: 1.33x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.65 ms: 1.33x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.07x slower                                                                    |

Benchmark hidden because not significant (7): richards_super, flaskblogging, richards, regex_effbot, coroutines, create_gc_cycles, pathlib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown