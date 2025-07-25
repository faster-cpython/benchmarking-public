# Results vs. 3.12.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: linux-x86_64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.038x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                                  |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                                |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 630 ms: 1.67x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                  |
| Geometric mean             | (ref)                                                        | 1.58x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                                 |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                                  |
| nbody          | 88.0 ms                                                      | 97.5 ms: 1.11x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| regex_dna      | 239 ms                                                       | 227 ms: 1.05x faster                                                                  |
| regex_effbot   | 3.57 ms                                                      | 3.73 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                                |
| unpickle_pure_python | 210 us                                                       | 195 us: 1.07x faster                                                                  |
| xml_etree_generate   | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                                 |
| xml_etree_parse      | 144 ms                                                       | 136 ms: 1.06x faster                                                                  |
| xml_etree_process    | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                                 |
| pickle_pure_python   | 318 us                                                       | 335 us: 1.05x slower                                                                  |
| json_loads           | 24.4 us                                                      | 26.8 us: 1.10x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                                 |
| python_startup         | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.16x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                                 |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                                |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                                  |
| async_tree_io_tg           | 1.05 sec                                                     | 630 ms: 1.67x faster                                                                  |
| async_tree_memoization     | 544 ms                                                       | 326 ms: 1.67x faster                                                                  |
| async_tree_memoization_tg  | 540 ms                                                       | 332 ms: 1.63x faster                                                                  |
| async_tree_none            | 452 ms                                                       | 278 ms: 1.62x faster                                                                  |
| async_tree_none_tg         | 431 ms                                                       | 269 ms: 1.60x faster                                                                  |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 500 ms: 1.39x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 506 ms: 1.38x faster                                                                  |
| deepcopy                   | 368 us                                                       | 277 us: 1.33x faster                                                                  |
| richards                   | 45.7 ms                                                      | 34.3 ms: 1.33x faster                                                                 |
| generators                 | 37.4 ms                                                      | 28.4 ms: 1.32x faster                                                                 |
| deepcopy_memo              | 36.8 us                                                      | 28.0 us: 1.31x faster                                                                 |
| richards_super             | 51.3 ms                                                      | 39.9 ms: 1.29x faster                                                                 |
| comprehensions             | 21.9 us                                                      | 17.2 us: 1.28x faster                                                                 |
| float                      | 76.6 ms                                                      | 63.6 ms: 1.21x faster                                                                 |
| go                         | 150 ms                                                       | 125 ms: 1.19x faster                                                                  |
| spectral_norm              | 91.6 ms                                                      | 77.6 ms: 1.18x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 1.89 sec: 1.14x faster                                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.97 us: 1.14x faster                                                                 |
| logging_format             | 7.48 us                                                      | 6.60 us: 1.13x faster                                                                 |
| deltablue                  | 3.24 ms                                                      | 2.87 ms: 1.13x faster                                                                 |
| pathlib                    | 18.9 ms                                                      | 16.8 ms: 1.12x faster                                                                 |
| logging_simple             | 6.71 us                                                      | 6.01 us: 1.12x faster                                                                 |
| dulwich_log                | 65.4 ms                                                      | 59.1 ms: 1.11x faster                                                                 |
| django_template            | 38.2 ms                                                      | 34.7 ms: 1.10x faster                                                                 |
| scimark_monte_carlo        | 69.0 ms                                                      | 62.7 ms: 1.10x faster                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.51 sec: 1.09x faster                                                                |
| pyflate                    | 439 ms                                                       | 401 ms: 1.09x faster                                                                  |
| chaos                      | 64.0 ms                                                      | 58.9 ms: 1.09x faster                                                                 |
| pprint_safe_repr           | 807 ms                                                       | 745 ms: 1.08x faster                                                                  |
| regex_compile              | 144 ms                                                       | 133 ms: 1.08x faster                                                                  |
| scimark_sor                | 109 ms                                                       | 101 ms: 1.08x faster                                                                  |
| unpickle_pure_python       | 210 us                                                       | 195 us: 1.07x faster                                                                  |
| sympy_integrate            | 23.9 ms                                                      | 22.3 ms: 1.07x faster                                                                 |
| xml_etree_generate         | 86.1 ms                                                      | 80.7 ms: 1.07x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                                  |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                                 |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                                  |
| xml_etree_process          | 58.4 ms                                                      | 55.3 ms: 1.06x faster                                                                 |
| raytrace                   | 298 ms                                                       | 283 ms: 1.05x faster                                                                  |
| regex_dna                  | 239 ms                                                       | 227 ms: 1.05x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 122 ms: 1.05x faster                                                                  |
| scimark_lu                 | 98.8 ms                                                      | 94.7 ms: 1.04x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 290 ms: 1.04x faster                                                                  |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 77.5 ms: 1.04x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 22.4 ms: 1.03x faster                                                                 |
| logging_silent             | 94.4 ns                                                      | 92.1 ns: 1.02x faster                                                                 |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                                                  |
| scimark_fft                | 301 ms                                                       | 298 ms: 1.01x faster                                                                  |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.82 us: 1.02x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                                                |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                                |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                                 |
| fannkuch                   | 350 ms                                                       | 359 ms: 1.03x slower                                                                  |
| sympy_expand               | 484 ms                                                       | 499 ms: 1.03x slower                                                                  |
| hexiom                     | 5.96 ms                                                      | 6.17 ms: 1.03x slower                                                                 |
| nqueens                    | 89.9 ms                                                      | 93.1 ms: 1.04x slower                                                                 |
| regex_effbot               | 3.57 ms                                                      | 3.73 ms: 1.05x slower                                                                 |
| pickle_pure_python         | 318 us                                                       | 335 us: 1.05x slower                                                                  |
| async_generators           | 390 ms                                                       | 417 ms: 1.07x slower                                                                  |
| json                       | 5.12 ms                                                      | 5.48 ms: 1.07x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 26.8 us: 1.10x slower                                                                 |
| nbody                      | 88.0 ms                                                      | 97.5 ms: 1.11x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 11.4 ms: 1.11x slower                                                                 |
| typing_runtime_protocols   | 152 us                                                       | 170 us: 1.12x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.96 ms: 1.18x slower                                                                 |
| coverage                   | 66.7 ms                                                      | 82.3 ms: 1.23x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 15.4 ms: 1.32x slower                                                                 |
| create_gc_cycles           | 1.59 ms                                                      | 2.93 ms: 1.84x slower                                                                 |
| gc_traversal               | 3.48 ms                                                      | 6.74 ms: 1.94x slower                                                                 |
| telco                      | 6.96 ms                                                      | 162 ms: 23.21x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                          |

Benchmark hidden because not significant (2): mako, regex_v8
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf2-x86_64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.038x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x