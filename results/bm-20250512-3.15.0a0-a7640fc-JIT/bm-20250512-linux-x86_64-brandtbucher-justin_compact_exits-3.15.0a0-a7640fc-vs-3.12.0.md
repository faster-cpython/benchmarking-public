# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: a7640fc
- commit date: 2025-05-12
- overall geometric mean: 1.082x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 263 ms: 1.04x faster                                                        |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                        |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.5 ms: 1.31x faster                                                       |
| nbody          | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                       |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                       |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                        |
| regex_dna      | 212 ms                                                 | 205 ms: 1.04x faster                                                        |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.15x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                       |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                       |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.3 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                       |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 599 ms: 1.93x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.86x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                        |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 496 ms: 1.46x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                        |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 30.1 us: 1.35x faster                                                       |
| float                      | 84.7 ms                                                | 64.5 ms: 1.31x faster                                                       |
| richards                   | 45.8 ms                                                | 35.0 ms: 1.31x faster                                                       |
| richards_super             | 51.5 ms                                                | 41.0 ms: 1.26x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.05 ms: 1.22x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.21x faster                                                       |
| comprehensions             | 21.8 us                                                | 18.0 us: 1.21x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                       |
| scimark_fft                | 382 ms                                                 | 326 ms: 1.17x faster                                                        |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                        |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.15x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                        |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                        |
| go                         | 139 ms                                                 | 124 ms: 1.13x faster                                                        |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 61.2 ms: 1.12x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                       |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                       |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.6 ms: 1.10x faster                                                       |
| async_generators           | 463 ms                                                 | 423 ms: 1.09x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                       |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                        |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 76.5 ms: 1.07x faster                                                       |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                        |
| logging_format             | 7.23 us                                                | 6.86 us: 1.05x faster                                                       |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| 2to3                       | 274 ms                                                 | 263 ms: 1.04x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                      |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 753 ms: 1.03x faster                                                        |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                        |
| nbody                      | 97.0 ms                                                | 94.3 ms: 1.03x faster                                                       |
| logging_simple             | 6.46 us                                                | 6.29 us: 1.03x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.02x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                       |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.00 ms: 1.01x faster                                                       |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                       |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                                       |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.54 ms: 1.02x slower                                                       |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                        |
| nqueens                    | 83.3 ms                                                | 85.2 ms: 1.02x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                       |
| generators                 | 31.2 ms                                                | 32.6 ms: 1.04x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 909 us: 1.08x slower                                                        |
| telco                      | 7.10 ms                                                | 7.71 ms: 1.09x slower                                                       |
| coroutines                 | 23.2 ms                                                | 25.2 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.15x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.3 ms: 1.28x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                       |
| dask                       | 372 ms                                                 | 923 ms: 2.48x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 93.3 ms: 3.89x slower                                                       |
| logging_silent             | 104 ns                                                 | 472 ns: 4.52x slower                                                        |
| coverage                   | 72.7 ms                                                | 419 ms: 5.76x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (4): pycparser, pickle_pure_python, asyncio_websockets, json
Ignored benchmarks (19) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (24) of results/bm-20250512-3.15.0a0-a7640fc-JIT/bm-20250512-linux-x86_64-brandtbucher-justin_compact_exits-3.15.0a0-a7640fc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.082x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x