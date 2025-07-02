# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_6_6
- machine: linux-x86_64
- commit hash: 6c99b17
- commit date: 2025-07-02
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                              |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                              |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                              |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                             |
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                             |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.39 ms: 1.07x faster                                             |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                            |
| unpickle_pure_python | 230 us                                                 | 192 us: 1.20x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 78.8 ms: 1.13x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                              |
| json_loads           | 28.5 us                                                | 28.9 us: 1.02x slower                                             |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                             |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                             |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                            |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 639 ms: 1.85x faster                                              |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 500 ms: 1.45x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                              |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                             |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                             |
| richards                   | 45.8 ms                                                | 34.7 ms: 1.32x faster                                             |
| richards_super             | 51.5 ms                                                | 39.3 ms: 1.31x faster                                             |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                             |
| spectral_norm              | 115 ms                                                 | 90.1 ms: 1.27x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                             |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                              |
| go                         | 139 ms                                                 | 115 ms: 1.22x faster                                              |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.21x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 192 us: 1.20x faster                                              |
| pyflate                    | 482 ms                                                 | 406 ms: 1.19x faster                                              |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                             |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                             |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                             |
| crypto_pyaes               | 81.9 ms                                                | 72.2 ms: 1.13x faster                                             |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 78.8 ms: 1.13x faster                                             |
| pprint_pformat             | 1.57 sec                                               | 1.39 sec: 1.13x faster                                            |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 67.1 ms: 1.12x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 698 ms: 1.11x faster                                              |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                             |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                              |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| meteor_contest             | 112 ms                                                 | 103 ms: 1.09x faster                                              |
| async_generators           | 463 ms                                                 | 427 ms: 1.08x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                             |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.39 ms: 1.07x faster                                             |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.05x faster                                             |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                              |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                             |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                            |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                             |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                            |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                              |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                             |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.02 ms: 1.01x faster                                             |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                             |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                              |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                             |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                             |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.02x slower                                             |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                              |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                              |
| coroutines                 | 23.2 ms                                                | 25.4 ms: 1.10x slower                                             |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                             |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.32x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.64 ms: 1.79x slower                                             |
| telco                      | 7.10 ms                                                | 161 ms: 22.71x slower                                             |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                      |

Benchmark hidden because not significant (2): regex_v8, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250702-3.15.0a0-6c99b17-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_6-3.15.0a0-6c99b17.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.19x