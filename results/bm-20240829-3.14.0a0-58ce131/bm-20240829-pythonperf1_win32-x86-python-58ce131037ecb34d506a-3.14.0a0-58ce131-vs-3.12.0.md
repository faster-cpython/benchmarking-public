# Results vs. 3.12.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.06x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 96.4 ms: 1.32x faster                                                          |
| float          | 76.7 ms                                                         | 62.3 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 174 us: 1.20x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                          |
| tomli_loads          | 2.20 sec                                                        | 1.92 sec: 1.14x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 262 us: 1.09x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 68.1 ms: 1.06x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.6 ms: 1.05x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.35 ms: 1.19x faster                                                          |
| django_template | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.8 us: 1.76x faster                                                          |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.1 ms: 1.42x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                          |
| spectral_norm              | 104 ms                                                          | 76.7 ms: 1.35x faster                                                          |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.68 ms: 1.34x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| logging_silent             | 101 ns                                                          | 76.0 ns: 1.33x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                           |
| nbody                      | 127 ms                                                          | 96.4 ms: 1.32x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.20 ms: 1.31x faster                                                          |
| raytrace                   | 308 ms                                                          | 236 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.5 ms: 1.31x faster                                                          |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 71.7 ms: 1.30x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.28x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.9 ms: 1.26x faster                                                          |
| float                      | 76.7 ms                                                         | 62.3 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.97 us: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 77.3 ms: 1.21x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 174 us: 1.20x faster                                                           |
| regex_compile              | 129 ms                                                          | 108 ms: 1.20x faster                                                           |
| pyflate                    | 424 ms                                                          | 354 ms: 1.20x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.73 us: 1.19x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.35 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 459 ms: 1.19x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.9 ms: 1.19x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 58.3 ms: 1.19x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| scimark_fft                | 271 ms                                                          | 234 ms: 1.16x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.6 ms: 1.15x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.14x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.92 sec: 1.14x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.8 ms: 1.13x faster                                                          |
| pycparser                  | 978 ms                                                          | 868 ms: 1.13x faster                                                           |
| sympy_str                  | 240 ms                                                          | 214 ms: 1.12x faster                                                           |
| 2to3                       | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                         |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 650 ms: 1.11x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.8 ms: 1.11x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 262 us: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.54 ms: 1.09x faster                                                          |
| fannkuch                   | 354 ms                                                          | 327 ms: 1.08x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 81.3 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.06x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 68.1 ms: 1.06x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 50.6 ms: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 87.1 ms: 1.05x faster                                                          |
| richards_super             | 46.5 ms                                                         | 44.4 ms: 1.05x faster                                                          |
| richards                   | 41.3 ms                                                         | 39.6 ms: 1.04x faster                                                          |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| async_generators           | 313 ms                                                          | 304 ms: 1.03x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 73.4 ms: 1.03x faster                                                          |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.00x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.60 ms: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.29 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.2 ms: 1.06x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 756 ms: 1.14x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 747 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 148 us: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.97 ms: 1.26x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 225 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown