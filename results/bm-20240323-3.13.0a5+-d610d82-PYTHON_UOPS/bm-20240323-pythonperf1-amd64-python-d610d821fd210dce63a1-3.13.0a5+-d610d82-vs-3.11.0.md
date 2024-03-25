# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.02x faster
- HPT reliability: 75.35%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 225 ms: 1.05x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.89 ms: 1.08x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.74 sec: 1.06x slower                                                      |
| tornado_http   | 92.8 ms                                                     | 87.1 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 222 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 274 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 564 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 210 ms: 1.47x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                        |
| async_tree_io              | 808 ms                                                      | 586 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 387 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 383 ms: 1.37x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.43x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                      | 148 ms: 1.02x faster                                                        |
| float          | 54.4 ms                                                     | 57.1 ms: 1.05x slower                                                       |
| nbody          | 70.3 ms                                                     | 79.6 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 116 ms                                                      | 120 ms: 1.03x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| regex_compile  | 91.0 ms                                                     | 103 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.63 ms: 1.44x faster                                                       |
| pickle_pure_python   | 208 us                                                      | 180 us: 1.16x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 91.9 ms: 1.06x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 18.4 us: 1.00x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.64 us: 1.02x slower                                                       |
| unpickle_pure_python | 157 us                                                      | 160 us: 1.02x slower                                                        |
| xml_etree_process    | 37.2 ms                                                     | 38.1 ms: 1.02x slower                                                       |
| tomli_loads          | 1.46 sec                                                    | 1.50 sec: 1.03x slower                                                      |
| xml_etree_generate   | 52.5 ms                                                     | 55.1 ms: 1.05x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.7 us: 1.06x slower                                                       |
| pickle               | 6.64 us                                                     | 7.12 us: 1.07x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.42 us: 1.11x slower                                                       |
| pickle_list          | 2.70 us                                                     | 3.12 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 20.5 ms: 1.03x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 39.9 ms                                                     | 36.0 ms: 1.11x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 16.9 ms: 1.09x faster                                                       |
| django_template | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| mako            | 7.58 ms                                                     | 7.39 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 73.5 us: 4.43x faster                                                       |
| generators                 | 34.0 ms                                                     | 21.9 ms: 1.55x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 481 ms: 1.51x faster                                                        |
| async_tree_none            | 332 ms                                                      | 222 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 274 ms: 1.48x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 564 ms: 1.47x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 210 ms: 1.47x faster                                                        |
| pylint                     | 323 ms                                                      | 220 ms: 1.47x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 276 ms: 1.45x faster                                                        |
| json_dumps                 | 8.09 ms                                                     | 5.63 ms: 1.44x faster                                                       |
| async_tree_io              | 808 ms                                                      | 586 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 387 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 383 ms: 1.37x faster                                                        |
| logging_silent             | 71.8 ns                                                     | 57.2 ns: 1.26x faster                                                       |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.62 sec: 1.25x faster                                                      |
| deltablue                  | 2.70 ms                                                     | 2.21 ms: 1.22x faster                                                       |
| richards_super             | 38.7 ms                                                     | 31.7 ms: 1.22x faster                                                       |
| comprehensions             | 15.6 us                                                     | 13.5 us: 1.16x faster                                                       |
| pickle_pure_python         | 208 us                                                      | 180 us: 1.16x faster                                                        |
| sqlglot_parse              | 953 us                                                      | 824 us: 1.16x faster                                                        |
| coroutines                 | 15.0 ms                                                     | 13.2 ms: 1.13x faster                                                       |
| richards                   | 31.4 ms                                                     | 28.2 ms: 1.12x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 36.0 ms: 1.11x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 23.5 us: 1.11x faster                                                       |
| sqlglot_transpile          | 1.16 ms                                                     | 1.05 ms: 1.10x faster                                                       |
| raytrace                   | 213 ms                                                      | 194 ms: 1.10x faster                                                        |
| genshi_text                | 18.4 ms                                                     | 16.9 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.77 us                                                     | 1.63 us: 1.09x faster                                                       |
| mdp                        | 1.59 sec                                                    | 1.47 sec: 1.08x faster                                                      |
| chameleon                  | 5.26 ms                                                     | 4.89 ms: 1.08x faster                                                       |
| chaos                      | 48.4 ms                                                     | 45.0 ms: 1.08x faster                                                       |
| logging_simple             | 6.86 us                                                     | 6.44 us: 1.07x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 87.1 ms: 1.07x faster                                                       |
| xml_etree_parse            | 97.6 ms                                                     | 91.9 ms: 1.06x faster                                                       |
| deepcopy                   | 246 us                                                      | 234 us: 1.06x faster                                                        |
| sympy_sum                  | 100 ms                                                      | 95.2 ms: 1.05x faster                                                       |
| logging_format             | 7.16 us                                                     | 6.86 us: 1.04x faster                                                       |
| unpack_sequence            | 46.9 ns                                                     | 44.9 ns: 1.04x faster                                                       |
| django_template            | 24.4 ms                                                     | 23.5 ms: 1.04x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 44.8 ms: 1.04x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 843 us: 1.03x faster                                                        |
| mako                       | 7.58 ms                                                     | 7.39 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 2.01 us: 1.02x faster                                                       |
| sympy_str                  | 185 ms                                                      | 181 ms: 1.02x faster                                                        |
| pidigits                   | 150 ms                                                      | 148 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 529 ms                                                      | 522 ms: 1.01x faster                                                        |
| gc_traversal               | 1.49 ms                                                     | 1.48 ms: 1.01x faster                                                       |
| sympy_integrate            | 14.0 ms                                                     | 13.9 ms: 1.01x faster                                                       |
| pickle_dict                | 18.5 us                                                     | 18.4 us: 1.00x faster                                                       |
| go                         | 101 ms                                                      | 101 ms: 1.00x faster                                                        |
| meteor_contest             | 75.2 ms                                                     | 75.6 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 49.6 ms: 1.02x slower                                                       |
| nqueens                    | 68.3 ms                                                     | 69.5 ms: 1.02x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.64 us: 1.02x slower                                                       |
| unpickle_pure_python       | 157 us                                                      | 160 us: 1.02x slower                                                        |
| mypy2                      | 459 ms                                                      | 470 ms: 1.02x slower                                                        |
| xml_etree_process          | 37.2 ms                                                     | 38.1 ms: 1.02x slower                                                       |
| tomli_loads                | 1.46 sec                                                    | 1.50 sec: 1.03x slower                                                      |
| bench_mp_pool              | 63.2 ms                                                     | 65.0 ms: 1.03x slower                                                       |
| sympy_expand               | 299 ms                                                      | 308 ms: 1.03x slower                                                        |
| python_startup             | 19.8 ms                                                     | 20.5 ms: 1.03x slower                                                       |
| regex_dna                  | 116 ms                                                      | 120 ms: 1.03x slower                                                        |
| create_gc_cycles           | 713 us                                                      | 744 us: 1.04x slower                                                        |
| aiohttp                    | 883 us                                                      | 921 us: 1.04x slower                                                        |
| xml_etree_generate         | 52.5 ms                                                     | 55.1 ms: 1.05x slower                                                       |
| float                      | 54.4 ms                                                     | 57.1 ms: 1.05x slower                                                       |
| 2to3                       | 214 ms                                                      | 225 ms: 1.05x slower                                                        |
| json_loads                 | 13.0 us                                                     | 13.7 us: 1.06x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.06x slower                                                       |
| docutils                   | 1.64 sec                                                    | 1.74 sec: 1.06x slower                                                      |
| coverage                   | 43.4 ms                                                     | 46.1 ms: 1.06x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 18.0 ms: 1.07x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.12 us: 1.07x slower                                                       |
| pyflate                    | 312 ms                                                      | 339 ms: 1.09x slower                                                        |
| fannkuch                   | 253 ms                                                      | 279 ms: 1.10x slower                                                        |
| pathlib                    | 70.9 ms                                                     | 78.6 ms: 1.11x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.42 us: 1.11x slower                                                       |
| scimark_monte_carlo        | 45.3 ms                                                     | 51.2 ms: 1.13x slower                                                       |
| nbody                      | 70.3 ms                                                     | 79.6 ms: 1.13x slower                                                       |
| regex_compile              | 91.0 ms                                                     | 103 ms: 1.13x slower                                                        |
| scimark_sor                | 78.1 ms                                                     | 89.2 ms: 1.14x slower                                                       |
| pickle_list                | 2.70 us                                                     | 3.12 us: 1.16x slower                                                       |
| hexiom                     | 4.55 ms                                                     | 5.35 ms: 1.17x slower                                                       |
| scimark_fft                | 179 ms                                                      | 212 ms: 1.18x slower                                                        |
| telco                      | 4.06 ms                                                     | 4.85 ms: 1.19x slower                                                       |
| spectral_norm              | 68.3 ms                                                     | 82.7 ms: 1.21x slower                                                       |
| scimark_lu                 | 62.8 ms                                                     | 78.1 ms: 1.24x slower                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 3.29 ms: 1.28x slower                                                       |
| async_generators           | 177 ms                                                      | 246 ms: 1.39x slower                                                        |
| thrift                     | 494 us                                                      | 9.52 ms: 19.27x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (5): json, pprint_pformat, html5lib, sqlglot_normalize, pycparser
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 75.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown