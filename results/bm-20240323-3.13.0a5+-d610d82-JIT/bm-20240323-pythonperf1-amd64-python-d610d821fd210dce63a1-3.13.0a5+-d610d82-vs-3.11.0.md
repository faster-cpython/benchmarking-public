# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 220 ms: 1.03x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.58 ms: 1.15x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.68 sec: 1.02x slower                                                      |
| html5lib       | 38.9 ms                                                     | 35.8 ms: 1.09x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 85.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 222 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 270 ms: 1.50x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 208 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 563 ms: 1.47x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 275 ms: 1.45x faster                                                        |
| async_tree_io              | 808 ms                                                      | 586 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 386 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 387 ms: 1.35x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.44x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 57.0 ms: 1.23x faster                                                       |
| float          | 54.4 ms                                                     | 46.2 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 83.7 ms: 1.09x faster                                                       |
| regex_dna      | 116 ms                                                      | 121 ms: 1.04x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.59 ms: 1.45x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 126 us: 1.24x faster                                                        |
| tomli_loads          | 1.46 sec                                                    | 1.20 sec: 1.21x faster                                                      |
| pickle_pure_python   | 208 us                                                      | 173 us: 1.20x faster                                                        |
| pickle_dict          | 18.5 us                                                     | 17.4 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| xml_etree_parse      | 97.6 ms                                                     | 92.2 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.2 ms                                                     | 36.2 ms: 1.03x faster                                                       |
| json_loads           | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| pickle_list          | 2.70 us                                                     | 2.87 us: 1.07x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| pickle               | 6.64 us                                                     | 7.36 us: 1.11x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.67 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 23.2 ms: 1.17x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 20.8 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.71 ms: 1.33x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 15.1 ms: 1.22x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 35.4 ms: 1.13x faster                                                       |
| django_template | 24.4 ms                                                     | 23.2 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 69.9 us: 4.66x faster                                                       |
| generators                 | 34.0 ms                                                     | 20.4 ms: 1.66x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 464 ms: 1.56x faster                                                        |
| pylint                     | 323 ms                                                      | 215 ms: 1.50x faster                                                        |
| async_tree_none            | 332 ms                                                      | 222 ms: 1.50x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 270 ms: 1.50x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 208 ms: 1.49x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 563 ms: 1.47x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 275 ms: 1.45x faster                                                        |
| json_dumps                 | 8.09 ms                                                     | 5.59 ms: 1.45x faster                                                       |
| comprehensions             | 15.6 us                                                     | 10.8 us: 1.45x faster                                                       |
| async_tree_io              | 808 ms                                                      | 586 ms: 1.38x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 386 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 387 ms: 1.35x faster                                                        |
| spectral_norm              | 68.3 ms                                                     | 50.9 ms: 1.34x faster                                                       |
| mako                       | 7.58 ms                                                     | 5.71 ms: 1.33x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 54.8 ns: 1.31x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 2.08 ms: 1.30x faster                                                       |
| unpickle_pure_python       | 157 us                                                      | 126 us: 1.24x faster                                                        |
| nbody                      | 70.3 ms                                                     | 57.0 ms: 1.23x faster                                                       |
| chaos                      | 48.4 ms                                                     | 39.3 ms: 1.23x faster                                                       |
| richards_super             | 38.7 ms                                                     | 31.5 ms: 1.23x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 21.2 us: 1.23x faster                                                       |
| genshi_text                | 18.4 ms                                                     | 15.1 ms: 1.22x faster                                                       |
| sqlglot_parse              | 953 us                                                      | 783 us: 1.22x faster                                                        |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.67 sec: 1.22x faster                                                      |
| tomli_loads                | 1.46 sec                                                    | 1.20 sec: 1.21x faster                                                      |
| pickle_pure_python         | 208 us                                                      | 173 us: 1.20x faster                                                        |
| raytrace                   | 213 ms                                                      | 181 ms: 1.18x faster                                                        |
| float                      | 54.4 ms                                                     | 46.2 ms: 1.18x faster                                                       |
| sqlglot_transpile          | 1.16 ms                                                     | 1.00 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.23 ms: 1.15x faster                                                       |
| logging_simple             | 6.86 us                                                     | 5.96 us: 1.15x faster                                                       |
| chameleon                  | 5.26 ms                                                     | 4.58 ms: 1.15x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 40.6 ms: 1.14x faster                                                       |
| fannkuch                   | 253 ms                                                      | 222 ms: 1.14x faster                                                        |
| sympy_sum                  | 100 ms                                                      | 87.9 ms: 1.14x faster                                                       |
| crypto_pyaes               | 48.9 ms                                                     | 43.3 ms: 1.13x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 35.4 ms: 1.13x faster                                                       |
| nqueens                    | 68.3 ms                                                     | 60.7 ms: 1.13x faster                                                       |
| sympy_str                  | 185 ms                                                      | 165 ms: 1.12x faster                                                        |
| deepcopy                   | 246 us                                                      | 219 us: 1.12x faster                                                        |
| logging_format             | 7.16 us                                                     | 6.39 us: 1.12x faster                                                       |
| richards                   | 31.4 ms                                                     | 28.0 ms: 1.12x faster                                                       |
| pprint_pformat             | 1.09 sec                                                    | 975 ms: 1.12x faster                                                        |
| pprint_safe_repr           | 529 ms                                                      | 476 ms: 1.11x faster                                                        |
| sqlite_synth               | 1.77 us                                                     | 1.59 us: 1.11x faster                                                       |
| coroutines                 | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                                       |
| pyflate                    | 312 ms                                                      | 283 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 45.3 ms                                                     | 41.3 ms: 1.10x faster                                                       |
| go                         | 101 ms                                                      | 92.6 ms: 1.09x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 85.1 ms: 1.09x faster                                                       |
| regex_compile              | 91.0 ms                                                     | 83.7 ms: 1.09x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 35.8 ms: 1.09x faster                                                       |
| sympy_integrate            | 14.0 ms                                                     | 13.2 ms: 1.06x faster                                                       |
| pycparser                  | 720 ms                                                      | 676 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                       |
| pickle_dict                | 18.5 us                                                     | 17.4 us: 1.06x faster                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 61.8 ms: 1.06x faster                                                       |
| scimark_fft                | 179 ms                                                      | 169 ms: 1.06x faster                                                        |
| xml_etree_parse            | 97.6 ms                                                     | 92.2 ms: 1.06x faster                                                       |
| django_template            | 24.4 ms                                                     | 23.2 ms: 1.05x faster                                                       |
| sympy_expand               | 299 ms                                                      | 284 ms: 1.05x faster                                                        |
| hexiom                     | 4.55 ms                                                     | 4.37 ms: 1.04x faster                                                       |
| bench_thread_pool          | 872 us                                                      | 837 us: 1.04x faster                                                        |
| sqlglot_normalize          | 190 ms                                                      | 183 ms: 1.04x faster                                                        |
| mdp                        | 1.59 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| xml_etree_process          | 37.2 ms                                                     | 36.2 ms: 1.03x faster                                                       |
| meteor_contest             | 75.2 ms                                                     | 74.2 ms: 1.01x faster                                                       |
| gc_traversal               | 1.49 ms                                                     | 1.48 ms: 1.01x faster                                                       |
| aiohttp                    | 883 us                                                      | 899 us: 1.02x slower                                                        |
| unpack_sequence            | 46.9 ns                                                     | 47.7 ns: 1.02x slower                                                       |
| docutils                   | 1.64 sec                                                    | 1.68 sec: 1.02x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.02x slower                                                       |
| create_gc_cycles           | 713 us                                                      | 733 us: 1.03x slower                                                        |
| 2to3                       | 214 ms                                                      | 220 ms: 1.03x slower                                                        |
| scimark_sor                | 78.1 ms                                                     | 81.3 ms: 1.04x slower                                                       |
| regex_dna                  | 116 ms                                                      | 121 ms: 1.04x slower                                                        |
| json_loads                 | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| pickle_list                | 2.70 us                                                     | 2.87 us: 1.07x slower                                                       |
| coverage                   | 43.4 ms                                                     | 46.4 ms: 1.07x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.78 us: 1.07x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.3 ms: 1.08x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 76.9 ms: 1.09x slower                                                       |
| bench_mp_pool              | 63.2 ms                                                     | 68.7 ms: 1.09x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.36 us: 1.11x slower                                                       |
| scimark_lu                 | 62.8 ms                                                     | 70.4 ms: 1.12x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.67 us: 1.14x slower                                                       |
| python_startup             | 19.8 ms                                                     | 23.2 ms: 1.17x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.77 ms: 1.17x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 20.8 ms: 1.24x slower                                                       |
| async_generators           | 177 ms                                                      | 244 ms: 1.38x slower                                                        |
| thrift                     | 494 us                                                      | 8.86 ms: 17.95x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (4): json, pidigits, xml_etree_generate, mypy2
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown