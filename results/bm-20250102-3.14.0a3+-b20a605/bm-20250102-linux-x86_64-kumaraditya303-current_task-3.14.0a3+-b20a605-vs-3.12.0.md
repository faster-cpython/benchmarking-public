# Results vs. 3.12.0

- fork: kumaraditya303
- ref: current_task
- machine: linux-x86_64
- commit hash: b20a605
- commit date: 2025-01-02
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 587 ms: 2.01x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 300 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.91x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                  |
| nbody          | 97.0 ms                                                | 94.7 ms: 1.02x faster                                                  |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_dna      | 212 ms                                                 | 213 ms: 1.01x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 96.8 ms: 1.10x faster                                                  |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 587 ms: 2.01x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 300 ms: 1.91x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.91x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 242 ms: 1.86x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.1 us: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 68.8 ms: 1.19x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                  |
| float                      | 84.7 ms                                                | 72.8 ms: 1.16x faster                                                  |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                   |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.3 ms: 1.12x faster                                                  |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                  |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 96.8 ms: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                   |
| async_generators           | 463 ms                                                 | 422 ms: 1.10x faster                                                   |
| scimark_fft                | 382 ms                                                 | 350 ms: 1.09x faster                                                   |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 716 ms: 1.08x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 63.8 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                  |
| json                       | 5.26 ms                                                | 4.95 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 84.1 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.06x faster                                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.05x faster                                                   |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.05x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                                  |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| richards                   | 45.8 ms                                                | 44.5 ms: 1.03x faster                                                  |
| nbody                      | 97.0 ms                                                | 94.7 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.28 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                   |
| richards_super             | 51.5 ms                                                | 50.6 ms: 1.02x faster                                                  |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                   |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 868 us: 1.03x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 25.3 ms: 1.09x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                  |
| telco                      | 7.10 ms                                                | 7.84 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 82.4 ms: 1.13x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.26x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): pycparser, asyncio_websockets, coroutines
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250102-3.14.0a3+-b20a605/bm-20250102-linux-x86_64-kumaraditya303-current_task-3.14.0a3+-b20a605.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x