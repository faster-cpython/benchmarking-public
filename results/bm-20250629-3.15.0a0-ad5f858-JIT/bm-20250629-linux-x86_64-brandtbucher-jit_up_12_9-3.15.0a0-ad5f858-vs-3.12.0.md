# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: ad5f858
- commit date: 2025-06-29
- overall geometric mean: 1.141x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                               |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                               |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.3 ms: 1.28x faster                                              |
| nbody          | 97.0 ms                                                | 96.3 ms: 1.01x faster                                              |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.42 ms: 1.06x faster                                              |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                             |
| unpickle_pure_python | 230 us                                                 | 190 us: 1.21x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 80.0 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                              |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                              |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                               |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.00x faster                                              |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                              |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                              |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                               |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| richards                   | 45.8 ms                                                | 31.9 ms: 1.44x faster                                              |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                               |
| richards_super             | 51.5 ms                                                | 36.3 ms: 1.42x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                              |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                              |
| float                      | 84.7 ms                                                | 66.3 ms: 1.28x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                              |
| spectral_norm              | 115 ms                                                 | 93.1 ms: 1.23x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.22x faster                                              |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 190 us: 1.21x faster                                               |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                              |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                               |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.7 ms: 1.14x faster                                              |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                              |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                              |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 80.0 ms: 1.11x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                              |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                             |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                              |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                              |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                               |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.42 ms: 1.06x faster                                              |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                             |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                              |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                              |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.99 ms: 1.01x faster                                              |
| nbody                      | 97.0 ms                                                | 96.3 ms: 1.01x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.00x faster                                              |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.00x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                               |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                               |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                               |
| generators                 | 31.2 ms                                                | 31.7 ms: 1.02x slower                                              |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                               |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                              |
| coverage                   | 72.7 ms                                                | 87.9 ms: 1.21x slower                                              |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.88 ms: 1.29x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                              |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                       |

Benchmark hidden because not significant (1): json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-ad5f858-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.141x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x