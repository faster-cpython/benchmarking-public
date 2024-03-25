# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 210 ms: 1.02x faster                                                        |
| chameleon      | 5.26 ms                                                     | 4.74 ms: 1.11x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| html5lib       | 38.9 ms                                                     | 36.3 ms: 1.07x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 83.2 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 221 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 271 ms: 1.49x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 208 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 563 ms: 1.47x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 381 ms: 1.39x faster                                                        |
| async_tree_io              | 808 ms                                                      | 583 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 388 ms: 1.35x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.44x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.4 ms                                                     | 52.7 ms: 1.03x faster                                                       |
| nbody          | 70.3 ms                                                     | 68.6 ms: 1.03x faster                                                       |
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 76.8 ms: 1.18x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.61 ms: 1.44x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 127 us: 1.23x faster                                                        |
| pickle_pure_python   | 208 us                                                      | 179 us: 1.16x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 91.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 63.3 ms: 1.04x faster                                                       |
| tomli_loads          | 1.46 sec                                                    | 1.42 sec: 1.02x faster                                                      |
| xml_etree_process    | 37.2 ms                                                     | 36.8 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.5 ms                                                     | 53.3 ms: 1.01x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.69 us: 1.04x slower                                                       |
| pickle_list          | 2.70 us                                                     | 2.84 us: 1.05x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.8 us: 1.07x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.39 us: 1.11x slower                                                       |
| pickle               | 6.64 us                                                     | 7.44 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 20.2 ms: 1.02x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 18.7 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 6.23 ms: 1.22x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 15.8 ms: 1.17x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 35.0 ms: 1.14x faster                                                       |
| django_template | 24.4 ms                                                     | 21.7 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 70.7 us: 4.61x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 465 ms: 1.56x faster                                                        |
| pylint                     | 323 ms                                                      | 209 ms: 1.55x faster                                                        |
| generators                 | 34.0 ms                                                     | 22.4 ms: 1.52x faster                                                       |
| async_tree_none            | 332 ms                                                      | 221 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 271 ms: 1.49x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 208 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 563 ms: 1.47x faster                                                        |
| comprehensions             | 15.6 us                                                     | 10.7 us: 1.46x faster                                                       |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                        |
| json_dumps                 | 8.09 ms                                                     | 5.61 ms: 1.44x faster                                                       |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 381 ms: 1.39x faster                                                        |
| async_tree_io              | 808 ms                                                      | 583 ms: 1.38x faster                                                        |
| deltablue                  | 2.70 ms                                                     | 1.98 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 388 ms: 1.35x faster                                                        |
| raytrace                   | 213 ms                                                      | 163 ms: 1.31x faster                                                        |
| logging_silent             | 71.8 ns                                                     | 55.4 ns: 1.29x faster                                                       |
| richards_super             | 38.7 ms                                                     | 30.7 ms: 1.26x faster                                                       |
| unpack_sequence            | 46.9 ns                                                     | 37.3 ns: 1.26x faster                                                       |
| sqlglot_parse              | 953 us                                                      | 761 us: 1.25x faster                                                        |
| chaos                      | 48.4 ms                                                     | 39.1 ms: 1.24x faster                                                       |
| unpickle_pure_python       | 157 us                                                      | 127 us: 1.23x faster                                                        |
| mako                       | 7.58 ms                                                     | 6.23 ms: 1.22x faster                                                       |
| hexiom                     | 4.55 ms                                                     | 3.78 ms: 1.21x faster                                                       |
| sympy_sum                  | 100 ms                                                      | 83.5 ms: 1.20x faster                                                       |
| sqlglot_transpile          | 1.16 ms                                                     | 972 us: 1.20x faster                                                        |
| go                         | 101 ms                                                      | 84.5 ms: 1.20x faster                                                       |
| nqueens                    | 68.3 ms                                                     | 57.6 ms: 1.19x faster                                                       |
| regex_compile              | 91.0 ms                                                     | 76.8 ms: 1.18x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 21.9 us: 1.18x faster                                                       |
| genshi_text                | 18.4 ms                                                     | 15.8 ms: 1.17x faster                                                       |
| sympy_str                  | 185 ms                                                      | 159 ms: 1.17x faster                                                        |
| scimark_monte_carlo        | 45.3 ms                                                     | 38.9 ms: 1.16x faster                                                       |
| pickle_pure_python         | 208 us                                                      | 179 us: 1.16x faster                                                        |
| scimark_lu                 | 62.8 ms                                                     | 54.4 ms: 1.15x faster                                                       |
| mdp                        | 1.59 sec                                                    | 1.38 sec: 1.15x faster                                                      |
| richards                   | 31.4 ms                                                     | 27.3 ms: 1.15x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 40.5 ms: 1.15x faster                                                       |
| sympy_integrate            | 14.0 ms                                                     | 12.3 ms: 1.14x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 35.0 ms: 1.14x faster                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 43.2 ms: 1.13x faster                                                       |
| django_template            | 24.4 ms                                                     | 21.7 ms: 1.13x faster                                                       |
| coroutines                 | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                                       |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.81 sec: 1.12x faster                                                      |
| logging_simple             | 6.86 us                                                     | 6.14 us: 1.12x faster                                                       |
| spectral_norm              | 68.3 ms                                                     | 61.2 ms: 1.12x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 83.2 ms: 1.11x faster                                                       |
| chameleon                  | 5.26 ms                                                     | 4.74 ms: 1.11x faster                                                       |
| logging_format             | 7.16 us                                                     | 6.49 us: 1.10x faster                                                       |
| pyflate                    | 312 ms                                                      | 284 ms: 1.10x faster                                                        |
| sqlite_synth               | 1.77 us                                                     | 1.61 us: 1.10x faster                                                       |
| sympy_expand               | 299 ms                                                      | 274 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.09 sec                                                    | 1.00 sec: 1.09x faster                                                      |
| pycparser                  | 720 ms                                                      | 663 ms: 1.09x faster                                                        |
| deepcopy                   | 246 us                                                      | 227 us: 1.08x faster                                                        |
| pprint_safe_repr           | 529 ms                                                      | 489 ms: 1.08x faster                                                        |
| bench_thread_pool          | 872 us                                                      | 807 us: 1.08x faster                                                        |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.40 ms: 1.07x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 36.3 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 190 ms                                                      | 179 ms: 1.06x faster                                                        |
| xml_etree_parse            | 97.6 ms                                                     | 91.9 ms: 1.06x faster                                                       |
| mypy2                      | 459 ms                                                      | 436 ms: 1.05x faster                                                        |
| scimark_fft                | 179 ms                                                      | 171 ms: 1.05x faster                                                        |
| fannkuch                   | 253 ms                                                      | 244 ms: 1.04x faster                                                        |
| xml_etree_iterparse        | 65.6 ms                                                     | 63.3 ms: 1.04x faster                                                       |
| float                      | 54.4 ms                                                     | 52.7 ms: 1.03x faster                                                       |
| meteor_contest             | 75.2 ms                                                     | 72.9 ms: 1.03x faster                                                       |
| nbody                      | 70.3 ms                                                     | 68.6 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.8 ms: 1.02x faster                                                       |
| tomli_loads                | 1.46 sec                                                    | 1.42 sec: 1.02x faster                                                      |
| gc_traversal               | 1.49 ms                                                     | 1.46 ms: 1.02x faster                                                       |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                        |
| 2to3                       | 214 ms                                                      | 210 ms: 1.02x faster                                                        |
| docutils                   | 1.64 sec                                                    | 1.62 sec: 1.02x faster                                                      |
| xml_etree_process          | 37.2 ms                                                     | 36.8 ms: 1.01x faster                                                       |
| scimark_sor                | 78.1 ms                                                     | 77.7 ms: 1.01x faster                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 63.6 ms: 1.01x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.01x slower                                                       |
| xml_etree_generate         | 52.5 ms                                                     | 53.3 ms: 1.01x slower                                                       |
| python_startup             | 19.8 ms                                                     | 20.2 ms: 1.02x slower                                                       |
| pickle_dict                | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.69 us: 1.04x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.57 ms: 1.04x slower                                                       |
| pickle_list                | 2.70 us                                                     | 2.84 us: 1.05x slower                                                       |
| json_loads                 | 13.0 us                                                     | 13.8 us: 1.07x slower                                                       |
| coverage                   | 43.4 ms                                                     | 46.9 ms: 1.08x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 77.2 ms: 1.09x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.39 us: 1.11x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 18.7 ms: 1.11x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.44 us: 1.12x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.75 ms: 1.17x slower                                                       |
| async_generators           | 177 ms                                                      | 227 ms: 1.28x slower                                                        |
| thrift                     | 494 us                                                      | 8.04 ms: 16.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (5): json, aiohttp, deepcopy_reduce, regex_dna, create_gc_cycles
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown