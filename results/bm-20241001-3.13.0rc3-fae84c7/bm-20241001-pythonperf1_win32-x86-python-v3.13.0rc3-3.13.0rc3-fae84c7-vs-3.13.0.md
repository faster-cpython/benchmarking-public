# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-x86
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 243 ms: 1.04x faster                                                  |
| chameleon      | 6.14 ms                                                         | 5.98 ms: 1.03x faster                                                 |
| docutils       | 1.82 sec                                                        | 1.77 sec: 1.03x faster                                                |
| html5lib       | 48.3 ms                                                         | 45.6 ms: 1.06x faster                                                 |
| tornado_http   | 104 ms                                                          | 102 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 739 ms: 1.14x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.08x faster                                                  |
| async_tree_none            | 246 ms                                                          | 231 ms: 1.06x faster                                                  |
| async_tree_none_tg         | 219 ms                                                          | 206 ms: 1.06x faster                                                  |
| async_tree_io_tg           | 509 ms                                                          | 482 ms: 1.06x faster                                                  |
| async_tree_io              | 537 ms                                                          | 508 ms: 1.06x faster                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 273 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 473 ms: 1.04x faster                                                  |
| async_generators           | 274 ms                                                          | 263 ms: 1.04x faster                                                  |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                  |
| coroutines                 | 15.7 ms                                                         | 15.6 ms: 1.00x faster                                                 |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 78.0 ms: 1.05x faster                                                 |
| float          | 57.8 ms                                                         | 55.2 ms: 1.05x faster                                                 |
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                           | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 99.5 ms: 1.04x faster                                                 |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.02x slower                                                 |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                  |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                           | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 3.09 us                                                         | 2.78 us: 1.11x faster                                                 |
| pickle               | 8.42 us                                                         | 7.79 us: 1.08x faster                                                 |
| pickle_dict          | 21.7 us                                                         | 20.3 us: 1.07x faster                                                 |
| xml_etree_parse      | 109 ms                                                          | 103 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 65.1 ms                                                         | 62.2 ms: 1.05x faster                                                 |
| tomli_loads          | 1.73 sec                                                        | 1.67 sec: 1.04x faster                                                |
| pickle_pure_python   | 238 us                                                          | 231 us: 1.03x faster                                                  |
| unpickle_pure_python | 162 us                                                          | 157 us: 1.03x faster                                                  |
| pickle_list          | 3.40 us                                                         | 3.32 us: 1.02x faster                                                 |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.02x faster                                                 |
| json_loads           | 21.0 us                                                         | 20.6 us: 1.02x faster                                                 |
| xml_etree_process    | 45.0 ms                                                         | 44.3 ms: 1.02x faster                                                 |
| json_dumps           | 7.40 ms                                                         | 7.48 ms: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.7 ms: 1.02x slower                                                 |
| python_startup_no_site | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 32.7 ms                                                         | 29.3 ms: 1.11x faster                                                 |
| genshi_xml      | 49.5 ms                                                         | 45.1 ms: 1.10x faster                                                 |
| genshi_text     | 22.4 ms                                                         | 20.9 ms: 1.08x faster                                                 |
| mako            | 7.31 ms                                                         | 7.06 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 739 ms: 1.14x faster                                                  |
| unpickle_list              | 3.09 us                                                         | 2.78 us: 1.11x faster                                                 |
| django_template            | 32.7 ms                                                         | 29.3 ms: 1.11x faster                                                 |
| sqlglot_parse              | 1.05 ms                                                         | 956 us: 1.10x faster                                                  |
| genshi_xml                 | 49.5 ms                                                         | 45.1 ms: 1.10x faster                                                 |
| sqlglot_transpile          | 1.29 ms                                                         | 1.19 ms: 1.09x faster                                                 |
| nqueens                    | 75.1 ms                                                         | 69.1 ms: 1.09x faster                                                 |
| pickle                     | 8.42 us                                                         | 7.79 us: 1.08x faster                                                 |
| genshi_text                | 22.4 ms                                                         | 20.9 ms: 1.08x faster                                                 |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.08x faster                                                  |
| raytrace                   | 205 ms                                                          | 191 ms: 1.07x faster                                                  |
| pycparser                  | 869 ms                                                          | 810 ms: 1.07x faster                                                  |
| pickle_dict                | 21.7 us                                                         | 20.3 us: 1.07x faster                                                 |
| async_tree_none            | 246 ms                                                          | 231 ms: 1.06x faster                                                  |
| chaos                      | 51.2 ms                                                         | 48.3 ms: 1.06x faster                                                 |
| async_tree_none_tg         | 219 ms                                                          | 206 ms: 1.06x faster                                                  |
| deltablue                  | 2.41 ms                                                         | 2.27 ms: 1.06x faster                                                 |
| html5lib                   | 48.3 ms                                                         | 45.6 ms: 1.06x faster                                                 |
| xml_etree_parse            | 109 ms                                                          | 103 ms: 1.06x faster                                                  |
| go                         | 111 ms                                                          | 105 ms: 1.06x faster                                                  |
| async_tree_io_tg           | 509 ms                                                          | 482 ms: 1.06x faster                                                  |
| async_tree_io              | 537 ms                                                          | 508 ms: 1.06x faster                                                  |
| deepcopy                   | 307 us                                                          | 291 us: 1.06x faster                                                  |
| pprint_safe_repr           | 644 ms                                                          | 610 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 220 ms                                                          | 209 ms: 1.05x faster                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 273 ms: 1.05x faster                                                  |
| scimark_monte_carlo        | 50.3 ms                                                         | 47.9 ms: 1.05x faster                                                 |
| telco                      | 6.67 ms                                                         | 6.35 ms: 1.05x faster                                                 |
| nbody                      | 81.9 ms                                                         | 78.0 ms: 1.05x faster                                                 |
| deepcopy_reduce            | 2.85 us                                                         | 2.72 us: 1.05x faster                                                 |
| sqlglot_optimize           | 42.5 ms                                                         | 40.5 ms: 1.05x faster                                                 |
| float                      | 57.8 ms                                                         | 55.2 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 65.1 ms                                                         | 62.2 ms: 1.05x faster                                                 |
| scimark_sor                | 91.8 ms                                                         | 88.0 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 473 ms: 1.04x faster                                                  |
| 2to3                       | 253 ms                                                          | 243 ms: 1.04x faster                                                  |
| async_generators           | 274 ms                                                          | 263 ms: 1.04x faster                                                  |
| pyflate                    | 326 ms                                                          | 313 ms: 1.04x faster                                                  |
| regex_compile              | 103 ms                                                          | 99.5 ms: 1.04x faster                                                 |
| fannkuch                   | 293 ms                                                          | 282 ms: 1.04x faster                                                  |
| tomli_loads                | 1.73 sec                                                        | 1.67 sec: 1.04x faster                                                |
| logging_silent             | 61.6 ns                                                         | 59.5 ns: 1.04x faster                                                 |
| mako                       | 7.31 ms                                                         | 7.06 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.30 sec                                                        | 1.25 sec: 1.03x faster                                                |
| bench_thread_pool          | 1.02 ms                                                         | 989 us: 1.03x faster                                                  |
| pickle_pure_python         | 238 us                                                          | 231 us: 1.03x faster                                                  |
| logging_format             | 8.57 us                                                         | 8.31 us: 1.03x faster                                                 |
| hexiom                     | 4.64 ms                                                         | 4.50 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 162 us                                                          | 157 us: 1.03x faster                                                  |
| docutils                   | 1.82 sec                                                        | 1.77 sec: 1.03x faster                                                |
| coverage                   | 333 ms                                                          | 324 ms: 1.03x faster                                                  |
| comprehensions             | 12.7 us                                                         | 12.4 us: 1.03x faster                                                 |
| generators                 | 22.1 ms                                                         | 21.5 ms: 1.03x faster                                                 |
| richards_super             | 38.0 ms                                                         | 37.0 ms: 1.03x faster                                                 |
| chameleon                  | 6.14 ms                                                         | 5.98 ms: 1.03x faster                                                 |
| logging_simple             | 7.87 us                                                         | 7.68 us: 1.03x faster                                                 |
| pickle_list                | 3.40 us                                                         | 3.32 us: 1.02x faster                                                 |
| scimark_lu                 | 63.5 ms                                                         | 62.1 ms: 1.02x faster                                                 |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                  |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.02x faster                                                 |
| mdp                        | 1.67 sec                                                        | 1.64 sec: 1.02x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                |
| create_gc_cycles           | 713 us                                                          | 699 us: 1.02x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 25.7 us: 1.02x faster                                                 |
| tornado_http               | 104 ms                                                          | 102 ms: 1.02x faster                                                  |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| json_loads                 | 21.0 us                                                         | 20.6 us: 1.02x faster                                                 |
| xml_etree_process          | 45.0 ms                                                         | 44.3 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                  |
| sympy_str                  | 215 ms                                                          | 212 ms: 1.01x faster                                                  |
| pathlib                    | 89.4 ms                                                         | 88.3 ms: 1.01x faster                                                 |
| dulwich_log                | 49.7 ms                                                         | 49.0 ms: 1.01x faster                                                 |
| pidigits                   | 202 ms                                                          | 200 ms: 1.01x faster                                                  |
| crypto_pyaes               | 58.2 ms                                                         | 57.5 ms: 1.01x faster                                                 |
| richards                   | 33.8 ms                                                         | 33.5 ms: 1.01x faster                                                 |
| sympy_expand               | 375 ms                                                          | 371 ms: 1.01x faster                                                  |
| meteor_contest             | 77.0 ms                                                         | 76.3 ms: 1.01x faster                                                 |
| scimark_fft                | 206 ms                                                          | 205 ms: 1.01x faster                                                  |
| coroutines                 | 15.7 ms                                                         | 15.6 ms: 1.00x faster                                                 |
| flaskblogging              | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                                |
| typing_runtime_protocols   | 136 us                                                          | 137 us: 1.01x slower                                                  |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                 |
| json_dumps                 | 7.40 ms                                                         | 7.48 ms: 1.01x slower                                                 |
| regex_v8                   | 15.6 ms                                                         | 15.8 ms: 1.02x slower                                                 |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                  |
| python_startup             | 24.3 ms                                                         | 24.7 ms: 1.02x slower                                                 |
| spectral_norm              | 71.3 ms                                                         | 73.1 ms: 1.02x slower                                                 |
| python_startup_no_site     | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                                 |
| bench_mp_pool              | 74.3 ms                                                         | 76.8 ms: 1.03x slower                                                 |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (7): pylint, json, thrift, scimark_sparse_mat_mult, xml_etree_generate, gc_traversal, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown