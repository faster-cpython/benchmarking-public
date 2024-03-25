# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-amd64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 210 ms: 1.04x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 83.2 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 563 ms: 1.37x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 271 ms: 1.35x faster                                                        |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.29x faster                                                        |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 52.7 ms: 1.08x faster                                                       |
| nbody          | 71.9 ms                                                     | 68.6 ms: 1.05x faster                                                       |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 76.8 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.3 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 179 us: 1.09x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.61 ms: 1.01x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| pickle_list          | 2.83 us                                                     | 2.84 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.39 us: 1.02x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 19.0 us: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (2): json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| python_startup_no_site | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| django_template | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 208 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 563 ms: 1.37x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 271 ms: 1.35x faster                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 70.7 us: 1.35x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                       |
| async_tree_none            | 291 ms                                                      | 221 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.29x faster                                                        |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| raytrace                   | 192 ms                                                      | 163 ms: 1.18x faster                                                        |
| mypy2                      | 509 ms                                                      | 436 ms: 1.17x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.81 sec: 1.16x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 76.8 ms: 1.14x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.23 ms: 1.14x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.9 ms: 1.12x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 43.2 ms: 1.12x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                       |
| sympy_str                  | 175 ms                                                      | 159 ms: 1.10x faster                                                        |
| sympy_sum                  | 91.5 ms                                                     | 83.5 ms: 1.10x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 61.2 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.61 us: 1.09x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 179 us: 1.09x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.4 ns: 1.09x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.6 ms: 1.09x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.98 ms: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 63.6 ms: 1.09x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.78 ms: 1.09x faster                                                       |
| go                         | 91.6 ms                                                     | 84.5 ms: 1.08x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.4 ms: 1.08x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.9 us: 1.08x faster                                                       |
| float                      | 56.8 ms                                                     | 52.7 ms: 1.08x faster                                                       |
| scimark_fft                | 184 ms                                                      | 171 ms: 1.08x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 83.2 ms: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.40 ms: 1.06x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 807 us: 1.06x faster                                                        |
| django_template            | 22.9 ms                                                     | 21.7 ms: 1.06x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 761 us: 1.06x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                                       |
| pycparser                  | 699 ms                                                      | 663 ms: 1.05x faster                                                        |
| async_generators           | 239 ms                                                      | 227 ms: 1.05x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 972 us: 1.05x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 489 ms: 1.05x faster                                                        |
| create_gc_cycles           | 752 us                                                      | 717 us: 1.05x faster                                                        |
| nbody                      | 71.9 ms                                                     | 68.6 ms: 1.05x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.3 ms: 1.05x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 465 ms: 1.05x faster                                                        |
| deepcopy                   | 238 us                                                      | 227 us: 1.05x faster                                                        |
| sqlglot_normalize          | 187 ms                                                      | 179 ms: 1.05x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 1.00 sec: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.92 ms: 1.04x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 77.2 ms: 1.04x faster                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.46 ms: 1.04x faster                                                       |
| 2to3                       | 218 ms                                                      | 210 ms: 1.04x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                       |
| pyflate                    | 295 ms                                                      | 284 ms: 1.04x faster                                                        |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                        |
| sympy_expand               | 284 ms                                                      | 274 ms: 1.03x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.49 us: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.3 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.14 us: 1.02x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.8 ms: 1.02x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.69 us: 1.02x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.06 us: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.61 ms: 1.01x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 77.7 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                        |
| generators                 | 22.5 ms                                                     | 22.4 ms: 1.01x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.3 ms: 1.00x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.84 us: 1.01x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.39 us: 1.02x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.0 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 18.7 ms: 1.15x slower                                                       |
| coverage                   | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.75 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (4): unpack_sequence, json_loads, aiohttp, pickle
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-pythonperf1-amd64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x


# Memory

- memory change: unknown