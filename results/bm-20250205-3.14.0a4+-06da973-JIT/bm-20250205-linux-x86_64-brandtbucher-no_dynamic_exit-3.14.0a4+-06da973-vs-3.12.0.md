# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_dynamic_exit
- machine: linux-x86_64
- commit hash: 06da973
- commit date: 2025-02-05
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                    |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                   |
| nbody          | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                   |
| regex_dna      | 212 ms                                                 | 213 ms: 1.00x slower                                                    |
| regex_v8       | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                    |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 95.1 ms: 1.12x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                    |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                   |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                   |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 622 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                    |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 326 ms: 1.77x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                    |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                   |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                   |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                   |
| spectral_norm              | 115 ms                                                 | 96.4 ms: 1.19x faster                                                   |
| mako                       | 11.9 ms                                                | 9.99 ms: 1.19x faster                                                   |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                   |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                   |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 70.4 ms: 1.16x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                    |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                    |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                   |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 95.1 ms: 1.12x faster                                                   |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                    |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                   |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                    |
| nbody                      | 97.0 ms                                                | 89.5 ms: 1.08x faster                                                   |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                    |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                    |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 390 ms: 1.07x faster                                                    |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                   |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                   |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 65.8 ms: 1.04x faster                                                   |
| richards_super             | 51.5 ms                                                | 49.5 ms: 1.04x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                    |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                   |
| json                       | 5.26 ms                                                | 5.14 ms: 1.02x faster                                                   |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.00x slower                                                    |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.03 ms: 1.01x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.66 ms: 1.04x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 886 us: 1.05x slower                                                    |
| regex_v8                   | 23.1 ms                                                | 24.4 ms: 1.06x slower                                                   |
| telco                      | 7.10 ms                                                | 7.66 ms: 1.08x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.9 ms: 1.09x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                   |
| coverage                   | 72.7 ms                                                | 90.1 ms: 1.24x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                   |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250205-3.14.0a4+-06da973-JIT/bm-20250205-linux-x86_64-brandtbucher-no_dynamic_exit-3.14.0a4+-06da973.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x