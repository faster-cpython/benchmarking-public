# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 50321ce
- commit date: 2025-06-30
- overall geometric mean: 1.144x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                               |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.2 ms: 1.28x faster                                              |
| nbody          | 97.0 ms                                                | 95.8 ms: 1.01x faster                                              |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                              |
| regex_dna      | 212 ms                                                 | 198 ms: 1.07x faster                                               |
| regex_v8       | 23.1 ms                                                | 22.6 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| unpickle_pure_python | 230 us                                                 | 192 us: 1.20x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                               |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                              |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| Geometric mean | (ref)                                                  | 1.13x slower                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                             |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                               |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                              |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                              |
| richards                   | 45.8 ms                                                | 34.7 ms: 1.32x faster                                              |
| richards_super             | 51.5 ms                                                | 39.7 ms: 1.30x faster                                              |
| float                      | 84.7 ms                                                | 66.2 ms: 1.28x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| spectral_norm              | 115 ms                                                 | 92.6 ms: 1.24x faster                                              |
| scimark_fft                | 382 ms                                                 | 308 ms: 1.24x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                              |
| go                         | 139 ms                                                 | 116 ms: 1.21x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 192 us: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 70.8 ms: 1.16x faster                                              |
| pyflate                    | 482 ms                                                 | 417 ms: 1.16x faster                                               |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                              |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                              |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.12x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.12x faster                                              |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.43 sec: 1.10x faster                                             |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                               |
| chaos                      | 67.0 ms                                                | 61.8 ms: 1.08x faster                                              |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                               |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                               |
| regex_dna                  | 212 ms                                                 | 198 ms: 1.07x faster                                               |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                               |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                               |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                             |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                              |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.6 ms: 1.02x faster                                              |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                              |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                               |
| nbody                      | 97.0 ms                                                | 95.8 ms: 1.01x faster                                              |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                               |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                              |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                              |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                              |
| coverage                   | 72.7 ms                                                | 87.2 ms: 1.20x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                              |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (4): nqueens, json, python_startup_no_site, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-50321ce-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.144x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x