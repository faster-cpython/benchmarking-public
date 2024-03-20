# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_plt
- machine: windows-amd64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 220 ms: 1.03x slower                                                    |
| chameleon      | 5.26 ms                                                     | 4.71 ms: 1.12x faster                                                   |
| docutils       | 1.64 sec                                                    | 1.58 sec: 1.04x faster                                                  |
| html5lib       | 38.9 ms                                                     | 36.0 ms: 1.08x faster                                                   |
| tornado_http   | 92.8 ms                                                     | 83.9 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                       | 1.06x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 332 ms                                                      | 262 ms: 1.27x faster                                                    |
| async_tree_memoization_tg  | 405 ms                                                      | 339 ms: 1.19x faster                                                    |
| async_tree_memoization     | 399 ms                                                      | 336 ms: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 451 ms: 1.18x faster                                                    |
| async_tree_none_tg         | 309 ms                                                      | 268 ms: 1.15x faster                                                    |
| async_tree_io              | 808 ms                                                      | 714 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 464 ms: 1.13x faster                                                    |
| async_tree_io_tg           | 829 ms                                                      | 740 ms: 1.12x faster                                                    |
| Geometric mean             | (ref)                                                       | 1.17x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 57.3 ms: 1.23x faster                                                   |
| float          | 54.4 ms                                                     | 48.3 ms: 1.13x faster                                                   |
| pidigits       | 150 ms                                                      | 149 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                       | 1.12x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 82.3 ms: 1.11x faster                                                   |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                   |
| regex_dna      | 116 ms                                                      | 125 ms: 1.08x slower                                                    |
| regex_v8       | 14.2 ms                                                     | 17.2 ms: 1.22x slower                                                   |
| Geometric mean | (ref)                                                       | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.48 ms: 1.48x faster                                                   |
| unpickle_pure_python | 157 us                                                      | 125 us: 1.26x faster                                                    |
| tomli_loads          | 1.46 sec                                                    | 1.19 sec: 1.23x faster                                                  |
| pickle_pure_python   | 208 us                                                      | 174 us: 1.20x faster                                                    |
| pickle_dict          | 18.5 us                                                     | 17.5 us: 1.06x faster                                                   |
| xml_etree_parse      | 97.6 ms                                                     | 93.7 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 65.6 ms                                                     | 63.1 ms: 1.04x faster                                                   |
| xml_etree_process    | 37.2 ms                                                     | 36.9 ms: 1.01x faster                                                   |
| xml_etree_generate   | 52.5 ms                                                     | 53.3 ms: 1.01x slower                                                   |
| pickle_list          | 2.70 us                                                     | 2.77 us: 1.03x slower                                                   |
| json_loads           | 13.0 us                                                     | 13.6 us: 1.04x slower                                                   |
| unpickle_list        | 2.59 us                                                     | 2.76 us: 1.07x slower                                                   |
| pickle               | 6.64 us                                                     | 7.25 us: 1.09x slower                                                   |
| unpickle             | 7.57 us                                                     | 8.57 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 23.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 16.8 ms                                                     | 21.0 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.52 ms: 1.37x faster                                                   |
| genshi_text     | 18.4 ms                                                     | 15.6 ms: 1.18x faster                                                   |
| genshi_xml      | 39.9 ms                                                     | 34.6 ms: 1.15x faster                                                   |
| django_template | 24.4 ms                                                     | 21.8 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf1-amd64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 68.2 us: 4.78x faster                                                   |
| generators                 | 34.0 ms                                                     | 19.7 ms: 1.73x faster                                                   |
| pylint                     | 323 ms                                                      | 207 ms: 1.56x faster                                                    |
| asyncio_tcp                | 726 ms                                                      | 472 ms: 1.54x faster                                                    |
| comprehensions             | 15.6 us                                                     | 10.4 us: 1.51x faster                                                   |
| json_dumps                 | 8.09 ms                                                     | 5.48 ms: 1.48x faster                                                   |
| mako                       | 7.58 ms                                                     | 5.52 ms: 1.37x faster                                                   |
| logging_silent             | 71.8 ns                                                     | 53.2 ns: 1.35x faster                                                   |
| deltablue                  | 2.70 ms                                                     | 2.00 ms: 1.35x faster                                                   |
| spectral_norm              | 68.3 ms                                                     | 51.5 ms: 1.33x faster                                                   |
| async_tree_none            | 332 ms                                                      | 262 ms: 1.27x faster                                                    |
| richards_super             | 38.7 ms                                                     | 30.6 ms: 1.27x faster                                                   |
| unpickle_pure_python       | 157 us                                                      | 125 us: 1.26x faster                                                    |
| sqlglot_parse              | 953 us                                                      | 761 us: 1.25x faster                                                    |
| nbody                      | 70.3 ms                                                     | 57.3 ms: 1.23x faster                                                   |
| tomli_loads                | 1.46 sec                                                    | 1.19 sec: 1.23x faster                                                  |
| chaos                      | 48.4 ms                                                     | 39.8 ms: 1.22x faster                                                   |
| pickle_pure_python         | 208 us                                                      | 174 us: 1.20x faster                                                    |
| deepcopy_memo              | 26.0 us                                                     | 21.6 us: 1.20x faster                                                   |
| raytrace                   | 213 ms                                                      | 178 ms: 1.20x faster                                                    |
| fannkuch                   | 253 ms                                                      | 212 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 405 ms                                                      | 339 ms: 1.19x faster                                                    |
| async_tree_memoization     | 399 ms                                                      | 336 ms: 1.19x faster                                                    |
| sqlglot_transpile          | 1.16 ms                                                     | 981 us: 1.19x faster                                                    |
| genshi_text                | 18.4 ms                                                     | 15.6 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 451 ms: 1.18x faster                                                    |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.73 sec: 1.17x faster                                                  |
| sympy_sum                  | 100 ms                                                      | 85.7 ms: 1.17x faster                                                   |
| logging_simple             | 6.86 us                                                     | 5.89 us: 1.16x faster                                                   |
| coroutines                 | 15.0 ms                                                     | 12.9 ms: 1.16x faster                                                   |
| genshi_xml                 | 39.9 ms                                                     | 34.6 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.24 ms: 1.15x faster                                                   |
| async_tree_none_tg         | 309 ms                                                      | 268 ms: 1.15x faster                                                    |
| richards                   | 31.4 ms                                                     | 27.4 ms: 1.15x faster                                                   |
| pprint_pformat             | 1.09 sec                                                    | 948 ms: 1.15x faster                                                    |
| sympy_str                  | 185 ms                                                      | 162 ms: 1.14x faster                                                    |
| nqueens                    | 68.3 ms                                                     | 60.3 ms: 1.13x faster                                                   |
| pprint_safe_repr           | 529 ms                                                      | 467 ms: 1.13x faster                                                    |
| logging_format             | 7.16 us                                                     | 6.33 us: 1.13x faster                                                   |
| async_tree_io              | 808 ms                                                      | 714 ms: 1.13x faster                                                    |
| scimark_monte_carlo        | 45.3 ms                                                     | 40.1 ms: 1.13x faster                                                   |
| sqlite_synth               | 1.77 us                                                     | 1.57 us: 1.13x faster                                                   |
| pyflate                    | 312 ms                                                      | 277 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 464 ms: 1.13x faster                                                    |
| deepcopy                   | 246 us                                                      | 219 us: 1.13x faster                                                    |
| float                      | 54.4 ms                                                     | 48.3 ms: 1.13x faster                                                   |
| crypto_pyaes               | 48.9 ms                                                     | 43.5 ms: 1.12x faster                                                   |
| async_tree_io_tg           | 829 ms                                                      | 740 ms: 1.12x faster                                                    |
| django_template            | 24.4 ms                                                     | 21.8 ms: 1.12x faster                                                   |
| chameleon                  | 5.26 ms                                                     | 4.71 ms: 1.12x faster                                                   |
| dulwich_log                | 46.4 ms                                                     | 41.6 ms: 1.11x faster                                                   |
| regex_compile              | 91.0 ms                                                     | 82.3 ms: 1.11x faster                                                   |
| tornado_http               | 92.8 ms                                                     | 83.9 ms: 1.11x faster                                                   |
| sqlglot_normalize          | 190 ms                                                      | 172 ms: 1.10x faster                                                    |
| sympy_integrate            | 14.0 ms                                                     | 12.9 ms: 1.09x faster                                                   |
| html5lib                   | 38.9 ms                                                     | 36.0 ms: 1.08x faster                                                   |
| pycparser                  | 720 ms                                                      | 669 ms: 1.08x faster                                                    |
| go                         | 101 ms                                                      | 94.1 ms: 1.07x faster                                                   |
| sympy_expand               | 299 ms                                                      | 278 ms: 1.07x faster                                                    |
| mdp                        | 1.59 sec                                                    | 1.49 sec: 1.07x faster                                                  |
| deepcopy_reduce            | 2.06 us                                                     | 1.94 us: 1.06x faster                                                   |
| scimark_fft                | 179 ms                                                      | 169 ms: 1.06x faster                                                    |
| hexiom                     | 4.55 ms                                                     | 4.29 ms: 1.06x faster                                                   |
| pickle_dict                | 18.5 us                                                     | 17.5 us: 1.06x faster                                                   |
| mypy2                      | 459 ms                                                      | 435 ms: 1.06x faster                                                    |
| bench_thread_pool          | 872 us                                                      | 837 us: 1.04x faster                                                    |
| xml_etree_parse            | 97.6 ms                                                     | 93.7 ms: 1.04x faster                                                   |
| docutils                   | 1.64 sec                                                    | 1.58 sec: 1.04x faster                                                  |
| xml_etree_iterparse        | 65.6 ms                                                     | 63.1 ms: 1.04x faster                                                   |
| meteor_contest             | 75.2 ms                                                     | 72.7 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 34.5 ms                                                     | 33.9 ms: 1.02x faster                                                   |
| xml_etree_process          | 37.2 ms                                                     | 36.9 ms: 1.01x faster                                                   |
| pidigits                   | 150 ms                                                      | 149 ms: 1.00x faster                                                    |
| xml_etree_generate         | 52.5 ms                                                     | 53.3 ms: 1.01x slower                                                   |
| aiohttp                    | 883 us                                                      | 897 us: 1.02x slower                                                    |
| gc_traversal               | 1.49 ms                                                     | 1.53 ms: 1.02x slower                                                   |
| pickle_list                | 2.70 us                                                     | 2.77 us: 1.03x slower                                                   |
| 2to3                       | 214 ms                                                      | 220 ms: 1.03x slower                                                    |
| scimark_sor                | 78.1 ms                                                     | 81.0 ms: 1.04x slower                                                   |
| json_loads                 | 13.0 us                                                     | 13.6 us: 1.04x slower                                                   |
| unpack_sequence            | 46.9 ns                                                     | 49.1 ns: 1.05x slower                                                   |
| create_gc_cycles           | 713 us                                                      | 748 us: 1.05x slower                                                    |
| unpickle_list              | 2.59 us                                                     | 2.76 us: 1.07x slower                                                   |
| regex_effbot               | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                   |
| regex_dna                  | 116 ms                                                      | 125 ms: 1.08x slower                                                    |
| pathlib                    | 70.9 ms                                                     | 76.6 ms: 1.08x slower                                                   |
| coverage                   | 43.4 ms                                                     | 47.3 ms: 1.09x slower                                                   |
| bench_mp_pool              | 63.2 ms                                                     | 69.0 ms: 1.09x slower                                                   |
| pickle                     | 6.64 us                                                     | 7.25 us: 1.09x slower                                                   |
| unpickle                   | 7.57 us                                                     | 8.57 us: 1.13x slower                                                   |
| scimark_lu                 | 62.8 ms                                                     | 72.2 ms: 1.15x slower                                                   |
| telco                      | 4.06 ms                                                     | 4.70 ms: 1.16x slower                                                   |
| python_startup             | 19.8 ms                                                     | 23.1 ms: 1.17x slower                                                   |
| regex_v8                   | 14.2 ms                                                     | 17.2 ms: 1.22x slower                                                   |
| python_startup_no_site     | 16.8 ms                                                     | 21.0 ms: 1.25x slower                                                   |
| async_generators           | 177 ms                                                      | 236 ms: 1.34x slower                                                    |
| thrift                     | 494 us                                                      | 9.08 ms: 18.38x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                            |

Benchmark hidden because not significant (1): json
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x


# Memory

- memory change: unknown