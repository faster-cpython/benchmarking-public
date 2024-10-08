# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a2
- machine: windows-x86
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 246 ms: 1.05x slower                                                |
| chameleon      | 5.71 ms                                                             | 5.96 ms: 1.04x slower                                               |
| docutils       | 1.81 sec                                                            | 1.78 sec: 1.02x faster                                              |
| html5lib       | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                               |
| tornado_http   | 94.3 ms                                                             | 98.2 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                               | 1.02x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 511 ms: 1.08x slower                                                |
| async_tree_none            | 228 ms                                                              | 254 ms: 1.11x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 506 ms: 1.13x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 317 ms: 1.15x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 619 ms: 1.17x slower                                                |
| async_tree_io              | 530 ms                                                              | 623 ms: 1.17x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 248 ms: 1.22x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 312 ms: 1.23x slower                                                |
| Geometric mean             | (ref)                                                               | 1.16x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                |
| float          | 52.4 ms                                                             | 59.8 ms: 1.14x slower                                               |
| nbody          | 76.9 ms                                                             | 88.9 ms: 1.16x slower                                               |
| Geometric mean | (ref)                                                               | 1.10x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                               |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                               |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                               | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.17 us: 1.12x faster                                               |
| pickle               | 8.07 us                                                             | 7.57 us: 1.07x faster                                               |
| pickle_dict          | 20.8 us                                                             | 19.8 us: 1.05x faster                                               |
| json_loads           | 20.5 us                                                             | 19.8 us: 1.04x faster                                               |
| unpickle             | 9.79 us                                                             | 9.58 us: 1.02x faster                                               |
| unpickle_list        | 2.93 us                                                             | 2.94 us: 1.00x slower                                               |
| json_dumps           | 6.84 ms                                                             | 6.96 ms: 1.02x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.03x slower                                                |
| xml_etree_generate   | 59.6 ms                                                             | 62.8 ms: 1.05x slower                                               |
| unpickle_pure_python | 147 us                                                              | 156 us: 1.06x slower                                                |
| pickle_pure_python   | 213 us                                                              | 231 us: 1.08x slower                                                |
| xml_etree_iterparse  | 64.2 ms                                                             | 69.5 ms: 1.08x slower                                               |
| xml_etree_process    | 42.1 ms                                                             | 45.8 ms: 1.09x slower                                               |
| tomli_loads          | 1.65 sec                                                            | 1.81 sec: 1.10x slower                                              |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                               |
| Geometric mean         | (ref)                                                               | 1.05x slower                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 31.2 ms: 1.04x slower                                               |
| genshi_text     | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                               |
| genshi_xml      | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                               |
| mako            | 6.94 ms                                                             | 7.72 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                               | 1.08x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231122-pythonperf1_win32-x86-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 98.7 us: 1.37x faster                                               |
| create_gc_cycles           | 756 us                                                              | 645 us: 1.17x faster                                                |
| pickle_list                | 3.57 us                                                             | 3.17 us: 1.12x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.84 us: 1.07x faster                                               |
| pickle                     | 8.07 us                                                             | 7.57 us: 1.07x faster                                               |
| pickle_dict                | 20.8 us                                                             | 19.8 us: 1.05x faster                                               |
| json_loads                 | 20.5 us                                                             | 19.8 us: 1.04x faster                                               |
| sympy_expand               | 375 ms                                                              | 362 ms: 1.04x faster                                                |
| gc_traversal               | 1.43 ms                                                             | 1.39 ms: 1.03x faster                                               |
| unpickle                   | 9.79 us                                                             | 9.58 us: 1.02x faster                                               |
| docutils                   | 1.81 sec                                                            | 1.78 sec: 1.02x faster                                              |
| sympy_str                  | 211 ms                                                              | 207 ms: 1.02x faster                                                |
| sympy_sum                  | 105 ms                                                              | 104 ms: 1.01x faster                                                |
| sqlglot_parse              | 964 us                                                              | 953 us: 1.01x faster                                                |
| crypto_pyaes               | 55.8 ms                                                             | 55.4 ms: 1.01x faster                                               |
| unpickle_list              | 2.93 us                                                             | 2.94 us: 1.00x slower                                               |
| html5lib                   | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                               |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                |
| telco                      | 6.03 ms                                                             | 6.08 ms: 1.01x slower                                               |
| json                       | 4.10 ms                                                             | 4.14 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.01x slower                                               |
| deepcopy_reduce            | 2.59 us                                                             | 2.63 us: 1.02x slower                                               |
| json_dumps                 | 6.84 ms                                                             | 6.96 ms: 1.02x slower                                               |
| sympy_integrate            | 14.6 ms                                                             | 14.9 ms: 1.02x slower                                               |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                               |
| regex_dna                  | 118 ms                                                              | 120 ms: 1.02x slower                                                |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                              |
| pprint_safe_repr           | 607 ms                                                              | 621 ms: 1.02x slower                                                |
| sqlglot_normalize          | 206 ms                                                              | 212 ms: 1.03x slower                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.28 sec: 1.03x slower                                              |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.03x slower                                                |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                               |
| django_template            | 30.1 ms                                                             | 31.2 ms: 1.04x slower                                               |
| pylint                     | 217 ms                                                              | 226 ms: 1.04x slower                                                |
| tornado_http               | 94.3 ms                                                             | 98.2 ms: 1.04x slower                                               |
| chameleon                  | 5.71 ms                                                             | 5.96 ms: 1.04x slower                                               |
| sqlglot_optimize           | 39.7 ms                                                             | 41.5 ms: 1.04x slower                                               |
| async_generators           | 266 ms                                                              | 278 ms: 1.04x slower                                                |
| xml_etree_generate         | 59.6 ms                                                             | 62.8 ms: 1.05x slower                                               |
| 2to3                       | 233 ms                                                              | 246 ms: 1.05x slower                                                |
| deepcopy                   | 280 us                                                              | 295 us: 1.06x slower                                                |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.06x slower                                                |
| comprehensions             | 11.9 us                                                             | 12.6 us: 1.06x slower                                               |
| unpickle_pure_python       | 147 us                                                              | 156 us: 1.06x slower                                                |
| bench_thread_pool          | 985 us                                                              | 1.05 ms: 1.06x slower                                               |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                              |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.07 ms: 1.07x slower                                               |
| go                         | 101 ms                                                              | 108 ms: 1.07x slower                                                |
| pathlib                    | 83.9 ms                                                             | 89.7 ms: 1.07x slower                                               |
| richards_super             | 35.5 ms                                                             | 38.0 ms: 1.07x slower                                               |
| richards                   | 31.2 ms                                                             | 33.7 ms: 1.08x slower                                               |
| chaos                      | 48.0 ms                                                             | 51.8 ms: 1.08x slower                                               |
| genshi_text                | 20.1 ms                                                             | 21.7 ms: 1.08x slower                                               |
| coroutines                 | 15.5 ms                                                             | 16.7 ms: 1.08x slower                                               |
| pickle_pure_python         | 213 us                                                              | 231 us: 1.08x slower                                                |
| xml_etree_iterparse        | 64.2 ms                                                             | 69.5 ms: 1.08x slower                                               |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 511 ms: 1.08x slower                                                |
| meteor_contest             | 74.1 ms                                                             | 80.4 ms: 1.09x slower                                               |
| pyflate                    | 308 ms                                                              | 335 ms: 1.09x slower                                                |
| xml_etree_process          | 42.1 ms                                                             | 45.8 ms: 1.09x slower                                               |
| genshi_xml                 | 44.3 ms                                                             | 48.4 ms: 1.09x slower                                               |
| logging_format             | 8.13 us                                                             | 8.90 us: 1.09x slower                                               |
| tomli_loads                | 1.65 sec                                                            | 1.81 sec: 1.10x slower                                              |
| python_startup_no_site     | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                               |
| thrift                     | 9.73 ms                                                             | 10.7 ms: 1.10x slower                                               |
| spectral_norm              | 68.0 ms                                                             | 75.0 ms: 1.10x slower                                               |
| pycparser                  | 777 ms                                                              | 862 ms: 1.11x slower                                                |
| scimark_fft                | 198 ms                                                              | 220 ms: 1.11x slower                                                |
| mako                       | 6.94 ms                                                             | 7.72 ms: 1.11x slower                                               |
| async_tree_none            | 228 ms                                                              | 254 ms: 1.11x slower                                                |
| fannkuch                   | 270 ms                                                              | 302 ms: 1.12x slower                                                |
| logging_simple             | 7.47 us                                                             | 8.35 us: 1.12x slower                                               |
| scimark_monte_carlo        | 45.2 ms                                                             | 50.6 ms: 1.12x slower                                               |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 506 ms: 1.13x slower                                                |
| deepcopy_memo              | 23.5 us                                                             | 26.6 us: 1.13x slower                                               |
| float                      | 52.4 ms                                                             | 59.8 ms: 1.14x slower                                               |
| deltablue                  | 2.23 ms                                                             | 2.55 ms: 1.14x slower                                               |
| async_tree_memoization     | 275 ms                                                              | 317 ms: 1.15x slower                                                |
| nbody                      | 76.9 ms                                                             | 88.9 ms: 1.16x slower                                               |
| scimark_lu                 | 59.4 ms                                                             | 69.0 ms: 1.16x slower                                               |
| nqueens                    | 68.7 ms                                                             | 80.1 ms: 1.17x slower                                               |
| async_tree_io_tg           | 529 ms                                                              | 619 ms: 1.17x slower                                                |
| async_tree_io              | 530 ms                                                              | 623 ms: 1.17x slower                                                |
| hexiom                     | 4.23 ms                                                             | 4.97 ms: 1.18x slower                                               |
| raytrace                   | 189 ms                                                              | 223 ms: 1.18x slower                                                |
| scimark_sor                | 81.0 ms                                                             | 97.7 ms: 1.21x slower                                               |
| logging_silent             | 57.9 ns                                                             | 70.3 ns: 1.22x slower                                               |
| async_tree_none_tg         | 203 ms                                                              | 248 ms: 1.22x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 312 ms: 1.23x slower                                                |
| generators                 | 21.2 ms                                                             | 27.0 ms: 1.28x slower                                               |
| coverage                   | 307 ms                                                              | 512 ms: 1.67x slower                                                |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                        |

Benchmark hidden because not significant (4): asyncio_tcp, bench_mp_pool, flaskblogging, python_startup

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown