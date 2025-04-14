# Results vs. 3.12.0

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: d737f33
- commit date: 2025-03-23
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                         |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.5 ms: 1.20x faster                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| nbody          | 97.0 ms                                                | 97.4 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.03x faster                                        |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                        |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                        |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                         |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                         |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                        |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.39x slower                                        |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.11x faster                                        |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.94x faster                                         |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                         |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                        |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                         |
| float                      | 84.7 ms                                                | 70.5 ms: 1.20x faster                                        |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                       |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                        |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                        |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                        |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                         |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                        |
| sympy_sum                  | 169 ms                                                 | 145 ms: 1.17x faster                                         |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                        |
| async_generators           | 463 ms                                                 | 399 ms: 1.16x faster                                         |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                        |
| sympy_str                  | 300 ms                                                 | 260 ms: 1.15x faster                                         |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                         |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                         |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.11x faster                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                        |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                        |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                        |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                        |
| scimark_fft                | 382 ms                                                 | 351 ms: 1.09x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 76.1 ms: 1.08x faster                                        |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                         |
| mdp                        | 2.63 sec                                               | 2.47 sec: 1.07x faster                                       |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                       |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                        |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                         |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                        |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 58.3 ms: 1.06x faster                                        |
| logging_silent             | 104 ns                                                 | 98.9 ns: 1.06x faster                                        |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                         |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                        |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.89 ms: 1.03x faster                                        |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.03x faster                                        |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                        |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                        |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                         |
| nbody                      | 97.0 ms                                                | 97.4 ms: 1.00x slower                                        |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                        |
| nqueens                    | 83.3 ms                                                | 85.7 ms: 1.03x slower                                        |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                         |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                         |
| fannkuch                   | 417 ms                                                 | 436 ms: 1.04x slower                                         |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                        |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                        |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                         |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                        |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                        |
| coverage                   | 72.7 ms                                                | 92.0 ms: 1.27x slower                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.39x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.6 ms: 3.48x slower                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (4): scimark_lu, coroutines, asyncio_websockets, pycparser
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250323-3.14.0a6+-d737f33/bm-20250323-linux-x86_64-iritkatriel-tuple-3.14.0a6+-d737f33.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x