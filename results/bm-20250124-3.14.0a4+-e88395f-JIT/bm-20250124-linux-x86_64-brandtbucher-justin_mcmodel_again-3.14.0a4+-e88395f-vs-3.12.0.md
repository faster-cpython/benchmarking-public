# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: e88395f
- commit date: 2025-01-24
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 63.2 ms: 1.34x faster                                                        |
| nbody          | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                        |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                         |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                        |
| json_loads           | 28.5 us                                                | 35.0 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 274 ms: 1.72x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 340 ms: 1.70x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                         |
| deepcopy                   | 371 us                                                 | 264 us: 1.40x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                        |
| float                      | 84.7 ms                                                | 63.2 ms: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.28x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 67.0 ms: 1.22x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 61.8 ms: 1.22x faster                                                        |
| nbody                      | 97.0 ms                                                | 80.4 ms: 1.21x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                        |
| spectral_norm              | 115 ms                                                 | 96.1 ms: 1.20x faster                                                        |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.18x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                         |
| chaos                      | 67.0 ms                                                | 56.9 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                        |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| scimark_sor                | 129 ms                                                 | 113 ms: 1.14x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                         |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                        |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                                        |
| richards                   | 45.8 ms                                                | 41.3 ms: 1.11x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.8 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 711 ms: 1.09x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                        |
| fannkuch                   | 417 ms                                                 | 384 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.66 ms: 1.08x faster                                                        |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                       |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                        |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| django_template            | 34.6 ms                                                | 33.7 ms: 1.03x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                        |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                         |
| nqueens                    | 83.3 ms                                                | 89.6 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                        |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.12 ms: 1.11x slower                                                        |
| json                       | 5.26 ms                                                | 5.95 ms: 1.13x slower                                                        |
| generators                 | 31.2 ms                                                | 35.8 ms: 1.15x slower                                                        |
| json_loads                 | 28.5 us                                                | 35.0 us: 1.23x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.3 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (3): sqlglot_optimize, regex_dna, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250124-3.14.0a4+-e88395f-JIT/bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.45x