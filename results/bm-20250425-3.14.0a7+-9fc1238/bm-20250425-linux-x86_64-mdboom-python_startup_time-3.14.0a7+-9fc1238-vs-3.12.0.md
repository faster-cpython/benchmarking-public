# Results vs. 3.12.0

- fork: mdboom
- ref: python_startup_time
- machine: linux-x86_64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                  |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                 |
| nbody          | 97.0 ms                                                | 98.7 ms: 1.02x slower                                                 |
| pidigits       | 187 ms                                                 | 194 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                 |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                 |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.31 ms: 1.05x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                 |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                  |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.3 us: 1.44x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.29x faster                                                 |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                 |
| raytrace                   | 312 ms                                                 | 262 ms: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| chaos                      | 67.0 ms                                                | 57.1 ms: 1.17x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                |
| async_generators           | 463 ms                                                 | 398 ms: 1.16x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 59.0 ms: 1.16x faster                                                 |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                                 |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.13x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                                 |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                 |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                 |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| richards                   | 45.8 ms                                                | 42.7 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                                 |
| richards_super             | 51.5 ms                                                | 48.5 ms: 1.06x faster                                                 |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                 |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                 |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 80.9 ms: 1.03x faster                                                 |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.34 ms: 1.01x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| nbody                      | 97.0 ms                                                | 98.7 ms: 1.02x slower                                                 |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                  |
| pidigits                   | 187 ms                                                 | 194 ms: 1.04x slower                                                  |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 883 us: 1.05x slower                                                  |
| json                       | 5.26 ms                                                | 5.53 ms: 1.05x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.31 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                 |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                 |
| coverage                   | 72.7 ms                                                | 93.3 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.00 ms: 1.32x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-linux-x86_64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x