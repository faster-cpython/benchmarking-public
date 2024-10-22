# Results vs. 3.13.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.71%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 106 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| async_tree_none            | 246 ms                                                          | 213 ms: 1.15x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 756 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.07x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                           |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.7 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 62.3 ms: 1.08x slower                                                          |
| nbody          | 81.9 ms                                                         | 96.4 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| regex_compile  | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| regex_dna      | 117 ms                                                          | 124 ms: 1.06x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.6 ms: 1.04x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 174 us: 1.08x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 262 us: 1.10x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 50.6 ms: 1.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 49.5 ms                                                         | 47.2 ms: 1.05x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| mako           | 7.31 ms                                                         | 8.35 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 742 us: 13.68x faster                                                          |
| coverage                   | 333 ms                                                          | 51.2 ms: 6.50x faster                                                          |
| deepcopy                   | 307 us                                                          | 247 us: 1.24x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.8 us: 1.20x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| async_tree_none            | 246 ms                                                          | 213 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.51 us: 1.13x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 756 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| go                         | 111 ms                                                          | 102 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.07x faster                                                           |
| genshi_xml                 | 49.5 ms                                                         | 47.2 ms: 1.05x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 87.1 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                         |
| bench_mp_pool              | 74.3 ms                                                         | 73.4 ms: 1.01x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| 2to3                       | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 459 ms: 1.01x faster                                                           |
| genshi_text                | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                                          |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| dulwich_log                | 49.7 ms                                                         | 49.9 ms: 1.01x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 650 ms: 1.01x slower                                                           |
| logging_simple             | 7.87 us                                                         | 7.97 us: 1.01x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| tornado_http               | 104 ms                                                          | 106 ms: 1.01x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.73 us: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                          | 383 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 225 ms: 1.02x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.03x slower                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 77.3 ms: 1.03x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                         |
| sqlglot_optimize           | 42.5 ms                                                         | 43.8 ms: 1.03x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.34 sec: 1.04x slower                                                         |
| pylint                     | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.6 ms: 1.04x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.09 ms: 1.04x slower                                                          |
| regex_compile              | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| telco                      | 6.67 ms                                                         | 6.97 ms: 1.05x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 747 us: 1.05x slower                                                           |
| meteor_contest             | 77.0 ms                                                         | 81.3 ms: 1.05x slower                                                          |
| regex_dna                  | 117 ms                                                          | 124 ms: 1.06x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| chaos                      | 51.2 ms                                                         | 54.9 ms: 1.07x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 76.7 ms: 1.08x slower                                                          |
| float                      | 57.8 ms                                                         | 62.3 ms: 1.08x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 174 us: 1.08x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 99.5 ms: 1.08x slower                                                          |
| pyflate                    | 326 ms                                                          | 354 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 148 us: 1.09x slower                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                          |
| comprehensions             | 12.7 us                                                         | 14.0 us: 1.10x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 262 us: 1.10x slower                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.9 ms: 1.11x slower                                                          |
| async_generators           | 274 ms                                                          | 304 ms: 1.11x slower                                                           |
| fannkuch                   | 293 ms                                                          | 327 ms: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.68 ms: 1.12x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.20 ms: 1.12x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 50.6 ms: 1.12x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 17.7 ms: 1.13x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 71.7 ms: 1.13x slower                                                          |
| scimark_fft                | 206 ms                                                          | 234 ms: 1.13x slower                                                           |
| mako                       | 7.31 ms                                                         | 8.35 ms: 1.14x slower                                                          |
| raytrace                   | 205 ms                                                          | 236 ms: 1.15x slower                                                           |
| richards_super             | 38.0 ms                                                         | 44.4 ms: 1.17x slower                                                          |
| richards                   | 33.8 ms                                                         | 39.6 ms: 1.17x slower                                                          |
| nbody                      | 81.9 ms                                                         | 96.4 ms: 1.18x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.54 ms: 1.22x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.1 ms: 1.22x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 76.0 ns: 1.23x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (11): bench_thread_pool, async_tree_io, sympy_sum, sympy_str, python_startup_no_site, pycparser, gc_traversal, django_template, crypto_pyaes, json, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.71% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown