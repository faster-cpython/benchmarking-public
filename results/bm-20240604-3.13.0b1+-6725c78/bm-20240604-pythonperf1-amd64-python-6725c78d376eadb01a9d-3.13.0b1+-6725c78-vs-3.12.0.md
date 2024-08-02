# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 82.3 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                        |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 611 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.2 ms: 1.13x faster                                                       |
| nbody          | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 178 us: 1.10x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.08x faster                                                        |
| unpickle_list        | 2.75 us                                                     | 2.59 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| pickle               | 7.43 us                                                     | 7.32 us: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.7 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.92 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): tomli_loads, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.40 ms: 1.11x faster                                                       |
| django_template | 22.9 ms                                                     | 21.2 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.43 sec: 1.46x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 203 ms: 1.40x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 611 ms: 1.26x faster                                                        |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                        |
| mypy2                      | 509 ms                                                      | 415 ms: 1.23x faster                                                        |
| raytrace                   | 192 ms                                                      | 161 ms: 1.20x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 38.5 ms: 1.15x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 53.0 ns: 1.14x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.90 ms: 1.14x faster                                                       |
| float                      | 56.8 ms                                                     | 50.2 ms: 1.13x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.4 ms: 1.13x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 55.9 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.2 ms: 1.12x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 53.0 ms: 1.11x faster                                                       |
| go                         | 91.6 ms                                                     | 82.7 ms: 1.11x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.40 ms: 1.11x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.70 us: 1.10x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 178 us: 1.10x faster                                                        |
| sympy_str                  | 175 ms                                                      | 159 ms: 1.10x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.13 us: 1.10x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 171 ms: 1.10x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 39.9 ms: 1.10x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.75 ms: 1.09x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 84.0 ms: 1.09x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 82.3 ms: 1.09x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.2 ms: 1.08x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.1 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.08x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 74.8 ms: 1.08x faster                                                       |
| deepcopy                   | 238 us                                                      | 222 us: 1.07x faster                                                        |
| bench_thread_pool          | 857 us                                                      | 798 us: 1.07x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.5 ms: 1.07x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 481 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 981 ms: 1.07x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 65.0 ms: 1.06x faster                                                       |
| scimark_fft                | 184 ms                                                      | 173 ms: 1.06x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 757 us: 1.06x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.97 us: 1.06x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.59 us: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.2 ms: 1.06x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 74.6 ms: 1.06x faster                                                       |
| pyflate                    | 295 ms                                                      | 279 ms: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 32.7 ms: 1.05x faster                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 970 us: 1.05x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.74 ms: 1.05x faster                                                       |
| sympy_expand               | 284 ms                                                      | 270 ms: 1.05x faster                                                        |
| async_generators           | 239 ms                                                      | 228 ms: 1.05x faster                                                        |
| 2to3                       | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| json                       | 3.05 ms                                                     | 2.91 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.45 ms: 1.04x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.31 sec: 1.04x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| nbody                      | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 31.0 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.9 us: 1.03x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                        |
| richards                   | 28.4 ms                                                     | 27.5 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.61 sec: 1.03x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.32 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 249 ms: 1.01x slower                                                        |
| aiohttp                    | 884 us                                                      | 894 us: 1.01x slower                                                        |
| pickle_dict                | 18.4 us                                                     | 18.7 us: 1.01x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.42 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.1 ms: 1.03x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.92 us: 1.03x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 101 us: 1.06x slower                                                        |
| coverage                   | 40.8 ms                                                     | 43.7 ms: 1.07x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.71 ms: 1.14x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 909 us: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (5): python_startup_no_site, tomli_loads, json_loads, json_dumps, pycparser
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown