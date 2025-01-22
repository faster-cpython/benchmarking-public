# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.050x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 282 ms: 1.01x faster                                                 |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                        | 1.00x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 621 ms: 1.70x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 325 ms: 1.66x faster                                                 |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 340 ms: 1.60x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 497 ms: 1.40x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                 |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                 |
| nbody          | 88.0 ms                                                      | 87.1 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                        | 1.05x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                |
| regex_compile  | 144 ms                                                       | 135 ms: 1.07x faster                                                 |
| regex_dna      | 239 ms                                                       | 236 ms: 1.01x faster                                                 |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                        | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 96.2 ms: 1.07x faster                                                |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                 |
| tomli_loads          | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                               |
| xml_etree_generate   | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                |
| xml_etree_process    | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                |
| unpickle_pure_python | 210 us                                                       | 219 us: 1.05x slower                                                 |
| json_loads           | 24.4 us                                                      | 25.5 us: 1.05x slower                                                |
| pickle_pure_python   | 318 us                                                       | 339 us: 1.06x slower                                                 |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                |
| mako            | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 621 ms: 1.70x faster                                                 |
| async_tree_io              | 1.04 sec                                                     | 626 ms: 1.67x faster                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 325 ms: 1.66x faster                                                 |
| async_tree_none            | 452 ms                                                       | 275 ms: 1.64x faster                                                 |
| async_tree_none_tg         | 431 ms                                                       | 266 ms: 1.62x faster                                                 |
| async_tree_memoization     | 544 ms                                                       | 340 ms: 1.60x faster                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 497 ms: 1.40x faster                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                 |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                |
| deepcopy                   | 368 us                                                       | 283 us: 1.30x faster                                                 |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.26x faster                                                |
| deepcopy_memo              | 36.8 us                                                      | 30.3 us: 1.21x faster                                                |
| go                         | 150 ms                                                       | 126 ms: 1.19x faster                                                 |
| pathlib                    | 18.9 ms                                                      | 16.0 ms: 1.18x faster                                                |
| regex_effbot               | 3.57 ms                                                      | 3.11 ms: 1.15x faster                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                |
| raytrace                   | 298 ms                                                       | 267 ms: 1.11x faster                                                 |
| float                      | 76.6 ms                                                      | 69.5 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.6 ms: 1.10x faster                                                |
| spectral_norm              | 91.6 ms                                                      | 83.7 ms: 1.09x faster                                                |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                 |
| coroutines                 | 23.0 ms                                                      | 21.0 ms: 1.09x faster                                                |
| crypto_pyaes               | 80.3 ms                                                      | 73.9 ms: 1.09x faster                                                |
| chaos                      | 64.0 ms                                                      | 59.5 ms: 1.08x faster                                                |
| sympy_sum                  | 162 ms                                                       | 151 ms: 1.07x faster                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 96.2 ms: 1.07x faster                                                |
| regex_compile              | 144 ms                                                       | 135 ms: 1.07x faster                                                 |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                |
| mdp                        | 2.57 sec                                                     | 2.44 sec: 1.05x faster                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.31 ms: 1.05x faster                                                |
| sqlglot_transpile          | 1.78 ms                                                      | 1.69 ms: 1.05x faster                                                |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                 |
| sympy_str                  | 302 ms                                                       | 289 ms: 1.05x faster                                                 |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                 |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                               |
| tomli_loads                | 2.16 sec                                                     | 2.08 sec: 1.04x faster                                               |
| pprint_safe_repr           | 807 ms                                                       | 779 ms: 1.04x faster                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 83.2 ms: 1.04x faster                                                |
| sympy_integrate            | 23.9 ms                                                      | 23.1 ms: 1.03x faster                                                |
| logging_format             | 7.48 us                                                      | 7.28 us: 1.03x faster                                                |
| bench_thread_pool          | 950 us                                                       | 926 us: 1.03x faster                                                 |
| scimark_lu                 | 98.8 ms                                                      | 96.3 ms: 1.03x faster                                                |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                               |
| regex_dna                  | 239 ms                                                       | 236 ms: 1.01x faster                                                 |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                 |
| 2to3                       | 285 ms                                                       | 282 ms: 1.01x faster                                                 |
| nbody                      | 88.0 ms                                                      | 87.1 ms: 1.01x faster                                                |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                               |
| sqlglot_optimize           | 57.5 ms                                                      | 57.7 ms: 1.00x slower                                                |
| hexiom                     | 5.96 ms                                                      | 6.00 ms: 1.01x slower                                                |
| dulwich_log                | 65.4 ms                                                      | 66.1 ms: 1.01x slower                                                |
| scimark_sor                | 109 ms                                                       | 111 ms: 1.01x slower                                                 |
| fannkuch                   | 350 ms                                                       | 356 ms: 1.02x slower                                                 |
| pyflate                    | 439 ms                                                       | 446 ms: 1.02x slower                                                 |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                |
| richards_super             | 51.3 ms                                                      | 52.6 ms: 1.02x slower                                                |
| sympy_expand               | 484 ms                                                       | 497 ms: 1.03x slower                                                 |
| logging_silent             | 94.4 ns                                                      | 97.1 ns: 1.03x slower                                                |
| deltablue                  | 3.24 ms                                                      | 3.36 ms: 1.04x slower                                                |
| xml_etree_process          | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                |
| unpickle_pure_python       | 210 us                                                       | 219 us: 1.05x slower                                                 |
| json_loads                 | 24.4 us                                                      | 25.5 us: 1.05x slower                                                |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                                |
| async_generators           | 390 ms                                                       | 410 ms: 1.05x slower                                                 |
| pickle_pure_python         | 318 us                                                       | 339 us: 1.06x slower                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.59 ms: 1.09x slower                                                |
| mako                       | 10.0 ms                                                      | 11.0 ms: 1.10x slower                                                |
| coverage                   | 66.7 ms                                                      | 74.1 ms: 1.11x slower                                                |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                |
| telco                      | 6.96 ms                                                      | 7.99 ms: 1.15x slower                                                |
| typing_runtime_protocols   | 152 us                                                       | 183 us: 1.21x slower                                                 |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.38x slower                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.75 ms: 1.73x slower                                                |
| gc_traversal               | 3.48 ms                                                      | 6.36 ms: 1.83x slower                                                |
| bench_mp_pool              | 4.76 ms                                                      | 1.87 sec: 392.48x slower                                             |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                         |

Benchmark hidden because not significant (6): richards, logging_simple, asyncio_websockets, nqueens, scimark_fft, sqlglot_normalize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf2-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.050x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x