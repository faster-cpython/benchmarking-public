# Results vs. 3.11.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: windows-amd64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 222 ms: 1.04x slower                                                        |
| chameleon      | 5.26 ms                                                     | 4.76 ms: 1.11x faster                                                       |
| docutils       | 1.64 sec                                                    | 1.60 sec: 1.02x faster                                                      |
| html5lib       | 38.9 ms                                                     | 37.0 ms: 1.05x faster                                                       |
| tornado_http   | 92.8 ms                                                     | 85.0 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 260 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 446 ms: 1.19x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 336 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 341 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 267 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 462 ms: 1.13x faster                                                        |
| async_tree_io              | 808 ms                                                      | 716 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 829 ms                                                      | 743 ms: 1.12x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 58.7 ms: 1.20x faster                                                       |
| float          | 54.4 ms                                                     | 47.8 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 83.1 ms: 1.10x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                       |
| regex_dna      | 116 ms                                                      | 126 ms: 1.09x slower                                                        |
| regex_v8       | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.49 ms: 1.48x faster                                                       |
| unpickle_pure_python | 157 us                                                      | 127 us: 1.23x faster                                                        |
| tomli_loads          | 1.46 sec                                                    | 1.18 sec: 1.23x faster                                                      |
| pickle_pure_python   | 208 us                                                      | 178 us: 1.17x faster                                                        |
| xml_etree_parse      | 97.6 ms                                                     | 92.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.6 ms                                                     | 62.3 ms: 1.05x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 17.9 us: 1.03x faster                                                       |
| xml_etree_process    | 37.2 ms                                                     | 36.9 ms: 1.01x faster                                                       |
| xml_etree_generate   | 52.5 ms                                                     | 53.2 ms: 1.01x slower                                                       |
| pickle_list          | 2.70 us                                                     | 2.77 us: 1.03x slower                                                       |
| json_loads           | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| unpickle_list        | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| pickle               | 6.64 us                                                     | 7.55 us: 1.14x slower                                                       |
| unpickle             | 7.57 us                                                     | 8.64 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 24.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 16.8 ms                                                     | 22.5 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.54 ms: 1.37x faster                                                       |
| genshi_text     | 18.4 ms                                                     | 15.3 ms: 1.21x faster                                                       |
| genshi_xml      | 39.9 ms                                                     | 34.9 ms: 1.15x faster                                                       |
| django_template | 24.4 ms                                                     | 21.5 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf1-amd64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 71.1 us: 4.58x faster                                                       |
| generators                 | 34.0 ms                                                     | 19.9 ms: 1.71x faster                                                       |
| asyncio_tcp                | 726 ms                                                      | 470 ms: 1.54x faster                                                        |
| pylint                     | 323 ms                                                      | 209 ms: 1.54x faster                                                        |
| json_dumps                 | 8.09 ms                                                     | 5.49 ms: 1.48x faster                                                       |
| comprehensions             | 15.6 us                                                     | 10.7 us: 1.46x faster                                                       |
| mako                       | 7.58 ms                                                     | 5.54 ms: 1.37x faster                                                       |
| spectral_norm              | 68.3 ms                                                     | 51.0 ms: 1.34x faster                                                       |
| deltablue                  | 2.70 ms                                                     | 2.03 ms: 1.33x faster                                                       |
| logging_silent             | 71.8 ns                                                     | 55.5 ns: 1.29x faster                                                       |
| async_tree_none            | 332 ms                                                      | 260 ms: 1.28x faster                                                        |
| sqlglot_parse              | 953 us                                                      | 772 us: 1.23x faster                                                        |
| unpickle_pure_python       | 157 us                                                      | 127 us: 1.23x faster                                                        |
| tomli_loads                | 1.46 sec                                                    | 1.18 sec: 1.23x faster                                                      |
| chaos                      | 48.4 ms                                                     | 39.4 ms: 1.23x faster                                                       |
| richards_super             | 38.7 ms                                                     | 31.6 ms: 1.23x faster                                                       |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.65 sec: 1.23x faster                                                      |
| genshi_text                | 18.4 ms                                                     | 15.3 ms: 1.21x faster                                                       |
| nbody                      | 70.3 ms                                                     | 58.7 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 446 ms: 1.19x faster                                                        |
| async_tree_memoization     | 399 ms                                                      | 336 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 405 ms                                                      | 341 ms: 1.19x faster                                                        |
| sqlglot_transpile          | 1.16 ms                                                     | 991 us: 1.18x faster                                                        |
| raytrace                   | 213 ms                                                      | 182 ms: 1.17x faster                                                        |
| pickle_pure_python         | 208 us                                                      | 178 us: 1.17x faster                                                        |
| logging_simple             | 6.86 us                                                     | 5.87 us: 1.17x faster                                                       |
| dulwich_log                | 46.4 ms                                                     | 39.7 ms: 1.17x faster                                                       |
| fannkuch                   | 253 ms                                                      | 217 ms: 1.17x faster                                                        |
| async_tree_none_tg         | 309 ms                                                      | 267 ms: 1.16x faster                                                        |
| logging_format             | 7.16 us                                                     | 6.24 us: 1.15x faster                                                       |
| genshi_xml                 | 39.9 ms                                                     | 34.9 ms: 1.15x faster                                                       |
| deepcopy_memo              | 26.0 us                                                     | 22.8 us: 1.14x faster                                                       |
| pprint_pformat             | 1.09 sec                                                    | 954 ms: 1.14x faster                                                        |
| float                      | 54.4 ms                                                     | 47.8 ms: 1.14x faster                                                       |
| pprint_safe_repr           | 529 ms                                                      | 466 ms: 1.13x faster                                                        |
| django_template            | 24.4 ms                                                     | 21.5 ms: 1.13x faster                                                       |
| nqueens                    | 68.3 ms                                                     | 60.3 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 462 ms: 1.13x faster                                                        |
| sympy_sum                  | 100 ms                                                      | 88.5 ms: 1.13x faster                                                       |
| sympy_str                  | 185 ms                                                      | 164 ms: 1.13x faster                                                        |
| crypto_pyaes               | 48.9 ms                                                     | 43.3 ms: 1.13x faster                                                       |
| coroutines                 | 15.0 ms                                                     | 13.3 ms: 1.13x faster                                                       |
| async_tree_io              | 808 ms                                                      | 716 ms: 1.13x faster                                                        |
| deepcopy                   | 246 us                                                      | 219 us: 1.12x faster                                                        |
| sqlite_synth               | 1.77 us                                                     | 1.58 us: 1.12x faster                                                       |
| async_tree_io_tg           | 829 ms                                                      | 743 ms: 1.12x faster                                                        |
| richards                   | 31.4 ms                                                     | 28.2 ms: 1.12x faster                                                       |
| mdp                        | 1.59 sec                                                    | 1.44 sec: 1.11x faster                                                      |
| chameleon                  | 5.26 ms                                                     | 4.76 ms: 1.11x faster                                                       |
| pyflate                    | 312 ms                                                      | 282 ms: 1.11x faster                                                        |
| regex_compile              | 91.0 ms                                                     | 83.1 ms: 1.10x faster                                                       |
| tornado_http               | 92.8 ms                                                     | 85.0 ms: 1.09x faster                                                       |
| sqlglot_normalize          | 190 ms                                                      | 175 ms: 1.09x faster                                                        |
| scimark_monte_carlo        | 45.3 ms                                                     | 41.9 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.39 ms: 1.08x faster                                                       |
| sympy_integrate            | 14.0 ms                                                     | 13.1 ms: 1.07x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 1.93 us: 1.07x faster                                                       |
| sympy_expand               | 299 ms                                                      | 281 ms: 1.06x faster                                                        |
| xml_etree_parse            | 97.6 ms                                                     | 92.2 ms: 1.06x faster                                                       |
| hexiom                     | 4.55 ms                                                     | 4.32 ms: 1.06x faster                                                       |
| mypy2                      | 459 ms                                                      | 436 ms: 1.05x faster                                                        |
| go                         | 101 ms                                                      | 96.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.6 ms                                                     | 62.3 ms: 1.05x faster                                                       |
| html5lib                   | 38.9 ms                                                     | 37.0 ms: 1.05x faster                                                       |
| scimark_fft                | 179 ms                                                      | 172 ms: 1.04x faster                                                        |
| pickle_dict                | 18.5 us                                                     | 17.9 us: 1.03x faster                                                       |
| docutils                   | 1.64 sec                                                    | 1.60 sec: 1.02x faster                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 34.3 ms: 1.01x faster                                                       |
| xml_etree_process          | 37.2 ms                                                     | 36.9 ms: 1.01x faster                                                       |
| gc_traversal               | 1.49 ms                                                     | 1.50 ms: 1.01x slower                                                       |
| xml_etree_generate         | 52.5 ms                                                     | 53.2 ms: 1.01x slower                                                       |
| pickle_list                | 2.70 us                                                     | 2.77 us: 1.03x slower                                                       |
| unpack_sequence            | 46.9 ns                                                     | 48.6 ns: 1.04x slower                                                       |
| 2to3                       | 214 ms                                                      | 222 ms: 1.04x slower                                                        |
| create_gc_cycles           | 713 us                                                      | 745 us: 1.04x slower                                                        |
| json_loads                 | 13.0 us                                                     | 13.8 us: 1.06x slower                                                       |
| unpickle_list              | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| regex_effbot               | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                       |
| scimark_sor                | 78.1 ms                                                     | 84.4 ms: 1.08x slower                                                       |
| pathlib                    | 70.9 ms                                                     | 76.6 ms: 1.08x slower                                                       |
| coverage                   | 43.4 ms                                                     | 47.1 ms: 1.08x slower                                                       |
| regex_dna                  | 116 ms                                                      | 126 ms: 1.09x slower                                                        |
| bench_mp_pool              | 63.2 ms                                                     | 70.3 ms: 1.11x slower                                                       |
| telco                      | 4.06 ms                                                     | 4.57 ms: 1.12x slower                                                       |
| scimark_lu                 | 62.8 ms                                                     | 70.7 ms: 1.13x slower                                                       |
| json                       | 2.98 ms                                                     | 3.36 ms: 1.13x slower                                                       |
| pickle                     | 6.64 us                                                     | 7.55 us: 1.14x slower                                                       |
| unpickle                   | 7.57 us                                                     | 8.64 us: 1.14x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 17.3 ms: 1.22x slower                                                       |
| python_startup             | 19.8 ms                                                     | 24.7 ms: 1.25x slower                                                       |
| python_startup_no_site     | 16.8 ms                                                     | 22.5 ms: 1.34x slower                                                       |
| async_generators           | 177 ms                                                      | 238 ms: 1.34x slower                                                        |
| thrift                     | 494 us                                                      | 9.00 ms: 18.23x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, pycparser, meteor_contest, pidigits, aiohttp
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown