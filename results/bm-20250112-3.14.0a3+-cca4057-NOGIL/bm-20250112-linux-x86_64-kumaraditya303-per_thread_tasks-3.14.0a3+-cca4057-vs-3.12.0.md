# Results vs. 3.12.0

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: cca4057
- commit date: 2025-01-12
- overall geometric mean: 1.121x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 340 ms: 1.24x slower                                                       |
| docutils       | 2.77 sec                                               | 2.98 sec: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 682 ms: 1.73x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 733 ms: 1.58x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                       |
| async_tree_none            | 472 ms                                                 | 344 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 436 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 583 ms: 1.25x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                       |
| float          | 84.7 ms                                                | 105 ms: 1.24x slower                                                       |
| nbody          | 97.0 ms                                                | 140 ms: 1.44x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                      |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                      |
| regex_compile  | 148 ms                                                 | 162 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.36 sec: 1.01x slower                                                     |
| json_loads           | 28.5 us                                                | 29.6 us: 1.04x slower                                                      |
| xml_etree_generate   | 89.2 ms                                                | 96.9 ms: 1.09x slower                                                      |
| xml_etree_process    | 61.7 ms                                                | 73.2 ms: 1.19x slower                                                      |
| json_dumps           | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 310 us: 1.35x slower                                                       |
| pickle_pure_python   | 324 us                                                 | 472 us: 1.46x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.62 ms: 1.39x slower                                                      |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.63x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 45.9 ms: 1.33x slower                                                      |
| mako            | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.42x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 682 ms: 1.73x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 733 ms: 1.58x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.48x faster                                                       |
| async_tree_none            | 472 ms                                                 | 344 ms: 1.37x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 536 ms: 1.35x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 436 ms: 1.33x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 583 ms: 1.25x faster                                                       |
| deepcopy                   | 371 us                                                 | 315 us: 1.18x faster                                                       |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.46 ms: 1.04x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.32 us: 1.01x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 40.4 us: 1.01x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                       |
| tomli_loads                | 2.33 sec                                               | 2.36 sec: 1.01x slower                                                     |
| json_loads                 | 28.5 us                                                | 29.6 us: 1.04x slower                                                      |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                       |
| async_generators           | 463 ms                                                 | 486 ms: 1.05x slower                                                       |
| spectral_norm              | 115 ms                                                 | 123 ms: 1.07x slower                                                       |
| docutils                   | 2.77 sec                                               | 2.98 sec: 1.07x slower                                                     |
| sympy_sum                  | 169 ms                                                 | 182 ms: 1.08x slower                                                       |
| xml_etree_generate         | 89.2 ms                                                | 96.9 ms: 1.09x slower                                                      |
| dulwich_log                | 68.5 ms                                                | 74.8 ms: 1.09x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                      |
| regex_compile              | 148 ms                                                 | 162 ms: 1.09x slower                                                       |
| scimark_fft                | 382 ms                                                 | 418 ms: 1.09x slower                                                       |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                      |
| sympy_str                  | 300 ms                                                 | 333 ms: 1.11x slower                                                       |
| mdp                        | 2.63 sec                                               | 2.93 sec: 1.11x slower                                                     |
| crypto_pyaes               | 81.9 ms                                                | 91.3 ms: 1.12x slower                                                      |
| sympy_integrate            | 21.4 ms                                                | 24.4 ms: 1.14x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.35 sec: 1.14x slower                                                     |
| meteor_contest             | 112 ms                                                 | 130 ms: 1.15x slower                                                       |
| sympy_expand               | 478 ms                                                 | 552 ms: 1.15x slower                                                       |
| comprehensions             | 21.8 us                                                | 25.3 us: 1.16x slower                                                      |
| generators                 | 31.2 ms                                                | 36.7 ms: 1.18x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 130 ms: 1.18x slower                                                       |
| nqueens                    | 83.3 ms                                                | 98.3 ms: 1.18x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 73.2 ms: 1.19x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 65.2 ms: 1.19x slower                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.02 ms: 1.19x slower                                                      |
| logging_format             | 7.23 us                                                | 8.71 us: 1.20x slower                                                      |
| logging_simple             | 6.46 us                                                | 7.81 us: 1.21x slower                                                      |
| fannkuch                   | 417 ms                                                 | 507 ms: 1.21x slower                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 180 ms: 1.23x slower                                                       |
| pprint_safe_repr           | 776 ms                                                 | 955 ms: 1.23x slower                                                       |
| float                      | 84.7 ms                                                | 105 ms: 1.24x slower                                                       |
| 2to3                       | 274 ms                                                 | 340 ms: 1.24x slower                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 23.6 ms: 1.26x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.98 sec: 1.26x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                      |
| pyflate                    | 482 ms                                                 | 621 ms: 1.29x slower                                                       |
| telco                      | 7.10 ms                                                | 9.18 ms: 1.29x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 207 us: 1.31x slower                                                       |
| django_template            | 34.6 ms                                                | 45.9 ms: 1.33x slower                                                      |
| scimark_lu                 | 118 ms                                                 | 157 ms: 1.33x slower                                                       |
| unpickle_pure_python       | 230 us                                                 | 310 us: 1.35x slower                                                       |
| richards                   | 45.8 ms                                                | 62.5 ms: 1.36x slower                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 103 ms: 1.37x slower                                                       |
| chaos                      | 67.0 ms                                                | 92.4 ms: 1.38x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 9.62 ms: 1.39x slower                                                      |
| richards_super             | 51.5 ms                                                | 72.4 ms: 1.40x slower                                                      |
| hexiom                     | 6.41 ms                                                | 9.07 ms: 1.41x slower                                                      |
| scimark_sor                | 129 ms                                                 | 183 ms: 1.42x slower                                                       |
| coverage                   | 72.7 ms                                                | 103 ms: 1.42x slower                                                       |
| nbody                      | 97.0 ms                                                | 140 ms: 1.44x slower                                                       |
| pickle_pure_python         | 324 us                                                 | 472 us: 1.46x slower                                                       |
| raytrace                   | 312 ms                                                 | 470 ms: 1.50x slower                                                       |
| sqlglot_transpile          | 1.68 ms                                                | 2.56 ms: 1.52x slower                                                      |
| mako                       | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                      |
| go                         | 139 ms                                                 | 214 ms: 1.53x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.35 ms: 1.59x slower                                                      |
| sqlglot_parse              | 1.36 ms                                                | 2.19 ms: 1.61x slower                                                      |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.63x slower                                                      |
| logging_silent             | 104 ns                                                 | 179 ns: 1.71x slower                                                       |
| deltablue                  | 3.72 ms                                                | 6.93 ms: 1.87x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 3.55 ms: 4.21x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.18x slower                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250112-3.14.0a3+-cca4057-NOGIL/bm-20250112-linux-x86_64-kumaraditya303-per_thread_tasks-3.14.0a3+-cca4057.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.30x