# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_6_12
- machine: linux-x86_64
- commit hash: ebec717
- commit date: 2025-07-02
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                               |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.84x faster                                               |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                               |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.3 ms: 1.30x faster                                              |
| nbody          | 97.0 ms                                                | 94.1 ms: 1.03x faster                                              |
| pidigits       | 187 ms                                                 | 201 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                              |
| regex_dna      | 212 ms                                                 | 206 ms: 1.03x faster                                               |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                             |
| unpickle_pure_python | 230 us                                                 | 190 us: 1.21x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                              |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                              |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                              |
| django_template | 34.6 ms                                                | 32.8 ms: 1.06x faster                                              |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                             |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.84x faster                                               |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 323 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 504 ms: 1.44x faster                                               |
| richards                   | 45.8 ms                                                | 32.0 ms: 1.43x faster                                              |
| richards_super             | 51.5 ms                                                | 36.2 ms: 1.42x faster                                              |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                              |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                              |
| float                      | 84.7 ms                                                | 65.3 ms: 1.30x faster                                              |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                             |
| spectral_norm              | 115 ms                                                 | 93.1 ms: 1.23x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 190 us: 1.21x faster                                               |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                               |
| scimark_fft                | 382 ms                                                 | 316 ms: 1.21x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.10 ms: 1.20x faster                                              |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                              |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                               |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                              |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                              |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                              |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 72.4 ms: 1.13x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 689 ms: 1.13x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                              |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.41 sec: 1.11x faster                                             |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                               |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                               |
| chaos                      | 67.0 ms                                                | 61.0 ms: 1.10x faster                                              |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                              |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                               |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                             |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.06x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                              |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                               |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                             |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                               |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                              |
| nbody                      | 97.0 ms                                                | 94.1 ms: 1.03x faster                                              |
| regex_dna                  | 212 ms                                                 | 206 ms: 1.03x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                              |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                               |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                              |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                              |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                               |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.17 ms: 1.02x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                              |
| pidigits                   | 187 ms                                                 | 201 ms: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| coverage                   | 72.7 ms                                                | 88.2 ms: 1.21x slower                                              |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 5.13 ms: 1.35x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.63 ms: 1.78x slower                                              |
| telco                      | 7.10 ms                                                | 160 ms: 22.60x slower                                              |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                       |

Benchmark hidden because not significant (3): json, asyncio_websockets, nqueens
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.18x