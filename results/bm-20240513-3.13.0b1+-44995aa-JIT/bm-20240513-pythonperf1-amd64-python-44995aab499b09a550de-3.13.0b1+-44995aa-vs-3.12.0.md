# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.04x faster
- HPT reliability: 97.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.08x slower                                                        |
| chameleon      | 4.98 ms                                                     | 5.07 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 85.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 623 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 399 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| async_tree_io              | 731 ms                                                      | 600 ms: 1.22x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                       |
| float          | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_compile  | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                       |
| regex_v8       | 14.2 ms                                                     | 16.0 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 174 us: 1.12x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.0 ms: 1.09x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| unpickle_pure_python | 133 us                                                      | 126 us: 1.06x faster                                                        |
| pickle_dict          | 18.4 us                                                     | 17.6 us: 1.05x faster                                                       |
| pickle               | 7.43 us                                                     | 7.17 us: 1.04x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| unpickle_list        | 2.75 us                                                     | 2.82 us: 1.03x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.05 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                       |
| python_startup         | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 4.93 ms: 1.44x faster                                                       |
| django_template | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| spectral_norm              | 66.9 ms                                                     | 44.1 ms: 1.52x faster                                                       |
| mako                       | 7.09 ms                                                     | 4.93 ms: 1.44x faster                                                       |
| nbody                      | 71.9 ms                                                     | 51.5 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.2 us: 1.38x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 213 ms: 1.34x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.58 sec: 1.33x faster                                                      |
| float                      | 56.8 ms                                                     | 43.4 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 389 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 226 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 623 ms: 1.24x faster                                                        |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 399 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.10 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 600 ms: 1.22x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 41.0 ms: 1.18x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.6 us: 1.15x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 446 ms: 1.15x faster                                                        |
| pyflate                    | 295 ms                                                      | 257 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 38.2 ms: 1.14x faster                                                       |
| fannkuch                   | 247 ms                                                      | 216 ms: 1.14x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 924 ms: 1.13x faster                                                        |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.12x faster                                                        |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.2 ms: 1.11x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| raytrace                   | 192 ms                                                      | 175 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.0 ms: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 51.6 ms: 1.08x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 55.9 ns: 1.08x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.2 ms: 1.08x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.87 us: 1.07x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.29 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 126 us: 1.06x faster                                                        |
| dulwich_log                | 44.3 ms                                                     | 42.1 ms: 1.05x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 17.6 us: 1.05x faster                                                       |
| generators                 | 22.5 ms                                                     | 21.6 ms: 1.04x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 85.9 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.17 us: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.4 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.8 ms: 1.02x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 61.4 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| sqlglot_parse              | 804 us                                                      | 800 us: 1.01x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 88.6 ms: 1.01x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 93.1 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                       |
| chameleon                  | 4.98 ms                                                     | 5.07 ms: 1.02x slower                                                       |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 2.14 us: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.6 ms: 1.02x slower                                                       |
| richards                   | 28.4 ms                                                     | 29.1 ms: 1.03x slower                                                       |
| unpickle_list              | 2.75 us                                                     | 2.82 us: 1.03x slower                                                       |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 248 ms: 1.04x slower                                                        |
| scimark_sor                | 78.8 ms                                                     | 82.2 ms: 1.04x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.60 us: 1.05x slower                                                       |
| aiohttp                    | 884 us                                                      | 940 us: 1.06x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 36.7 ms: 1.06x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.46 sec: 1.06x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 73.9 ms: 1.07x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.79 sec: 1.08x slower                                                      |
| 2to3                       | 218 ms                                                      | 234 ms: 1.08x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.05 us: 1.08x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 14.0 ms: 1.08x slower                                                       |
| pycparser                  | 699 ms                                                      | 756 ms: 1.08x slower                                                        |
| coverage                   | 40.8 ms                                                     | 44.5 ms: 1.09x slower                                                       |
| sympy_expand               | 284 ms                                                      | 311 ms: 1.10x slower                                                        |
| deltablue                  | 2.16 ms                                                     | 2.37 ms: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.55 ms: 1.10x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 18.2 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.8 ms: 1.13x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 16.0 ms: 1.13x slower                                                       |
| python_startup             | 19.5 ms                                                     | 22.0 ms: 1.13x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.67 ms: 1.14x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 572 ms: 1.17x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 920 us: 1.22x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 72.2 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (6): mypy2, pathlib, deepcopy, json_dumps, json, bench_thread_pool
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.84% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown