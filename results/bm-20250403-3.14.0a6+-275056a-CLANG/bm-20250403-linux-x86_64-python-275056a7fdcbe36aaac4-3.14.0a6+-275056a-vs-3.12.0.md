# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.166x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 244 ms: 1.13x faster                                                   |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 304 ms: 1.90x faster                                                   |
| async_tree_none            | 472 ms                                                 | 253 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.79x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                  |
| nbody          | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                  |
| pidigits       | 187 ms                                                 | 201 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 124 ms: 1.20x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                  |
| regex_dna      | 212 ms                                                 | 188 ms: 1.13x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 210 us: 1.09x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                                   |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.07 ms: 1.16x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                  |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.20 sec: 2.20x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.94x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 304 ms: 1.90x faster                                                   |
| async_tree_none            | 472 ms                                                 | 253 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 243 ms: 1.85x faster                                                   |
| deepcopy                   | 371 us                                                 | 243 us: 1.53x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.44x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.53 us: 1.32x faster                                                  |
| go                         | 139 ms                                                 | 106 ms: 1.31x faster                                                   |
| spectral_norm              | 115 ms                                                 | 87.5 ms: 1.31x faster                                                  |
| pathlib                    | 19.3 ms                                                | 14.9 ms: 1.30x faster                                                  |
| scimark_fft                | 382 ms                                                 | 296 ms: 1.29x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 3.96 ms: 1.28x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 58.8 ms: 1.28x faster                                                  |
| deltablue                  | 3.72 ms                                                | 2.92 ms: 1.27x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                 |
| raytrace                   | 312 ms                                                 | 249 ms: 1.25x faster                                                   |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                  |
| chaos                      | 67.0 ms                                                | 53.9 ms: 1.24x faster                                                  |
| scimark_sor                | 129 ms                                                 | 107 ms: 1.21x faster                                                   |
| async_generators           | 463 ms                                                 | 383 ms: 1.21x faster                                                   |
| logging_format             | 7.23 us                                                | 5.99 us: 1.21x faster                                                  |
| regex_compile              | 148 ms                                                 | 124 ms: 1.20x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 57.8 ms: 1.18x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                  |
| pyflate                    | 482 ms                                                 | 410 ms: 1.18x faster                                                   |
| logging_silent             | 104 ns                                                 | 88.8 ns: 1.18x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.08 ms: 1.17x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 145 ms: 1.17x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 18.4 ms: 1.16x faster                                                  |
| nbody                      | 97.0 ms                                                | 83.5 ms: 1.16x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.15x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 71.0 ms: 1.15x faster                                                  |
| richards                   | 45.8 ms                                                | 39.8 ms: 1.15x faster                                                  |
| sympy_str                  | 300 ms                                                 | 261 ms: 1.15x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| regex_dna                  | 212 ms                                                 | 188 ms: 1.13x faster                                                   |
| 2to3                       | 274 ms                                                 | 244 ms: 1.13x faster                                                   |
| richards_super             | 51.5 ms                                                | 46.0 ms: 1.12x faster                                                  |
| hexiom                     | 6.41 ms                                                | 5.79 ms: 1.11x faster                                                  |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 210 us: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                 |
| coroutines                 | 23.2 ms                                                | 21.5 ms: 1.08x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                   |
| sympy_expand               | 478 ms                                                 | 448 ms: 1.07x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 111 ms: 1.06x faster                                                   |
| nqueens                    | 83.3 ms                                                | 78.7 ms: 1.06x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.68 us: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| typing_runtime_protocols   | 158 us                                                 | 154 us: 1.03x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                  |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                  |
| telco                      | 7.10 ms                                                | 7.50 ms: 1.06x slower                                                  |
| pidigits                   | 187 ms                                                 | 201 ms: 1.08x slower                                                   |
| coverage                   | 72.7 ms                                                | 81.1 ms: 1.12x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.07 ms: 1.16x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 12.5 ms: 1.20x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.70x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.4 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, bench_thread_pool, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.166x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.11x