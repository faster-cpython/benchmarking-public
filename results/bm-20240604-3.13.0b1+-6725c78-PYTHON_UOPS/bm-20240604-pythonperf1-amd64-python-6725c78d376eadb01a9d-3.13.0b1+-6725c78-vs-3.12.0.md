# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-amd64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.05x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 236 ms: 1.08x slower                                                        |
| chameleon      | 4.98 ms                                                     | 5.40 ms: 1.08x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.86 sec: 1.12x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 87.8 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 277 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.31x faster                                                        |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 632 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 602 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 293 ms: 1.16x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| nbody          | 71.9 ms                                                     | 80.1 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 110 ms: 1.26x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                       |
| pickle               | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.89 us: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.44 us: 1.03x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.54 sec: 1.13x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 228 us: 1.16x slower                                                        |
| unpickle_pure_python | 133 us                                                      | 169 us: 1.27x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.78 ms: 1.10x slower                                                       |
| django_template | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.50 sec: 1.40x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 277 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 218 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.31x faster                                                        |
| async_tree_none            | 291 ms                                                      | 234 ms: 1.25x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 632 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 402 ms: 1.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 602 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 293 ms: 1.16x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.7 ms: 1.14x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.7 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.7 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.05x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 89.8 ms: 1.04x faster                                                       |
| raytrace                   | 192 ms                                                      | 186 ms: 1.03x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.19 us: 1.03x faster                                                       |
| json                       | 3.05 ms                                                     | 2.95 ms: 1.03x faster                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 67.0 ms: 1.03x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 87.8 ms: 1.02x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 841 us: 1.02x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.60 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.24 us: 1.01x faster                                                       |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                        |
| dulwich_log                | 44.3 ms                                                     | 44.7 ms: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.89 us: 1.02x slower                                                       |
| comprehensions             | 14.1 us                                                     | 14.4 us: 1.02x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.84 us: 1.03x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.44 us: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.58 ms: 1.04x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.90 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 67.6 ms: 1.04x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| chaos                      | 43.3 ms                                                     | 45.5 ms: 1.05x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 78.4 ms: 1.05x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.5 ms: 1.05x slower                                                       |
| aiohttp                    | 884 us                                                      | 937 us: 1.06x slower                                                        |
| richards_super             | 32.1 ms                                                     | 34.1 ms: 1.06x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.2 ms: 1.07x slower                                                       |
| richards                   | 28.4 ms                                                     | 30.4 ms: 1.07x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.48 sec: 1.08x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.26 us: 1.08x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 15.4 ms: 1.08x slower                                                       |
| 2to3                       | 218 ms                                                      | 236 ms: 1.08x slower                                                        |
| chameleon                  | 4.98 ms                                                     | 5.40 ms: 1.08x slower                                                       |
| coverage                   | 40.8 ms                                                     | 44.4 ms: 1.09x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 99.8 ms: 1.09x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 53.0 ms: 1.09x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.78 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 567 ms: 1.10x slower                                                        |
| deepcopy                   | 238 us                                                      | 263 us: 1.11x slower                                                        |
| nqueens                    | 62.8 ms                                                     | 69.7 ms: 1.11x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.16 sec: 1.11x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.6 ms: 1.11x slower                                                       |
| nbody                      | 71.9 ms                                                     | 80.1 ms: 1.11x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.86 sec: 1.12x slower                                                      |
| sympy_str                  | 175 ms                                                      | 197 ms: 1.13x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 38.9 ms: 1.13x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.54 sec: 1.13x slower                                                      |
| go                         | 91.6 ms                                                     | 104 ms: 1.13x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.16 ms: 1.14x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.8 ms: 1.14x slower                                                       |
| scimark_fft                | 184 ms                                                      | 212 ms: 1.15x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 926 us: 1.15x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 90.8 ms: 1.15x slower                                                       |
| fannkuch                   | 247 ms                                                      | 285 ms: 1.15x slower                                                        |
| spectral_norm              | 66.9 ms                                                     | 77.8 ms: 1.16x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 228 us: 1.16x slower                                                        |
| pyflate                    | 295 ms                                                      | 345 ms: 1.17x slower                                                        |
| sympy_expand               | 284 ms                                                      | 336 ms: 1.18x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.98 ms: 1.21x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 915 us: 1.22x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 53.5 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.22x slower                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.20 ms: 1.25x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.71 ms: 1.25x slower                                                       |
| pycparser                  | 699 ms                                                      | 876 ms: 1.25x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 110 ms: 1.26x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 76.2 ns: 1.26x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 169 us: 1.27x slower                                                        |
| deepcopy_memo              | 23.7 us                                                     | 31.9 us: 1.35x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.66 ms: 1.38x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 81.9 ms: 1.39x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                |

Benchmark hidden because not significant (4): mypy2, asyncio_tcp, float, python_startup_no_site
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf1-amd64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown