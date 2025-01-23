# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-x86_64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.050x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 622 ms: 1.69x faster                                                   |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                   |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                   |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.61x faster                                                   |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 505 ms: 1.38x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.6 ms: 1.10x faster                                                  |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.05x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.04 ms: 1.18x faster                                                  |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                   |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                                   |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                        | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 95.3 ms: 1.08x faster                                                  |
| xml_etree_parse      | 144 ms                                                       | 134 ms: 1.07x faster                                                   |
| tomli_loads          | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                  |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                                  |
| xml_etree_process    | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                                  |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.04x slower                                                   |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                   |
| json_dumps           | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                  |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                  |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 622 ms: 1.69x faster                                                   |
| async_tree_io              | 1.04 sec                                                     | 624 ms: 1.67x faster                                                   |
| async_tree_memoization_tg  | 540 ms                                                       | 327 ms: 1.65x faster                                                   |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                   |
| async_tree_none_tg         | 431 ms                                                       | 267 ms: 1.61x faster                                                   |
| async_tree_memoization     | 544 ms                                                       | 341 ms: 1.60x faster                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 499 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 505 ms: 1.38x faster                                                   |
| generators                 | 37.4 ms                                                      | 28.2 ms: 1.33x faster                                                  |
| deepcopy                   | 368 us                                                       | 282 us: 1.31x faster                                                   |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.26x faster                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                  |
| pathlib                    | 18.9 ms                                                      | 15.9 ms: 1.19x faster                                                  |
| regex_effbot               | 3.57 ms                                                      | 3.04 ms: 1.18x faster                                                  |
| go                         | 150 ms                                                       | 127 ms: 1.18x faster                                                   |
| deepcopy_reduce            | 3.37 us                                                      | 2.92 us: 1.16x faster                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                   |
| float                      | 76.6 ms                                                      | 69.6 ms: 1.10x faster                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 73.1 ms: 1.10x faster                                                  |
| raytrace                   | 298 ms                                                       | 272 ms: 1.10x faster                                                   |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                  |
| chaos                      | 64.0 ms                                                      | 58.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 95.3 ms: 1.08x faster                                                  |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                   |
| xml_etree_parse            | 144 ms                                                       | 134 ms: 1.07x faster                                                   |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                   |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.7 ms: 1.07x faster                                                  |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                  |
| spectral_norm              | 91.6 ms                                                      | 86.6 ms: 1.06x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.32 ms: 1.05x faster                                                  |
| sqlglot_transpile          | 1.78 ms                                                      | 1.70 ms: 1.05x faster                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.07 sec: 1.04x faster                                                 |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                  |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                   |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                   |
| mdp                        | 2.57 sec                                                     | 2.48 sec: 1.04x faster                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                  |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                 |
| logging_format             | 7.48 us                                                      | 7.27 us: 1.03x faster                                                  |
| pprint_safe_repr           | 807 ms                                                       | 788 ms: 1.02x faster                                                   |
| logging_simple             | 6.71 us                                                      | 6.56 us: 1.02x faster                                                  |
| pyflate                    | 439 ms                                                       | 431 ms: 1.02x faster                                                   |
| 2to3                       | 285 ms                                                       | 281 ms: 1.02x faster                                                   |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                 |
| nqueens                    | 89.9 ms                                                      | 88.8 ms: 1.01x faster                                                  |
| scimark_sor                | 109 ms                                                       | 108 ms: 1.01x faster                                                   |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                  |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                                   |
| hexiom                     | 5.96 ms                                                      | 6.03 ms: 1.01x slower                                                  |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                                   |
| richards                   | 45.7 ms                                                      | 46.7 ms: 1.02x slower                                                  |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                  |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.02x slower                                                  |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                  |
| json                       | 5.12 ms                                                      | 5.28 ms: 1.03x slower                                                  |
| async_generators           | 390 ms                                                       | 403 ms: 1.03x slower                                                   |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                   |
| richards_super             | 51.3 ms                                                      | 53.1 ms: 1.03x slower                                                  |
| python_startup_no_site     | 8.64 ms                                                      | 8.98 ms: 1.04x slower                                                  |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                                  |
| xml_etree_process          | 58.4 ms                                                      | 61.0 ms: 1.04x slower                                                  |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.04x slower                                                   |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.48 ms: 1.06x slower                                                  |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                  |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.7 ms: 1.15x slower                                                  |
| telco                      | 6.96 ms                                                      | 8.06 ms: 1.16x slower                                                  |
| typing_runtime_protocols   | 152 us                                                       | 178 us: 1.17x slower                                                   |
| coverage                   | 66.7 ms                                                      | 79.1 ms: 1.19x slower                                                  |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.83 ms: 1.78x slower                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.47 ms: 1.86x slower                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 1.70 sec: 356.18x slower                                               |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                           |

Benchmark hidden because not significant (6): bench_thread_pool, nbody, asyncio_websockets, scimark_fft, docutils, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-pythonperf2-x86_64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x