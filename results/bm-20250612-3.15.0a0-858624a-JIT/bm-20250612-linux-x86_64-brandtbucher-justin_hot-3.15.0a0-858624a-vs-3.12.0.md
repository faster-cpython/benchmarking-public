# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                              |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.2 ms: 1.30x faster                                             |
| nbody          | 97.0 ms                                                | 93.5 ms: 1.04x faster                                             |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                             |
| regex_v8       | 23.1 ms                                                | 23.7 ms: 1.02x slower                                             |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                            |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| json_loads           | 28.5 us                                                | 28.1 us: 1.02x faster                                             |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                              |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                             |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                             |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.13x faster                                             |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                             |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                            |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                              |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.82x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.82x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                              |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                              |
| richards                   | 45.8 ms                                                | 32.9 ms: 1.39x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                             |
| richards_super             | 51.5 ms                                                | 38.3 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                             |
| float                      | 84.7 ms                                                | 65.2 ms: 1.30x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.06 ms: 1.22x faster                                             |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                              |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                              |
| pyflate                    | 482 ms                                                 | 416 ms: 1.16x faster                                              |
| scimark_fft                | 382 ms                                                 | 330 ms: 1.16x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                             |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                             |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                              |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                             |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.13x faster                                             |
| dulwich_log                | 68.5 ms                                                | 61.5 ms: 1.11x faster                                             |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                             |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 74.9 ms: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                             |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                              |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                             |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                              |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                             |
| logging_format             | 7.23 us                                                | 6.79 us: 1.06x faster                                             |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                              |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                            |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                             |
| nbody                      | 97.0 ms                                                | 93.5 ms: 1.04x faster                                             |
| logging_simple             | 6.46 us                                                | 6.24 us: 1.04x faster                                             |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                              |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                             |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                              |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.02x faster                                             |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                              |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                             |
| regex_v8                   | 23.1 ms                                                | 23.7 ms: 1.02x slower                                             |
| scimark_lu                 | 118 ms                                                 | 121 ms: 1.03x slower                                              |
| pprint_pformat             | 1.57 sec                                               | 1.61 sec: 1.03x slower                                            |
| pprint_safe_repr           | 776 ms                                                 | 800 ms: 1.03x slower                                              |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                             |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                             |
| telco                      | 7.10 ms                                                | 7.76 ms: 1.09x slower                                             |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                             |
| gc_traversal               | 3.79 ms                                                | 5.14 ms: 1.36x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                             |
| logging_silent             | 104 ns                                                 | 475 ns: 4.55x slower                                              |
| coverage                   | 72.7 ms                                                | 425 ms: 5.84x slower                                              |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                      |

Benchmark hidden because not significant (5): json, nqueens, sqlite_synth, pycparser, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.15x