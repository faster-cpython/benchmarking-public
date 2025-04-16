# Results vs. 3.12.0

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: 10cd875
- commit date: 2025-04-16
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 274 ms: 1.04x faster                                                             |
| docutils       | 2.87 sec                                                     | 2.85 sec: 1.00x faster                                                           |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 336 ms: 1.61x faster                                                             |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                             |
| Geometric mean             | (ref)                                                        | 1.56x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 67.2 ms: 1.14x faster                                                            |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                             |
| nbody          | 88.0 ms                                                      | 94.9 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                            |
| regex_compile  | 144 ms                                                       | 132 ms: 1.09x faster                                                             |
| regex_dna      | 239 ms                                                       | 239 ms: 1.00x slower                                                             |
| regex_v8       | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                           |
| xml_etree_iterparse  | 103 ms                                                       | 97.8 ms: 1.05x faster                                                            |
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                             |
| xml_etree_generate   | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                            |
| unpickle_pure_python | 210 us                                                       | 210 us: 1.00x slower                                                             |
| xml_etree_process    | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                            |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                             |
| json_loads           | 24.4 us                                                      | 26.6 us: 1.09x slower                                                            |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                            |
| python_startup         | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                            |
| mako            | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.27 sec: 2.02x faster                                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 634 ms: 1.66x faster                                                             |
| async_tree_memoization     | 544 ms                                                       | 328 ms: 1.66x faster                                                             |
| async_tree_io              | 1.04 sec                                                     | 629 ms: 1.66x faster                                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 336 ms: 1.61x faster                                                             |
| async_tree_none            | 452 ms                                                       | 284 ms: 1.59x faster                                                             |
| async_tree_none_tg         | 431 ms                                                       | 272 ms: 1.58x faster                                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 504 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 507 ms: 1.37x faster                                                             |
| deepcopy                   | 368 us                                                       | 276 us: 1.34x faster                                                             |
| deepcopy_memo              | 36.8 us                                                      | 27.8 us: 1.32x faster                                                            |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                                            |
| generators                 | 37.4 ms                                                      | 30.0 ms: 1.25x faster                                                            |
| go                         | 150 ms                                                       | 123 ms: 1.22x faster                                                             |
| deepcopy_reduce            | 3.37 us                                                      | 2.90 us: 1.16x faster                                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 60.3 ms: 1.14x faster                                                            |
| regex_effbot               | 3.57 ms                                                      | 3.13 ms: 1.14x faster                                                            |
| float                      | 76.6 ms                                                      | 67.2 ms: 1.14x faster                                                            |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                            |
| chaos                      | 64.0 ms                                                      | 58.3 ms: 1.10x faster                                                            |
| regex_compile              | 144 ms                                                       | 132 ms: 1.09x faster                                                             |
| logging_simple             | 6.71 us                                                      | 6.14 us: 1.09x faster                                                            |
| raytrace                   | 298 ms                                                       | 273 ms: 1.09x faster                                                             |
| sympy_integrate            | 23.9 ms                                                      | 21.9 ms: 1.09x faster                                                            |
| logging_format             | 7.48 us                                                      | 6.87 us: 1.09x faster                                                            |
| sqlalchemy_declarative     | 159 ms                                                       | 148 ms: 1.08x faster                                                             |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                             |
| django_template            | 38.2 ms                                                      | 35.4 ms: 1.08x faster                                                            |
| dulwich_log                | 65.4 ms                                                      | 61.0 ms: 1.07x faster                                                            |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                             |
| tomli_loads                | 2.16 sec                                                     | 2.04 sec: 1.06x faster                                                           |
| pprint_pformat             | 1.65 sec                                                     | 1.57 sec: 1.06x faster                                                           |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                             |
| pprint_safe_repr           | 807 ms                                                       | 766 ms: 1.05x faster                                                             |
| xml_etree_iterparse        | 103 ms                                                       | 97.8 ms: 1.05x faster                                                            |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                            |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.9 ms: 1.05x faster                                                            |
| deltablue                  | 3.24 ms                                                      | 3.10 ms: 1.04x faster                                                            |
| logging_silent             | 94.4 ns                                                      | 90.5 ns: 1.04x faster                                                            |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                             |
| scimark_lu                 | 98.8 ms                                                      | 95.0 ms: 1.04x faster                                                            |
| 2to3                       | 285 ms                                                       | 274 ms: 1.04x faster                                                             |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.04x faster                                                             |
| spectral_norm              | 91.6 ms                                                      | 89.4 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                            |
| richards                   | 45.7 ms                                                      | 44.9 ms: 1.02x faster                                                            |
| scimark_fft                | 301 ms                                                       | 295 ms: 1.02x faster                                                             |
| richards_super             | 51.3 ms                                                      | 50.6 ms: 1.01x faster                                                            |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                                           |
| crypto_pyaes               | 80.3 ms                                                      | 79.7 ms: 1.01x faster                                                            |
| docutils                   | 2.87 sec                                                     | 2.85 sec: 1.00x faster                                                           |
| unpickle_pure_python       | 210 us                                                       | 210 us: 1.00x slower                                                             |
| regex_dna                  | 239 ms                                                       | 239 ms: 1.00x slower                                                             |
| pyflate                    | 439 ms                                                       | 440 ms: 1.00x slower                                                             |
| sympy_expand               | 484 ms                                                       | 487 ms: 1.01x slower                                                             |
| xml_etree_process          | 58.4 ms                                                      | 58.9 ms: 1.01x slower                                                            |
| hexiom                     | 5.96 ms                                                      | 6.03 ms: 1.01x slower                                                            |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                             |
| sqlite_synth               | 2.77 us                                                      | 2.86 us: 1.03x slower                                                            |
| fannkuch                   | 350 ms                                                       | 362 ms: 1.03x slower                                                             |
| nqueens                    | 89.9 ms                                                      | 93.0 ms: 1.03x slower                                                            |
| regex_v8                   | 23.6 ms                                                      | 24.5 ms: 1.04x slower                                                            |
| async_generators           | 390 ms                                                       | 413 ms: 1.06x slower                                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.51 ms: 1.07x slower                                                            |
| nbody                      | 88.0 ms                                                      | 94.9 ms: 1.08x slower                                                            |
| json                       | 5.12 ms                                                      | 5.57 ms: 1.09x slower                                                            |
| mako                       | 10.0 ms                                                      | 10.9 ms: 1.09x slower                                                            |
| json_loads                 | 24.4 us                                                      | 26.6 us: 1.09x slower                                                            |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.09x slower                                                             |
| telco                      | 6.96 ms                                                      | 7.68 ms: 1.10x slower                                                            |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                            |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.22x slower                                                            |
| coverage                   | 66.7 ms                                                      | 82.3 ms: 1.23x slower                                                            |
| python_startup             | 11.6 ms                                                      | 16.5 ms: 1.42x slower                                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                            |
| gc_traversal               | 3.48 ms                                                      | 6.57 ms: 1.89x slower                                                            |
| bench_mp_pool              | 4.76 ms                                                      | 1.30 sec: 272.64x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, bench_thread_pool
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-10cd875/bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x