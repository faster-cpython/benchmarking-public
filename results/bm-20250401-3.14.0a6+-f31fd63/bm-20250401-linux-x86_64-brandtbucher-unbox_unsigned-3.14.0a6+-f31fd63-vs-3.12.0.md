# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox_unsigned
- machine: linux-x86_64
- commit hash: f31fd63
- commit date: 2025-04-01
- overall geometric mean: 1.089x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.0 ms: 1.13x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| nbody          | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                  |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                 |
| xml_etree_parse     | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_iterparse | 107 ms                                                 | 99.8 ms: 1.07x faster                                                  |
| xml_etree_generate  | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| xml_etree_process   | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                  |
| pickle_pure_python  | 324 us                                                 | 333 us: 1.03x slower                                                   |
| json_dumps          | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                  |
| json_loads          | 28.5 us                                                | 32.3 us: 1.13x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                  |
| mako            | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.10x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 631 ms: 1.83x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 262 us: 1.41x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.31x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.24x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                  |
| spectral_norm              | 115 ms                                                 | 97.4 ms: 1.18x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.17x faster                                                  |
| async_generators           | 463 ms                                                 | 400 ms: 1.16x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                                  |
| float                      | 84.7 ms                                                | 75.0 ms: 1.13x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| logging_format             | 7.23 us                                                | 6.42 us: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                   |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                  |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.80 us: 1.11x faster                                                  |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.11x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                  |
| generators                 | 31.2 ms                                                | 28.6 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 70.0 ms: 1.07x faster                                                  |
| coroutines                 | 23.2 ms                                                | 21.6 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.8 ms: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                 |
| 2to3                       | 274 ms                                                 | 264 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                                   |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                  |
| scimark_sor                | 129 ms                                                 | 128 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| scimark_fft                | 382 ms                                                 | 383 ms: 1.00x slower                                                   |
| deltablue                  | 3.72 ms                                                | 3.74 ms: 1.01x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.59 sec: 1.01x slower                                                 |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                   |
| nbody                      | 97.0 ms                                                | 98.1 ms: 1.01x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                   |
| richards                   | 45.8 ms                                                | 47.1 ms: 1.03x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 333 us: 1.03x slower                                                   |
| mako                       | 11.9 ms                                                | 12.3 ms: 1.03x slower                                                  |
| richards_super             | 51.5 ms                                                | 53.3 ms: 1.03x slower                                                  |
| fannkuch                   | 417 ms                                                 | 435 ms: 1.04x slower                                                   |
| json                       | 5.26 ms                                                | 5.50 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 889 us: 1.06x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 125 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                  |
| json_loads                 | 28.5 us                                                | 32.3 us: 1.13x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.2 ms: 1.17x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.1 ms: 3.50x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (7): scimark_sparse_mat_mult, crypto_pyaes, hexiom, nqueens, asyncio_websockets, unpickle_pure_python, pprint_safe_repr
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-f31fd63/bm-20250401-linux-x86_64-brandtbucher-unbox_unsigned-3.14.0a6+-f31fd63.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.089x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x