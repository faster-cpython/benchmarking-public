# Results vs. 3.12.0

- fork: brandtbucher
- ref: keep_tracing
- machine: linux-x86_64
- commit hash: 8746972
- commit date: 2025-06-09
- overall geometric mean: 1.089x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.4 ms: 1.30x faster                                               |
| nbody          | 97.0 ms                                                | 90.4 ms: 1.07x faster                                               |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.49 ms: 1.03x faster                                               |
| regex_v8       | 23.1 ms                                                | 22.8 ms: 1.01x faster                                               |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                              |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 145 ms: 1.10x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                               |
| pickle_pure_python   | 324 us                                                 | 330 us: 1.02x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                               |
| django_template | 34.6 ms                                                | 32.8 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.26 sec: 2.08x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                               |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                               |
| float                      | 84.7 ms                                                | 65.4 ms: 1.30x faster                                               |
| richards                   | 45.8 ms                                                | 37.0 ms: 1.24x faster                                               |
| richards_super             | 51.5 ms                                                | 42.4 ms: 1.22x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.82 us: 1.18x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                               |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| pyflate                    | 482 ms                                                 | 425 ms: 1.14x faster                                                |
| scimark_fft                | 382 ms                                                 | 339 ms: 1.13x faster                                                |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                |
| dulwich_log                | 68.5 ms                                                | 61.7 ms: 1.11x faster                                               |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                               |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 145 ms: 1.10x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                               |
| async_generators           | 463 ms                                                 | 424 ms: 1.09x faster                                                |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| nbody                      | 97.0 ms                                                | 90.4 ms: 1.07x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 76.7 ms: 1.07x faster                                               |
| chaos                      | 67.0 ms                                                | 62.9 ms: 1.07x faster                                               |
| logging_format             | 7.23 us                                                | 6.79 us: 1.06x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                |
| logging_simple             | 6.46 us                                                | 6.09 us: 1.06x faster                                               |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.05x faster                                               |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                               |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.49 ms: 1.03x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.91 ms: 1.03x faster                                               |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                               |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.8 ms: 1.01x faster                                               |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                               |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| pickle_pure_python         | 324 us                                                 | 330 us: 1.02x slower                                                |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.74 ms: 1.05x slower                                               |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                              |
| pprint_safe_repr           | 776 ms                                                 | 831 ms: 1.07x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                |
| coroutines                 | 23.2 ms                                                | 25.2 ms: 1.09x slower                                               |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| gc_traversal               | 3.79 ms                                                | 5.18 ms: 1.37x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                               |
| logging_silent             | 104 ns                                                 | 487 ns: 4.66x slower                                                |
| coverage                   | 72.7 ms                                                | 428 ms: 5.89x slower                                                |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (3): nqueens, pycparser, fannkuch
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250609-3.15.0a0-8746972-JIT/bm-20250609-linux-x86_64-brandtbucher-keep_tracing-3.15.0a0-8746972.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x