# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_os
- machine: linux-x86_64
- commit hash: 33054dd
- commit date: 2025-06-28
- overall geometric mean: 1.145x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                          |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.05x faster                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 630 ms: 1.88x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                          |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.2 ms: 1.30x faster                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                          |
| nbody          | 97.0 ms                                                | 97.9 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                         |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                         |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                        |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                          |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.9 ms: 1.12x faster                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                         |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                          |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                         |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.13x faster                                         |
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                         |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                        |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                          |
| async_tree_io_tg           | 1.18 sec                                               | 630 ms: 1.88x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.84x faster                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                          |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                          |
| richards                   | 45.8 ms                                                | 32.1 ms: 1.43x faster                                         |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                         |
| richards_super             | 51.5 ms                                                | 37.8 ms: 1.36x faster                                         |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                         |
| float                      | 84.7 ms                                                | 65.2 ms: 1.30x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                        |
| spectral_norm              | 115 ms                                                 | 91.8 ms: 1.25x faster                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                         |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                          |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                          |
| pyflate                    | 482 ms                                                 | 411 ms: 1.17x faster                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                          |
| dulwich_log                | 68.5 ms                                                | 59.1 ms: 1.16x faster                                         |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 65.5 ms: 1.15x faster                                         |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                          |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                         |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                          |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                          |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.13x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.9 ms: 1.12x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                         |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.41 sec: 1.11x faster                                        |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                          |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                          |
| chaos                      | 67.0 ms                                                | 61.6 ms: 1.09x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                         |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.08x faster                                          |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                          |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                         |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                          |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                        |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                          |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.05x faster                                        |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                         |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                          |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                         |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                          |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                         |
| nqueens                    | 83.3 ms                                                | 82.6 ms: 1.01x faster                                         |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                         |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                          |
| nbody                      | 97.0 ms                                                | 97.9 ms: 1.01x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                         |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                         |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                         |
| coverage                   | 72.7 ms                                                | 87.9 ms: 1.21x slower                                         |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                         |
| gc_traversal               | 3.79 ms                                                | 5.09 ms: 1.34x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                         |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                  |

Benchmark hidden because not significant (6): json_loads, asyncio_websockets, scimark_sparse_mat_mult, logging_silent, scimark_lu, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-33054dd-JIT/bm-20250628-linux-x86_64-brandtbucher-jit_os-3.15.0a0-33054dd.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.145x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x