# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-amd64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.14x slower
- HPT reliability: 65.23%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 214 ms                                                      | 234 ms: 1.10x slower                                                      |
| chameleon      | 5.26 ms                                                     | 4.73 ms: 1.11x faster                                                     |
| docutils       | 1.64 sec                                                    | 2.45 sec: 1.49x slower                                                    |
| html5lib       | 38.9 ms                                                     | 40.4 ms: 1.04x slower                                                     |
| tornado_http   | 92.8 ms                                                     | 86.4 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                       | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 530 ms                                                      | 2.23 sec: 4.21x slower                                                    |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 2.43 sec: 4.65x slower                                                    |
| async_tree_none            | 332 ms                                                      | 1.78 sec: 5.37x slower                                                    |
| async_tree_memoization     | 399 ms                                                      | 2.29 sec: 5.74x slower                                                    |
| async_tree_memoization_tg  | 405 ms                                                      | 2.51 sec: 6.19x slower                                                    |
| async_tree_none_tg         | 309 ms                                                      | 1.96 sec: 6.36x slower                                                    |
| async_tree_io              | 808 ms                                                      | 7.14 sec: 8.85x slower                                                    |
| async_tree_io_tg           | 829 ms                                                      | 7.69 sec: 9.28x slower                                                    |
| Geometric mean             | (ref)                                                       | 6.11x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 70.3 ms                                                     | 54.9 ms: 1.28x faster                                                     |
| pidigits       | 150 ms                                                      | 147 ms: 1.02x faster                                                      |
| float          | 54.4 ms                                                     | 80.3 ms: 1.48x slower                                                     |
| Geometric mean | (ref)                                                       | 1.04x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 91.0 ms                                                     | 83.6 ms: 1.09x faster                                                     |
| regex_dna      | 116 ms                                                      | 120 ms: 1.04x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.05x slower                                                     |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 8.09 ms                                                     | 5.56 ms: 1.46x faster                                                     |
| unpickle_pure_python | 157 us                                                      | 126 us: 1.25x faster                                                      |
| tomli_loads          | 1.46 sec                                                    | 1.21 sec: 1.20x faster                                                    |
| pickle_pure_python   | 208 us                                                      | 180 us: 1.16x faster                                                      |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                                     |
| unpickle_list        | 2.59 us                                                     | 2.74 us: 1.06x slower                                                     |
| json_loads           | 13.0 us                                                     | 13.8 us: 1.06x slower                                                     |
| pickle               | 6.64 us                                                     | 7.13 us: 1.07x slower                                                     |
| pickle_list          | 2.70 us                                                     | 2.90 us: 1.08x slower                                                     |
| unpickle             | 7.57 us                                                     | 8.38 us: 1.11x slower                                                     |
| xml_etree_process    | 37.2 ms                                                     | 41.2 ms: 1.11x slower                                                     |
| xml_etree_generate   | 52.5 ms                                                     | 59.9 ms: 1.14x slower                                                     |
| xml_etree_parse      | 97.6 ms                                                     | 124 ms: 1.27x slower                                                      |
| xml_etree_iterparse  | 65.6 ms                                                     | 93.1 ms: 1.42x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.8 ms                                                     | 23.4 ms: 1.18x slower                                                     |
| python_startup_no_site | 16.8 ms                                                     | 20.9 ms: 1.24x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.58 ms                                                     | 5.23 ms: 1.45x faster                                                     |
| genshi_text     | 18.4 ms                                                     | 15.7 ms: 1.17x faster                                                     |
| django_template | 24.4 ms                                                     | 22.5 ms: 1.09x faster                                                     |
| genshi_xml      | 39.9 ms                                                     | 38.0 ms: 1.05x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 326 us                                                      | 71.9 us: 4.53x faster                                                     |
| generators                 | 34.0 ms                                                     | 20.2 ms: 1.68x faster                                                     |
| asyncio_tcp                | 726 ms                                                      | 472 ms: 1.54x faster                                                      |
| spectral_norm              | 68.3 ms                                                     | 45.5 ms: 1.50x faster                                                     |
| comprehensions             | 15.6 us                                                     | 10.7 us: 1.46x faster                                                     |
| json_dumps                 | 8.09 ms                                                     | 5.56 ms: 1.46x faster                                                     |
| mako                       | 7.58 ms                                                     | 5.23 ms: 1.45x faster                                                     |
| logging_silent             | 71.8 ns                                                     | 55.7 ns: 1.29x faster                                                     |
| nbody                      | 70.3 ms                                                     | 54.9 ms: 1.28x faster                                                     |
| deltablue                  | 2.70 ms                                                     | 2.16 ms: 1.25x faster                                                     |
| unpickle_pure_python       | 157 us                                                      | 126 us: 1.25x faster                                                      |
| chaos                      | 48.4 ms                                                     | 39.2 ms: 1.23x faster                                                     |
| fannkuch                   | 253 ms                                                      | 205 ms: 1.23x faster                                                      |
| asyncio_tcp_ssl            | 2.03 sec                                                    | 1.67 sec: 1.22x faster                                                    |
| tomli_loads                | 1.46 sec                                                    | 1.21 sec: 1.20x faster                                                    |
| scimark_sparse_mat_mult    | 2.58 ms                                                     | 2.16 ms: 1.19x faster                                                     |
| scimark_monte_carlo        | 45.3 ms                                                     | 38.0 ms: 1.19x faster                                                     |
| richards_super             | 38.7 ms                                                     | 32.5 ms: 1.19x faster                                                     |
| logging_simple             | 6.86 us                                                     | 5.84 us: 1.18x faster                                                     |
| genshi_text                | 18.4 ms                                                     | 15.7 ms: 1.17x faster                                                     |
| pyflate                    | 312 ms                                                      | 266 ms: 1.17x faster                                                      |
| crypto_pyaes               | 48.9 ms                                                     | 42.0 ms: 1.16x faster                                                     |
| pickle_pure_python         | 208 us                                                      | 180 us: 1.16x faster                                                      |
| raytrace                   | 213 ms                                                      | 184 ms: 1.16x faster                                                      |
| deepcopy_memo              | 26.0 us                                                     | 22.5 us: 1.15x faster                                                     |
| pprint_pformat             | 1.09 sec                                                    | 944 ms: 1.15x faster                                                      |
| pprint_safe_repr           | 529 ms                                                      | 462 ms: 1.15x faster                                                      |
| scimark_fft                | 179 ms                                                      | 157 ms: 1.14x faster                                                      |
| sympy_sum                  | 100 ms                                                      | 88.1 ms: 1.14x faster                                                     |
| sqlite_synth               | 1.77 us                                                     | 1.56 us: 1.14x faster                                                     |
| dulwich_log                | 46.4 ms                                                     | 41.0 ms: 1.13x faster                                                     |
| logging_format             | 7.16 us                                                     | 6.34 us: 1.13x faster                                                     |
| nqueens                    | 68.3 ms                                                     | 60.6 ms: 1.13x faster                                                     |
| sqlglot_parse              | 953 us                                                      | 846 us: 1.13x faster                                                      |
| chameleon                  | 5.26 ms                                                     | 4.73 ms: 1.11x faster                                                     |
| coroutines                 | 15.0 ms                                                     | 13.5 ms: 1.11x faster                                                     |
| sympy_str                  | 185 ms                                                      | 167 ms: 1.11x faster                                                      |
| mdp                        | 1.59 sec                                                    | 1.45 sec: 1.10x faster                                                    |
| regex_compile              | 91.0 ms                                                     | 83.6 ms: 1.09x faster                                                     |
| django_template            | 24.4 ms                                                     | 22.5 ms: 1.09x faster                                                     |
| gc_traversal               | 1.49 ms                                                     | 1.37 ms: 1.09x faster                                                     |
| sqlglot_transpile          | 1.16 ms                                                     | 1.07 ms: 1.09x faster                                                     |
| deepcopy                   | 246 us                                                      | 228 us: 1.08x faster                                                      |
| richards                   | 31.4 ms                                                     | 29.1 ms: 1.08x faster                                                     |
| tornado_http               | 92.8 ms                                                     | 86.4 ms: 1.07x faster                                                     |
| sympy_integrate            | 14.0 ms                                                     | 13.1 ms: 1.07x faster                                                     |
| hexiom                     | 4.55 ms                                                     | 4.28 ms: 1.06x faster                                                     |
| genshi_xml                 | 39.9 ms                                                     | 38.0 ms: 1.05x faster                                                     |
| bench_thread_pool          | 872 us                                                      | 832 us: 1.05x faster                                                      |
| deepcopy_reduce            | 2.06 us                                                     | 1.98 us: 1.04x faster                                                     |
| sqlglot_normalize          | 190 ms                                                      | 184 ms: 1.03x faster                                                      |
| sympy_expand               | 299 ms                                                      | 291 ms: 1.03x faster                                                      |
| meteor_contest             | 75.2 ms                                                     | 73.3 ms: 1.03x faster                                                     |
| pidigits                   | 150 ms                                                      | 147 ms: 1.02x faster                                                      |
| go                         | 101 ms                                                      | 99.1 ms: 1.02x faster                                                     |
| pickle_dict                | 18.5 us                                                     | 18.2 us: 1.02x faster                                                     |
| regex_dna                  | 116 ms                                                      | 120 ms: 1.04x slower                                                      |
| html5lib                   | 38.9 ms                                                     | 40.4 ms: 1.04x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.05x slower                                                     |
| regex_effbot               | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                     |
| create_gc_cycles           | 713 us                                                      | 750 us: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.05x slower                                                     |
| aiohttp                    | 883 us                                                      | 932 us: 1.06x slower                                                      |
| unpickle_list              | 2.59 us                                                     | 2.74 us: 1.06x slower                                                     |
| json_loads                 | 13.0 us                                                     | 13.8 us: 1.06x slower                                                     |
| scimark_sor                | 78.1 ms                                                     | 83.2 ms: 1.07x slower                                                     |
| coverage                   | 43.4 ms                                                     | 46.6 ms: 1.07x slower                                                     |
| pickle                     | 6.64 us                                                     | 7.13 us: 1.07x slower                                                     |
| pickle_list                | 2.70 us                                                     | 2.90 us: 1.08x slower                                                     |
| pathlib                    | 70.9 ms                                                     | 77.1 ms: 1.09x slower                                                     |
| 2to3                       | 214 ms                                                      | 234 ms: 1.10x slower                                                      |
| mypy2                      | 459 ms                                                      | 505 ms: 1.10x slower                                                      |
| scimark_lu                 | 62.8 ms                                                     | 69.2 ms: 1.10x slower                                                     |
| unpickle                   | 7.57 us                                                     | 8.38 us: 1.11x slower                                                     |
| xml_etree_process          | 37.2 ms                                                     | 41.2 ms: 1.11x slower                                                     |
| bench_mp_pool              | 63.2 ms                                                     | 71.3 ms: 1.13x slower                                                     |
| xml_etree_generate         | 52.5 ms                                                     | 59.9 ms: 1.14x slower                                                     |
| pycparser                  | 720 ms                                                      | 829 ms: 1.15x slower                                                      |
| telco                      | 4.06 ms                                                     | 4.75 ms: 1.17x slower                                                     |
| python_startup             | 19.8 ms                                                     | 23.4 ms: 1.18x slower                                                     |
| python_startup_no_site     | 16.8 ms                                                     | 20.9 ms: 1.24x slower                                                     |
| xml_etree_parse            | 97.6 ms                                                     | 124 ms: 1.27x slower                                                      |
| unpack_sequence            | 46.9 ns                                                     | 66.6 ns: 1.42x slower                                                     |
| xml_etree_iterparse        | 65.6 ms                                                     | 93.1 ms: 1.42x slower                                                     |
| float                      | 54.4 ms                                                     | 80.3 ms: 1.48x slower                                                     |
| docutils                   | 1.64 sec                                                    | 2.45 sec: 1.49x slower                                                    |
| async_generators           | 177 ms                                                      | 291 ms: 1.64x slower                                                      |
| pylint                     | 323 ms                                                      | 577 ms: 1.78x slower                                                      |
| async_tree_cpu_io_mixed    | 530 ms                                                      | 2.23 sec: 4.21x slower                                                    |
| async_tree_cpu_io_mixed_tg | 523 ms                                                      | 2.43 sec: 4.65x slower                                                    |
| async_tree_none            | 332 ms                                                      | 1.78 sec: 5.37x slower                                                    |
| async_tree_memoization     | 399 ms                                                      | 2.29 sec: 5.74x slower                                                    |
| async_tree_memoization_tg  | 405 ms                                                      | 2.51 sec: 6.19x slower                                                    |
| async_tree_none_tg         | 309 ms                                                      | 1.96 sec: 6.36x slower                                                    |
| async_tree_io              | 808 ms                                                      | 7.14 sec: 8.85x slower                                                    |
| async_tree_io_tg           | 829 ms                                                      | 7.69 sec: 9.28x slower                                                    |
| thrift                     | 494 us                                                      | 8.98 ms: 18.18x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.14x slower                                                              |

Benchmark hidden because not significant (1): json
Ignored benchmarks (4) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 65.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown