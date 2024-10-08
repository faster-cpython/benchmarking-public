# Results vs. 3.12.0

- fork: python
- ref: 58ce131037ecb34d506a
- machine: windows-x86
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                         |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.27x faster                                                           |
| async_tree_io              | 693 ms                                                          | 556 ms: 1.25x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 97.8 ms: 1.30x faster                                                          |
| float          | 76.7 ms                                                         | 62.1 ms: 1.24x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.18x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 180 us: 1.17x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 258 us: 1.11x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.52 ms: 1.02x slower                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.45 ms: 1.18x faster                                                          |
| django_template | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.14x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.2 us: 1.73x faster                                                          |
| deepcopy                   | 360 us                                                          | 249 us: 1.45x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.5 ms: 1.40x faster                                                          |
| comprehensions             | 19.2 us                                                         | 14.0 us: 1.37x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 257 ms: 1.37x faster                                                           |
| spectral_norm              | 104 ms                                                          | 76.2 ms: 1.36x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 204 ms: 1.36x faster                                                           |
| logging_silent             | 101 ns                                                          | 74.6 ns: 1.36x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 69.6 ms: 1.34x faster                                                          |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.32x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.74 ms: 1.31x faster                                                          |
| go                         | 137 ms                                                          | 105 ms: 1.31x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.48 us: 1.30x faster                                                          |
| nbody                      | 127 ms                                                          | 97.8 ms: 1.30x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.27 ms: 1.29x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 284 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 531 ms: 1.27x faster                                                           |
| raytrace                   | 308 ms                                                          | 245 ms: 1.26x faster                                                           |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.5 ms: 1.25x faster                                                          |
| async_tree_io              | 693 ms                                                          | 556 ms: 1.25x faster                                                           |
| float                      | 76.7 ms                                                         | 62.1 ms: 1.24x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 78.0 ms: 1.20x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.15 us: 1.20x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.23 ms: 1.20x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.0 ms: 1.19x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.45 ms: 1.18x faster                                                          |
| regex_compile              | 129 ms                                                          | 110 ms: 1.18x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.7 ms: 1.18x faster                                                          |
| pyflate                    | 424 ms                                                          | 360 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.9 ms: 1.17x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 180 us: 1.17x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.94 us: 1.16x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 471 ms: 1.16x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| dulwich_log                | 58.5 ms                                                         | 50.9 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.1 ms: 1.14x faster                                                          |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.13x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.12x faster                                                           |
| 2to3                       | 280 ms                                                          | 250 ms: 1.12x faster                                                           |
| pycparser                  | 978 ms                                                          | 873 ms: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.12 ms: 1.11x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.38 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.35 sec: 1.11x faster                                                         |
| mdp                        | 1.91 sec                                                        | 1.73 sec: 1.11x faster                                                         |
| pickle_pure_python         | 286 us                                                          | 258 us: 1.11x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.2 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 658 ms: 1.09x faster                                                           |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| async_generators           | 313 ms                                                          | 294 ms: 1.07x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.8 ms: 1.06x faster                                                          |
| fannkuch                   | 354 ms                                                          | 334 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.7 ms: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.89 sec: 1.05x faster                                                         |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.4 ms: 1.05x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| sympy_expand               | 398 ms                                                          | 386 ms: 1.03x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 73.1 ms: 1.03x faster                                                          |
| richards_super             | 46.5 ms                                                         | 45.7 ms: 1.02x faster                                                          |
| richards                   | 41.3 ms                                                         | 40.8 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.52 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                          |
| json                       | 4.15 ms                                                         | 4.36 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.1 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.8 ms: 1.09x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 736 ms: 1.11x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 747 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 158 us: 1.25x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.99 ms: 1.27x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                   |

Benchmark hidden because not significant (2): gc_traversal, tornado_http
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-pythonperf1_win32-x86-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown