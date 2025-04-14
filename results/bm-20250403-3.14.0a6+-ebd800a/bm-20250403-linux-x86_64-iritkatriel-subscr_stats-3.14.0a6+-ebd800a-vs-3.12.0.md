# Results vs. 3.12.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: ebd800a
- commit date: 2025-04-03
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| nbody          | 97.0 ms                                                | 96.6 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.02x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.76 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                               |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                               |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                               |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                               |
| go                         | 139 ms                                                 | 114 ms: 1.23x faster                                                |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                                |
| dulwich_log                | 68.5 ms                                                | 58.1 ms: 1.18x faster                                               |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                |
| spectral_norm              | 115 ms                                                 | 97.7 ms: 1.18x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                               |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                               |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                               |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                               |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                               |
| scimark_fft                | 382 ms                                                 | 346 ms: 1.10x faster                                                |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                               |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                               |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.8 ms: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                               |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 742 ms: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 458 ms: 1.04x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                              |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                               |
| pyflate                    | 482 ms                                                 | 468 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                               |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                               |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.02x faster                                               |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.8 ms: 1.01x faster                                               |
| nbody                      | 97.0 ms                                                | 96.6 ms: 1.00x faster                                               |
| fannkuch                   | 417 ms                                                 | 426 ms: 1.02x slower                                                |
| bench_thread_pool          | 842 us                                                 | 871 us: 1.04x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                |
| regex_effbot               | 3.61 ms                                                | 3.76 ms: 1.04x slower                                               |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                               |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                               |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (3): pickle_pure_python, asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-ebd800a/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-ebd800a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x