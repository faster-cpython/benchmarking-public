# Results vs. 3.12.0

- fork: iritkatriel
- ref: subscr_stats
- machine: linux-x86_64
- commit hash: 9e0e134
- commit date: 2025-04-03
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 610 ms: 1.94x faster                                                |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| nbody          | 97.0 ms                                                | 97.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.9 ms: 1.01x faster                                               |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.17x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                               |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                               |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                |
| json_loads           | 28.5 us                                                | 29.5 us: 1.03x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 610 ms: 1.94x faster                                                |
| async_tree_io              | 1.16 sec                                               | 608 ms: 1.90x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 476 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                               |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                               |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                               |
| async_generators           | 463 ms                                                 | 392 ms: 1.18x faster                                                |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                               |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                |
| dulwich_log                | 68.5 ms                                                | 58.5 ms: 1.17x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.17x faster                                              |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                |
| spectral_norm              | 115 ms                                                 | 100.0 ms: 1.15x faster                                              |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                               |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                               |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                               |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                               |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                               |
| logging_silent             | 104 ns                                                 | 96.1 ns: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                               |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| scimark_fft                | 382 ms                                                 | 354 ms: 1.08x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.2 ms: 1.06x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.05x faster                                               |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                               |
| richards_super             | 51.5 ms                                                | 50.0 ms: 1.03x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                               |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                                |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.9 ms: 1.01x faster                                               |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                |
| fannkuch                   | 417 ms                                                 | 419 ms: 1.01x slower                                                |
| nbody                      | 97.0 ms                                                | 97.7 ms: 1.01x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                                |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.03x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.05x slower                                               |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                               |
| coverage                   | 72.7 ms                                                | 82.8 ms: 1.14x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                               |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-9e0e134/bm-20250403-linux-x86_64-iritkatriel-subscr_stats-3.14.0a6+-9e0e134.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x