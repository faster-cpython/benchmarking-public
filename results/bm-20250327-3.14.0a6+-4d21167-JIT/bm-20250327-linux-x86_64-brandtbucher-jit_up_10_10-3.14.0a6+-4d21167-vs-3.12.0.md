# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_up_10_10
- machine: linux-x86_64
- commit hash: 4d21167
- commit date: 2025-03-27
- overall geometric mean: 1.105x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.7 ms: 1.29x faster                                                |
| nbody          | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.42 ms: 1.05x faster                                                |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                 |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 471 ms: 1.54x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                 |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                |
| float                      | 84.7 ms                                                | 65.7 ms: 1.29x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                                |
| spectral_norm              | 115 ms                                                 | 95.1 ms: 1.21x faster                                                |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                 |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 60.6 ms: 1.13x faster                                                |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                |
| pyflate                    | 482 ms                                                 | 435 ms: 1.11x faster                                                 |
| async_generators           | 463 ms                                                 | 419 ms: 1.11x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 80.8 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                |
| go                         | 139 ms                                                 | 127 ms: 1.10x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                 |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                 |
| nbody                      | 97.0 ms                                                | 89.0 ms: 1.09x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 56.7 ms: 1.09x faster                                                |
| logging_silent             | 104 ns                                                 | 96.1 ns: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.68 ms: 1.08x faster                                                |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                 |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 76.1 ms: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.42 ms: 1.05x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.05x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.05x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                 |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                               |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 771 ms: 1.01x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                 |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                 |
| nqueens                    | 83.3 ms                                                | 86.4 ms: 1.04x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.04x slower                                                |
| bench_thread_pool          | 842 us                                                 | 888 us: 1.05x slower                                                 |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.03 ms: 1.10x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                |
| telco                      | 7.10 ms                                                | 7.90 ms: 1.11x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                |
| coverage                   | 72.7 ms                                                | 86.3 ms: 1.19x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                                |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (4): sympy_expand, asyncio_websockets, pycparser, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250327-3.14.0a6+-4d21167-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_10_10-3.14.0a6+-4d21167.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.105x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x