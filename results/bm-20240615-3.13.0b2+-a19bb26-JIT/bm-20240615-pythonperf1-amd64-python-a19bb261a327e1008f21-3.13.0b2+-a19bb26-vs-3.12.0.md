# Results vs. 3.12.0

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.05x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| chameleon      | 4.98 ms                                                     | 4.95 ms: 1.01x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 85.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                        |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 397 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.4 ms: 1.40x faster                                                       |
| float          | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 22.7 ms: 1.60x slower                                                       |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.14x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 125 us: 1.06x faster                                                        |
| pickle_dict          | 18.4 us                                                     | 17.5 us: 1.05x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| pickle               | 7.43 us                                                     | 7.28 us: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.85 us: 1.04x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.98 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): json_dumps, json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                       |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                       |
| django_template | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 45.1 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.45 sec: 1.45x faster                                                      |
| nbody                      | 71.9 ms                                                     | 51.4 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.39x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.18 ms: 1.37x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 214 ms: 1.33x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 385 ms: 1.30x faster                                                        |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                       |
| async_tree_none            | 291 ms                                                      | 228 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 622 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 397 ms: 1.23x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 276 ms: 1.23x faster                                                        |
| scimark_fft                | 184 ms                                                      | 152 ms: 1.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 603 ms: 1.21x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.20x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.1 us: 1.18x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                       |
| pyflate                    | 295 ms                                                      | 259 ms: 1.14x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.14x faster                                                        |
| pprint_safe_repr           | 513 ms                                                      | 452 ms: 1.14x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.21 sec: 1.13x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 929 ms: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.12x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                       |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                        |
| fannkuch                   | 247 ms                                                      | 226 ms: 1.09x faster                                                        |
| logging_silent             | 60.5 ns                                                     | 55.6 ns: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 40.7 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.77 us: 1.09x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.19 us: 1.08x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 792 us: 1.08x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 125 us: 1.06x faster                                                        |
| pathlib                    | 80.5 ms                                                     | 76.0 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.05x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.5 us: 1.05x faster                                                       |
| json                       | 3.05 ms                                                     | 2.90 ms: 1.05x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 85.7 ms: 1.05x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                       |
| asyncio_tcp                | 487 ms                                                      | 471 ms: 1.04x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.28 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 91.7 ms: 1.01x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| chameleon                  | 4.98 ms                                                     | 4.95 ms: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.1 ms: 1.01x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.08 us: 1.01x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 809 us: 1.01x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 88.9 ms: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.2 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.04 ms: 1.02x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 93.6 ms: 1.02x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.1 ms: 1.02x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                       |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.85 us: 1.04x slower                                                       |
| async_generators           | 239 ms                                                      | 250 ms: 1.04x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 82.7 ms: 1.05x slower                                                       |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                        |
| aiohttp                    | 884 us                                                      | 932 us: 1.05x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.9 ms: 1.07x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.78 sec: 1.07x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.1 ms: 1.09x slower                                                       |
| coverage                   | 40.8 ms                                                     | 44.5 ms: 1.09x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.36 ms: 1.09x slower                                                       |
| pycparser                  | 699 ms                                                      | 764 ms: 1.09x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 17.8 ms: 1.09x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.98 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.56 ms: 1.10x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.4 ms: 1.11x slower                                                       |
| sympy_expand               | 284 ms                                                      | 316 ms: 1.11x slower                                                        |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.68 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 69.6 ms: 1.18x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 917 us: 1.22x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 22.7 ms: 1.60x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (6): bench_mp_pool, deepcopy, json_dumps, generators, json_loads, pickle_list
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240615-3.13.0b2+-a19bb26-JIT/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown