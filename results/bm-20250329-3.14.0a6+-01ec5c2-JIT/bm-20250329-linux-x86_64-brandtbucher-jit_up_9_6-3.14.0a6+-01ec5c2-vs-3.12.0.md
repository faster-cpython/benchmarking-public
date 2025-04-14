# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_9_6
- machine: linux-x86_64
- commit hash: 01ec5c2
- commit date: 2025-03-29
- overall geometric mean: 1.107x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.02x faster                                               |
| docutils       | 2.77 sec                                               | 2.73 sec: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.88x faster                                               |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 504 ms: 1.44x faster                                               |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.8 ms: 1.29x faster                                              |
| nbody          | 97.0 ms                                                | 87.6 ms: 1.11x faster                                              |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.13x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.40 ms: 1.06x faster                                              |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.24x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.1 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 57.0 ms: 1.08x faster                                              |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                               |
| pickle_pure_python   | 324 us                                                 | 326 us: 1.01x slower                                               |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.18 ms: 1.18x slower                                              |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                              |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                              |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                              |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 627 ms: 1.88x faster                                               |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 28.2 us: 1.45x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 504 ms: 1.44x faster                                               |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                               |
| float                      | 84.7 ms                                                | 65.8 ms: 1.29x faster                                              |
| richards                   | 45.8 ms                                                | 35.8 ms: 1.28x faster                                              |
| richards_super             | 51.5 ms                                                | 40.8 ms: 1.26x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.24x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                              |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                               |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                              |
| spectral_norm              | 115 ms                                                 | 98.7 ms: 1.16x faster                                              |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.16x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                              |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.66 us: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                               |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                               |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                              |
| async_generators           | 463 ms                                                 | 415 ms: 1.12x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.1 ms: 1.11x faster                                              |
| pyflate                    | 482 ms                                                 | 434 ms: 1.11x faster                                               |
| nbody                      | 97.0 ms                                                | 87.6 ms: 1.11x faster                                              |
| chaos                      | 67.0 ms                                                | 60.7 ms: 1.10x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                              |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 57.0 ms: 1.08x faster                                              |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                              |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                               |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                              |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                              |
| go                         | 139 ms                                                 | 130 ms: 1.08x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.40 ms: 1.06x faster                                              |
| logging_silent             | 104 ns                                                 | 98.6 ns: 1.06x faster                                              |
| mdp                        | 2.63 sec                                               | 2.50 sec: 1.05x faster                                             |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 141 ms: 1.04x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                              |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 754 ms: 1.03x faster                                               |
| 2to3                       | 274 ms                                                 | 270 ms: 1.02x faster                                               |
| docutils                   | 2.77 sec                                               | 2.73 sec: 1.01x faster                                             |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                              |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                              |
| pickle_pure_python         | 324 us                                                 | 326 us: 1.01x slower                                               |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                             |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                               |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| nqueens                    | 83.3 ms                                                | 85.0 ms: 1.02x slower                                              |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                              |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                               |
| hexiom                     | 6.41 ms                                                | 6.99 ms: 1.09x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                              |
| telco                      | 7.10 ms                                                | 8.25 ms: 1.16x slower                                              |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 8.18 ms: 1.18x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                              |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 83.5 ms: 3.48x slower                                              |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                       |

Benchmark hidden because not significant (3): sympy_expand, pprint_pformat, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-01ec5c2-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_9_6-3.14.0a6+-01ec5c2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.107x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x