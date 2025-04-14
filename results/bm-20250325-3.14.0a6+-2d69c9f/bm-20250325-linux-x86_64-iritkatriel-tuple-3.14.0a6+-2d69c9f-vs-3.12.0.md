# Results vs. 3.12.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 2d69c9f
- commit date: 2025-03-25
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                         |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.81x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| nbody          | 97.0 ms                                                | 96.4 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                        |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                        |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                        |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                         |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                         |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                        |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                        |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                        |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                         |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 318 ms: 1.81x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.41x faster                                        |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                        |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                         |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.09 ms: 1.20x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                       |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                         |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                         |
| dulwich_log                | 68.5 ms                                                | 58.4 ms: 1.17x faster                                        |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                        |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                        |
| async_generators           | 463 ms                                                 | 396 ms: 1.17x faster                                         |
| spectral_norm              | 115 ms                                                 | 98.4 ms: 1.17x faster                                        |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                        |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                        |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                         |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                         |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                         |
| scimark_fft                | 382 ms                                                 | 344 ms: 1.11x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                        |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                        |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 76.1 ms: 1.08x faster                                        |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                         |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                         |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                         |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                        |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                        |
| logging_silent             | 104 ns                                                 | 98.6 ns: 1.06x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                       |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                       |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                         |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                         |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                        |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                         |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                        |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                         |
| nqueens                    | 83.3 ms                                                | 82.7 ms: 1.01x faster                                        |
| nbody                      | 97.0 ms                                                | 96.4 ms: 1.01x faster                                        |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                        |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                         |
| fannkuch                   | 417 ms                                                 | 431 ms: 1.03x slower                                         |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                         |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                        |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                        |
| coverage                   | 72.7 ms                                                | 91.4 ms: 1.26x slower                                        |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                        |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250325-3.14.0a6+-2d69c9f/bm-20250325-linux-x86_64-iritkatriel-tuple-3.14.0a6+-2d69c9f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x