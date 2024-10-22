# Results vs. 3.12.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-x86
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 265 ms: 1.06x faster                                                            |
| docutils       | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                          |
| tornado_http   | 105 ms                                                          | 108 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| async_tree_io              | 693 ms                                                          | 514 ms: 1.35x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 543 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 499 ms: 1.13x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 65.2 ms: 1.95x faster                                                           |
| float          | 76.7 ms                                                         | 46.1 ms: 1.66x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.48x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 104 ms: 1.24x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.86 ms: 1.10x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 40.5 ms: 1.31x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 161 us: 1.30x faster                                                            |
| xml_etree_generate   | 72.1 ms                                                         | 55.8 ms: 1.29x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 230 us: 1.24x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.8 ms: 1.22x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.03x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.40 us: 1.01x slower                                                           |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.3 us: 1.06x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 21.2 us: 1.06x slower                                                           |
| pickle               | 7.79 us                                                         | 8.44 us: 1.08x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 8.31 ms: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| python_startup         | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.75 ms: 1.73x faster                                                           |
| django_template | 36.9 ms                                                         | 32.1 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 17.0 us: 2.26x faster                                                           |
| nbody                      | 127 ms                                                          | 65.2 ms: 1.95x faster                                                           |
| scimark_sor                | 130 ms                                                          | 68.5 ms: 1.89x faster                                                           |
| logging_silent             | 101 ns                                                          | 56.2 ns: 1.80x faster                                                           |
| spectral_norm              | 104 ms                                                          | 57.8 ms: 1.79x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.75 ms: 1.73x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.6 ms: 1.68x faster                                                           |
| float                      | 76.7 ms                                                         | 46.1 ms: 1.66x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.5 ms: 1.57x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.50 ms: 1.55x faster                                                           |
| generators                 | 38.5 ms                                                         | 24.9 ms: 1.55x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 40.5 ns: 1.54x faster                                                           |
| deepcopy                   | 360 us                                                          | 236 us: 1.53x faster                                                            |
| scimark_fft                | 271 ms                                                          | 180 ms: 1.51x faster                                                            |
| comprehensions             | 19.2 us                                                         | 12.7 us: 1.51x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.49 sec: 1.47x faster                                                          |
| fannkuch                   | 354 ms                                                          | 248 ms: 1.43x faster                                                            |
| go                         | 137 ms                                                          | 96.6 ms: 1.42x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.53 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.39x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 50.2 ms: 1.38x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 255 ms: 1.38x faster                                                            |
| async_tree_none            | 298 ms                                                          | 219 ms: 1.36x faster                                                            |
| async_tree_io              | 693 ms                                                          | 514 ms: 1.35x faster                                                            |
| pyflate                    | 424 ms                                                          | 316 ms: 1.34x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.43 us: 1.33x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.36 us: 1.32x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.5 ms: 1.31x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 161 us: 1.30x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.8 ms: 1.29x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.11 us: 1.28x faster                                                           |
| chaos                      | 69.4 ms                                                         | 55.1 ms: 1.26x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 74.6 ms: 1.26x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.46 ms: 1.25x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 543 ms: 1.25x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.21 sec: 1.24x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 230 us: 1.24x faster                                                            |
| regex_compile              | 129 ms                                                          | 104 ms: 1.24x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 585 ms: 1.23x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.8 ms: 1.22x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.21x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 72.1 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                           |
| pycparser                  | 978 ms                                                          | 821 ms: 1.19x faster                                                            |
| dulwich_log                | 58.5 ms                                                         | 49.5 ms: 1.18x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.1 ms: 1.15x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.34 ms: 1.15x faster                                                           |
| raytrace                   | 308 ms                                                          | 271 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 483 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 499 ms: 1.13x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 995 us: 1.11x faster                                                            |
| richards_super             | 46.5 ms                                                         | 42.3 ms: 1.10x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.86 ms: 1.10x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.3 ms: 1.08x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                            |
| 2to3                       | 280 ms                                                          | 265 ms: 1.06x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 116 ms: 1.06x faster                                                            |
| sympy_str                  | 240 ms                                                          | 229 ms: 1.05x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.03x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 88.5 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.01x faster                                                          |
| sympy_expand               | 398 ms                                                          | 394 ms: 1.01x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 17.4 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.40 us: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 49.2 ms: 1.01x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.4 ms: 1.02x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.03 sec: 1.02x slower                                                          |
| tornado_http               | 105 ms                                                          | 108 ms: 1.03x slower                                                            |
| async_generators           | 313 ms                                                          | 324 ms: 1.04x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.3 us: 1.06x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 21.2 us: 1.06x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.44 us: 1.08x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.08 ms: 1.10x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.5 ms: 1.10x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.12x slower                                                            |
| json_dumps                 | 7.40 ms                                                         | 8.31 ms: 1.12x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.7 ms: 1.19x slower                                                           |
| json                       | 4.15 ms                                                         | 4.99 ms: 1.20x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 826 ms: 1.25x slower                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 94.3 ms: 1.25x slower                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.80 ms: 1.25x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 1.20 ms: 1.84x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 239 ms: 2.38x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.17x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown