# Results vs. 3.12.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: linux-x86_64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.146x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                 |
| nbody          | 97.0 ms                                                | 93.4 ms: 1.04x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| regex_v8       | 23.1 ms                                                | 21.9 ms: 1.06x faster                                                 |
| regex_dna      | 212 ms                                                 | 202 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.1 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.5 ms: 1.14x faster                                                 |
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.13x faster                                                |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 641 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                  |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                  |
| richards                   | 45.8 ms                                                | 32.2 ms: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                 |
| richards_super             | 51.5 ms                                                | 37.9 ms: 1.36x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                 |
| float                      | 84.7 ms                                                | 65.3 ms: 1.30x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                 |
| spectral_norm              | 115 ms                                                 | 92.2 ms: 1.25x faster                                                 |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                                 |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                  |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.15x faster                                                 |
| pyflate                    | 482 ms                                                 | 418 ms: 1.15x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| mako                       | 11.9 ms                                                | 10.5 ms: 1.14x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.11x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 712 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.5 ms: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                  |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                |
| regex_v8                   | 23.1 ms                                                | 21.9 ms: 1.06x faster                                                 |
| regex_dna                  | 212 ms                                                 | 202 ms: 1.05x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                  |
| nbody                      | 97.0 ms                                                | 93.4 ms: 1.04x faster                                                 |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                  |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.24 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.1 us: 1.01x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| pidigits                   | 187 ms                                                 | 188 ms: 1.01x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                 |
| telco                      | 7.10 ms                                                | 7.65 ms: 1.08x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.2 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.96 ms: 1.31x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (2): python_startup_no_site, scimark_lu
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-linux-x86_64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.146x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x