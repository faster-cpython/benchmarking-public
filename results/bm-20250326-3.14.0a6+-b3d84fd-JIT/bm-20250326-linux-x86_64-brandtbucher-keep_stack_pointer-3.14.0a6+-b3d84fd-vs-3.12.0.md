# Results vs. 3.12.0

- fork: brandtbucher
- ref: keep_stack_pointer
- machine: linux-x86_64
- commit hash: b3d84fd
- commit date: 2025-03-26
- overall geometric mean: 1.129x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                       |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                       |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 62.5 ms: 1.36x faster                                                      |
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                      |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                      |
| regex_v8       | 23.1 ms                                                | 22.6 ms: 1.03x faster                                                      |
| regex_dna      | 212 ms                                                 | 211 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                                       |
| json_loads           | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                      |
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 614 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                       |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 472 ms: 1.54x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                       |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.43x faster                                                      |
| float                      | 84.7 ms                                                | 62.5 ms: 1.36x faster                                                      |
| richards                   | 45.8 ms                                                | 34.7 ms: 1.32x faster                                                      |
| richards_super             | 51.5 ms                                                | 39.8 ms: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                                      |
| spectral_norm              | 115 ms                                                 | 90.9 ms: 1.26x faster                                                      |
| deltablue                  | 3.72 ms                                                | 2.97 ms: 1.25x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                       |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.20x faster                                                      |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                       |
| logging_format             | 7.23 us                                                | 6.17 us: 1.17x faster                                                      |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                      |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                       |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.15x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                      |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                      |
| async_generators           | 463 ms                                                 | 411 ms: 1.13x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                       |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 55.6 ms: 1.11x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.59 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                      |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                       |
| generators                 | 31.2 ms                                                | 28.5 ms: 1.10x faster                                                      |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 75.2 ms: 1.09x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                      |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                       |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                     |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                     |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                     |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.04x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                                       |
| regex_v8                   | 23.1 ms                                                | 22.6 ms: 1.03x faster                                                      |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                       |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.00x faster                                                       |
| json                       | 5.26 ms                                                | 5.30 ms: 1.01x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.61 ms: 1.03x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.9 us: 1.05x slower                                                      |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                      |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                                      |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.3 ms: 3.47x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                               |

Benchmark hidden because not significant (3): asyncio_websockets, fannkuch, nqueens
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250326-3.14.0a6+-b3d84fd-JIT/bm-20250326-linux-x86_64-brandtbucher-keep_stack_pointer-3.14.0a6+-b3d84fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.129x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x