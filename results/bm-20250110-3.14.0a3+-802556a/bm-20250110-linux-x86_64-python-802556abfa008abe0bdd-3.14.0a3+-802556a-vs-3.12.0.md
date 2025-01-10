# Results vs. 3.12.0

- fork: python
- ref: 802556abfa008abe0bdd
- machine: linux-x86_64
- commit hash: 802556a
- commit date: 2025-01-10
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 588 ms: 2.01x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 461 ms: 1.57x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.7 ms: 1.16x faster                                                  |
| nbody          | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                  |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                  |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 96.9 ms: 1.10x faster                                                  |
| json_loads           | 28.5 us                                                | 26.7 us: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| mako            | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 588 ms: 2.01x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 461 ms: 1.57x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.0 us: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.6 ms: 1.24x faster                                                  |
| go                         | 139 ms                                                 | 118 ms: 1.18x faster                                                   |
| logging_format             | 7.23 us                                                | 6.15 us: 1.18x faster                                                  |
| float                      | 84.7 ms                                                | 72.7 ms: 1.16x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                  |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                   |
| generators                 | 31.2 ms                                                | 27.4 ms: 1.14x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 72.1 ms: 1.14x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                  |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 96.9 ms: 1.10x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                  |
| scimark_fft                | 382 ms                                                 | 349 ms: 1.09x faster                                                   |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                  |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.7 us: 1.07x faster                                                  |
| json                       | 5.26 ms                                                | 4.93 ms: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 52.5 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.87 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.04x faster                                                  |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                                   |
| nbody                      | 97.0 ms                                                | 93.8 ms: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| richards                   | 45.8 ms                                                | 45.2 ms: 1.02x faster                                                  |
| fannkuch                   | 417 ms                                                 | 412 ms: 1.01x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.35 ms: 1.01x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.61 sec: 1.01x faster                                                 |
| richards_super             | 51.5 ms                                                | 51.2 ms: 1.01x faster                                                  |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                   |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                   |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                   |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 863 us: 1.03x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                  |
| telco                      | 7.10 ms                                                | 7.74 ms: 1.09x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.8 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250110-3.14.0a3+-802556a/bm-20250110-linux-x86_64-python-802556abfa008abe0bdd-3.14.0a3+-802556a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.09x