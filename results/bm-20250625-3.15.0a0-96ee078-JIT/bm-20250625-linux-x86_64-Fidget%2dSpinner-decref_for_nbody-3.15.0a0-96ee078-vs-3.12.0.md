# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: decref_for_nbody
- machine: linux-x86_64
- commit hash: 96ee078
- commit date: 2025-06-25
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                        |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                        |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.5 ms: 1.29x faster                                                       |
| nbody          | 97.0 ms                                                | 90.3 ms: 1.07x faster                                                       |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                       |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                        |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                       |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                       |
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                        |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                        |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                       |
| richards                   | 45.8 ms                                                | 33.7 ms: 1.36x faster                                                       |
| richards_super             | 51.5 ms                                                | 39.7 ms: 1.30x faster                                                       |
| float                      | 84.7 ms                                                | 65.5 ms: 1.29x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                       |
| spectral_norm              | 115 ms                                                 | 94.2 ms: 1.22x faster                                                       |
| scimark_fft                | 382 ms                                                 | 314 ms: 1.21x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.13 ms: 1.19x faster                                                       |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                        |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                        |
| pyflate                    | 482 ms                                                 | 423 ms: 1.14x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                        |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.10x faster                                                       |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                       |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                        |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                       |
| async_generators           | 463 ms                                                 | 430 ms: 1.08x faster                                                        |
| nbody                      | 97.0 ms                                                | 90.3 ms: 1.07x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.38 ms: 1.07x faster                                                       |
| logging_format             | 7.23 us                                                | 6.77 us: 1.07x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                        |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                        |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                        |
| logging_simple             | 6.46 us                                                | 6.15 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                      |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                       |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                       |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                       |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                        |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                       |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.45 ms: 1.01x slower                                                       |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                       |
| json                       | 5.26 ms                                                | 5.31 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 776 ms                                                 | 803 ms: 1.04x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                        |
| telco                      | 7.10 ms                                                | 7.65 ms: 1.08x slower                                                       |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                       |
| coverage                   | 72.7 ms                                                | 87.6 ms: 1.20x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                                       |
| logging_silent             | 104 ns                                                 | 473 ns: 4.53x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                |

Benchmark hidden because not significant (2): pycparser, pickle_pure_python
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250625-3.15.0a0-96ee078-JIT/bm-20250625-linux-x86_64-Fidget%2dSpinner-decref_for_nbody-3.15.0a0-96ee078.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x