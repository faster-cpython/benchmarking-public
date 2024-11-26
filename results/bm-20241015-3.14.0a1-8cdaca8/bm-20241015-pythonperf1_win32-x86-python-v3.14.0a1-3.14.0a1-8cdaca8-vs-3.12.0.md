# Results vs. 3.12.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                                |
| docutils       | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                              |
| tornado_http   | 105 ms                                                          | 104 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 558 ms: 1.21x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.18x faster                                                |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 87.2 ms: 1.46x faster                                               |
| float          | 76.7 ms                                                         | 61.9 ms: 1.24x faster                                               |
| Geometric mean | (ref)                                                           | 1.22x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 105 ms: 1.23x faster                                                |
| regex_effbot   | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                               |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 178 us: 1.18x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                              |
| xml_etree_process    | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.5 ms: 1.12x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 66.5 ms: 1.08x faster                                               |
| pickle_pure_python   | 286 us                                                          | 265 us: 1.08x faster                                                |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                               |
| unpickle_list        | 2.95 us                                                         | 2.98 us: 1.01x slower                                               |
| pickle_list          | 3.37 us                                                         | 3.49 us: 1.04x slower                                               |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                               |
| pickle_dict          | 19.9 us                                                         | 21.6 us: 1.08x slower                                               |
| pickle               | 7.79 us                                                         | 8.56 us: 1.10x slower                                               |
| json_dumps           | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                               |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                               |
| python_startup         | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.83 ms: 1.27x faster                                               |
| django_template | 36.9 ms                                                         | 32.5 ms: 1.14x faster                                               |
| Geometric mean  | (ref)                                                           | 1.20x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.3 us: 1.72x faster                                               |
| generators                 | 38.5 ms                                                         | 24.1 ms: 1.60x faster                                               |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                |
| nbody                      | 127 ms                                                          | 87.2 ms: 1.46x faster                                               |
| logging_silent             | 101 ns                                                          | 69.5 ns: 1.45x faster                                               |
| comprehensions             | 19.2 us                                                         | 13.4 us: 1.43x faster                                               |
| go                         | 137 ms                                                          | 99.5 ms: 1.38x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 67.6 ms: 1.38x faster                                               |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 205 ms: 1.35x faster                                                |
| hexiom                     | 6.82 ms                                                         | 5.05 ms: 1.35x faster                                               |
| spectral_norm              | 104 ms                                                          | 77.3 ms: 1.34x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.68 ms: 1.34x faster                                               |
| async_tree_none            | 298 ms                                                          | 223 ms: 1.34x faster                                                |
| raytrace                   | 308 ms                                                          | 236 ms: 1.30x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 280 ms: 1.30x faster                                                |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                |
| mako                       | 9.96 ms                                                         | 7.83 ms: 1.27x faster                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.55 us: 1.26x faster                                               |
| nqueens                    | 93.7 ms                                                         | 74.5 ms: 1.26x faster                                               |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                |
| unpack_sequence            | 62.5 ns                                                         | 49.8 ns: 1.25x faster                                               |
| chaos                      | 69.4 ms                                                         | 55.4 ms: 1.25x faster                                               |
| float                      | 76.7 ms                                                         | 61.9 ms: 1.24x faster                                               |
| regex_compile              | 129 ms                                                          | 105 ms: 1.23x faster                                                |
| logging_simple             | 9.75 us                                                         | 7.95 us: 1.23x faster                                               |
| coroutines                 | 20.9 ms                                                         | 17.1 ms: 1.22x faster                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.17 ms: 1.22x faster                                               |
| async_tree_io_tg           | 677 ms                                                          | 558 ms: 1.21x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 467 ms: 1.21x faster                                                |
| logging_format             | 10.4 us                                                         | 8.70 us: 1.20x faster                                               |
| pycparser                  | 978 ms                                                          | 825 ms: 1.18x faster                                                |
| unpickle_pure_python       | 210 us                                                          | 178 us: 1.18x faster                                                |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.18x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.87 sec: 1.18x faster                                              |
| sqlglot_parse              | 1.25 ms                                                         | 1.06 ms: 1.17x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 60.0 ms: 1.15x faster                                               |
| pyflate                    | 424 ms                                                          | 368 ms: 1.15x faster                                                |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                |
| scimark_monte_carlo        | 66.4 ms                                                         | 58.2 ms: 1.14x faster                                               |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                                |
| django_template            | 36.9 ms                                                         | 32.5 ms: 1.14x faster                                               |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                               |
| xml_etree_process          | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.82 ms: 1.12x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.5 ms: 1.12x faster                                               |
| dulwich_log                | 58.5 ms                                                         | 52.5 ms: 1.11x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                              |
| sqlglot_optimize           | 48.5 ms                                                         | 43.6 ms: 1.11x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 997 us: 1.11x faster                                                |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                |
| pprint_pformat             | 1.50 sec                                                        | 1.37 sec: 1.09x faster                                              |
| pprint_safe_repr           | 721 ms                                                          | 662 ms: 1.09x faster                                                |
| fannkuch                   | 354 ms                                                          | 325 ms: 1.09x faster                                                |
| xml_etree_generate         | 72.1 ms                                                         | 66.5 ms: 1.08x faster                                               |
| meteor_contest             | 86.9 ms                                                         | 80.3 ms: 1.08x faster                                               |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| pickle_pure_python         | 286 us                                                          | 265 us: 1.08x faster                                                |
| docutils                   | 1.98 sec                                                        | 1.85 sec: 1.07x faster                                              |
| sqlite_synth               | 2.07 us                                                         | 1.99 us: 1.04x faster                                               |
| pathlib                    | 91.4 ms                                                         | 88.2 ms: 1.04x faster                                               |
| sympy_expand               | 398 ms                                                          | 387 ms: 1.03x faster                                                |
| async_generators           | 313 ms                                                          | 306 ms: 1.03x faster                                                |
| tornado_http               | 105 ms                                                          | 104 ms: 1.01x faster                                                |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.01x faster                                              |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                               |
| unpickle_list              | 2.95 us                                                         | 2.98 us: 1.01x slower                                               |
| richards_super             | 46.5 ms                                                         | 47.3 ms: 1.02x slower                                               |
| pickle_list                | 3.37 us                                                         | 3.49 us: 1.04x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                               |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                               |
| coverage                   | 48.4 ms                                                         | 51.9 ms: 1.07x slower                                               |
| pickle_dict                | 19.9 us                                                         | 21.6 us: 1.08x slower                                               |
| pickle                     | 7.79 us                                                         | 8.56 us: 1.10x slower                                               |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                |
| bench_mp_pool              | 75.4 ms                                                         | 89.0 ms: 1.18x slower                                               |
| python_startup             | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                               |
| telco                      | 5.51 ms                                                         | 6.58 ms: 1.19x slower                                               |
| json_dumps                 | 7.40 ms                                                         | 9.09 ms: 1.23x slower                                               |
| asyncio_tcp                | 662 ms                                                          | 819 ms: 1.24x slower                                                |
| gc_traversal               | 1.44 ms                                                         | 1.81 ms: 1.26x slower                                               |
| json                       | 4.15 ms                                                         | 5.97 ms: 1.44x slower                                               |
| create_gc_cycles           | 652 us                                                          | 1.19 ms: 1.83x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 224 ms: 2.24x slower                                                |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, pidigits, richards
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.118x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown