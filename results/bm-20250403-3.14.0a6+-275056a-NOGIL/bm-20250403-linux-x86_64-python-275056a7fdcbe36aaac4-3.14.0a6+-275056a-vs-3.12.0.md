# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: linux-x86_64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.041x faster
- HPT reliability: 54.12%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 287 ms: 1.05x slower                                                   |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 508 ms: 2.33x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 547 ms: 2.11x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 223 ms: 2.01x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 295 ms: 1.95x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.78x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 449 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.86x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                  |
| pidigits       | 187 ms                                                 | 184 ms: 1.02x faster                                                   |
| nbody          | 97.0 ms                                                | 119 ms: 1.23x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                  |
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 94.0 ms: 1.14x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 147 ms: 1.09x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.17 sec: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 240 us: 1.04x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 93.5 ms: 1.05x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 65.5 ms: 1.06x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 345 us: 1.06x slower                                                   |
| json_loads           | 28.5 us                                                | 32.0 us: 1.12x slower                                                  |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 10.9 ms: 1.58x slower                                                  |
| python_startup         | 9.55 ms                                                | 15.6 ms: 1.63x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 38.5 ms: 1.11x slower                                                  |
| mako            | 11.9 ms                                                | 15.6 ms: 1.31x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 508 ms: 2.33x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 547 ms: 2.11x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 223 ms: 2.01x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 295 ms: 1.95x faster                                                   |
| mdp                        | 2.63 sec                                               | 1.38 sec: 1.91x faster                                                 |
| gc_traversal               | 3.79 ms                                                | 2.03 ms: 1.87x faster                                                  |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.78x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 449 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                   |
| deepcopy                   | 371 us                                                 | 290 us: 1.28x faster                                                   |
| float                      | 84.7 ms                                                | 68.4 ms: 1.24x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 35.8 us: 1.14x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.0 ms: 1.14x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.4 us: 1.12x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.02 us: 1.11x faster                                                  |
| async_generators           | 463 ms                                                 | 423 ms: 1.10x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 62.6 ms: 1.09x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 147 ms: 1.09x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.17 sec: 1.08x faster                                                 |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                 |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                  |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                  |
| chaos                      | 67.0 ms                                                | 65.3 ms: 1.03x faster                                                  |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                   |
| pidigits                   | 187 ms                                                 | 184 ms: 1.02x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.69 ms: 1.01x faster                                                  |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                 |
| logging_simple             | 6.46 us                                                | 6.57 us: 1.02x slower                                                  |
| logging_format             | 7.23 us                                                | 7.36 us: 1.02x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| sympy_str                  | 300 ms                                                 | 308 ms: 1.03x slower                                                   |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                  |
| pyflate                    | 482 ms                                                 | 501 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 240 us: 1.04x slower                                                   |
| 2to3                       | 274 ms                                                 | 287 ms: 1.05x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.05x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 93.5 ms: 1.05x slower                                                  |
| json                       | 5.26 ms                                                | 5.52 ms: 1.05x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 86.5 ms: 1.06x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 65.5 ms: 1.06x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 79.8 ms: 1.06x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 345 us: 1.06x slower                                                   |
| pprint_safe_repr           | 776 ms                                                 | 826 ms: 1.07x slower                                                   |
| nqueens                    | 83.3 ms                                                | 89.8 ms: 1.08x slower                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 158 ms: 1.08x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.70 sec: 1.09x slower                                                 |
| sympy_expand               | 478 ms                                                 | 520 ms: 1.09x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.6 ms: 1.10x slower                                                  |
| richards                   | 45.8 ms                                                | 50.7 ms: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.60 ms: 1.11x slower                                                  |
| django_template            | 34.6 ms                                                | 38.5 ms: 1.11x slower                                                  |
| json_loads                 | 28.5 us                                                | 32.0 us: 1.12x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.20 ms: 1.12x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.68 ms: 1.14x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 135 ms: 1.14x slower                                                   |
| richards_super             | 51.5 ms                                                | 59.0 ms: 1.15x slower                                                  |
| meteor_contest             | 112 ms                                                 | 130 ms: 1.16x slower                                                   |
| fannkuch                   | 417 ms                                                 | 487 ms: 1.17x slower                                                   |
| nbody                      | 97.0 ms                                                | 119 ms: 1.23x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 197 us: 1.25x slower                                                   |
| telco                      | 7.10 ms                                                | 8.99 ms: 1.27x slower                                                  |
| mako                       | 11.9 ms                                                | 15.6 ms: 1.31x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 10.9 ms: 1.58x slower                                                  |
| python_startup             | 9.55 ms                                                | 15.6 ms: 1.63x slower                                                  |
| coverage                   | 72.7 ms                                                | 119 ms: 1.64x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 90.3 ms: 3.76x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.25 ms: 3.86x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, raytrace
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-275056a-NOGIL/bm-20250403-linux-x86_64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 54.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.33x