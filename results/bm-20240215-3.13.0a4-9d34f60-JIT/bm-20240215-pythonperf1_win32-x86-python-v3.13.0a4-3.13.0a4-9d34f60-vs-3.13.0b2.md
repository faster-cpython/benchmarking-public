# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 256 ms: 1.10x slower                                                |
| chameleon      | 5.71 ms                                                             | 6.01 ms: 1.05x slower                                               |
| docutils       | 1.81 sec                                                            | 1.82 sec: 1.00x slower                                              |
| tornado_http   | 94.3 ms                                                             | 99.9 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                               | 1.05x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 515 ms: 1.09x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 503 ms: 1.12x slower                                                |
| async_tree_none            | 228 ms                                                              | 260 ms: 1.14x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 612 ms: 1.16x slower                                                |
| async_tree_io              | 530 ms                                                              | 624 ms: 1.18x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 325 ms: 1.18x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 246 ms: 1.21x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 313 ms: 1.23x slower                                                |
| Geometric mean             | (ref)                                                               | 1.16x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 202 ms: 1.02x slower                                                |
| float          | 52.4 ms                                                             | 53.9 ms: 1.03x slower                                               |
| nbody          | 76.9 ms                                                             | 89.7 ms: 1.17x slower                                               |
| Geometric mean | (ref)                                                               | 1.07x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.02x slower                                               |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                               |
| regex_compile  | 99.9 ms                                                             | 110 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                               | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.35 us: 1.06x faster                                               |
| pickle_dict          | 20.8 us                                                             | 19.9 us: 1.04x faster                                               |
| unpickle_list        | 2.93 us                                                             | 2.87 us: 1.02x faster                                               |
| json_loads           | 20.5 us                                                             | 20.3 us: 1.01x faster                                               |
| pickle               | 8.07 us                                                             | 8.11 us: 1.00x slower                                               |
| xml_etree_generate   | 59.6 ms                                                             | 60.2 ms: 1.01x slower                                               |
| json_dumps           | 6.84 ms                                                             | 6.95 ms: 1.02x slower                                               |
| xml_etree_process    | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                               |
| xml_etree_iterparse  | 64.2 ms                                                             | 65.9 ms: 1.03x slower                                               |
| unpickle             | 9.79 us                                                             | 10.1 us: 1.03x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.05x slower                                                |
| pickle_pure_python   | 213 us                                                              | 223 us: 1.05x slower                                                |
| unpickle_pure_python | 147 us                                                              | 156 us: 1.06x slower                                                |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.5 ms: 1.01x slower                                               |
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 6.94 ms                                                             | 7.43 ms: 1.07x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 98.7 us: 1.37x faster                                               |
| create_gc_cycles           | 756 us                                                              | 646 us: 1.17x faster                                                |
| pickle_list                | 3.57 us                                                             | 3.35 us: 1.06x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.85 us: 1.06x faster                                               |
| asyncio_tcp                | 662 ms                                                              | 632 ms: 1.05x faster                                                |
| pickle_dict                | 20.8 us                                                             | 19.9 us: 1.04x faster                                               |
| coroutines                 | 15.5 ms                                                             | 14.9 ms: 1.04x faster                                               |
| deepcopy_reduce            | 2.59 us                                                             | 2.51 us: 1.03x faster                                               |
| unpickle_list              | 2.93 us                                                             | 2.87 us: 1.02x faster                                               |
| gc_traversal               | 1.43 ms                                                             | 1.42 ms: 1.01x faster                                               |
| json_loads                 | 20.5 us                                                             | 20.3 us: 1.01x faster                                               |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 16.7 sec: 1.01x faster                                              |
| docutils                   | 1.81 sec                                                            | 1.82 sec: 1.00x slower                                              |
| pickle                     | 8.07 us                                                             | 8.11 us: 1.00x slower                                               |
| xml_etree_generate         | 59.6 ms                                                             | 60.2 ms: 1.01x slower                                               |
| sympy_expand               | 375 ms                                                              | 379 ms: 1.01x slower                                                |
| python_startup             | 22.2 ms                                                             | 22.5 ms: 1.01x slower                                               |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.02x slower                                               |
| regex_dna                  | 118 ms                                                              | 120 ms: 1.02x slower                                                |
| pidigits                   | 199 ms                                                              | 202 ms: 1.02x slower                                                |
| json_dumps                 | 6.84 ms                                                             | 6.95 ms: 1.02x slower                                               |
| sqlglot_transpile          | 1.19 ms                                                             | 1.21 ms: 1.02x slower                                               |
| xml_etree_process          | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                               |
| deepcopy                   | 280 us                                                              | 285 us: 1.02x slower                                                |
| xml_etree_iterparse        | 64.2 ms                                                             | 65.9 ms: 1.03x slower                                               |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                               |
| richards_super             | 35.5 ms                                                             | 36.5 ms: 1.03x slower                                               |
| float                      | 52.4 ms                                                             | 53.9 ms: 1.03x slower                                               |
| bench_mp_pool              | 69.4 ms                                                             | 71.5 ms: 1.03x slower                                               |
| richards                   | 31.2 ms                                                             | 32.2 ms: 1.03x slower                                               |
| unpickle                   | 9.79 us                                                             | 10.1 us: 1.03x slower                                               |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.04x slower                                                |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                               |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                               |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.05x slower                                                |
| pickle_pure_python         | 213 us                                                              | 223 us: 1.05x slower                                                |
| sympy_sum                  | 105 ms                                                              | 110 ms: 1.05x slower                                                |
| chameleon                  | 5.71 ms                                                             | 6.01 ms: 1.05x slower                                               |
| unpickle_pure_python       | 147 us                                                              | 156 us: 1.06x slower                                                |
| tornado_http               | 94.3 ms                                                             | 99.9 ms: 1.06x slower                                               |
| mako                       | 6.94 ms                                                             | 7.43 ms: 1.07x slower                                               |
| deepcopy_memo              | 23.5 us                                                             | 25.3 us: 1.08x slower                                               |
| spectral_norm              | 68.0 ms                                                             | 73.2 ms: 1.08x slower                                               |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.12 ms: 1.09x slower                                               |
| telco                      | 6.03 ms                                                             | 6.55 ms: 1.09x slower                                               |
| sqlglot_normalize          | 206 ms                                                              | 224 ms: 1.09x slower                                                |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                               |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 515 ms: 1.09x slower                                                |
| crypto_pyaes               | 55.8 ms                                                             | 61.0 ms: 1.09x slower                                               |
| 2to3                       | 233 ms                                                              | 256 ms: 1.10x slower                                                |
| sqlglot_optimize           | 39.7 ms                                                             | 43.7 ms: 1.10x slower                                               |
| logging_format             | 8.13 us                                                             | 8.97 us: 1.10x slower                                               |
| regex_compile              | 99.9 ms                                                             | 110 ms: 1.10x slower                                                |
| scimark_lu                 | 59.4 ms                                                             | 65.6 ms: 1.10x slower                                               |
| scimark_sor                | 81.0 ms                                                             | 89.6 ms: 1.11x slower                                               |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.12x slower                                               |
| logging_simple             | 7.47 us                                                             | 8.35 us: 1.12x slower                                               |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 503 ms: 1.12x slower                                                |
| async_generators           | 266 ms                                                              | 300 ms: 1.13x slower                                                |
| meteor_contest             | 74.1 ms                                                             | 83.8 ms: 1.13x slower                                               |
| async_tree_none            | 228 ms                                                              | 260 ms: 1.14x slower                                                |
| pycparser                  | 777 ms                                                              | 891 ms: 1.15x slower                                                |
| mdp                        | 1.60 sec                                                            | 1.85 sec: 1.15x slower                                              |
| deltablue                  | 2.23 ms                                                             | 2.58 ms: 1.15x slower                                               |
| async_tree_io_tg           | 529 ms                                                              | 612 ms: 1.16x slower                                                |
| logging_silent             | 57.9 ns                                                             | 67.1 ns: 1.16x slower                                               |
| generators                 | 21.2 ms                                                             | 24.6 ms: 1.16x slower                                               |
| nbody                      | 76.9 ms                                                             | 89.7 ms: 1.17x slower                                               |
| pprint_safe_repr           | 607 ms                                                              | 713 ms: 1.18x slower                                                |
| async_tree_io              | 530 ms                                                              | 624 ms: 1.18x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 325 ms: 1.18x slower                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.47 sec: 1.19x slower                                              |
| comprehensions             | 11.9 us                                                             | 14.1 us: 1.19x slower                                               |
| fannkuch                   | 270 ms                                                              | 322 ms: 1.19x slower                                                |
| pyflate                    | 308 ms                                                              | 370 ms: 1.20x slower                                                |
| scimark_fft                | 198 ms                                                              | 239 ms: 1.21x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 246 ms: 1.21x slower                                                |
| go                         | 101 ms                                                              | 123 ms: 1.22x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 313 ms: 1.23x slower                                                |
| chaos                      | 48.0 ms                                                             | 61.0 ms: 1.27x slower                                               |
| raytrace                   | 189 ms                                                              | 240 ms: 1.27x slower                                                |
| nqueens                    | 68.7 ms                                                             | 88.7 ms: 1.29x slower                                               |
| coverage                   | 307 ms                                                              | 464 ms: 1.51x slower                                                |
| hexiom                     | 4.23 ms                                                             | 6.61 ms: 1.56x slower                                               |
| scimark_monte_carlo        | 45.2 ms                                                             | 71.6 ms: 1.58x slower                                               |
| Geometric mean             | (ref)                                                               | 1.08x slower                                                        |

Benchmark hidden because not significant (3): sqlglot_parse, tomli_loads, pathlib
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown