# Results vs. 3.12.0

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.00x slower
- HPT reliability: 95.99%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 222 ms: 1.02x slower                                                   |
| docutils       | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                 |
| tornado_http   | 89.5 ms                                                     | 84.1 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                       | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                                   |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                   |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                   |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.26x faster                                                   |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                   |
| nbody          | 71.9 ms                                                     | 81.8 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                       | 1.04x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                   |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| regex_compile  | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                  |
| regex_v8       | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                       | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                                  |
| unpickle_list        | 2.75 us                                                     | 2.72 us: 1.01x faster                                                  |
| xml_etree_parse      | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                  |
| pickle_dict          | 18.4 us                                                     | 18.7 us: 1.02x slower                                                  |
| json_loads           | 13.9 us                                                     | 14.6 us: 1.05x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                  |
| pickle_list          | 2.83 us                                                     | 2.99 us: 1.06x slower                                                  |
| xml_etree_process    | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                  |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.09x slower                                                   |
| json_dumps           | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                  |
| unpickle             | 8.18 us                                                     | 9.28 us: 1.13x slower                                                  |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                   |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.07x slower                                                  |
| python_startup         | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                  |
| django_template | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.45x faster                                                   |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                   |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                   |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.52 sec: 1.38x faster                                                 |
| async_tree_io_tg           | 771 ms                                                      | 560 ms: 1.38x faster                                                   |
| async_tree_memoization     | 339 ms                                                      | 259 ms: 1.31x faster                                                   |
| async_tree_io              | 731 ms                                                      | 566 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 395 ms: 1.27x faster                                                   |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                   |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 390 ms: 1.26x faster                                                   |
| comprehensions             | 14.1 us                                                     | 11.7 us: 1.21x faster                                                  |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                                  |
| pathlib                    | 80.5 ms                                                     | 73.5 ms: 1.10x faster                                                  |
| deepcopy_reduce            | 2.09 us                                                     | 1.92 us: 1.09x faster                                                  |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.08x faster                                                  |
| generators                 | 22.5 ms                                                     | 21.0 ms: 1.07x faster                                                  |
| tornado_http               | 89.5 ms                                                     | 84.1 ms: 1.06x faster                                                  |
| bench_thread_pool          | 857 us                                                      | 805 us: 1.06x faster                                                   |
| go                         | 91.6 ms                                                     | 87.3 ms: 1.05x faster                                                  |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                   |
| dulwich_log                | 44.3 ms                                                     | 42.6 ms: 1.04x faster                                                  |
| bench_mp_pool              | 69.2 ms                                                     | 66.6 ms: 1.04x faster                                                  |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                                  |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                   |
| mako                       | 7.09 ms                                                     | 6.89 ms: 1.03x faster                                                  |
| raytrace                   | 192 ms                                                      | 188 ms: 1.03x faster                                                   |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                  |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                  |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                   |
| unpickle_list              | 2.75 us                                                     | 2.72 us: 1.01x faster                                                  |
| crypto_pyaes               | 48.5 ms                                                     | 48.1 ms: 1.01x faster                                                  |
| xml_etree_parse            | 93.0 ms                                                     | 93.8 ms: 1.01x slower                                                  |
| chaos                      | 43.3 ms                                                     | 43.7 ms: 1.01x slower                                                  |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                  |
| pickle_dict                | 18.4 us                                                     | 18.7 us: 1.02x slower                                                  |
| logging_simple             | 6.28 us                                                     | 6.39 us: 1.02x slower                                                  |
| 2to3                       | 218 ms                                                      | 222 ms: 1.02x slower                                                   |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                   |
| sympy_integrate            | 13.0 ms                                                     | 13.2 ms: 1.02x slower                                                  |
| docutils                   | 1.66 sec                                                    | 1.70 sec: 1.02x slower                                                 |
| logging_format             | 6.72 us                                                     | 6.88 us: 1.02x slower                                                  |
| sqlglot_normalize          | 187 ms                                                      | 193 ms: 1.03x slower                                                   |
| spectral_norm              | 66.9 ms                                                     | 69.0 ms: 1.03x slower                                                  |
| logging_silent             | 60.5 ns                                                     | 62.6 ns: 1.04x slower                                                  |
| meteor_contest             | 74.6 ms                                                     | 77.9 ms: 1.04x slower                                                  |
| regex_compile              | 87.5 ms                                                     | 91.5 ms: 1.05x slower                                                  |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                  |
| json_loads                 | 13.9 us                                                     | 14.6 us: 1.05x slower                                                  |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                  |
| sqlglot_optimize           | 34.5 ms                                                     | 36.5 ms: 1.06x slower                                                  |
| pickle_list                | 2.83 us                                                     | 2.99 us: 1.06x slower                                                  |
| regex_v8                   | 14.2 ms                                                     | 15.1 ms: 1.06x slower                                                  |
| pprint_pformat             | 1.05 sec                                                    | 1.11 sec: 1.06x slower                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.72 ms: 1.06x slower                                                  |
| pprint_safe_repr           | 513 ms                                                      | 546 ms: 1.06x slower                                                   |
| hexiom                     | 4.10 ms                                                     | 4.39 ms: 1.07x slower                                                  |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.07x slower                                                  |
| scimark_lu                 | 58.9 ms                                                     | 63.6 ms: 1.08x slower                                                  |
| pyflate                    | 295 ms                                                      | 319 ms: 1.08x slower                                                   |
| xml_etree_process          | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                  |
| sympy_expand               | 284 ms                                                      | 307 ms: 1.08x slower                                                   |
| django_template            | 22.9 ms                                                     | 24.9 ms: 1.09x slower                                                  |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.09x slower                                                   |
| mdp                        | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.23 ms: 1.09x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                  |
| scimark_fft                | 184 ms                                                      | 203 ms: 1.10x slower                                                   |
| python_startup             | 19.5 ms                                                     | 21.4 ms: 1.10x slower                                                  |
| unpack_sequence            | 37.5 ns                                                     | 41.3 ns: 1.10x slower                                                  |
| sqlglot_parse              | 804 us                                                      | 900 us: 1.12x slower                                                   |
| scimark_sor                | 78.8 ms                                                     | 88.8 ms: 1.13x slower                                                  |
| richards_super             | 32.1 ms                                                     | 36.4 ms: 1.13x slower                                                  |
| unpickle                   | 8.18 us                                                     | 9.28 us: 1.13x slower                                                  |
| nbody                      | 71.9 ms                                                     | 81.8 ms: 1.14x slower                                                  |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.9 ms: 1.14x slower                                                  |
| richards                   | 28.4 ms                                                     | 32.4 ms: 1.14x slower                                                  |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                   |
| pycparser                  | 699 ms                                                      | 802 ms: 1.15x slower                                                   |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                  |
| typing_runtime_protocols   | 95.1 us                                                     | 111 us: 1.16x slower                                                   |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.17x slower                                                 |
| create_gc_cycles           | 752 us                                                      | 878 us: 1.17x slower                                                   |
| fannkuch                   | 247 ms                                                      | 292 ms: 1.18x slower                                                   |
| telco                      | 4.13 ms                                                     | 5.16 ms: 1.25x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                           |

Benchmark hidden because not significant (6): sympy_sum, float, async_generators, xml_etree_iterparse, gc_traversal, json
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 95.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown