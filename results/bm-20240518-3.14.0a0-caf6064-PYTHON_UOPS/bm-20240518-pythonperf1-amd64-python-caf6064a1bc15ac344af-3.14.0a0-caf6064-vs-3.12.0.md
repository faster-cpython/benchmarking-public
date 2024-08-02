# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-amd64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.02x slower
- HPT reliability: 96.29%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| chameleon      | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                      |
| docutils       | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 87.0 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 217 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 231 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 612 ms: 1.19x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.26x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 53.6 ms: 1.06x faster                                                      |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 75.0 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 15.9 ms: 1.11x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 106 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.11 us: 1.05x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                      |
| pickle_dict          | 18.4 us                                                     | 18.4 us: 1.00x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 5.81 ms: 1.02x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.58 us: 1.05x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| pickle_pure_python   | 195 us                                                      | 217 us: 1.11x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 155 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 7.35 ms: 1.04x slower                                                      |
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.50 sec: 1.40x faster                                                     |
| async_tree_memoization_tg  | 367 ms                                                      | 272 ms: 1.35x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 217 ms: 1.32x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 388 ms: 1.29x faster                                                       |
| async_tree_none            | 291 ms                                                      | 231 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 628 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 400 ms: 1.22x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 278 ms: 1.22x faster                                                       |
| async_tree_io              | 731 ms                                                      | 612 ms: 1.19x faster                                                       |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 12.8 ms: 1.12x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.63 us: 1.08x faster                                                      |
| comprehensions             | 14.1 us                                                     | 13.1 us: 1.07x faster                                                      |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                       |
| float                      | 56.8 ms                                                     | 53.6 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.11 us: 1.05x faster                                                      |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.3 ms: 1.03x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 87.0 ms: 1.03x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 67.6 ms: 1.02x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 839 us: 1.02x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 79.2 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.67 us: 1.01x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.23 us: 1.01x faster                                                      |
| richards                   | 28.4 ms                                                     | 28.2 ms: 1.00x faster                                                      |
| pickle_dict                | 18.4 us                                                     | 18.4 us: 1.00x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 49.2 ms: 1.01x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 56.6 ms: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.81 ms: 1.02x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.81 us: 1.02x slower                                                      |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                     |
| python_startup             | 19.5 ms                                                     | 20.0 ms: 1.03x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.15 us: 1.03x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| meteor_contest             | 74.6 ms                                                     | 76.7 ms: 1.03x slower                                                      |
| chameleon                  | 4.98 ms                                                     | 5.12 ms: 1.03x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 530 ms: 1.03x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.93 us: 1.04x slower                                                      |
| mako                       | 7.09 ms                                                     | 7.35 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| nbody                      | 71.9 ms                                                     | 75.0 ms: 1.04x slower                                                      |
| deepcopy                   | 238 us                                                      | 249 us: 1.05x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.5 ms: 1.05x slower                                                      |
| unpickle                   | 8.18 us                                                     | 8.58 us: 1.05x slower                                                      |
| 2to3                       | 218 ms                                                      | 229 ms: 1.05x slower                                                       |
| scimark_fft                | 184 ms                                                      | 195 ms: 1.06x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 66.4 ms: 1.06x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.47 sec: 1.07x slower                                                     |
| fannkuch                   | 247 ms                                                      | 267 ms: 1.08x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 99.3 ms: 1.08x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 47.6 ms: 1.09x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 881 us: 1.10x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.3 ms: 1.10x slower                                                      |
| go                         | 91.6 ms                                                     | 100 ms: 1.10x slower                                                       |
| coverage                   | 40.8 ms                                                     | 44.8 ms: 1.10x slower                                                      |
| pyflate                    | 295 ms                                                      | 324 ms: 1.10x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.83 sec: 1.10x slower                                                     |
| pickle_pure_python         | 195 us                                                      | 217 us: 1.11x slower                                                       |
| sympy_str                  | 175 ms                                                      | 195 ms: 1.11x slower                                                       |
| pycparser                  | 699 ms                                                      | 777 ms: 1.11x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 74.5 ms: 1.11x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 15.9 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 38.6 ms: 1.12x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.5 ms: 1.12x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 68.2 ns: 1.13x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 155 us: 1.16x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.01 ms: 1.18x slower                                                      |
| deepcopy_memo              | 23.7 us                                                     | 28.0 us: 1.18x slower                                                      |
| sympy_expand               | 284 ms                                                      | 337 ms: 1.19x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.91 ms: 1.19x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.59 ms: 1.20x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 106 ms: 1.21x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 912 us: 1.21x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 116 us: 1.21x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 5.23 ms: 1.28x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 77.2 ms: 1.31x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (5): richards_super, chaos, json_loads, xml_etree_iterparse, python_startup_no_site
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-pythonperf1-amd64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 96.29% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown