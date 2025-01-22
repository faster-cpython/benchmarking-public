# Results vs. 3.12.0

- fork: mdboom
- ref: aa_test_2025
- machine: linux-x86_64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.042x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 312 ms: 1.14x slower                                           |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 556 ms: 2.13x faster                                           |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                           |
| async_tree_none            | 472 ms                                                 | 292 ms: 1.62x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 372 ms: 1.55x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 534 ms: 1.36x faster                                           |
| Geometric mean             | (ref)                                                  | 1.69x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.3 ms: 1.08x faster                                          |
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                           |
| nbody          | 97.0 ms                                                | 137 ms: 1.41x slower                                           |
| Geometric mean | (ref)                                                  | 1.08x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.48 ms: 1.04x faster                                          |
| regex_compile  | 148 ms                                                 | 152 ms: 1.03x slower                                           |
| regex_dna      | 212 ms                                                 | 224 ms: 1.06x slower                                           |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.6 ms: 1.12x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                           |
| tomli_loads          | 2.33 sec                                               | 2.43 sec: 1.04x slower                                         |
| xml_etree_generate   | 89.2 ms                                                | 96.6 ms: 1.08x slower                                          |
| json_loads           | 28.5 us                                                | 31.8 us: 1.12x slower                                          |
| unpickle_pure_python | 230 us                                                 | 270 us: 1.17x slower                                           |
| xml_etree_process    | 61.7 ms                                                | 72.5 ms: 1.17x slower                                          |
| pickle_pure_python   | 324 us                                                 | 385 us: 1.19x slower                                           |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                          |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.35 ms: 1.35x slower                                          |
| python_startup         | 9.55 ms                                                | 15.1 ms: 1.58x slower                                          |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 41.6 ms: 1.20x slower                                          |
| mako            | 11.9 ms                                                | 16.4 ms: 1.38x slower                                          |
| Geometric mean  | (ref)                                                  | 1.29x slower                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 556 ms: 2.13x faster                                           |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                           |
| async_tree_none_tg         | 450 ms                                                 | 244 ms: 1.84x faster                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                           |
| async_tree_none            | 472 ms                                                 | 292 ms: 1.62x faster                                           |
| async_tree_memoization     | 578 ms                                                 | 372 ms: 1.55x faster                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 534 ms: 1.36x faster                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                          |
| deepcopy                   | 371 us                                                 | 317 us: 1.17x faster                                           |
| xml_etree_iterparse        | 107 ms                                                 | 95.6 ms: 1.12x faster                                          |
| float                      | 84.7 ms                                                | 78.3 ms: 1.08x faster                                          |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                           |
| async_generators           | 463 ms                                                 | 443 ms: 1.04x faster                                           |
| comprehensions             | 21.8 us                                                | 20.9 us: 1.04x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.48 ms: 1.04x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                          |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                           |
| deepcopy_memo              | 40.7 us                                                | 39.7 us: 1.03x faster                                          |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                          |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                           |
| generators                 | 31.2 ms                                                | 31.7 ms: 1.02x slower                                          |
| regex_compile              | 148 ms                                                 | 152 ms: 1.03x slower                                           |
| dulwich_log                | 68.5 ms                                                | 70.4 ms: 1.03x slower                                          |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                           |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                         |
| tomli_loads                | 2.33 sec                                               | 2.43 sec: 1.04x slower                                         |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                         |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.05x slower                                         |
| regex_dna                  | 212 ms                                                 | 224 ms: 1.06x slower                                           |
| sympy_sum                  | 169 ms                                                 | 180 ms: 1.06x slower                                           |
| json                       | 5.26 ms                                                | 5.63 ms: 1.07x slower                                          |
| logging_simple             | 6.46 us                                                | 6.93 us: 1.07x slower                                          |
| sympy_str                  | 300 ms                                                 | 322 ms: 1.07x slower                                           |
| logging_format             | 7.23 us                                                | 7.78 us: 1.08x slower                                          |
| xml_etree_generate         | 89.2 ms                                                | 96.6 ms: 1.08x slower                                          |
| pyflate                    | 482 ms                                                 | 523 ms: 1.08x slower                                           |
| scimark_fft                | 382 ms                                                 | 419 ms: 1.10x slower                                           |
| sqlglot_normalize          | 110 ms                                                 | 121 ms: 1.10x slower                                           |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                          |
| scimark_sor                | 129 ms                                                 | 142 ms: 1.10x slower                                           |
| sqlglot_optimize           | 54.8 ms                                                | 61.0 ms: 1.11x slower                                          |
| coroutines                 | 23.2 ms                                                | 25.8 ms: 1.11x slower                                          |
| crypto_pyaes               | 81.9 ms                                                | 91.3 ms: 1.12x slower                                          |
| sympy_expand               | 478 ms                                                 | 534 ms: 1.12x slower                                           |
| json_loads                 | 28.5 us                                                | 31.8 us: 1.12x slower                                          |
| chaos                      | 67.0 ms                                                | 75.0 ms: 1.12x slower                                          |
| pprint_safe_repr           | 776 ms                                                 | 869 ms: 1.12x slower                                           |
| sqlalchemy_declarative     | 147 ms                                                 | 165 ms: 1.12x slower                                           |
| sympy_integrate            | 21.4 ms                                                | 24.1 ms: 1.12x slower                                          |
| logging_silent             | 104 ns                                                 | 117 ns: 1.12x slower                                           |
| sqlalchemy_imperative      | 18.7 ms                                                | 21.1 ms: 1.13x slower                                          |
| 2to3                       | 274 ms                                                 | 312 ms: 1.14x slower                                           |
| pprint_pformat             | 1.57 sec                                               | 1.79 sec: 1.14x slower                                         |
| raytrace                   | 312 ms                                                 | 356 ms: 1.14x slower                                           |
| sqlglot_parse              | 1.36 ms                                                | 1.56 ms: 1.14x slower                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.96 ms: 1.17x slower                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 87.8 ms: 1.17x slower                                          |
| gc_traversal               | 3.79 ms                                                | 4.45 ms: 1.17x slower                                          |
| unpickle_pure_python       | 230 us                                                 | 270 us: 1.17x slower                                           |
| xml_etree_process          | 61.7 ms                                                | 72.5 ms: 1.17x slower                                          |
| richards                   | 45.8 ms                                                | 54.2 ms: 1.18x slower                                          |
| pickle_pure_python         | 324 us                                                 | 385 us: 1.19x slower                                           |
| nqueens                    | 83.3 ms                                                | 99.1 ms: 1.19x slower                                          |
| scimark_lu                 | 118 ms                                                 | 140 ms: 1.19x slower                                           |
| meteor_contest             | 112 ms                                                 | 134 ms: 1.19x slower                                           |
| django_template            | 34.6 ms                                                | 41.6 ms: 1.20x slower                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.12 ms: 1.21x slower                                          |
| fannkuch                   | 417 ms                                                 | 507 ms: 1.22x slower                                           |
| richards_super             | 51.5 ms                                                | 62.8 ms: 1.22x slower                                          |
| hexiom                     | 6.41 ms                                                | 7.83 ms: 1.22x slower                                          |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                          |
| deltablue                  | 3.72 ms                                                | 4.70 ms: 1.26x slower                                          |
| telco                      | 7.10 ms                                                | 9.14 ms: 1.29x slower                                          |
| python_startup_no_site     | 6.94 ms                                                | 9.35 ms: 1.35x slower                                          |
| typing_runtime_protocols   | 158 us                                                 | 215 us: 1.36x slower                                           |
| mako                       | 11.9 ms                                                | 16.4 ms: 1.38x slower                                          |
| nbody                      | 97.0 ms                                                | 137 ms: 1.41x slower                                           |
| coverage                   | 72.7 ms                                                | 107 ms: 1.47x slower                                           |
| python_startup             | 9.55 ms                                                | 15.1 ms: 1.58x slower                                          |
| bench_mp_pool              | 24.0 ms                                                | 89.6 ms: 3.73x slower                                          |
| bench_thread_pool          | 842 us                                                 | 3.49 ms: 4.15x slower                                          |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                   |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-4844db8-NOGIL/bm-20250121-linux-x86_64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.31x