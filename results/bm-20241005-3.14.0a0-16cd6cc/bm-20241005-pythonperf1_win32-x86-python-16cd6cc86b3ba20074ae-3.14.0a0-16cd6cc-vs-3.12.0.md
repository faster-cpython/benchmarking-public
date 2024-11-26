# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-x86
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.9 ms: 1.35x faster                                                          |
| float          | 76.7 ms                                                         | 62.7 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 111 ms: 1.17x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 77.6 ms                                                         | 67.3 ms: 1.15x faster                                                          |
| tomli_loads          | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 188 us: 1.12x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 263 us: 1.09x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                          |
| pickle_list          | 3.37 us                                                         | 3.33 us: 1.01x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| pickle               | 7.79 us                                                         | 8.00 us: 1.03x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.5 us: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                          |
| unpickle_list        | 2.95 us                                                         | 3.07 us: 1.04x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                          |
| django_template | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.64x faster                                                          |
| deepcopy                   | 360 us                                                          | 250 us: 1.44x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.8 ms: 1.44x faster                                                          |
| unpack_sequence            | 62.5 ns                                                         | 44.0 ns: 1.42x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 253 ms: 1.39x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.9 us: 1.38x faster                                                          |
| logging_silent             | 101 ns                                                          | 73.7 ns: 1.37x faster                                                          |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                           |
| nbody                      | 127 ms                                                          | 93.9 ms: 1.35x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 70.5 ms: 1.32x faster                                                          |
| spectral_norm              | 104 ms                                                          | 78.6 ms: 1.32x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 521 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 540 ms: 1.28x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.81 ms: 1.27x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.36 ms: 1.27x faster                                                          |
| scimark_sor                | 130 ms                                                          | 104 ms: 1.25x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.25x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 75.5 ms: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 111 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.15 ms: 1.23x faster                                                          |
| float                      | 76.7 ms                                                         | 62.7 ms: 1.22x faster                                                          |
| raytrace                   | 308 ms                                                          | 252 ms: 1.22x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.31 ms: 1.20x faster                                                          |
| chaos                      | 69.4 ms                                                         | 58.0 ms: 1.20x faster                                                          |
| logging_simple             | 9.75 us                                                         | 8.23 us: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.0 ms: 1.17x faster                                                          |
| regex_compile              | 129 ms                                                          | 111 ms: 1.17x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.91 us: 1.17x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 468 ms: 1.17x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.3 ms: 1.15x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.91 sec: 1.15x faster                                                         |
| pyflate                    | 424 ms                                                          | 370 ms: 1.14x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.3 ms: 1.14x faster                                                          |
| scimark_fft                | 271 ms                                                          | 238 ms: 1.14x faster                                                           |
| pycparser                  | 978 ms                                                          | 863 ms: 1.13x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.10 ms: 1.13x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.5 ms: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.69 sec: 1.13x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.12x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.37 ms: 1.12x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 188 us: 1.12x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                                          |
| 2to3                       | 280 ms                                                          | 252 ms: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 263 us: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.09x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 668 ms: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 80.6 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.40 sec: 1.07x faster                                                         |
| django_template            | 36.9 ms                                                         | 34.7 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 45.8 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.2 ms: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 1.99 us: 1.04x faster                                                          |
| fannkuch                   | 354 ms                                                          | 340 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 384 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 70.2 ms: 1.03x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 51.8 ms: 1.03x faster                                                          |
| gc_traversal               | 1.44 ms                                                         | 1.41 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| pickle_list                | 3.37 us                                                         | 3.33 us: 1.01x faster                                                          |
| async_generators           | 313 ms                                                          | 310 ms: 1.01x faster                                                           |
| richards_super             | 46.5 ms                                                         | 46.8 ms: 1.01x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 77.0 ms: 1.02x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.00 us: 1.03x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.5 us: 1.03x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.61 ms: 1.03x slower                                                          |
| json                       | 4.15 ms                                                         | 4.29 ms: 1.03x slower                                                          |
| unpickle_list              | 2.95 us                                                         | 3.07 us: 1.04x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 696 ms: 1.05x slower                                                           |
| coverage                   | 48.4 ms                                                         | 51.0 ms: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.5 ms: 1.08x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.09x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 723 us: 1.11x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.82 ms: 1.24x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 238 ms: 2.37x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): richards, tornado_http
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1_win32-x86-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.115x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown