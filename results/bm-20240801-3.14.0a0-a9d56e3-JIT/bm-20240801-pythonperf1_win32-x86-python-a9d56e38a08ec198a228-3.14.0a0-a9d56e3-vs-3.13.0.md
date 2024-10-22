# Results vs. 3.13.0

- fork: python
- ref: a9d56e38a08ec198a228
- machine: windows-x86
- commit hash: a9d56e3
- commit date: 2024-08-01
- overall geometric mean: 1.11x faster
- HPT reliability: 98.82%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 107 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 666 ms: 1.26x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| async_tree_io              | 537 ms                                                          | 544 ms: 1.01x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| async_generators           | 274 ms                                                          | 313 ms: 1.14x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 52.2 ms: 1.57x faster                                                          |
| float          | 57.8 ms                                                         | 42.8 ms: 1.35x faster                                                          |
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 94.5 ms: 1.09x faster                                                          |
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                         |
| pickle_pure_python   | 238 us                                                          | 209 us: 1.14x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 145 us: 1.11x faster                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 59.1 ms: 1.06x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.6 ms: 1.02x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.6 ms: 1.02x faster                                                          |
| python_startup         | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.38 ms: 1.36x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| genshi_xml     | 49.5 ms                                                         | 50.8 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240801-pythonperf1_win32-x86-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 769 us: 13.20x faster                                                          |
| coverage                   | 333 ms                                                          | 51.0 ms: 6.53x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 16.0 us: 1.64x faster                                                          |
| nbody                      | 81.9 ms                                                         | 52.2 ms: 1.57x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 47.3 ms: 1.51x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.38 ms: 1.36x faster                                                          |
| float                      | 57.8 ms                                                         | 42.8 ms: 1.35x faster                                                          |
| fannkuch                   | 293 ms                                                          | 224 ms: 1.31x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 45.9 ms: 1.27x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 666 ms: 1.26x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.31 ms: 1.26x faster                                                          |
| pyflate                    | 326 ms                                                          | 260 ms: 1.25x faster                                                           |
| scimark_fft                | 206 ms                                                          | 166 ms: 1.25x faster                                                           |
| deepcopy                   | 307 us                                                          | 251 us: 1.22x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 41.2 ms: 1.22x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.49 us: 1.15x faster                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.51 sec: 1.14x faster                                                         |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| pickle_pure_python         | 238 us                                                          | 209 us: 1.14x faster                                                           |
| telco                      | 6.67 ms                                                         | 5.88 ms: 1.13x faster                                                          |
| comprehensions             | 12.7 us                                                         | 11.3 us: 1.13x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 145 us: 1.11x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| pycparser                  | 869 ms                                                          | 794 ms: 1.09x faster                                                           |
| regex_compile              | 103 ms                                                          | 94.5 ms: 1.09x faster                                                          |
| meteor_contest             | 77.0 ms                                                         | 70.4 ms: 1.09x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| logging_silent             | 61.6 ns                                                         | 56.8 ns: 1.08x faster                                                          |
| pprint_safe_repr           | 644 ms                                                          | 597 ms: 1.08x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.22 sec: 1.06x faster                                                         |
| sqlglot_parse              | 1.05 ms                                                         | 988 us: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 59.1 ms: 1.06x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 976 us: 1.05x faster                                                           |
| richards                   | 33.8 ms                                                         | 32.7 ms: 1.03x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| nqueens                    | 75.1 ms                                                         | 73.1 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 63.6 ms: 1.02x faster                                                          |
| xml_etree_process          | 45.0 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.27 ms: 1.02x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| logging_simple             | 7.87 us                                                         | 7.72 us: 1.02x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 19.6 ms: 1.02x faster                                                          |
| logging_format             | 8.57 us                                                         | 8.44 us: 1.02x faster                                                          |
| richards_super             | 38.0 ms                                                         | 37.4 ms: 1.01x faster                                                          |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 88.6 ms: 1.01x faster                                                          |
| pidigits                   | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| dulwich_log                | 49.7 ms                                                         | 49.2 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.47 ms: 1.01x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 4.69 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 222 ms: 1.01x slower                                                           |
| async_tree_io              | 537 ms                                                          | 544 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 43.1 ms: 1.01x slower                                                          |
| 2to3                       | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| genshi_text                | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| sympy_str                  | 215 ms                                                          | 220 ms: 1.02x slower                                                           |
| chaos                      | 51.2 ms                                                         | 52.5 ms: 1.03x slower                                                          |
| tornado_http               | 104 ms                                                          | 107 ms: 1.03x slower                                                           |
| genshi_xml                 | 49.5 ms                                                         | 50.8 ms: 1.03x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 111 ms: 1.03x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.73 sec: 1.03x slower                                                         |
| generators                 | 22.1 ms                                                         | 22.9 ms: 1.04x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 77.3 ms: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                          | 392 ms: 1.04x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.94 sec: 1.07x slower                                                         |
| create_gc_cycles           | 713 us                                                          | 764 us: 1.07x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.4 ms: 1.08x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 99.7 ms: 1.09x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| raytrace                   | 205 ms                                                          | 229 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 153 us: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.71 ms: 1.13x slower                                                          |
| pylint                     | 225 ms                                                          | 253 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| async_generators           | 274 ms                                                          | 313 ms: 1.14x slower                                                           |
| scimark_lu                 | 63.5 ms                                                         | 73.9 ms: 1.16x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (5): async_tree_io_tg, go, regex_dna, django_template, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.82% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown