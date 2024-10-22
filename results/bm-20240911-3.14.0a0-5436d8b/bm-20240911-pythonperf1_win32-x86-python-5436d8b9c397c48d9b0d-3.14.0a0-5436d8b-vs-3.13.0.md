# Results vs. 3.13.0

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-x86
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.03x faster
- HPT reliability: 98.97%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 44.1 ms: 1.10x faster                                                          |
| tornado_http   | 104 ms                                                          | 94.8 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 666 ms: 1.26x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.07x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 457 ms: 1.01x faster                                                           |
| async_generators           | 274 ms                                                          | 305 ms: 1.12x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.7 ms: 1.19x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 62.2 ms: 1.08x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.9 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_compile  | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.42 us                                                         | 7.99 us: 1.05x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.9 ms: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| pickle_list          | 3.40 us                                                         | 3.65 us: 1.07x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 68.2 ms: 1.09x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 262 us: 1.10x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 49.8 ms: 1.11x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 181 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 49.5 ms                                                         | 46.9 ms: 1.06x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| mako           | 7.31 ms                                                         | 8.18 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 737 us: 13.77x faster                                                          |
| coverage                   | 333 ms                                                          | 54.7 ms: 6.08x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 666 ms: 1.26x faster                                                           |
| deepcopy                   | 307 us                                                          | 246 us: 1.25x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 22.3 us: 1.18x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.54 us: 1.12x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.11x faster                                                           |
| tornado_http               | 104 ms                                                          | 94.8 ms: 1.10x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 44.1 ms: 1.10x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 81.8 ms: 1.09x faster                                                          |
| go                         | 111 ms                                                          | 104 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.07x faster                                                           |
| bench_mp_pool              | 74.3 ms                                                         | 69.9 ms: 1.06x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 46.9 ms: 1.06x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.99 us: 1.05x faster                                                          |
| telco                      | 6.67 ms                                                         | 6.37 ms: 1.05x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.39 ms: 1.04x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| json_loads                 | 21.0 us                                                         | 20.6 us: 1.02x faster                                                          |
| 2to3                       | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 457 ms: 1.01x faster                                                           |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| pycparser                  | 869 ms                                                          | 864 ms: 1.01x faster                                                           |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.01x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.01x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.02x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 43.2 ms: 1.02x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.04 us: 1.02x slower                                                          |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                           |
| dulwich_log                | 49.7 ms                                                         | 50.8 ms: 1.02x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| pprint_safe_repr           | 644 ms                                                          | 659 ms: 1.02x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.77 us: 1.02x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 731 us: 1.03x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 226 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 66.9 ms: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.62 ms: 1.03x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.08 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                          | 388 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.04x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.35 sec: 1.04x slower                                                         |
| regex_compile              | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| chaos                      | 51.2 ms                                                         | 53.7 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.08 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 145 us: 1.06x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 81.9 ms: 1.06x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 76.1 ms: 1.07x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 68.1 ms: 1.07x slower                                                          |
| pickle_list                | 3.40 us                                                         | 3.65 us: 1.07x slower                                                          |
| float                      | 57.8 ms                                                         | 62.2 ms: 1.08x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_generate         | 62.6 ms                                                         | 68.2 ms: 1.09x slower                                                          |
| comprehensions             | 12.7 us                                                         | 14.0 us: 1.10x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 262 us: 1.10x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 49.8 ms: 1.11x slower                                                          |
| pyflate                    | 326 ms                                                          | 360 ms: 1.11x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.15 ms: 1.11x slower                                                          |
| async_generators           | 274 ms                                                          | 305 ms: 1.12x slower                                                           |
| mako                       | 7.31 ms                                                         | 8.18 ms: 1.12x slower                                                          |
| nbody                      | 81.9 ms                                                         | 91.9 ms: 1.12x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 181 us: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.72 ms: 1.13x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 104 ms: 1.13x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 57.5 ms: 1.14x slower                                                          |
| scimark_fft                | 206 ms                                                          | 236 ms: 1.14x slower                                                           |
| raytrace                   | 205 ms                                                          | 235 ms: 1.15x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 49.3 ns: 1.15x slower                                                          |
| fannkuch                   | 293 ms                                                          | 338 ms: 1.15x slower                                                           |
| richards                   | 33.8 ms                                                         | 39.8 ms: 1.18x slower                                                          |
| generators                 | 22.1 ms                                                         | 26.2 ms: 1.18x slower                                                          |
| richards_super             | 38.0 ms                                                         | 45.0 ms: 1.19x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.7 ms: 1.19x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 75.0 ns: 1.22x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (13): async_tree_io, python_startup_no_site, sympy_sum, json, xml_etree_parse, nqueens, django_template, crypto_pyaes, bench_thread_pool, async_tree_io_tg, unpickle_list, sqlite_synth, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 98.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown