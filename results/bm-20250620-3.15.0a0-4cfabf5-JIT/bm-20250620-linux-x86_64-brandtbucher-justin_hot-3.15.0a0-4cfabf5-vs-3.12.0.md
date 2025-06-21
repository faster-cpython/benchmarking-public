# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                              |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                              |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.9 ms: 1.31x faster                                             |
| nbody          | 97.0 ms                                                | 92.2 ms: 1.05x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                             |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.90 sec: 1.23x faster                                            |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                              |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                             |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                             |
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                             |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.27 sec: 2.07x faster                                            |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                              |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                              |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                             |
| richards                   | 45.8 ms                                                | 34.1 ms: 1.34x faster                                             |
| richards_super             | 51.5 ms                                                | 39.4 ms: 1.31x faster                                             |
| float                      | 84.7 ms                                                | 64.9 ms: 1.31x faster                                             |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.90 sec: 1.23x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.12 ms: 1.19x faster                                             |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                              |
| scimark_fft                | 382 ms                                                 | 330 ms: 1.16x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                             |
| go                         | 139 ms                                                 | 122 ms: 1.15x faster                                              |
| pyflate                    | 482 ms                                                 | 422 ms: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                             |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                              |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                             |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                             |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                             |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 74.9 ms: 1.09x faster                                             |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                             |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                              |
| chaos                      | 67.0 ms                                                | 62.4 ms: 1.07x faster                                             |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                              |
| logging_format             | 7.23 us                                                | 6.83 us: 1.06x faster                                             |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                             |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| nbody                      | 97.0 ms                                                | 92.2 ms: 1.05x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                              |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                            |
| logging_simple             | 6.46 us                                                | 6.25 us: 1.03x faster                                             |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                             |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                             |
| generators                 | 31.2 ms                                                | 30.9 ms: 1.01x faster                                             |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.00x faster                                             |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                             |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                             |
| hexiom                     | 6.41 ms                                                | 6.44 ms: 1.00x slower                                             |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                              |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                            |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                              |
| pprint_safe_repr           | 776 ms                                                 | 835 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                             |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                             |
| coroutines                 | 23.2 ms                                                | 25.3 ms: 1.09x slower                                             |
| coverage                   | 72.7 ms                                                | 87.6 ms: 1.20x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                             |
| logging_silent             | 104 ns                                                 | 472 ns: 4.52x slower                                              |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, json, pickle_pure_python
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x