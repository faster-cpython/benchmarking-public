# Results vs. 3.12.0

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: windows-x86
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 263 ms: 1.07x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| tornado_http   | 105 ms                                                          | 98.3 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 292 ms: 1.25x faster                                                           |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                           |
| async_tree_io              | 693 ms                                                          | 577 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 102 ms: 1.24x faster                                                           |
| float          | 76.7 ms                                                         | 67.9 ms: 1.13x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 116 ms: 1.11x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.97 sec: 1.12x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 70.0 ms: 1.11x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 193 us: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 72.5 ms: 1.00x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.91 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.86 ms: 1.12x faster                                                          |
| django_template | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.08x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 25.5 us: 1.50x faster                                                          |
| deepcopy                   | 360 us                                                          | 264 us: 1.36x faster                                                           |
| generators                 | 38.5 ms                                                         | 28.6 ms: 1.35x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                           |
| spectral_norm              | 104 ms                                                          | 79.8 ms: 1.30x faster                                                          |
| raytrace                   | 308 ms                                                          | 242 ms: 1.27x faster                                                           |
| logging_silent             | 101 ns                                                          | 79.9 ns: 1.26x faster                                                          |
| comprehensions             | 19.2 us                                                         | 15.2 us: 1.26x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 292 ms: 1.25x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 75.0 ms: 1.24x faster                                                          |
| nbody                      | 127 ms                                                          | 102 ms: 1.24x faster                                                           |
| async_tree_none            | 298 ms                                                          | 240 ms: 1.24x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.90 ms: 1.23x faster                                                          |
| scimark_sor                | 130 ms                                                          | 106 ms: 1.23x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.56 ms: 1.23x faster                                                          |
| async_tree_io              | 693 ms                                                          | 577 ms: 1.20x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 78.4 ms: 1.19x faster                                                          |
| chaos                      | 69.4 ms                                                         | 58.2 ms: 1.19x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.73 us: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 470 ms: 1.16x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 18.1 ms: 1.15x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.56 us: 1.14x faster                                                          |
| pyflate                    | 424 ms                                                          | 374 ms: 1.13x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                         |
| float                      | 76.7 ms                                                         | 67.9 ms: 1.13x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.86 ms: 1.12x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.97 sec: 1.12x faster                                                         |
| logging_format             | 10.4 us                                                         | 9.35 us: 1.11x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 70.0 ms: 1.11x faster                                                          |
| regex_compile              | 129 ms                                                          | 116 ms: 1.11x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.51 ms: 1.10x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 193 us: 1.08x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 84.3 ms: 1.08x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 16.3 ms: 1.08x faster                                                          |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| go                         | 137 ms                                                          | 128 ms: 1.08x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 64.5 ms: 1.07x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 115 ms: 1.07x faster                                                           |
| pycparser                  | 978 ms                                                          | 913 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 62.1 ms: 1.07x faster                                                          |
| tornado_http               | 105 ms                                                          | 98.3 ms: 1.07x faster                                                          |
| 2to3                       | 280 ms                                                          | 263 ms: 1.07x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 106 ms: 1.07x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 71.3 ms: 1.06x faster                                                          |
| scimark_fft                | 271 ms                                                          | 256 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.6 ms: 1.05x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                         |
| sqlglot_transpile          | 1.53 ms                                                         | 1.46 ms: 1.05x faster                                                          |
| django_template            | 36.9 ms                                                         | 35.4 ms: 1.04x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.45 sec: 1.04x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.20 ms: 1.04x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 46.9 ms: 1.03x faster                                                          |
| richards_super             | 46.5 ms                                                         | 44.9 ms: 1.03x faster                                                          |
| sympy_str                  | 240 ms                                                          | 232 ms: 1.03x faster                                                           |
| fannkuch                   | 354 ms                                                          | 349 ms: 1.01x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 52.5 ms: 1.01x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 711 ms: 1.01x faster                                                           |
| async_generators           | 313 ms                                                          | 310 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 72.5 ms: 1.00x slower                                                          |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.03x slower                                                          |
| sympy_expand               | 398 ms                                                          | 410 ms: 1.03x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.1 ms: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.42 ms: 1.06x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.91 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 741 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.69 ms: 1.21x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 165 us: 1.30x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 245 ms: 2.44x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (5): richards, python_startup_no_site, pickle_pure_python, gc_traversal, asyncio_tcp
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8/bm-20240629-pythonperf1_win32-x86-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown