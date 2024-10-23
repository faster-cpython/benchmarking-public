# Results vs. 3.12.0

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 255 ms: 1.10x faster                                                     |
| docutils       | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                   |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                           | 1.02x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                     |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                     |
| async_tree_io              | 693 ms                                                          | 522 ms: 1.33x faster                                                     |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                     |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                     |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 57.9 ms: 2.19x faster                                                    |
| float          | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                    |
| pidigits       | 199 ms                                                          | 203 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                           | 1.53x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 97.7 ms: 1.32x faster                                                    |
| regex_effbot   | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                    |
| regex_dna      | 127 ms                                                          | 113 ms: 1.12x faster                                                     |
| regex_v8       | 15.0 ms                                                         | 15.2 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                           | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                   |
| unpickle_pure_python | 210 us                                                          | 156 us: 1.35x faster                                                     |
| xml_etree_generate   | 72.1 ms                                                         | 54.9 ms: 1.31x faster                                                    |
| xml_etree_process    | 53.2 ms                                                         | 40.8 ms: 1.30x faster                                                    |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                    |
| pickle_pure_python   | 286 us                                                          | 237 us: 1.21x faster                                                     |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.03x faster                                                     |
| json_loads           | 20.4 us                                                         | 20.8 us: 1.02x slower                                                    |
| json_dumps           | 7.40 ms                                                         | 8.03 ms: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                           | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                                    |
| python_startup         | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.14x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                    |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                    |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 15.8 us: 2.42x faster                                                    |
| nbody                      | 127 ms                                                          | 57.9 ms: 2.19x faster                                                    |
| scimark_sor                | 130 ms                                                          | 67.0 ms: 1.94x faster                                                    |
| logging_silent             | 101 ns                                                          | 55.1 ns: 1.83x faster                                                    |
| spectral_norm              | 104 ms                                                          | 58.7 ms: 1.77x faster                                                    |
| mako                       | 9.96 ms                                                         | 5.68 ms: 1.75x faster                                                    |
| scimark_monte_carlo        | 66.4 ms                                                         | 37.9 ms: 1.75x faster                                                    |
| generators                 | 38.5 ms                                                         | 22.4 ms: 1.72x faster                                                    |
| float                      | 76.7 ms                                                         | 45.9 ms: 1.67x faster                                                    |
| scimark_lu                 | 93.2 ms                                                         | 57.7 ms: 1.61x faster                                                    |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.48 ms: 1.56x faster                                                    |
| deepcopy                   | 360 us                                                          | 233 us: 1.55x faster                                                     |
| scimark_fft                | 271 ms                                                          | 175 ms: 1.54x faster                                                     |
| go                         | 137 ms                                                          | 89.2 ms: 1.54x faster                                                    |
| comprehensions             | 19.2 us                                                         | 12.5 us: 1.54x faster                                                    |
| fannkuch                   | 354 ms                                                          | 232 ms: 1.53x faster                                                     |
| hexiom                     | 6.82 ms                                                         | 4.70 ms: 1.45x faster                                                    |
| tomli_loads                | 2.20 sec                                                        | 1.51 sec: 1.45x faster                                                   |
| deltablue                  | 3.58 ms                                                         | 2.52 ms: 1.42x faster                                                    |
| crypto_pyaes               | 69.2 ms                                                         | 48.9 ms: 1.42x faster                                                    |
| pyflate                    | 424 ms                                                          | 300 ms: 1.41x faster                                                     |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                     |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                     |
| deepcopy_reduce            | 3.23 us                                                         | 2.36 us: 1.36x faster                                                    |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.35x faster                                                     |
| async_tree_io              | 693 ms                                                          | 522 ms: 1.33x faster                                                     |
| pprint_pformat             | 1.50 sec                                                        | 1.13 sec: 1.33x faster                                                   |
| regex_compile              | 129 ms                                                          | 97.7 ms: 1.32x faster                                                    |
| xml_etree_generate         | 72.1 ms                                                         | 54.9 ms: 1.31x faster                                                    |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                     |
| chaos                      | 69.4 ms                                                         | 53.0 ms: 1.31x faster                                                    |
| xml_etree_process          | 53.2 ms                                                         | 40.8 ms: 1.30x faster                                                    |
| logging_simple             | 9.75 us                                                         | 7.50 us: 1.30x faster                                                    |
| pprint_safe_repr           | 721 ms                                                          | 556 ms: 1.30x faster                                                     |
| nqueens                    | 93.7 ms                                                         | 73.4 ms: 1.28x faster                                                    |
| logging_format             | 10.4 us                                                         | 8.23 us: 1.26x faster                                                    |
| pycparser                  | 978 ms                                                          | 781 ms: 1.25x faster                                                     |
| sqlglot_parse              | 1.25 ms                                                         | 1.01 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 677 ms                                                          | 549 ms: 1.23x faster                                                     |
| meteor_contest             | 86.9 ms                                                         | 70.7 ms: 1.23x faster                                                    |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.5 ms: 1.22x faster                                                    |
| pickle_pure_python         | 286 us                                                          | 237 us: 1.21x faster                                                     |
| dulwich_log                | 58.5 ms                                                         | 48.7 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 470 ms: 1.20x faster                                                     |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                    |
| richards                   | 41.3 ms                                                         | 34.9 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                     |
| sqlglot_transpile          | 1.53 ms                                                         | 1.30 ms: 1.18x faster                                                    |
| raytrace                   | 308 ms                                                          | 263 ms: 1.17x faster                                                     |
| regex_effbot               | 2.04 ms                                                         | 1.76 ms: 1.16x faster                                                    |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.15x faster                                                   |
| richards_super             | 46.5 ms                                                         | 40.7 ms: 1.14x faster                                                    |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                    |
| regex_dna                  | 127 ms                                                          | 113 ms: 1.12x faster                                                     |
| 2to3                       | 280 ms                                                          | 255 ms: 1.10x faster                                                     |
| bench_thread_pool          | 1.10 ms                                                         | 1.00 ms: 1.10x faster                                                    |
| sympy_str                  | 240 ms                                                          | 219 ms: 1.09x faster                                                     |
| sympy_sum                  | 123 ms                                                          | 114 ms: 1.08x faster                                                     |
| sympy_expand               | 398 ms                                                          | 382 ms: 1.04x faster                                                     |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.03x faster                                                     |
| pathlib                    | 91.4 ms                                                         | 88.4 ms: 1.03x faster                                                    |
| sympy_integrate            | 17.5 ms                                                         | 17.0 ms: 1.03x faster                                                    |
| sqlglot_optimize           | 48.5 ms                                                         | 47.8 ms: 1.01x faster                                                    |
| sqlglot_normalize          | 100 ms                                                          | 99.3 ms: 1.01x faster                                                    |
| docutils                   | 1.98 sec                                                        | 1.97 sec: 1.01x faster                                                   |
| regex_v8                   | 15.0 ms                                                         | 15.2 ms: 1.01x slower                                                    |
| async_generators           | 313 ms                                                          | 319 ms: 1.02x slower                                                     |
| pidigits                   | 199 ms                                                          | 203 ms: 1.02x slower                                                     |
| json_loads                 | 20.4 us                                                         | 20.8 us: 1.02x slower                                                    |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                     |
| python_startup_no_site     | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                                    |
| json_dumps                 | 7.40 ms                                                         | 8.03 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                     |
| coverage                   | 48.4 ms                                                         | 53.3 ms: 1.10x slower                                                    |
| telco                      | 5.51 ms                                                         | 6.16 ms: 1.12x slower                                                    |
| python_startup             | 22.4 ms                                                         | 27.0 ms: 1.21x slower                                                    |
| json                       | 4.15 ms                                                         | 5.15 ms: 1.24x slower                                                    |
| bench_mp_pool              | 75.4 ms                                                         | 93.6 ms: 1.24x slower                                                    |
| gc_traversal               | 1.44 ms                                                         | 1.82 ms: 1.26x slower                                                    |
| create_gc_cycles           | 652 us                                                          | 1.18 ms: 1.80x slower                                                    |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                             |
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown