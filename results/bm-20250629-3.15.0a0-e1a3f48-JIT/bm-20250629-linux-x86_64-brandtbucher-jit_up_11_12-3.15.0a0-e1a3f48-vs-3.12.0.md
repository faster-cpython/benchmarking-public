# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: e1a3f48
- commit date: 2025-06-29
- overall geometric mean: 1.143x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.91x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.0 ms: 1.28x faster                                               |
| nbody          | 97.0 ms                                                | 96.1 ms: 1.01x faster                                               |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                               |
| regex_dna      | 212 ms                                                 | 200 ms: 1.06x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                              |
| unpickle_pure_python | 230 us                                                 | 190 us: 1.21x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 81.2 ms: 1.10x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                               |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 9.55 ms                                                | 12.2 ms: 1.27x slower                                               |
| Geometric mean | (ref)                                                  | 1.13x slower                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.12x faster                                               |
| django_template | 34.6 ms                                                | 32.8 ms: 1.05x faster                                               |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                              |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.91x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                               |
| richards                   | 45.8 ms                                                | 34.7 ms: 1.32x faster                                               |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| richards_super             | 51.5 ms                                                | 39.8 ms: 1.29x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                              |
| float                      | 84.7 ms                                                | 66.0 ms: 1.28x faster                                               |
| spectral_norm              | 115 ms                                                 | 91.7 ms: 1.25x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.02 ms: 1.23x faster                                               |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                               |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 190 us: 1.21x faster                                                |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                               |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 65.3 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                               |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.9 ms: 1.14x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.12x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                               |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                |
| chaos                      | 67.0 ms                                                | 61.0 ms: 1.10x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 81.2 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                              |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                |
| regex_dna                  | 212 ms                                                 | 200 ms: 1.06x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.05x faster                                               |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.88 ms: 1.04x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.21 ms: 1.03x faster                                               |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                               |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                |
| nbody                      | 97.0 ms                                                | 96.1 ms: 1.01x faster                                               |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                               |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.09x slower                                               |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                               |
| coverage                   | 72.7 ms                                                | 88.2 ms: 1.21x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                               |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                               |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (4): json, python_startup_no_site, pickle_pure_python, generators
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250629-3.15.0a0-e1a3f48-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.143x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x