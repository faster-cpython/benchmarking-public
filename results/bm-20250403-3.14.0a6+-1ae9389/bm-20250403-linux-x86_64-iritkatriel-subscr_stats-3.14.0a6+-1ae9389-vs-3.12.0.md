# Results vs. 3.12.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 1ae9389
- commit date: 2025-04-03
- overall geometric mean: 1.123x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.9 ms: 1.21x faster                                               |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| regex_effbot   | 3.61 ms                                                | 3.86 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 97.9 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                                |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                               |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                               |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                |
| float                      | 84.7 ms                                                | 69.9 ms: 1.21x faster                                               |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                              |
| dulwich_log                | 68.5 ms                                                | 58.3 ms: 1.18x faster                                               |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                               |
| async_generators           | 463 ms                                                 | 395 ms: 1.17x faster                                                |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                               |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                               |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                               |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 97.9 ms: 1.09x faster                                               |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                               |
| logging_silent             | 104 ns                                                 | 97.0 ns: 1.08x faster                                               |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 736 ms: 1.05x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| scimark_fft                | 382 ms                                                 | 364 ms: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.4 ms: 1.01x faster                                               |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                |
| json                       | 5.26 ms                                                | 5.30 ms: 1.01x slower                                               |
| fannkuch                   | 417 ms                                                 | 427 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.86 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.65 ms: 1.23x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.6 ms: 3.44x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, asyncio_websockets, nbody
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-1ae9389/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-1ae9389.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.123x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x