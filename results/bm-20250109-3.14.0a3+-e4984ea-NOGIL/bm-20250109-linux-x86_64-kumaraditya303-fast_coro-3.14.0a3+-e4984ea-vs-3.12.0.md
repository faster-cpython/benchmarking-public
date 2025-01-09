# Results vs. 3.12.0

- fork: kumaraditya303
- ref: fast_coro
- machine: linux-x86_64
- commit hash: e4984ea
- commit date: 2025-01-09
- overall geometric mean: 1.124x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 342 ms: 1.25x slower                                                |
| docutils       | 2.77 sec                                               | 3.01 sec: 1.09x slower                                              |
| Geometric mean | (ref)                                                  | 1.16x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 683 ms: 1.73x faster                                                |
| async_tree_io              | 1.16 sec                                               | 732 ms: 1.58x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                |
| async_tree_none            | 472 ms                                                 | 341 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.34x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 435 ms: 1.33x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 587 ms: 1.24x faster                                                |
| Geometric mean             | (ref)                                                  | 1.44x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 187 ms                                                 | 181 ms: 1.03x faster                                                |
| float          | 84.7 ms                                                | 103 ms: 1.22x slower                                                |
| nbody          | 97.0 ms                                                | 135 ms: 1.39x slower                                                |
| Geometric mean | (ref)                                                  | 1.18x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.60 ms: 1.00x faster                                               |
| regex_compile  | 148 ms                                                 | 161 ms: 1.09x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| regex_dna      | 212 ms                                                 | 233 ms: 1.10x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.3 ms: 1.11x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| tomli_loads          | 2.33 sec                                               | 2.35 sec: 1.01x slower                                              |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| xml_etree_generate   | 89.2 ms                                                | 100.0 ms: 1.12x slower                                              |
| xml_etree_process    | 61.7 ms                                                | 74.2 ms: 1.20x slower                                               |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                               |
| unpickle_pure_python | 230 us                                                 | 309 us: 1.35x slower                                                |
| pickle_pure_python   | 324 us                                                 | 468 us: 1.45x slower                                                |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.65 ms: 1.39x slower                                               |
| python_startup         | 9.55 ms                                                | 15.6 ms: 1.63x slower                                               |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 46.6 ms: 1.35x slower                                               |
| mako            | 11.9 ms                                                | 18.1 ms: 1.52x slower                                               |
| Geometric mean  | (ref)                                                  | 1.43x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 683 ms: 1.73x faster                                                |
| async_tree_io              | 1.16 sec                                               | 732 ms: 1.58x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 294 ms: 1.53x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 387 ms: 1.49x faster                                                |
| async_tree_none            | 472 ms                                                 | 341 ms: 1.38x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 544 ms: 1.34x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 435 ms: 1.33x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 587 ms: 1.24x faster                                                |
| deepcopy                   | 371 us                                                 | 317 us: 1.17x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 96.3 ms: 1.11x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                |
| pidigits                   | 187 ms                                                 | 181 ms: 1.03x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 40.3 us: 1.01x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.60 ms: 1.00x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.35 sec: 1.01x slower                                              |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                               |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                               |
| async_generators           | 463 ms                                                 | 496 ms: 1.07x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.08 ms: 1.08x slower                                               |
| sympy_sum                  | 169 ms                                                 | 184 ms: 1.09x slower                                                |
| docutils                   | 2.77 sec                                               | 3.01 sec: 1.09x slower                                              |
| spectral_norm              | 115 ms                                                 | 125 ms: 1.09x slower                                                |
| regex_compile              | 148 ms                                                 | 161 ms: 1.09x slower                                                |
| dulwich_log                | 68.5 ms                                                | 74.9 ms: 1.09x slower                                               |
| scimark_fft                | 382 ms                                                 | 418 ms: 1.09x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.4 ms: 1.10x slower                                               |
| regex_dna                  | 212 ms                                                 | 233 ms: 1.10x slower                                                |
| sympy_str                  | 300 ms                                                 | 333 ms: 1.11x slower                                                |
| xml_etree_generate         | 89.2 ms                                                | 100.0 ms: 1.12x slower                                              |
| crypto_pyaes               | 81.9 ms                                                | 91.8 ms: 1.12x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 24.3 ms: 1.14x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.34 sec: 1.14x slower                                              |
| mdp                        | 2.63 sec                                               | 3.01 sec: 1.14x slower                                              |
| sympy_expand               | 478 ms                                                 | 555 ms: 1.16x slower                                                |
| nqueens                    | 83.3 ms                                                | 97.8 ms: 1.17x slower                                               |
| sqlglot_normalize          | 110 ms                                                 | 130 ms: 1.18x slower                                                |
| comprehensions             | 21.8 us                                                | 25.6 us: 1.18x slower                                               |
| meteor_contest             | 112 ms                                                 | 133 ms: 1.18x slower                                                |
| generators                 | 31.2 ms                                                | 36.9 ms: 1.18x slower                                               |
| logging_format             | 7.23 us                                                | 8.57 us: 1.19x slower                                               |
| sqlglot_optimize           | 54.8 ms                                                | 65.1 ms: 1.19x slower                                               |
| logging_simple             | 6.46 us                                                | 7.74 us: 1.20x slower                                               |
| xml_etree_process          | 61.7 ms                                                | 74.2 ms: 1.20x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.13 ms: 1.21x slower                                               |
| float                      | 84.7 ms                                                | 103 ms: 1.22x slower                                                |
| pprint_safe_repr           | 776 ms                                                 | 949 ms: 1.22x slower                                                |
| fannkuch                   | 417 ms                                                 | 514 ms: 1.23x slower                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 182 ms: 1.24x slower                                                |
| 2to3                       | 274 ms                                                 | 342 ms: 1.25x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 1.97 sec: 1.25x slower                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 23.6 ms: 1.26x slower                                               |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                               |
| telco                      | 7.10 ms                                                | 9.32 ms: 1.31x slower                                               |
| pyflate                    | 482 ms                                                 | 636 ms: 1.32x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 208 us: 1.32x slower                                                |
| scimark_lu                 | 118 ms                                                 | 158 ms: 1.34x slower                                                |
| unpickle_pure_python       | 230 us                                                 | 309 us: 1.35x slower                                                |
| django_template            | 34.6 ms                                                | 46.6 ms: 1.35x slower                                               |
| richards                   | 45.8 ms                                                | 62.3 ms: 1.36x slower                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 102 ms: 1.36x slower                                                |
| chaos                      | 67.0 ms                                                | 92.1 ms: 1.38x slower                                               |
| richards_super             | 51.5 ms                                                | 70.9 ms: 1.38x slower                                               |
| nbody                      | 97.0 ms                                                | 135 ms: 1.39x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 9.65 ms: 1.39x slower                                               |
| coverage                   | 72.7 ms                                                | 102 ms: 1.40x slower                                                |
| hexiom                     | 6.41 ms                                                | 9.06 ms: 1.41x slower                                               |
| scimark_sor                | 129 ms                                                 | 183 ms: 1.41x slower                                                |
| pickle_pure_python         | 324 us                                                 | 468 us: 1.45x slower                                                |
| sqlglot_transpile          | 1.68 ms                                                | 2.51 ms: 1.49x slower                                               |
| raytrace                   | 312 ms                                                 | 469 ms: 1.50x slower                                                |
| go                         | 139 ms                                                 | 212 ms: 1.52x slower                                                |
| mako                       | 11.9 ms                                                | 18.1 ms: 1.52x slower                                               |
| sqlglot_parse              | 1.36 ms                                                | 2.16 ms: 1.58x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.38 ms: 1.61x slower                                               |
| python_startup             | 9.55 ms                                                | 15.6 ms: 1.63x slower                                               |
| logging_silent             | 104 ns                                                 | 171 ns: 1.64x slower                                                |
| deltablue                  | 3.72 ms                                                | 6.85 ms: 1.84x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 95.3 ms: 3.97x slower                                               |
| bench_thread_pool          | 842 us                                                 | 3.56 ms: 4.23x slower                                               |
| Geometric mean             | (ref)                                                  | 1.18x slower                                                        |

Benchmark hidden because not significant (2): asyncio_websockets, deepcopy_reduce
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250109-3.14.0a3+-e4984ea-NOGIL/bm-20250109-linux-x86_64-kumaraditya303-fast_coro-3.14.0a3+-e4984ea.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.124x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.30x