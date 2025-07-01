# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_6
- machine: linux-x86_64
- commit hash: a33098b
- commit date: 2025-06-30
- overall geometric mean: 1.147x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                               |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                               |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.1 ms: 1.28x faster                                              |
| nbody          | 97.0 ms                                                | 98.2 ms: 1.01x slower                                              |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.04x faster                                              |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                             |
| unpickle_pure_python | 230 us                                                 | 191 us: 1.20x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                              |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                              |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                               |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                              |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.4 ms: 1.15x faster                                              |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                             |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| richards                   | 45.8 ms                                                | 29.5 ms: 1.55x faster                                              |
| richards_super             | 51.5 ms                                                | 33.8 ms: 1.53x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                               |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                              |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.33x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                             |
| float                      | 84.7 ms                                                | 66.1 ms: 1.28x faster                                              |
| spectral_norm              | 115 ms                                                 | 91.7 ms: 1.25x faster                                              |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.22x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 191 us: 1.20x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.81 us: 1.19x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| pyflate                    | 482 ms                                                 | 415 ms: 1.16x faster                                               |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                              |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.6 ms: 1.15x faster                                              |
| mako                       | 11.9 ms                                                | 10.4 ms: 1.15x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                              |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.10x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                             |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                               |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                               |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                              |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.77 ms: 1.06x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                             |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.04x faster                                              |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                              |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                               |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                               |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                               |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                              |
| nqueens                    | 83.3 ms                                                | 82.4 ms: 1.01x faster                                              |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                               |
| nbody                      | 97.0 ms                                                | 98.2 ms: 1.01x slower                                              |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.67 ms: 1.08x slower                                              |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                              |
| Geometric mean             | (ref)                                                  | 1.15x faster                                                       |

Benchmark hidden because not significant (1): json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250630-3.15.0a0-a33098b-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_12_6-3.15.0a0-a33098b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x