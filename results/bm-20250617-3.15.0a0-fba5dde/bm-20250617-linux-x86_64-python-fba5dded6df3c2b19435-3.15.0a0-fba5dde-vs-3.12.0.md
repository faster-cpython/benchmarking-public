# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.4 ms: 1.15x faster                                                 |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| nbody          | 97.0 ms                                                | 99.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| regex_dna      | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.9 ms: 1.08x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.04x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                  |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                 |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                                 |
| float                      | 84.7 ms                                                | 73.4 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                                 |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                  |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                  |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 69.0 ms: 1.09x faster                                                 |
| chaos                      | 67.0 ms                                                | 61.8 ms: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.9 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                 |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                 |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                  |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                 |
| logging_format             | 7.23 us                                                | 6.91 us: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.04x faster                                                 |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.04x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.57 ms: 1.04x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.24 us: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.2 us: 1.01x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                  |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| fannkuch                   | 417 ms                                                 | 419 ms: 1.00x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.00x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                  |
| nbody                      | 97.0 ms                                                | 99.4 ms: 1.02x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.19 ms: 1.03x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 818 ms: 1.05x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.66 sec: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                 |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.8 ms: 1.21x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.09 ms: 1.34x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 468 ns: 4.48x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x