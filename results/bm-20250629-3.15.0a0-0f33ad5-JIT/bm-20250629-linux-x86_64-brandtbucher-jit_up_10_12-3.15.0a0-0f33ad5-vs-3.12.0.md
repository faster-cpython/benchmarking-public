# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_10_12
- machine: linux-x86_64
- commit hash: 0f33ad5
- commit date: 2025-06-29
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                               |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.00x faster                                               |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| unpickle_pure_python | 230 us                                                 | 192 us: 1.20x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 79.5 ms: 1.12x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                               |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                               |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                               |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                               |
| django_template | 34.6 ms                                                | 33.0 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                              |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                               |
| richards                   | 45.8 ms                                                | 34.3 ms: 1.34x faster                                               |
| richards_super             | 51.5 ms                                                | 39.4 ms: 1.31x faster                                               |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                               |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| spectral_norm              | 115 ms                                                 | 92.0 ms: 1.25x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                               |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 192 us: 1.20x faster                                                |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                                |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| pyflate                    | 482 ms                                                 | 414 ms: 1.17x faster                                                |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 71.6 ms: 1.14x faster                                               |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.9 ms: 1.14x faster                                               |
| logging_simple             | 6.46 us                                                | 5.67 us: 1.14x faster                                               |
| logging_format             | 7.23 us                                                | 6.36 us: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                               |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 79.5 ms: 1.12x faster                                               |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                               |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.10x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                               |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                |
| django_template            | 34.6 ms                                                | 33.0 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.89 ms: 1.04x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 754 ms: 1.03x faster                                                |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                               |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                               |
| json                       | 5.26 ms                                                | 5.19 ms: 1.01x faster                                               |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.01x faster                                               |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.00x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                               |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.58 ms: 1.07x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| coverage                   | 72.7 ms                                                | 87.6 ms: 1.21x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                               |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (3): nbody, asyncio_websockets, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-0f33ad5-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_10_12-3.15.0a0-0f33ad5.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x