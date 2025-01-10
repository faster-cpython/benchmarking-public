# Results vs. 3.12.0

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.127x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 346 ms: 1.26x slower                                                   |
| docutils       | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 680 ms: 1.74x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 724 ms: 1.60x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 291 ms: 1.54x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                   |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 578 ms: 1.26x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.46x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                                   |
| float          | 84.7 ms                                                | 107 ms: 1.26x slower                                                   |
| nbody          | 97.0 ms                                                | 135 ms: 1.39x slower                                                   |
| Geometric mean | (ref)                                                  | 1.19x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                  |
| regex_dna      | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| regex_compile  | 148 ms                                                 | 164 ms: 1.10x slower                                                   |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                   |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                  |
| tomli_loads          | 2.33 sec                                               | 2.48 sec: 1.07x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 72.4 ms: 1.17x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.2 ms: 1.27x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 313 us: 1.36x slower                                                   |
| pickle_pure_python   | 324 us                                                 | 475 us: 1.47x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.60 ms: 1.38x slower                                                  |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 46.9 ms: 1.36x slower                                                  |
| mako            | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.44x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 680 ms: 1.74x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 724 ms: 1.60x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 291 ms: 1.54x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                                   |
| async_tree_none            | 472 ms                                                 | 335 ms: 1.41x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 529 ms: 1.37x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 431 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 578 ms: 1.26x faster                                                   |
| deepcopy                   | 371 us                                                 | 316 us: 1.18x faster                                                   |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 96.2 ms: 1.11x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 3.67 ms: 1.03x faster                                                  |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 40.2 us: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.36 us: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                  |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.07x slower                                                   |
| tomli_loads                | 2.33 sec                                               | 2.48 sec: 1.07x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.96 sec: 1.07x slower                                                 |
| async_generators           | 463 ms                                                 | 497 ms: 1.07x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 183 ms: 1.08x slower                                                   |
| spectral_norm              | 115 ms                                                 | 125 ms: 1.09x slower                                                   |
| dulwich_log                | 68.5 ms                                                | 75.1 ms: 1.10x slower                                                  |
| scimark_fft                | 382 ms                                                 | 419 ms: 1.10x slower                                                   |
| regex_compile              | 148 ms                                                 | 164 ms: 1.10x slower                                                   |
| sympy_str                  | 300 ms                                                 | 334 ms: 1.11x slower                                                   |
| crypto_pyaes               | 81.9 ms                                                | 91.9 ms: 1.12x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 24.5 ms: 1.15x slower                                                  |
| mdp                        | 2.63 sec                                               | 3.03 sec: 1.15x slower                                                 |
| coroutines                 | 23.2 ms                                                | 26.7 ms: 1.15x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.36 sec: 1.15x slower                                                 |
| sympy_expand               | 478 ms                                                 | 556 ms: 1.16x slower                                                   |
| comprehensions             | 21.8 us                                                | 25.4 us: 1.16x slower                                                  |
| meteor_contest             | 112 ms                                                 | 131 ms: 1.17x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 129 ms: 1.17x slower                                                   |
| xml_etree_process          | 61.7 ms                                                | 72.4 ms: 1.17x slower                                                  |
| generators                 | 31.2 ms                                                | 36.9 ms: 1.18x slower                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 64.9 ms: 1.18x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.08 ms: 1.20x slower                                                  |
| nqueens                    | 83.3 ms                                                | 100 ms: 1.21x slower                                                   |
| logging_simple             | 6.46 us                                                | 7.84 us: 1.21x slower                                                  |
| logging_format             | 7.23 us                                                | 8.79 us: 1.22x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 958 ms: 1.23x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 181 ms: 1.24x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 23.4 ms: 1.25x slower                                                  |
| fannkuch                   | 417 ms                                                 | 525 ms: 1.26x slower                                                   |
| 2to3                       | 274 ms                                                 | 346 ms: 1.26x slower                                                   |
| float                      | 84.7 ms                                                | 107 ms: 1.26x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 13.2 ms: 1.27x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.00 sec: 1.28x slower                                                 |
| telco                      | 7.10 ms                                                | 9.14 ms: 1.29x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 155 ms: 1.31x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 208 us: 1.32x slower                                                   |
| django_template            | 34.6 ms                                                | 46.9 ms: 1.36x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 313 us: 1.36x slower                                                   |
| richards                   | 45.8 ms                                                | 62.5 ms: 1.36x slower                                                  |
| pyflate                    | 482 ms                                                 | 659 ms: 1.37x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 9.60 ms: 1.38x slower                                                  |
| nbody                      | 97.0 ms                                                | 135 ms: 1.39x slower                                                   |
| chaos                      | 67.0 ms                                                | 93.4 ms: 1.40x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 105 ms: 1.40x slower                                                   |
| coverage                   | 72.7 ms                                                | 102 ms: 1.40x slower                                                   |
| richards_super             | 51.5 ms                                                | 73.9 ms: 1.43x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 475 us: 1.47x slower                                                   |
| hexiom                     | 6.41 ms                                                | 9.49 ms: 1.48x slower                                                  |
| raytrace                   | 312 ms                                                 | 471 ms: 1.51x slower                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 2.54 ms: 1.51x slower                                                  |
| mako                       | 11.9 ms                                                | 18.2 ms: 1.53x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.34 ms: 1.59x slower                                                  |
| go                         | 139 ms                                                 | 222 ms: 1.59x slower                                                   |
| sqlglot_parse              | 1.36 ms                                                | 2.19 ms: 1.61x slower                                                  |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                  |
| scimark_sor                | 129 ms                                                 | 211 ms: 1.63x slower                                                   |
| logging_silent             | 104 ns                                                 | 175 ns: 1.68x slower                                                   |
| deltablue                  | 3.72 ms                                                | 7.04 ms: 1.90x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 95.3 ms: 3.97x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.56 ms: 4.23x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.18x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, sqlite_synth
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-b20a605-NOGIL/bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.127x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.30x