# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: outline
- machine: linux-x86_64
- commit hash: 69dad45
- commit date: 2025-05-08
- overall geometric mean: 1.094x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                                |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                               |
| nbody          | 97.0 ms                                                | 99.3 ms: 1.02x slower                                               |
| pidigits       | 187 ms                                                 | 195 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.95 ms: 1.23x faster                                               |
| regex_compile  | 148 ms                                                 | 130 ms: 1.15x faster                                                |
| regex_dna      | 212 ms                                                 | 195 ms: 1.09x faster                                                |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.12x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 58.7 ms: 1.05x faster                                               |
| unpickle_pure_python | 230 us                                                 | 234 us: 1.02x slower                                                |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                               |
| pickle_pure_python   | 324 us                                                 | 335 us: 1.03x slower                                                |
| json_dumps           | 10.4 ms                                                | 12.1 ms: 1.17x slower                                               |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.96 ms: 1.00x slower                                               |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.29 sec: 2.04x faster                                              |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 622 ms: 1.90x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.80x faster                                                |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                |
| deepcopy                   | 371 us                                                 | 260 us: 1.43x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                               |
| regex_effbot               | 3.61 ms                                                | 2.95 ms: 1.23x faster                                               |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                               |
| richards                   | 45.8 ms                                                | 38.5 ms: 1.19x faster                                               |
| richards_super             | 51.5 ms                                                | 43.8 ms: 1.18x faster                                               |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.16x faster                                               |
| regex_compile              | 148 ms                                                 | 130 ms: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                              |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                |
| logging_format             | 7.23 us                                                | 6.41 us: 1.13x faster                                               |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.12x faster                                               |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                |
| dulwich_log                | 68.5 ms                                                | 62.5 ms: 1.10x faster                                               |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                |
| async_generators           | 463 ms                                                 | 426 ms: 1.09x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                               |
| regex_dna                  | 212 ms                                                 | 195 ms: 1.09x faster                                                |
| logging_silent             | 104 ns                                                 | 97.4 ns: 1.07x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                               |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                |
| scimark_fft                | 382 ms                                                 | 362 ms: 1.06x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 58.7 ms: 1.05x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.8 ms: 1.05x faster                                               |
| django_template            | 34.6 ms                                                | 32.9 ms: 1.05x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 71.6 ms: 1.05x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.55 ms: 1.05x faster                                               |
| pyflate                    | 482 ms                                                 | 462 ms: 1.05x faster                                                |
| go                         | 139 ms                                                 | 135 ms: 1.04x faster                                                |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                                |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                               |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                              |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 80.0 ms: 1.02x faster                                               |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                               |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.96 ms: 1.00x slower                                               |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                |
| sympy_expand               | 478 ms                                                 | 481 ms: 1.01x slower                                                |
| unpickle_pure_python       | 230 us                                                 | 234 us: 1.02x slower                                                |
| nbody                      | 97.0 ms                                                | 99.3 ms: 1.02x slower                                               |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                               |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                |
| pickle_pure_python         | 324 us                                                 | 335 us: 1.03x slower                                                |
| pidigits                   | 187 ms                                                 | 195 ms: 1.04x slower                                                |
| fannkuch                   | 417 ms                                                 | 437 ms: 1.05x slower                                                |
| pprint_safe_repr           | 776 ms                                                 | 820 ms: 1.06x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                               |
| bench_thread_pool          | 842 us                                                 | 900 us: 1.07x slower                                                |
| pprint_pformat             | 1.57 sec                                               | 1.69 sec: 1.08x slower                                              |
| hexiom                     | 6.41 ms                                                | 7.08 ms: 1.10x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 175 us: 1.11x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.79 ms: 1.14x slower                                               |
| telco                      | 7.10 ms                                                | 8.21 ms: 1.16x slower                                               |
| json_dumps                 | 10.4 ms                                                | 12.1 ms: 1.17x slower                                               |
| coverage                   | 72.7 ms                                                | 88.0 ms: 1.21x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.73 ms: 1.25x slower                                               |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 93.4 ms: 3.89x slower                                               |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, json, nqueens
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250508-3.14.0a7+-69dad45-JIT/bm-20250508-linux-x86_64-Fidget%2dSpinner-outline-3.14.0a7+-69dad45.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.094x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.14x