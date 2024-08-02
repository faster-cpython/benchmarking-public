# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.02x slower
- HPT reliability: 99.01%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 234 ms: 1.07x slower                                                        |
| chameleon      | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                      |
| tornado_http   | 89.5 ms                                                     | 87.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 216 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 280 ms: 1.21x faster                                                        |
| async_tree_io              | 731 ms                                                      | 604 ms: 1.21x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 51.7 ms: 1.10x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| nbody          | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| regex_compile  | 87.5 ms                                                     | 107 ms: 1.23x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| pickle               | 7.43 us                                                     | 7.16 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.73 us: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.5 us: 1.00x slower                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.36 us: 1.02x slower                                                       |
| xml_etree_process    | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 212 us: 1.08x slower                                                        |
| pickle_list          | 2.83 us                                                     | 3.11 us: 1.10x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                       |
| python_startup         | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.20 ms: 1.02x slower                                                       |
| django_template | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.55 sec: 1.35x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 273 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 216 ms: 1.32x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                        |
| async_tree_none            | 291 ms                                                      | 232 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 401 ms: 1.22x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 280 ms: 1.21x faster                                                        |
| async_tree_io              | 731 ms                                                      | 604 ms: 1.21x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 12.6 ms: 1.13x faster                                                       |
| float                      | 56.8 ms                                                     | 51.7 ms: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.09x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| comprehensions             | 14.1 us                                                     | 13.1 us: 1.08x faster                                                       |
| json                       | 3.05 ms                                                     | 2.88 ms: 1.06x faster                                                       |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                        |
| xml_etree_parse            | 93.0 ms                                                     | 88.5 ms: 1.05x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.16 us: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.56 ms: 1.04x faster                                                       |
| tornado_http               | 89.5 ms                                                     | 87.9 ms: 1.02x faster                                                       |
| logging_simple             | 6.28 us                                                     | 6.17 us: 1.02x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.60 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 64.2 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 68.3 ms: 1.01x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.9 ms: 1.01x faster                                                       |
| unpickle_list              | 2.75 us                                                     | 2.73 us: 1.01x faster                                                       |
| pickle_dict                | 18.4 us                                                     | 18.5 us: 1.00x slower                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 56.1 ms: 1.01x slower                                                       |
| richards                   | 28.4 ms                                                     | 28.5 ms: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 241 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 75.3 ms: 1.01x slower                                                       |
| nbody                      | 71.9 ms                                                     | 72.7 ms: 1.01x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                       |
| mako                       | 7.09 ms                                                     | 7.20 ms: 1.02x slower                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 49.3 ms: 1.02x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.6 ms: 1.02x slower                                                       |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.36 us: 1.02x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                       |
| chameleon                  | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.57 ms: 1.03x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 38.9 ms: 1.03x slower                                                       |
| scimark_fft                | 184 ms                                                      | 190 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 513 ms                                                      | 532 ms: 1.04x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.42 sec: 1.04x slower                                                      |
| dulwich_log                | 44.3 ms                                                     | 46.0 ms: 1.04x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 65.3 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                      |
| python_startup             | 19.5 ms                                                     | 20.3 ms: 1.04x slower                                                       |
| deepcopy                   | 238 us                                                      | 248 us: 1.04x slower                                                        |
| fannkuch                   | 247 ms                                                      | 261 ms: 1.06x slower                                                        |
| django_template            | 22.9 ms                                                     | 24.5 ms: 1.07x slower                                                       |
| 2to3                       | 218 ms                                                      | 234 ms: 1.07x slower                                                        |
| sympy_sum                  | 91.5 ms                                                     | 98.4 ms: 1.07x slower                                                       |
| aiohttp                    | 884 us                                                      | 953 us: 1.08x slower                                                        |
| sqlglot_parse              | 804 us                                                      | 869 us: 1.08x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.4 ms: 1.08x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 212 us: 1.08x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.11 ms: 1.08x slower                                                       |
| go                         | 91.6 ms                                                     | 99.6 ms: 1.09x slower                                                       |
| pyflate                    | 295 ms                                                      | 321 ms: 1.09x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                       |
| coverage                   | 40.8 ms                                                     | 44.6 ms: 1.09x slower                                                       |
| pycparser                  | 699 ms                                                      | 768 ms: 1.10x slower                                                        |
| docutils                   | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.11 us: 1.10x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.8 ms: 1.10x slower                                                       |
| sympy_str                  | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 34.5 ms                                                     | 38.2 ms: 1.11x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.52 sec: 1.11x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.6 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.88 ms: 1.13x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 76.0 ms: 1.14x slower                                                       |
| logging_silent             | 60.5 ns                                                     | 69.1 ns: 1.14x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.17x slower                                                        |
| sympy_expand               | 284 ms                                                      | 332 ms: 1.17x slower                                                        |
| deepcopy_memo              | 23.7 us                                                     | 27.8 us: 1.17x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.54 ms: 1.17x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.88 ms: 1.18x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 578 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                        |
| create_gc_cycles           | 752 us                                                      | 914 us: 1.22x slower                                                        |
| regex_compile              | 87.5 ms                                                     | 107 ms: 1.23x slower                                                        |
| scimark_lu                 | 58.9 ms                                                     | 74.9 ms: 1.27x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.23 ms: 1.28x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (3): chaos, json_dumps, bench_thread_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown