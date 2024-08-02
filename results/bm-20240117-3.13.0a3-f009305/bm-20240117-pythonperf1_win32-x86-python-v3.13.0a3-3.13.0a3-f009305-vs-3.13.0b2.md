# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a3
- machine: windows-x86
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.02x faster
- HPT reliability: 90.87%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 232 ms: 1.01x faster                                                |
| chameleon      | 5.71 ms                                                             | 5.40 ms: 1.06x faster                                               |
| docutils       | 1.81 sec                                                            | 1.72 sec: 1.06x faster                                              |
| html5lib       | 45.4 ms                                                             | 44.0 ms: 1.03x faster                                               |
| tornado_http   | 94.3 ms                                                             | 96.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 499 ms: 1.06x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 571 ms: 1.08x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 489 ms: 1.09x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 303 ms: 1.10x slower                                                |
| async_tree_io              | 530 ms                                                              | 588 ms: 1.11x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 229 ms: 1.13x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 290 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                               | 1.10x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 74.0 ms: 1.04x faster                                               |
| float          | 52.4 ms                                                             | 51.1 ms: 1.02x faster                                               |
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                               | 1.02x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 92.5 ms: 1.08x faster                                               |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                               |
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                               |
| regex_dna      | 118 ms                                                              | 125 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                               | 1.00x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.33 us: 1.07x faster                                               |
| unpickle_pure_python | 147 us                                                              | 140 us: 1.05x faster                                                |
| pickle               | 8.07 us                                                             | 7.71 us: 1.05x faster                                               |
| pickle_pure_python   | 213 us                                                              | 204 us: 1.05x faster                                                |
| pickle_dict          | 20.8 us                                                             | 20.0 us: 1.04x faster                                               |
| json_loads           | 20.5 us                                                             | 19.8 us: 1.04x faster                                               |
| xml_etree_process    | 42.1 ms                                                             | 41.1 ms: 1.02x faster                                               |
| tomli_loads          | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                              |
| xml_etree_generate   | 59.6 ms                                                             | 58.8 ms: 1.01x faster                                               |
| json_dumps           | 6.84 ms                                                             | 6.75 ms: 1.01x faster                                               |
| unpickle             | 9.79 us                                                             | 9.71 us: 1.01x faster                                               |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.4 ms: 1.03x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                |
| unpickle_list        | 2.93 us                                                             | 3.08 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                               | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.7 ms: 1.02x slower                                               |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 18.1 ms: 1.11x faster                                               |
| genshi_xml      | 44.3 ms                                                             | 41.6 ms: 1.06x faster                                               |
| django_template | 30.1 ms                                                             | 29.0 ms: 1.04x faster                                               |
| mako            | 6.94 ms                                                             | 6.84 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                               | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 87.7 us: 1.55x faster                                               |
| deepcopy_reduce            | 2.59 us                                                             | 2.22 us: 1.16x faster                                               |
| create_gc_cycles           | 756 us                                                              | 651 us: 1.16x faster                                                |
| sqlglot_parse              | 964 us                                                              | 848 us: 1.14x faster                                                |
| richards_super             | 35.5 ms                                                             | 31.4 ms: 1.13x faster                                               |
| richards                   | 31.2 ms                                                             | 27.8 ms: 1.12x faster                                               |
| pprint_safe_repr           | 607 ms                                                              | 543 ms: 1.12x faster                                                |
| genshi_text                | 20.1 ms                                                             | 18.1 ms: 1.11x faster                                               |
| pprint_pformat             | 1.24 sec                                                            | 1.12 sec: 1.11x faster                                              |
| sqlglot_transpile          | 1.19 ms                                                             | 1.08 ms: 1.11x faster                                               |
| deepcopy                   | 280 us                                                              | 255 us: 1.10x faster                                                |
| crypto_pyaes               | 55.8 ms                                                             | 51.0 ms: 1.09x faster                                               |
| sympy_expand               | 375 ms                                                              | 343 ms: 1.09x faster                                                |
| coroutines                 | 15.5 ms                                                             | 14.2 ms: 1.09x faster                                               |
| deepcopy_memo              | 23.5 us                                                             | 21.6 us: 1.09x faster                                               |
| sympy_str                  | 211 ms                                                              | 194 ms: 1.09x faster                                                |
| sqlite_synth               | 1.96 us                                                             | 1.81 us: 1.09x faster                                               |
| regex_compile              | 99.9 ms                                                             | 92.5 ms: 1.08x faster                                               |
| spectral_norm              | 68.0 ms                                                             | 63.0 ms: 1.08x faster                                               |
| telco                      | 6.03 ms                                                             | 5.62 ms: 1.07x faster                                               |
| pickle_list                | 3.57 us                                                             | 3.33 us: 1.07x faster                                               |
| sympy_sum                  | 105 ms                                                              | 98.5 ms: 1.07x faster                                               |
| genshi_xml                 | 44.3 ms                                                             | 41.6 ms: 1.06x faster                                               |
| comprehensions             | 11.9 us                                                             | 11.2 us: 1.06x faster                                               |
| go                         | 101 ms                                                              | 95.1 ms: 1.06x faster                                               |
| chameleon                  | 5.71 ms                                                             | 5.40 ms: 1.06x faster                                               |
| docutils                   | 1.81 sec                                                            | 1.72 sec: 1.06x faster                                              |
| chaos                      | 48.0 ms                                                             | 45.5 ms: 1.05x faster                                               |
| unpickle_pure_python       | 147 us                                                              | 140 us: 1.05x faster                                                |
| mdp                        | 1.60 sec                                                            | 1.53 sec: 1.05x faster                                              |
| sympy_integrate            | 14.6 ms                                                             | 14.0 ms: 1.05x faster                                               |
| pickle                     | 8.07 us                                                             | 7.71 us: 1.05x faster                                               |
| pickle_pure_python         | 213 us                                                              | 204 us: 1.05x faster                                                |
| sqlglot_normalize          | 206 ms                                                              | 197 ms: 1.04x faster                                                |
| pickle_dict                | 20.8 us                                                             | 20.0 us: 1.04x faster                                               |
| sqlglot_optimize           | 39.7 ms                                                             | 38.2 ms: 1.04x faster                                               |
| nbody                      | 76.9 ms                                                             | 74.0 ms: 1.04x faster                                               |
| asyncio_tcp                | 662 ms                                                              | 638 ms: 1.04x faster                                                |
| json_loads                 | 20.5 us                                                             | 19.8 us: 1.04x faster                                               |
| django_template            | 30.1 ms                                                             | 29.0 ms: 1.04x faster                                               |
| html5lib                   | 45.4 ms                                                             | 44.0 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.79 ms: 1.03x faster                                               |
| gc_traversal               | 1.43 ms                                                             | 1.40 ms: 1.02x faster                                               |
| float                      | 52.4 ms                                                             | 51.1 ms: 1.02x faster                                               |
| deltablue                  | 2.23 ms                                                             | 2.18 ms: 1.02x faster                                               |
| xml_etree_process          | 42.1 ms                                                             | 41.1 ms: 1.02x faster                                               |
| hexiom                     | 4.23 ms                                                             | 4.14 ms: 1.02x faster                                               |
| tomli_loads                | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                              |
| scimark_monte_carlo        | 45.2 ms                                                             | 44.3 ms: 1.02x faster                                               |
| scimark_sor                | 81.0 ms                                                             | 79.6 ms: 1.02x faster                                               |
| xml_etree_generate         | 59.6 ms                                                             | 58.8 ms: 1.01x faster                                               |
| mako                       | 6.94 ms                                                             | 6.84 ms: 1.01x faster                                               |
| logging_silent             | 57.9 ns                                                             | 57.1 ns: 1.01x faster                                               |
| json_dumps                 | 6.84 ms                                                             | 6.75 ms: 1.01x faster                                               |
| fannkuch                   | 270 ms                                                              | 267 ms: 1.01x faster                                                |
| pyflate                    | 308 ms                                                              | 306 ms: 1.01x faster                                                |
| unpickle                   | 9.79 us                                                             | 9.71 us: 1.01x faster                                               |
| meteor_contest             | 74.1 ms                                                             | 73.7 ms: 1.01x faster                                               |
| 2to3                       | 233 ms                                                              | 232 ms: 1.01x faster                                                |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                                |
| raytrace                   | 189 ms                                                              | 191 ms: 1.01x slower                                                |
| scimark_lu                 | 59.4 ms                                                             | 60.2 ms: 1.01x slower                                               |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                               |
| python_startup             | 22.2 ms                                                             | 22.7 ms: 1.02x slower                                               |
| async_generators           | 266 ms                                                              | 271 ms: 1.02x slower                                                |
| pycparser                  | 777 ms                                                              | 793 ms: 1.02x slower                                                |
| tornado_http               | 94.3 ms                                                             | 96.3 ms: 1.02x slower                                               |
| logging_format             | 8.13 us                                                             | 8.33 us: 1.02x slower                                               |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.03x slower                                               |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                               |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                              |
| logging_simple             | 7.47 us                                                             | 7.69 us: 1.03x slower                                               |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.4 ms: 1.03x slower                                               |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                |
| unpickle_list              | 2.93 us                                                             | 3.08 us: 1.05x slower                                               |
| thrift                     | 9.73 ms                                                             | 10.3 ms: 1.05x slower                                               |
| regex_dna                  | 118 ms                                                              | 125 ms: 1.05x slower                                                |
| pathlib                    | 83.9 ms                                                             | 88.6 ms: 1.06x slower                                               |
| nqueens                    | 68.7 ms                                                             | 72.6 ms: 1.06x slower                                               |
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 499 ms: 1.06x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 571 ms: 1.08x slower                                                |
| bench_mp_pool              | 69.4 ms                                                             | 74.9 ms: 1.08x slower                                               |
| generators                 | 21.2 ms                                                             | 22.9 ms: 1.08x slower                                               |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 489 ms: 1.09x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 303 ms: 1.10x slower                                                |
| async_tree_io              | 530 ms                                                              | 588 ms: 1.11x slower                                                |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                               |
| async_tree_none_tg         | 203 ms                                                              | 229 ms: 1.13x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 290 ms: 1.14x slower                                                |
| coverage                   | 307 ms                                                              | 479 ms: 1.56x slower                                                |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                        |

Benchmark hidden because not significant (4): scimark_fft, flaskblogging, pylint, json

# HPT report

- Reliability score: 90.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown