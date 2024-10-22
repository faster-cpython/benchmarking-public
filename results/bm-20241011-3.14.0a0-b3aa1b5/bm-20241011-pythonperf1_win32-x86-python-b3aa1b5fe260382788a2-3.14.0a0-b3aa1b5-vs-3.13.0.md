# Results vs. 3.13.0

- fork: python
- ref: b3aa1b5fe260382788a2
- machine: windows-x86
- commit hash: b3aa1b5
- commit date: 2024-10-11
- overall geometric mean: 1.03x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 248 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.88 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 246 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 738 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 519 ms: 1.02x slower                                                           |
| async_generators           | 274 ms                                                          | 301 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 199 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 60.9 ms: 1.05x slower                                                          |
| nbody          | 81.9 ms                                                         | 86.7 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.84 ms: 1.02x slower                                                          |
| regex_compile  | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_list        | 3.09 us                                                         | 2.89 us: 1.07x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.1 us: 1.04x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.42 us: 1.01x slower                                                          |
| pickle               | 8.42 us                                                         | 8.55 us: 1.02x slower                                                          |
| xml_etree_parse      | 109 ms                                                          | 113 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.7 ms: 1.06x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 48.3 ms: 1.07x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 67.7 ms: 1.08x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 265 us: 1.11x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 19.9 ms                                                         | 20.7 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.5 ms: 1.04x faster                                                          |
| mako            | 7.31 ms                                                         | 7.76 ms: 1.06x slower                                                          |
| django_template | 32.7 ms                                                         | 34.8 ms: 1.06x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241011-pythonperf1_win32-x86-python-b3aa1b5fe260382788a2-3.14.0a0-b3aa1b5 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 738 us: 13.75x faster                                                          |
| coverage                   | 333 ms                                                          | 52.7 ms: 6.32x faster                                                          |
| deepcopy                   | 307 us                                                          | 245 us: 1.25x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.3 us: 1.23x faster                                                          |
| async_tree_none            | 246 ms                                                          | 213 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.49 us: 1.14x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 738 ms: 1.14x faster                                                           |
| go                         | 111 ms                                                          | 99.3 ms: 1.12x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| unpickle_list              | 3.09 us                                                         | 2.89 us: 1.07x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 47.0 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 471 ms: 1.05x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.1 us: 1.04x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 21.5 ms: 1.04x faster                                                          |
| pycparser                  | 869 ms                                                          | 836 ms: 1.04x faster                                                           |
| 2to3                       | 253 ms                                                          | 248 ms: 1.02x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 47.3 ms: 1.02x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 88.1 ms: 1.02x faster                                                          |
| pidigits                   | 202 ms                                                          | 199 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                           |
| regex_v8                   | 15.6 ms                                                         | 15.7 ms: 1.01x slower                                                          |
| pickle_list                | 3.40 us                                                         | 3.42 us: 1.01x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.30 ms: 1.01x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 43.4 ns: 1.01x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.84 ms: 1.02x slower                                                          |
| pickle                     | 8.42 us                                                         | 8.55 us: 1.02x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.32 sec: 1.02x slower                                                         |
| typing_runtime_protocols   | 136 us                                                          | 139 us: 1.02x slower                                                           |
| sympy_str                  | 215 ms                                                          | 219 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 519 ms: 1.02x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.71 sec: 1.02x slower                                                         |
| python_startup             | 24.3 ms                                                         | 24.9 ms: 1.03x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.6 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                          | 386 ms: 1.03x slower                                                           |
| comprehensions             | 12.7 us                                                         | 13.1 us: 1.03x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.88 sec: 1.03x slower                                                         |
| xml_etree_parse            | 109 ms                                                          | 113 ms: 1.03x slower                                                           |
| regex_compile              | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 44.0 ms: 1.04x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 74.0 ms: 1.04x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 80.0 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 20.7 ms: 1.04x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 51.7 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 229 ms: 1.04x slower                                                           |
| telco                      | 6.67 ms                                                         | 6.98 ms: 1.05x slower                                                          |
| fannkuch                   | 293 ms                                                          | 308 ms: 1.05x slower                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 61.1 ms: 1.05x slower                                                          |
| float                      | 57.8 ms                                                         | 60.9 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 68.7 ms: 1.06x slower                                                          |
| nbody                      | 81.9 ms                                                         | 86.7 ms: 1.06x slower                                                          |
| mako                       | 7.31 ms                                                         | 7.76 ms: 1.06x slower                                                          |
| generators                 | 22.1 ms                                                         | 23.5 ms: 1.06x slower                                                          |
| django_template            | 32.7 ms                                                         | 34.8 ms: 1.06x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.09 ms: 1.06x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 4.96 ms: 1.07x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 48.3 ms: 1.07x slower                                                          |
| chaos                      | 51.2 ms                                                         | 55.0 ms: 1.07x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 68.5 ms: 1.08x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.87 sec: 1.08x slower                                                         |
| scimark_sor                | 91.8 ms                                                         | 99.4 ms: 1.08x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 67.7 ms: 1.08x slower                                                          |
| pyflate                    | 326 ms                                                          | 356 ms: 1.09x slower                                                           |
| logging_silent             | 61.6 ns                                                         | 67.4 ns: 1.09x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 783 us: 1.10x slower                                                           |
| async_generators           | 274 ms                                                          | 301 ms: 1.10x slower                                                           |
| scimark_fft                | 206 ms                                                          | 229 ms: 1.11x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.9 ms: 1.11x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 265 us: 1.11x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.70 ms: 1.12x slower                                                          |
| raytrace                   | 205 ms                                                          | 243 ms: 1.18x slower                                                           |
| richards_super             | 38.0 ms                                                         | 45.3 ms: 1.19x slower                                                          |
| richards                   | 33.8 ms                                                         | 40.5 ms: 1.20x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 9.01 ms: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (18): bench_thread_pool, async_tree_io, nqueens, tornado_http, bench_mp_pool, logging_simple, gc_traversal, pickle_dict, json, logging_format, json_loads, asyncio_tcp_ssl, sqlite_synth, pprint_safe_repr, regex_dna, sympy_sum, sqlglot_parse, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown