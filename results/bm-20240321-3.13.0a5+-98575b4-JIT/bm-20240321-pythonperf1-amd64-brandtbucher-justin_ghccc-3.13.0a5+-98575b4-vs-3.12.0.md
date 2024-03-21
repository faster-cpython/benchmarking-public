# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: windows-amd64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.17x slower
- HPT reliability: 67.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.07x slower                                                      |
| chameleon      | 4.98 ms                                                     | 4.73 ms: 1.05x faster                                                     |
| docutils       | 1.66 sec                                                    | 2.45 sec: 1.47x slower                                                    |
| tornado_http   | 89.5 ms                                                     | 86.4 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                       | 1.10x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 489 ms                                                      | 2.23 sec: 4.56x slower                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 2.43 sec: 4.84x slower                                                    |
| async_tree_none            | 291 ms                                                      | 1.78 sec: 6.12x slower                                                    |
| async_tree_memoization     | 339 ms                                                      | 2.29 sec: 6.75x slower                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 2.51 sec: 6.83x slower                                                    |
| async_tree_none_tg         | 285 ms                                                      | 1.96 sec: 6.89x slower                                                    |
| async_tree_io              | 731 ms                                                      | 7.14 sec: 9.77x slower                                                    |
| async_tree_io_tg           | 771 ms                                                      | 7.69 sec: 9.97x slower                                                    |
| Geometric mean             | (ref)                                                       | 6.72x slower                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 54.9 ms: 1.31x faster                                                     |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                      |
| float          | 56.8 ms                                                     | 80.3 ms: 1.41x slower                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                     |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                     |
| regex_v8       | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                    |
| pickle_pure_python   | 195 us                                                      | 180 us: 1.09x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                      |
| pickle               | 7.43 us                                                     | 7.13 us: 1.04x faster                                                     |
| json_dumps           | 5.70 ms                                                     | 5.56 ms: 1.02x faster                                                     |
| pickle_dict          | 18.4 us                                                     | 18.2 us: 1.01x faster                                                     |
| json_loads           | 13.9 us                                                     | 13.8 us: 1.01x faster                                                     |
| unpickle             | 8.18 us                                                     | 8.38 us: 1.02x slower                                                     |
| pickle_list          | 2.83 us                                                     | 2.90 us: 1.03x slower                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 59.9 ms: 1.07x slower                                                     |
| xml_etree_process    | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                     |
| xml_etree_parse      | 93.0 ms                                                     | 124 ms: 1.33x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 93.1 ms: 1.43x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                     |
| python_startup_no_site | 16.2 ms                                                     | 20.9 ms: 1.28x slower                                                     |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.23 ms: 1.35x faster                                                     |
| django_template | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                                     |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 45.5 ms: 1.47x faster                                                     |
| mako                       | 7.09 ms                                                     | 5.23 ms: 1.35x faster                                                     |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                     |
| typing_runtime_protocols   | 95.1 us                                                     | 71.9 us: 1.32x faster                                                     |
| nbody                      | 71.9 ms                                                     | 54.9 ms: 1.31x faster                                                     |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.67 sec: 1.26x faster                                                    |
| fannkuch                   | 247 ms                                                      | 205 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.16 ms: 1.19x faster                                                     |
| scimark_fft                | 184 ms                                                      | 157 ms: 1.18x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 42.0 ms: 1.15x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.0 ms: 1.15x faster                                                     |
| sqlite_synth               | 1.76 us                                                     | 1.56 us: 1.13x faster                                                     |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                    |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.11x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 462 ms: 1.11x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.37 ms: 1.11x faster                                                     |
| pyflate                    | 295 ms                                                      | 266 ms: 1.11x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 944 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                     |
| pickle_pure_python         | 195 us                                                      | 180 us: 1.09x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 55.7 ns: 1.09x faster                                                     |
| dulwich_log                | 44.3 ms                                                     | 41.0 ms: 1.08x faster                                                     |
| logging_simple             | 6.28 us                                                     | 5.84 us: 1.08x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.34 us: 1.06x faster                                                     |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 22.5 us: 1.05x faster                                                     |
| chameleon                  | 4.98 ms                                                     | 4.73 ms: 1.05x faster                                                     |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                      |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 83.6 ms: 1.05x faster                                                     |
| raytrace                   | 192 ms                                                      | 184 ms: 1.05x faster                                                      |
| deepcopy                   | 238 us                                                      | 228 us: 1.04x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 77.1 ms: 1.04x faster                                                     |
| pickle                     | 7.43 us                                                     | 7.13 us: 1.04x faster                                                     |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.1 ms: 1.04x faster                                                     |
| nqueens                    | 62.8 ms                                                     | 60.6 ms: 1.04x faster                                                     |
| tornado_http               | 89.5 ms                                                     | 86.4 ms: 1.04x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 832 us: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                     |
| json_dumps                 | 5.70 ms                                                     | 5.56 ms: 1.02x faster                                                     |
| django_template            | 22.9 ms                                                     | 22.5 ms: 1.02x faster                                                     |
| meteor_contest             | 74.6 ms                                                     | 73.3 ms: 1.02x faster                                                     |
| sqlglot_normalize          | 187 ms                                                      | 184 ms: 1.02x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.2 us: 1.01x faster                                                     |
| json_loads                 | 13.9 us                                                     | 13.8 us: 1.01x faster                                                     |
| richards_super             | 32.1 ms                                                     | 32.5 ms: 1.01x slower                                                     |
| sympy_integrate            | 13.0 ms                                                     | 13.1 ms: 1.01x slower                                                     |
| unpickle                   | 8.18 us                                                     | 8.38 us: 1.02x slower                                                     |
| richards                   | 28.4 ms                                                     | 29.1 ms: 1.02x slower                                                     |
| sympy_expand               | 284 ms                                                      | 291 ms: 1.03x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.90 us: 1.03x slower                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 71.3 ms: 1.03x slower                                                     |
| regex_v8                   | 14.2 ms                                                     | 14.8 ms: 1.04x slower                                                     |
| hexiom                     | 4.10 ms                                                     | 4.28 ms: 1.04x slower                                                     |
| sqlglot_transpile          | 1.02 ms                                                     | 1.07 ms: 1.05x slower                                                     |
| sqlglot_parse              | 804 us                                                      | 846 us: 1.05x slower                                                      |
| aiohttp                    | 884 us                                                      | 932 us: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                    |
| sqlglot_optimize           | 34.5 ms                                                     | 36.4 ms: 1.06x slower                                                     |
| scimark_sor                | 78.8 ms                                                     | 83.2 ms: 1.06x slower                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 59.9 ms: 1.07x slower                                                     |
| 2to3                       | 218 ms                                                      | 234 ms: 1.07x slower                                                      |
| go                         | 91.6 ms                                                     | 99.1 ms: 1.08x slower                                                     |
| xml_etree_process          | 37.7 ms                                                     | 41.2 ms: 1.09x slower                                                     |
| coverage                   | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                     |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                                     |
| scimark_lu                 | 58.9 ms                                                     | 69.2 ms: 1.17x slower                                                     |
| pycparser                  | 699 ms                                                      | 829 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 23.4 ms: 1.20x slower                                                     |
| async_generators           | 239 ms                                                      | 291 ms: 1.21x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.9 ms: 1.28x slower                                                     |
| xml_etree_parse            | 93.0 ms                                                     | 124 ms: 1.33x slower                                                      |
| float                      | 56.8 ms                                                     | 80.3 ms: 1.41x slower                                                     |
| xml_etree_iterparse        | 65.2 ms                                                     | 93.1 ms: 1.43x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.45 sec: 1.47x slower                                                    |
| unpack_sequence            | 37.5 ns                                                     | 66.6 ns: 1.78x slower                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 2.23 sec: 4.56x slower                                                    |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 2.43 sec: 4.84x slower                                                    |
| async_tree_none            | 291 ms                                                      | 1.78 sec: 6.12x slower                                                    |
| async_tree_memoization     | 339 ms                                                      | 2.29 sec: 6.75x slower                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 2.51 sec: 6.83x slower                                                    |
| async_tree_none_tg         | 285 ms                                                      | 1.96 sec: 6.89x slower                                                    |
| async_tree_io              | 731 ms                                                      | 7.14 sec: 9.77x slower                                                    |
| async_tree_io_tg           | 771 ms                                                      | 7.69 sec: 9.97x slower                                                    |
| Geometric mean             | (ref)                                                       | 1.17x slower                                                              |

Benchmark hidden because not significant (5): json, mypy2, create_gc_cycles, unpickle_list, deltablue
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240321-3.13.0a5+-98575b4-JIT/bm-20240321-pythonperf1-amd64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 67.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown