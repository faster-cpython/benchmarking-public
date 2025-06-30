# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_12_10
- machine: linux-x86_64
- commit hash: 0d5e4e2
- commit date: 2025-06-29
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.37 ms: 1.07x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.11x faster                                               |
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                               |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 320 ms: 1.79x faster                                                |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                |
| richards                   | 45.8 ms                                                | 32.4 ms: 1.41x faster                                               |
| richards_super             | 51.5 ms                                                | 37.6 ms: 1.37x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                               |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                               |
| spectral_norm              | 115 ms                                                 | 90.2 ms: 1.27x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                               |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                               |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                |
| pyflate                    | 482 ms                                                 | 406 ms: 1.19x faster                                                |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.26 us: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                               |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.11x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 704 ms: 1.10x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                               |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.43 sec: 1.09x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                               |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.37 ms: 1.07x faster                                               |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                               |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                |
| async_generators           | 463 ms                                                 | 438 ms: 1.06x faster                                                |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                              |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.26 ms: 1.02x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.94 ms: 1.02x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                              |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                               |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.7 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                               |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                               |
| coverage                   | 72.7 ms                                                | 88.0 ms: 1.21x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| gc_traversal               | 3.79 ms                                                | 5.17 ms: 1.36x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.77x slower                                               |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (5): pickle_pure_python, regex_dna, json_loads, nbody, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-0d5e4e2-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_10-3.15.0a0-0d5e4e2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x