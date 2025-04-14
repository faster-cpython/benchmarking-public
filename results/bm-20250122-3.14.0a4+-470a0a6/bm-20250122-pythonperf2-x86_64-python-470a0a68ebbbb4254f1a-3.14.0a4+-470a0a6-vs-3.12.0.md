# Results vs. 3.12.0

- fork: python
- ref: 470a0a68ebbbb4254f1a
- machine: linux-x86_64
- commit hash: 470a0a6
- commit date: 2025-01-22
- overall geometric mean: 1.050x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| docutils       | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 620 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 622 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                         |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 497 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.5 ms: 1.09x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| regex_dna      | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| xml_etree_generate   | 86.1 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                                         |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                         |
| xml_etree_process    | 58.4 ms                                                      | 62.0 ms: 1.06x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                        |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 620 ms: 1.70x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 622 ms: 1.67x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                         |
| async_tree_none            | 452 ms                                                       | 274 ms: 1.65x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 497 ms: 1.40x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                        |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                         |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.18x faster                                                        |
| go                         | 150 ms                                                       | 128 ms: 1.17x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.18 ms: 1.12x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.6 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.10x faster                                                         |
| float                      | 76.6 ms                                                      | 70.5 ms: 1.09x faster                                                        |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.08x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.4 ms: 1.08x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 85.4 ms: 1.07x faster                                                        |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 75.4 ms: 1.07x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 97.0 ms: 1.06x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.44 sec: 1.05x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.69 ms: 1.05x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.31 ms: 1.05x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.14 us: 1.05x faster                                                        |
| scimark_lu                 | 98.8 ms                                                      | 94.3 ms: 1.05x faster                                                        |
| chaos                      | 64.0 ms                                                      | 61.1 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.58 sec: 1.05x faster                                                       |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.44 us: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 782 ms: 1.03x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 83.6 ms: 1.03x faster                                                        |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                         |
| nqueens                    | 89.9 ms                                                      | 87.9 ms: 1.02x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 930 us: 1.02x faster                                                         |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                         |
| pyflate                    | 439 ms                                                       | 431 ms: 1.02x faster                                                         |
| nbody                      | 88.0 ms                                                      | 86.5 ms: 1.02x faster                                                        |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                         |
| docutils                   | 2.87 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 58.3 ms: 1.02x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.29 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                                        |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.02x slower                                                         |
| async_generators           | 390 ms                                                       | 398 ms: 1.02x slower                                                         |
| logging_silent             | 94.4 ns                                                      | 96.5 ns: 1.02x slower                                                        |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.2 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.31 ms: 1.04x slower                                                        |
| richards_super             | 51.3 ms                                                      | 53.4 ms: 1.04x slower                                                        |
| fannkuch                   | 350 ms                                                       | 364 ms: 1.04x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                                         |
| regex_dna                  | 239 ms                                                       | 251 ms: 1.05x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.44 ms: 1.06x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 62.0 ms: 1.06x slower                                                        |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 26.8 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.6 ms: 1.14x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                                         |
| coverage                   | 66.7 ms                                                      | 79.0 ms: 1.18x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.27 ms: 1.19x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.78 ms: 1.75x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.11 ms: 1.76x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.63 sec: 341.67x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (4): asyncio_websockets, richards, hexiom, pycparser
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250122-3.14.0a4+-470a0a6/bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x