# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: 54cf0c1
- commit date: 2025-06-29
- overall geometric mean: 1.137x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.9 ms: 1.29x faster                                               |
| nbody          | 97.0 ms                                                | 95.2 ms: 1.02x faster                                               |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.44 ms: 1.05x faster                                               |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| unpickle_pure_python | 230 us                                                 | 192 us: 1.20x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                               |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| Geometric mean | (ref)                                                  | 1.13x slower                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.11x faster                                               |
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                               |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                              |
| async_tree_io              | 1.16 sec                                               | 602 ms: 1.92x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 637 ms: 1.86x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                               |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                               |
| float                      | 84.7 ms                                                | 65.9 ms: 1.29x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                              |
| spectral_norm              | 115 ms                                                 | 91.2 ms: 1.26x faster                                               |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 192 us: 1.20x faster                                                |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                |
| richards                   | 45.8 ms                                                | 39.2 ms: 1.17x faster                                               |
| pyflate                    | 482 ms                                                 | 416 ms: 1.16x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 64.8 ms: 1.16x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 70.7 ms: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                               |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                               |
| richards_super             | 51.5 ms                                                | 45.1 ms: 1.14x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.12x faster                                                |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.11x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                               |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                              |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                              |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                               |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.80 ms: 1.05x faster                                               |
| logging_silent             | 104 ns                                                 | 99.2 ns: 1.05x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.44 ms: 1.05x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                               |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.05x faster                                              |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                               |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                                |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                |
| nbody                      | 97.0 ms                                                | 95.2 ms: 1.02x faster                                               |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.5 ms: 1.01x faster                                               |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.00x faster                                               |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                               |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.8 ms: 1.12x slower                                               |
| coverage                   | 72.7 ms                                                | 87.7 ms: 1.21x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                               |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (4): json, python_startup_no_site, asyncio_websockets, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-54cf0c1-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x