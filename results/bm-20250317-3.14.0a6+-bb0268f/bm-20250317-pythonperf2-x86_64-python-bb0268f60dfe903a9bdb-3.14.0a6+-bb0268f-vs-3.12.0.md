# Results vs. 3.12.0

- fork: python
- ref: bb0268f60dfe903a9bdb
- machine: linux-x86_64
- commit hash: bb0268f
- commit date: 2025-03-17
- overall geometric mean: 1.019x faster
- HPT reliability: 75.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| docutils       | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 644 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.52x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 71.3 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 99.3 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.07 ms: 1.16x faster                                                        |
| regex_dna      | 239 ms                                                       | 229 ms: 1.04x faster                                                         |
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                       |
| xml_etree_process    | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                        |
| json_loads           | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| pickle_pure_python   | 318 us                                                       | 342 us: 1.08x slower                                                         |
| unpickle_pure_python | 210 us                                                       | 228 us: 1.09x slower                                                         |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                                        |
| mako            | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 644 ms: 1.62x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 655 ms: 1.61x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 342 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 347 ms: 1.57x faster                                                         |
| async_tree_none            | 452 ms                                                       | 290 ms: 1.56x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 278 ms: 1.55x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 520 ms: 1.34x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.6 ms: 1.31x faster                                                        |
| deepcopy                   | 368 us                                                       | 289 us: 1.27x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                        |
| comprehensions             | 21.9 us                                                      | 18.1 us: 1.21x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.07 ms: 1.16x faster                                                        |
| go                         | 150 ms                                                       | 131 ms: 1.14x faster                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.03 us: 1.11x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.1 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 146 ms: 1.09x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 71.3 ms: 1.07x faster                                                        |
| dulwich_log                | 65.4 ms                                                      | 62.6 ms: 1.04x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.04x faster                                                         |
| regex_dna                  | 239 ms                                                       | 229 ms: 1.04x faster                                                         |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.0 ms: 1.04x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                                         |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                         |
| raytrace                   | 298 ms                                                       | 293 ms: 1.02x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.36 us: 1.02x faster                                                        |
| sympy_integrate            | 23.9 ms                                                      | 23.5 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 84.9 ms: 1.01x faster                                                        |
| django_template            | 38.2 ms                                                      | 37.7 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.01x faster                                                       |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 92.0 ms: 1.00x slower                                                        |
| 2to3                       | 285 ms                                                       | 286 ms: 1.00x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.18 sec: 1.01x slower                                                       |
| scimark_sor                | 109 ms                                                       | 110 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.0 ms: 1.01x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 95.7 ns: 1.01x slower                                                        |
| chaos                      | 64.0 ms                                                      | 65.3 ms: 1.02x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.93 sec: 1.02x slower                                                       |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 82.9 ms: 1.03x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                                       |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                                        |
| xml_etree_process          | 58.4 ms                                                      | 60.7 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.40 ms: 1.05x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 94.8 ms: 1.05x slower                                                        |
| scimark_fft                | 301 ms                                                       | 318 ms: 1.05x slower                                                         |
| richards                   | 45.7 ms                                                      | 48.8 ms: 1.07x slower                                                        |
| richards_super             | 51.3 ms                                                      | 55.0 ms: 1.07x slower                                                        |
| json_loads                 | 24.4 us                                                      | 26.1 us: 1.07x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 342 us: 1.08x slower                                                         |
| pyflate                    | 439 ms                                                       | 474 ms: 1.08x slower                                                         |
| async_generators           | 390 ms                                                       | 422 ms: 1.08x slower                                                         |
| unpickle_pure_python       | 210 us                                                       | 228 us: 1.09x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.54 ms: 1.10x slower                                                        |
| fannkuch                   | 350 ms                                                       | 386 ms: 1.10x slower                                                         |
| mako                       | 10.0 ms                                                      | 11.1 ms: 1.11x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.74 ms: 1.13x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.13x slower                                                        |
| nbody                      | 88.0 ms                                                      | 99.3 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.16x slower                                                         |
| telco                      | 6.96 ms                                                      | 8.13 ms: 1.17x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 10.5 ms: 1.21x slower                                                        |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.84 ms: 1.79x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.58 ms: 1.89x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 1.26 sec: 265.34x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (5): xml_etree_parse, asyncio_websockets, logging_simple, pprint_safe_repr, bench_thread_pool
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250317-3.14.0a6+-bb0268f/bm-20250317-pythonperf2-x86_64-python-bb0268f60dfe903a9bdb-3.14.0a6+-bb0268f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 75.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x