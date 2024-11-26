# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.009x slower
- HPT reliability: 75.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                                           |
| docutils       | 2.87 sec                                                     | 3.04 sec: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                                           |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 839 ms: 1.26x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                           |
| Geometric mean             | (ref)                                                        | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                           |
| nbody          | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                          |
| float          | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.34 ms: 1.07x faster                                                          |
| regex_compile  | 144 ms                                                       | 143 ms: 1.01x faster                                                           |
| regex_dna      | 239 ms                                                       | 253 ms: 1.06x slower                                                           |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                          |
| unpickle_pure_python | 210 us                                                       | 201 us: 1.04x faster                                                           |
| xml_etree_process    | 58.4 ms                                                      | 57.4 ms: 1.02x faster                                                          |
| xml_etree_iterparse  | 103 ms                                                       | 102 ms: 1.01x faster                                                           |
| tomli_loads          | 2.16 sec                                                     | 2.21 sec: 1.03x slower                                                         |
| json_loads           | 24.4 us                                                      | 25.2 us: 1.04x slower                                                          |
| pickle_pure_python   | 318 us                                                       | 345 us: 1.09x slower                                                           |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                          |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                          |
| django_template | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 386 ms: 1.40x faster                                                           |
| async_tree_none            | 452 ms                                                       | 333 ms: 1.36x faster                                                           |
| async_tree_memoization     | 544 ms                                                       | 408 ms: 1.33x faster                                                           |
| async_tree_none_tg         | 431 ms                                                       | 339 ms: 1.27x faster                                                           |
| deepcopy_memo              | 36.8 us                                                      | 29.1 us: 1.26x faster                                                          |
| async_tree_io_tg           | 1.05 sec                                                     | 839 ms: 1.26x faster                                                           |
| async_tree_io              | 1.04 sec                                                     | 838 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 565 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 576 ms: 1.21x faster                                                           |
| deepcopy                   | 368 us                                                       | 310 us: 1.19x faster                                                           |
| pathlib                    | 18.9 ms                                                      | 16.5 ms: 1.14x faster                                                          |
| comprehensions             | 21.9 us                                                      | 19.6 us: 1.12x faster                                                          |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                          |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                                          |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                           |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                                          |
| regex_effbot               | 3.57 ms                                                      | 3.34 ms: 1.07x faster                                                          |
| scimark_sor                | 109 ms                                                       | 102 ms: 1.07x faster                                                           |
| mako                       | 10.0 ms                                                      | 9.42 ms: 1.06x faster                                                          |
| xml_etree_generate         | 86.1 ms                                                      | 81.5 ms: 1.06x faster                                                          |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                           |
| scimark_lu                 | 98.8 ms                                                      | 94.5 ms: 1.04x faster                                                          |
| richards                   | 45.7 ms                                                      | 43.8 ms: 1.04x faster                                                          |
| unpickle_pure_python       | 210 us                                                       | 201 us: 1.04x faster                                                           |
| richards_super             | 51.3 ms                                                      | 50.1 ms: 1.03x faster                                                          |
| nbody                      | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                          |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.4 ms: 1.02x faster                                                          |
| xml_etree_process          | 58.4 ms                                                      | 57.4 ms: 1.02x faster                                                          |
| logging_format             | 7.48 us                                                      | 7.36 us: 1.02x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.5 ms: 1.01x faster                                                          |
| xml_etree_iterparse        | 103 ms                                                       | 102 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 807 ms                                                       | 798 ms: 1.01x faster                                                           |
| logging_silent             | 94.4 ns                                                      | 93.6 ns: 1.01x faster                                                          |
| regex_compile              | 144 ms                                                       | 143 ms: 1.01x faster                                                           |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                                           |
| deltablue                  | 3.24 ms                                                      | 3.26 ms: 1.01x slower                                                          |
| scimark_fft                | 301 ms                                                       | 303 ms: 1.01x slower                                                           |
| json                       | 5.12 ms                                                      | 5.16 ms: 1.01x slower                                                          |
| logging_simple             | 6.71 us                                                      | 6.77 us: 1.01x slower                                                          |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                                          |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                         |
| mdp                        | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                         |
| sympy_integrate            | 23.9 ms                                                      | 24.4 ms: 1.02x slower                                                          |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                                           |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                                           |
| tomli_loads                | 2.16 sec                                                     | 2.21 sec: 1.03x slower                                                         |
| sympy_str                  | 302 ms                                                       | 311 ms: 1.03x slower                                                           |
| json_loads                 | 24.4 us                                                      | 25.2 us: 1.04x slower                                                          |
| chaos                      | 64.0 ms                                                      | 66.3 ms: 1.04x slower                                                          |
| dulwich_log                | 65.4 ms                                                      | 67.8 ms: 1.04x slower                                                          |
| python_startup_no_site     | 8.64 ms                                                      | 8.99 ms: 1.04x slower                                                          |
| float                      | 76.6 ms                                                      | 79.9 ms: 1.04x slower                                                          |
| pycparser                  | 1.23 sec                                                     | 1.29 sec: 1.04x slower                                                         |
| go                         | 150 ms                                                       | 157 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.87 ms: 1.06x slower                                                          |
| spectral_norm              | 91.6 ms                                                      | 96.9 ms: 1.06x slower                                                          |
| docutils                   | 2.87 sec                                                     | 3.04 sec: 1.06x slower                                                         |
| regex_dna                  | 239 ms                                                       | 253 ms: 1.06x slower                                                           |
| django_template            | 38.2 ms                                                      | 40.8 ms: 1.07x slower                                                          |
| sqlglot_parse              | 1.38 ms                                                      | 1.48 ms: 1.08x slower                                                          |
| raytrace                   | 298 ms                                                       | 322 ms: 1.08x slower                                                           |
| pickle_pure_python         | 318 us                                                       | 345 us: 1.09x slower                                                           |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.09x slower                                                          |
| pyflate                    | 439 ms                                                       | 477 ms: 1.09x slower                                                           |
| sqlglot_normalize          | 116 ms                                                       | 126 ms: 1.09x slower                                                           |
| sqlglot_optimize           | 57.5 ms                                                      | 63.0 ms: 1.10x slower                                                          |
| telco                      | 6.96 ms                                                      | 7.64 ms: 1.10x slower                                                          |
| sympy_expand               | 484 ms                                                       | 531 ms: 1.10x slower                                                           |
| fannkuch                   | 350 ms                                                       | 384 ms: 1.10x slower                                                           |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                          |
| nqueens                    | 89.9 ms                                                      | 102 ms: 1.13x slower                                                           |
| generators                 | 37.4 ms                                                      | 42.9 ms: 1.15x slower                                                          |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.87 ms: 1.16x slower                                                          |
| coverage                   | 66.7 ms                                                      | 79.6 ms: 1.19x slower                                                          |
| hexiom                     | 5.96 ms                                                      | 7.12 ms: 1.20x slower                                                          |
| async_generators           | 390 ms                                                       | 475 ms: 1.22x slower                                                           |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                           |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                          |
| gc_traversal               | 3.48 ms                                                      | 5.82 ms: 1.67x slower                                                          |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                          |
| bench_mp_pool              | 4.76 ms                                                      | 1.37 sec: 288.57x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                   |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_parse, bench_thread_pool
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.009x slower
# HPT report

- Reliability score: 75.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.05x