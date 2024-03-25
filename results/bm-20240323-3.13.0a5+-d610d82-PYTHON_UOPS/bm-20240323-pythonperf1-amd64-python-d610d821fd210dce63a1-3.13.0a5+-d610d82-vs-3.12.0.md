# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.01x slower
- HPT reliability: 97.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 87.1 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 564 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 274 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| nbody          | 71.9 ms                                                     | 79.6 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 103 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 180 us: 1.09x faster                                                        |
| pickle               | 7.43 us                                                     | 7.12 us: 1.04x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.64 us: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.63 ms: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.12 us: 1.10x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 160 us: 1.20x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 23.5 ms: 1.02x slower                                                       |
| mako            | 7.09 ms                                                     | 7.39 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 564 ms: 1.37x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 210 ms: 1.36x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 274 ms: 1.34x faster                                                        |
| async_tree_none            | 291 ms                                                      | 222 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.62 sec: 1.29x faster                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 73.5 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 387 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 180 us: 1.09x faster                                                        |
| mypy2                      | 509 ms                                                      | 470 ms: 1.08x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 65.0 ms: 1.06x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 57.2 ns: 1.06x faster                                                       |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| comprehensions             | 14.1 us                                                     | 13.5 us: 1.05x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.12 us: 1.04x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.64 us: 1.04x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.01 us: 1.04x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.48 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                        |
| generators                 | 22.5 ms                                                     | 21.9 ms: 1.03x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 87.1 ms: 1.03x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 78.6 ms: 1.02x faster                                                       |
| deepcopy                   | 238 us                                                      | 234 us: 1.02x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.89 ms: 1.02x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 843 us: 1.02x faster                                                        |
| richards_super             | 32.1 ms                                                     | 31.7 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 55.1 ms: 1.01x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.63 ms: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 13.7 us: 1.01x faster                                                       |
| create_gc_cycles           | 752 us                                                      | 744 us: 1.01x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 23.5 us: 1.01x faster                                                       |
| richards                   | 28.4 ms                                                     | 28.2 ms: 1.01x faster                                                       |
| raytrace                   | 192 ms                                                      | 194 ms: 1.01x slower                                                        |
| xml_etree_process          | 37.7 ms                                                     | 38.1 ms: 1.01x slower                                                       |
| dulwich_log                | 44.3 ms                                                     | 44.8 ms: 1.01x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 75.6 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 522 ms: 1.02x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 191 ms: 1.02x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.86 us: 1.02x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.6 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.6 ms: 1.02x slower                                                       |
| django_template            | 22.9 ms                                                     | 23.5 ms: 1.02x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 824 us: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                     | 6.44 us: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                        |
| unpickle                   | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.05 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.08 sec: 1.03x slower                                                      |
| sympy_str                  | 175 ms                                                      | 181 ms: 1.03x slower                                                        |
| chaos                      | 43.3 ms                                                     | 45.0 ms: 1.04x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 95.2 ms: 1.04x slower                                                       |
| aiohttp                    | 884 us                                                      | 921 us: 1.04x slower                                                        |
| pycparser                  | 699 ms                                                      | 728 ms: 1.04x slower                                                        |
| mako                       | 7.09 ms                                                     | 7.39 ms: 1.04x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.0 ms: 1.05x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.9 ms: 1.08x slower                                                       |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.50 sec: 1.09x slower                                                      |
| go                         | 91.6 ms                                                     | 101 ms: 1.10x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.12 us: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.0 ms: 1.11x slower                                                       |
| nbody                      | 71.9 ms                                                     | 79.6 ms: 1.11x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 69.5 ms: 1.11x slower                                                       |
| fannkuch                   | 247 ms                                                      | 279 ms: 1.13x slower                                                        |
| coverage                   | 40.8 ms                                                     | 46.1 ms: 1.13x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 89.2 ms: 1.13x slower                                                       |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                        |
| pyflate                    | 295 ms                                                      | 339 ms: 1.15x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.2 ms: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.85 ms: 1.17x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 103 ms: 1.18x slower                                                        |
| unpack_sequence            | 37.5 ns                                                     | 44.9 ns: 1.20x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 160 us: 1.20x slower                                                        |
| spectral_norm              | 66.9 ms                                                     | 82.7 ms: 1.24x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.29 ms: 1.29x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.35 ms: 1.30x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 78.1 ms: 1.33x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (3): asyncio_tcp, pickle_dict, float
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-PYTHON_UOPS/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 97.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: unknown