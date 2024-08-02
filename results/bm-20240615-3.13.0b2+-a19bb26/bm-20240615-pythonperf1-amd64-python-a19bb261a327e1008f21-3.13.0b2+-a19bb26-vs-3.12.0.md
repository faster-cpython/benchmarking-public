# Results vs. 3.12.0

- fork: python
- ref: a19bb261a327e1008f21
- machine: windows-amd64
- commit hash: a19bb26
- commit date: 2024-06-15
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 615 ms: 1.25x faster                                                        |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.9 ms: 1.12x faster                                                       |
| nbody          | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                       |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.0 ms: 1.14x faster                                                       |
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.07x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.66 us: 1.03x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| pickle               | 7.43 us                                                     | 7.27 us: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 19.2 us: 1.04x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.02 us: 1.07x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.79 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.39 ms: 1.11x faster                                                       |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 260 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.54 sec: 1.36x faster                                                      |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 263 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 615 ms: 1.25x faster                                                        |
| async_tree_io              | 731 ms                                                      | 584 ms: 1.25x faster                                                        |
| raytrace                   | 192 ms                                                      | 159 ms: 1.21x faster                                                        |
| mypy2                      | 509 ms                                                      | 423 ms: 1.20x faster                                                        |
| deltablue                  | 2.16 ms                                                     | 1.89 ms: 1.14x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 53.0 ns: 1.14x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.9 ms: 1.14x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.0 ms: 1.14x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.2 ms: 1.13x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 763 us: 1.12x faster                                                        |
| generators                 | 22.5 ms                                                     | 20.1 ms: 1.12x faster                                                       |
| float                      | 56.8 ms                                                     | 50.9 ms: 1.12x faster                                                       |
| go                         | 91.6 ms                                                     | 82.5 ms: 1.11x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.70 ms: 1.11x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                        |
| mako                       | 7.09 ms                                                     | 6.39 ms: 1.11x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 57.0 ms: 1.10x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| scimark_lu                 | 58.9 ms                                                     | 54.0 ms: 1.09x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.79 us: 1.08x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 44.8 ms: 1.08x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.20 us: 1.08x faster                                                       |
| sympy_str                  | 175 ms                                                      | 162 ms: 1.08x faster                                                        |
| spectral_norm              | 66.9 ms                                                     | 62.0 ms: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 84.9 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 476 ms: 1.08x faster                                                        |
| async_generators           | 239 ms                                                      | 223 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.07x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 64.5 ms: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.1 ms: 1.07x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.3 ms: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                        |
| richards_super             | 32.1 ms                                                     | 30.1 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 980 ms: 1.07x faster                                                        |
| deepcopy                   | 238 us                                                      | 223 us: 1.07x faster                                                        |
| richards                   | 28.4 ms                                                     | 26.6 ms: 1.07x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 176 ms: 1.06x faster                                                        |
| chameleon                  | 4.98 ms                                                     | 4.71 ms: 1.06x faster                                                       |
| 2to3                       | 218 ms                                                      | 207 ms: 1.05x faster                                                        |
| scimark_fft                | 184 ms                                                      | 175 ms: 1.05x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 765 us: 1.05x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.6 ms: 1.05x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.6 us: 1.05x faster                                                       |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 281 ms: 1.05x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 975 us: 1.05x faster                                                        |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 75.5 ms: 1.04x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.5 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 71.6 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.46 ms: 1.04x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 33.3 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| nbody                      | 71.9 ms                                                     | 69.4 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.51 ms: 1.03x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.66 us: 1.03x faster                                                       |
| sympy_expand               | 284 ms                                                      | 275 ms: 1.03x faster                                                        |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.8 ms: 1.03x faster                                                       |
| fannkuch                   | 247 ms                                                      | 241 ms: 1.02x faster                                                        |
| pickle                     | 7.43 us                                                     | 7.27 us: 1.02x faster                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.05 us: 1.02x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.63 sec: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 91.3 ms: 1.02x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.38 sec: 1.01x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                      |
| aiohttp                    | 884 us                                                      | 899 us: 1.02x slower                                                        |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 19.2 us: 1.04x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.02 us: 1.07x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.79 us: 1.07x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                        |
| coverage                   | 40.8 ms                                                     | 45.4 ms: 1.11x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.2 ms: 1.14x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.76 ms: 1.15x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 913 us: 1.21x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (4): python_startup_no_site, json_loads, json, pycparser
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240615-3.13.0b2+-a19bb26/bm-20240615-pythonperf1-amd64-python-a19bb261a327e1008f21-3.13.0b2+-a19bb26.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown