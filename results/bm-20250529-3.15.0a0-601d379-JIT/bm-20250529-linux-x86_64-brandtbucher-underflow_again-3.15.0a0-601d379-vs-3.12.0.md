# Results vs. 3.12.0

- fork: brandtbucher
- ref: underflow_again
- machine: linux-x86_64
- commit hash: 601d379
- commit date: 2025-05-29
- overall geometric mean: 1.598x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.3 ms: 1.32x faster                                                  |
| nbody          | 97.0 ms                                                | 89.7 ms: 1.08x faster                                                  |
| pidigits       | 187 ms                                                 | 195 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.37 ms: 1.07x faster                                                  |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                   |
| regex_v8       | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 202 us: 1.14x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| json_loads           | 28.5 us                                                | 30.7 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pprint_pformat             | 1.57 sec                                               | 1.47 us: 1065703.16x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 857 ns: 905263.43x faster                                              |
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.11x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                   |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                   |
| richards                   | 45.8 ms                                                | 33.7 ms: 1.36x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                  |
| richards_super             | 51.5 ms                                                | 38.2 ms: 1.35x faster                                                  |
| float                      | 84.7 ms                                                | 64.3 ms: 1.32x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                  |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.16x faster                                                   |
| spectral_norm              | 115 ms                                                 | 99.8 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 202 us: 1.14x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                   |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 61.6 ms: 1.11x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                  |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                   |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                  |
| nbody                      | 97.0 ms                                                | 89.7 ms: 1.08x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.37 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 70.3 ms: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                   |
| logging_format             | 7.23 us                                                | 6.88 us: 1.05x faster                                                  |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                                  |
| chaos                      | 67.0 ms                                                | 63.9 ms: 1.05x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.19 us: 1.04x faster                                                  |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                 |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.03x faster                                                   |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                   |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                  |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                                   |
| nqueens                    | 83.3 ms                                                | 84.3 ms: 1.01x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                   |
| json                       | 5.26 ms                                                | 5.40 ms: 1.03x slower                                                  |
| pidigits                   | 187 ms                                                 | 195 ms: 1.04x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.2 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                  |
| json_loads                 | 28.5 us                                                | 30.7 us: 1.08x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.9 ms: 1.12x slower                                                  |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 93.5 ms: 3.89x slower                                                  |
| logging_silent             | 104 ns                                                 | 476 ns: 4.55x slower                                                   |
| coverage                   | 72.7 ms                                                | 432 ms: 5.94x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.50x faster                                                           |

Benchmark hidden because not significant (3): pycparser, asyncio_websockets, hexiom
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250529-3.15.0a0-601d379-JIT/bm-20250529-linux-x86_64-brandtbucher-underflow_again-3.15.0a0-601d379.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.598x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.14x