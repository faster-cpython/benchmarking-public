# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 249 ms: 1.10x faster                                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                  |
| nbody          | 97.0 ms                                                | 91.3 ms: 1.06x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.19x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                  |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                   |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                   |
| deepcopy                   | 371 us                                                 | 253 us: 1.47x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                  |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                  |
| raytrace                   | 312 ms                                                 | 258 ms: 1.21x faster                                                   |
| float                      | 84.7 ms                                                | 70.2 ms: 1.21x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| regex_compile              | 148 ms                                                 | 124 ms: 1.19x faster                                                   |
| chaos                      | 67.0 ms                                                | 56.5 ms: 1.18x faster                                                  |
| async_generators           | 463 ms                                                 | 391 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                  |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                                  |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                   |
| logging_silent             | 104 ns                                                 | 94.4 ns: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                  |
| 2to3                       | 274 ms                                                 | 249 ms: 1.10x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.64 ms: 1.09x faster                                                  |
| pyflate                    | 482 ms                                                 | 445 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.35 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                                   |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| nbody                      | 97.0 ms                                                | 91.3 ms: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.05x faster                                                  |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                                  |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                                   |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                                  |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.4 ms: 1.16x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.17 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.130x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x