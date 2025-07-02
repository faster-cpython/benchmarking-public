# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_7_12
- machine: linux-x86_64
- commit hash: 459e94c
- commit date: 2025-07-01
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                               |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                               |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                               |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.0 ms: 1.28x faster                                              |
| nbody          | 97.0 ms                                                | 92.3 ms: 1.05x faster                                              |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.41 ms: 1.06x faster                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                              |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                              |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                               |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                              |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                             |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                               |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                               |
| richards                   | 45.8 ms                                                | 31.0 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                               |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                               |
| richards_super             | 51.5 ms                                                | 35.9 ms: 1.44x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                              |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                              |
| float                      | 84.7 ms                                                | 66.0 ms: 1.28x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                             |
| spectral_norm              | 115 ms                                                 | 91.5 ms: 1.26x faster                                              |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.79 us: 1.20x faster                                              |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                               |
| pyflate                    | 482 ms                                                 | 404 ms: 1.20x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                              |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                              |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.7 ms: 1.11x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                              |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                              |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                             |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                               |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                               |
| fannkuch                   | 417 ms                                                 | 392 ms: 1.06x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 729 ms: 1.06x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.41 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                              |
| nbody                      | 97.0 ms                                                | 92.3 ms: 1.05x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                              |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                               |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                              |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                              |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                              |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                              |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                               |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                               |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.73 ms: 1.09x slower                                              |
| coroutines                 | 23.2 ms                                                | 25.6 ms: 1.10x slower                                              |
| coverage                   | 72.7 ms                                                | 88.0 ms: 1.21x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.92 ms: 1.30x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.76x slower                                              |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (2): nqueens, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250701-3.15.0a0-459e94c-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_7_12-3.15.0a0-459e94c.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.141x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.16x