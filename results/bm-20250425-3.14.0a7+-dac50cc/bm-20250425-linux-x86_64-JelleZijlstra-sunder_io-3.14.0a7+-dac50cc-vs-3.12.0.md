# Results vs. 3.12.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-x86_64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                               |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 593 ms: 1.95x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.4 ms: 1.24x faster                                              |
| nbody          | 97.0 ms                                                | 99.4 ms: 1.03x slower                                              |
| pidigits       | 187 ms                                                 | 195 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.19 ms: 1.13x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                              |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.8 ms: 1.08x faster                                              |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 84.9 ms: 1.05x faster                                              |
| pickle_pure_python   | 324 us                                                 | 312 us: 1.04x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 59.5 ms: 1.04x faster                                              |
| json_loads           | 28.5 us                                                | 30.4 us: 1.07x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                              |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                              |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                              |
| mako            | 11.9 ms                                                | 11.7 ms: 1.01x faster                                              |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                             |
| async_tree_io              | 1.16 sec                                               | 593 ms: 1.95x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                               |
| deepcopy                   | 371 us                                                 | 253 us: 1.47x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                              |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                              |
| float                      | 84.7 ms                                                | 68.4 ms: 1.24x faster                                              |
| go                         | 139 ms                                                 | 113 ms: 1.23x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                             |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                               |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                               |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                              |
| chaos                      | 67.0 ms                                                | 56.9 ms: 1.18x faster                                              |
| logging_simple             | 6.46 us                                                | 5.54 us: 1.17x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                              |
| async_generators           | 463 ms                                                 | 403 ms: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                              |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.19 ms: 1.13x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.13x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 72.7 ms: 1.13x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                              |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.41 ms: 1.09x faster                                              |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                               |
| logging_silent             | 104 ns                                                 | 96.0 ns: 1.09x faster                                              |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 98.8 ms: 1.08x faster                                              |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                              |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                               |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                             |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                               |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                              |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                             |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 84.9 ms: 1.05x faster                                              |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                              |
| pickle_pure_python         | 324 us                                                 | 312 us: 1.04x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.5 ms: 1.04x faster                                              |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                              |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                             |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.01x faster                                              |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                              |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.00x faster                                               |
| nbody                      | 97.0 ms                                                | 99.4 ms: 1.03x slower                                              |
| pidigits                   | 187 ms                                                 | 195 ms: 1.04x slower                                               |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                               |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                              |
| json_loads                 | 28.5 us                                                | 30.4 us: 1.07x slower                                              |
| json                       | 5.26 ms                                                | 5.62 ms: 1.07x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 175 us: 1.11x slower                                               |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                              |
| coverage                   | 72.7 ms                                                | 92.8 ms: 1.28x slower                                              |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.4 ms: 3.43x slower                                              |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (3): asyncio_websockets, sqlite_synth, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-linux-x86_64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x