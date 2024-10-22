# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-x86
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 245 ms: 1.03x faster                                                  |
| chameleon      | 6.14 ms                                                         | 5.83 ms: 1.05x faster                                                 |
| docutils       | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                |
| html5lib       | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 717 ms: 1.17x faster                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                  |
| async_tree_none            | 246 ms                                                          | 230 ms: 1.07x faster                                                  |
| async_tree_none_tg         | 219 ms                                                          | 208 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 452 ms: 1.03x faster                                                  |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                |
| async_generators           | 274 ms                                                          | 278 ms: 1.02x slower                                                  |
| coroutines                 | 15.7 ms                                                         | 16.0 ms: 1.02x slower                                                 |
| async_tree_io_tg           | 509 ms                                                          | 537 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 53.5 ms: 1.08x faster                                                 |
| nbody          | 81.9 ms                                                         | 79.6 ms: 1.03x faster                                                 |
| pidigits       | 202 ms                                                          | 199 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                           | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 101 ms: 1.02x faster                                                  |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                 |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                  |
| regex_effbot   | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                           | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 3.40 us                                                         | 3.15 us: 1.08x faster                                                 |
| pickle_dict          | 21.7 us                                                         | 20.4 us: 1.06x faster                                                 |
| unpickle_list        | 3.09 us                                                         | 2.92 us: 1.06x faster                                                 |
| unpickle             | 10.5 us                                                         | 10.0 us: 1.05x faster                                                 |
| json_dumps           | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                 |
| pickle               | 8.42 us                                                         | 8.01 us: 1.05x faster                                                 |
| tomli_loads          | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                                |
| pickle_pure_python   | 238 us                                                          | 228 us: 1.04x faster                                                  |
| unpickle_pure_python | 162 us                                                          | 155 us: 1.04x faster                                                  |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                  |
| json_loads           | 21.0 us                                                         | 20.6 us: 1.02x faster                                                 |
| xml_etree_generate   | 62.6 ms                                                         | 62.2 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 19.8 ms: 1.14x faster                                                 |
| genshi_xml      | 49.5 ms                                                         | 43.9 ms: 1.13x faster                                                 |
| django_template | 32.7 ms                                                         | 31.1 ms: 1.05x faster                                                 |
| mako            | 7.31 ms                                                         | 7.08 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 717 ms: 1.17x faster                                                  |
| genshi_text                | 22.4 ms                                                         | 19.8 ms: 1.14x faster                                                 |
| genshi_xml                 | 49.5 ms                                                         | 43.9 ms: 1.13x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                  |
| pycparser                  | 869 ms                                                          | 798 ms: 1.09x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                  |
| nqueens                    | 75.1 ms                                                         | 69.5 ms: 1.08x faster                                                 |
| float                      | 57.8 ms                                                         | 53.5 ms: 1.08x faster                                                 |
| pickle_list                | 3.40 us                                                         | 3.15 us: 1.08x faster                                                 |
| pylint                     | 225 ms                                                          | 210 ms: 1.07x faster                                                  |
| async_tree_none            | 246 ms                                                          | 230 ms: 1.07x faster                                                  |
| raytrace                   | 205 ms                                                          | 193 ms: 1.07x faster                                                  |
| deepcopy                   | 307 us                                                          | 288 us: 1.06x faster                                                  |
| sqlglot_transpile          | 1.29 ms                                                         | 1.22 ms: 1.06x faster                                                 |
| sqlglot_parse              | 1.05 ms                                                         | 989 us: 1.06x faster                                                  |
| pickle_dict                | 21.7 us                                                         | 20.4 us: 1.06x faster                                                 |
| pprint_safe_repr           | 644 ms                                                          | 608 ms: 1.06x faster                                                  |
| unpickle_list              | 3.09 us                                                         | 2.92 us: 1.06x faster                                                 |
| html5lib                   | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                 |
| deepcopy_reduce            | 2.85 us                                                         | 2.70 us: 1.06x faster                                                 |
| unpickle                   | 10.5 us                                                         | 10.0 us: 1.05x faster                                                 |
| chameleon                  | 6.14 ms                                                         | 5.83 ms: 1.05x faster                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.03 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 219 ms                                                          | 208 ms: 1.05x faster                                                  |
| pickle                     | 8.42 us                                                         | 8.01 us: 1.05x faster                                                 |
| deepcopy_memo              | 26.2 us                                                         | 24.9 us: 1.05x faster                                                 |
| django_template            | 32.7 ms                                                         | 31.1 ms: 1.05x faster                                                 |
| scimark_sor                | 91.8 ms                                                         | 87.5 ms: 1.05x faster                                                 |
| crypto_pyaes               | 58.2 ms                                                         | 55.4 ms: 1.05x faster                                                 |
| tomli_loads                | 1.73 sec                                                        | 1.65 sec: 1.05x faster                                                |
| chaos                      | 51.2 ms                                                         | 48.9 ms: 1.05x faster                                                 |
| sqlglot_normalize          | 220 ms                                                          | 210 ms: 1.05x faster                                                  |
| sqlglot_optimize           | 42.5 ms                                                         | 40.6 ms: 1.04x faster                                                 |
| pickle_pure_python         | 238 us                                                          | 228 us: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.30 sec                                                        | 1.25 sec: 1.04x faster                                                |
| unpickle_pure_python       | 162 us                                                          | 155 us: 1.04x faster                                                  |
| go                         | 111 ms                                                          | 108 ms: 1.03x faster                                                  |
| mako                       | 7.31 ms                                                         | 7.08 ms: 1.03x faster                                                 |
| 2to3                       | 253 ms                                                          | 245 ms: 1.03x faster                                                  |
| nbody                      | 81.9 ms                                                         | 79.6 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.82 ms: 1.03x faster                                                 |
| deltablue                  | 2.41 ms                                                         | 2.34 ms: 1.03x faster                                                 |
| coverage                   | 333 ms                                                          | 324 ms: 1.03x faster                                                  |
| fannkuch                   | 293 ms                                                          | 286 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 452 ms: 1.03x faster                                                  |
| logging_silent             | 61.6 ns                                                         | 60.1 ns: 1.02x faster                                                 |
| scimark_lu                 | 63.5 ms                                                         | 62.0 ms: 1.02x faster                                                 |
| regex_compile              | 103 ms                                                          | 101 ms: 1.02x faster                                                  |
| scimark_monte_carlo        | 50.3 ms                                                         | 49.2 ms: 1.02x faster                                                 |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                  |
| json_loads                 | 21.0 us                                                         | 20.6 us: 1.02x faster                                                 |
| pyflate                    | 326 ms                                                          | 319 ms: 1.02x faster                                                  |
| sympy_str                  | 215 ms                                                          | 211 ms: 1.02x faster                                                  |
| comprehensions             | 12.7 us                                                         | 12.5 us: 1.02x faster                                                 |
| sympy_expand               | 375 ms                                                          | 368 ms: 1.02x faster                                                  |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| bench_mp_pool              | 74.3 ms                                                         | 73.1 ms: 1.02x faster                                                 |
| telco                      | 6.67 ms                                                         | 6.56 ms: 1.02x faster                                                 |
| meteor_contest             | 77.0 ms                                                         | 75.8 ms: 1.02x faster                                                 |
| generators                 | 22.1 ms                                                         | 21.8 ms: 1.02x faster                                                 |
| spectral_norm              | 71.3 ms                                                         | 70.3 ms: 1.01x faster                                                 |
| pidigits                   | 202 ms                                                          | 199 ms: 1.01x faster                                                  |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.01x faster                                                  |
| richards                   | 33.8 ms                                                         | 33.3 ms: 1.01x faster                                                 |
| mdp                        | 1.67 sec                                                        | 1.65 sec: 1.01x faster                                                |
| hexiom                     | 4.64 ms                                                         | 4.58 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                |
| logging_simple             | 7.87 us                                                         | 7.79 us: 1.01x faster                                                 |
| logging_format             | 8.57 us                                                         | 8.48 us: 1.01x faster                                                 |
| scimark_fft                | 206 ms                                                          | 204 ms: 1.01x faster                                                  |
| dulwich_log                | 49.7 ms                                                         | 49.2 ms: 1.01x faster                                                 |
| pathlib                    | 89.4 ms                                                         | 88.7 ms: 1.01x faster                                                 |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                 |
| xml_etree_generate         | 62.6 ms                                                         | 62.2 ms: 1.01x faster                                                 |
| richards_super             | 38.0 ms                                                         | 37.7 ms: 1.01x faster                                                 |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                 |
| async_generators           | 274 ms                                                          | 278 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 136 us                                                          | 139 us: 1.02x slower                                                  |
| docutils                   | 1.82 sec                                                        | 1.85 sec: 1.02x slower                                                |
| regex_v8                   | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                 |
| coroutines                 | 15.7 ms                                                         | 16.0 ms: 1.02x slower                                                 |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                  |
| regex_effbot               | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                                 |
| create_gc_cycles           | 713 us                                                          | 751 us: 1.05x slower                                                  |
| async_tree_io_tg           | 509 ms                                                          | 537 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (11): bench_thread_pool, xml_etree_process, python_startup, tornado_http, thrift, unpack_sequence, python_startup_no_site, async_tree_io, json, flaskblogging, xml_etree_iterparse

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown