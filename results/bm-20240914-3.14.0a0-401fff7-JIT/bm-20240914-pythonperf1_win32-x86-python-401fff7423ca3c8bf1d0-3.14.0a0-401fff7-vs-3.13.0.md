# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: windows-x86
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.10x faster
- HPT reliability: 99.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 257 ms: 1.01x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                                          |
| tornado_http   | 104 ms                                                          | 99.7 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 612 ms: 1.37x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 258 ms: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 485 ms: 1.02x faster                                                           |
| async_tree_io              | 537 ms                                                          | 547 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 476 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 524 ms: 1.03x slower                                                           |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 50.6 ms: 1.62x faster                                                          |
| float          | 57.8 ms                                                         | 43.8 ms: 1.32x faster                                                          |
| pidigits       | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 62.6 ms                                                         | 52.7 ms: 1.19x faster                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.50 sec: 1.15x faster                                                         |
| xml_etree_process    | 45.0 ms                                                         | 39.5 ms: 1.14x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| pickle               | 8.42 us                                                         | 7.94 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 61.7 ms: 1.05x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.05x faster                                                           |
| unpickle_list        | 3.09 us                                                         | 2.97 us: 1.04x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.29 us: 1.03x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 164 us: 1.01x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 247 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.5 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.47 ms: 1.34x faster                                                          |
| django_template | 32.7 ms                                                         | 35.1 ms: 1.07x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 56.0 ms: 1.13x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf1_win32-x86-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 768 us: 13.21x faster                                                          |
| coverage                   | 333 ms                                                          | 53.8 ms: 6.18x faster                                                          |
| sqlglot_normalize          | 220 ms                                                          | 100.0 ms: 2.20x faster                                                         |
| deepcopy_memo              | 26.2 us                                                         | 15.2 us: 1.72x faster                                                          |
| nbody                      | 81.9 ms                                                         | 50.6 ms: 1.62x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 46.0 ms: 1.55x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 612 ms: 1.37x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 68.7 ms: 1.34x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.47 ms: 1.34x faster                                                          |
| float                      | 57.8 ms                                                         | 43.8 ms: 1.32x faster                                                          |
| deepcopy                   | 307 us                                                          | 233 us: 1.32x faster                                                           |
| fannkuch                   | 293 ms                                                          | 238 ms: 1.23x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 47.5 ms: 1.22x faster                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.39 ms: 1.22x faster                                                          |
| scimark_fft                | 206 ms                                                          | 174 ms: 1.19x faster                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 52.7 ms: 1.19x faster                                                          |
| pyflate                    | 326 ms                                                          | 274 ms: 1.19x faster                                                           |
| deltablue                  | 2.41 ms                                                         | 2.09 ms: 1.15x faster                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.50 sec: 1.15x faster                                                         |
| xml_etree_process          | 45.0 ms                                                         | 39.5 ms: 1.14x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.52 us: 1.13x faster                                                          |
| comprehensions             | 12.7 us                                                         | 11.3 us: 1.13x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 258 ms: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.71 ms: 1.10x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 19.9 us: 1.09x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 82.2 ms: 1.09x faster                                                          |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.08x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.20 ms: 1.07x faster                                                          |
| pprint_safe_repr           | 644 ms                                                          | 600 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                           |
| json                       | 4.27 ms                                                         | 4.01 ms: 1.07x faster                                                          |
| scimark_lu                 | 63.5 ms                                                         | 59.9 ms: 1.06x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.94 us: 1.06x faster                                                          |
| meteor_contest             | 77.0 ms                                                         | 72.7 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 61.7 ms: 1.05x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.05x faster                                                           |
| tornado_http               | 104 ms                                                          | 99.7 ms: 1.04x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 2.97 us: 1.04x faster                                                          |
| richards_super             | 38.0 ms                                                         | 36.4 ms: 1.04x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 984 us: 1.04x faster                                                           |
| pycparser                  | 869 ms                                                          | 839 ms: 1.04x faster                                                           |
| unpack_sequence            | 42.9 ns                                                         | 41.5 ns: 1.04x faster                                                          |
| pidigits                   | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| pickle_list                | 3.40 us                                                         | 3.29 us: 1.03x faster                                                          |
| dulwich_log                | 49.7 ms                                                         | 48.3 ms: 1.03x faster                                                          |
| richards                   | 33.8 ms                                                         | 33.0 ms: 1.02x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 47.2 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| python_startup             | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| logging_silent             | 61.6 ns                                                         | 60.3 ns: 1.02x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 19.5 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.27 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 485 ms: 1.02x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.42 ms: 1.02x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.94 us: 1.01x faster                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 49.9 ms: 1.01x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.93 us: 1.01x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 75.0 ms: 1.01x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 164 us: 1.01x slower                                                           |
| 2to3                       | 253 ms                                                          | 257 ms: 1.01x slower                                                           |
| async_tree_io              | 537 ms                                                          | 547 ms: 1.02x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 476 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 524 ms: 1.03x slower                                                           |
| sympy_str                  | 215 ms                                                          | 222 ms: 1.03x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 247 us: 1.04x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 78.7 ms: 1.05x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.36 ms: 1.05x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 750 us: 1.05x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.05x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 4.91 ms: 1.06x slower                                                          |
| chaos                      | 51.2 ms                                                         | 54.6 ms: 1.07x slower                                                          |
| sympy_expand               | 375 ms                                                          | 402 ms: 1.07x slower                                                           |
| django_template            | 32.7 ms                                                         | 35.1 ms: 1.07x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                          |
| generators                 | 22.1 ms                                                         | 24.0 ms: 1.08x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 46.4 ms: 1.09x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.83 sec: 1.09x slower                                                         |
| docutils                   | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 151 us: 1.10x slower                                                           |
| genshi_xml                 | 49.5 ms                                                         | 56.0 ms: 1.13x slower                                                          |
| genshi_text                | 22.4 ms                                                         | 25.8 ms: 1.15x slower                                                          |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| pylint                     | 225 ms                                                          | 265 ms: 1.18x slower                                                           |
| raytrace                   | 205 ms                                                          | 248 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (4): regex_compile, regex_dna, logging_format, sqlglot_parse
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.44% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown