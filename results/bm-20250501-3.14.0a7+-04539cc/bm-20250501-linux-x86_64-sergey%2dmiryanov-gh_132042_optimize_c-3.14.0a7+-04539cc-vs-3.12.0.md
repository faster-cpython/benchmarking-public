# Results vs. 3.12.0

- fork: sergey-miryanov
- ref: gh_132042_optimize_c
- machine: linux-x86_64
- commit hash: 04539cc
- commit date: 2025-05-01
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                              |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                              |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                                              |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                              |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                              |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                             |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                              |
| nbody          | 97.0 ms                                                | 101 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                              |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                             |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                             |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                              |
| xml_etree_iterparse  | 107 ms                                                 | 99.5 ms: 1.07x faster                                                             |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                              |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                             |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                              |
| json_loads           | 28.5 us                                                | 30.3 us: 1.06x slower                                                             |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                             |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                             |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.13x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                              |
| async_tree_io_tg           | 1.18 sec                                               | 615 ms: 1.92x faster                                                              |
| async_tree_memoization_tg  | 575 ms                                                 | 305 ms: 1.88x faster                                                              |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                              |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                              |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                                              |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                              |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                             |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                             |
| go                         | 139 ms                                                 | 112 ms: 1.24x faster                                                              |
| float                      | 84.7 ms                                                | 69.3 ms: 1.22x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                             |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                                            |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                              |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                             |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                             |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                             |
| async_generators           | 463 ms                                                 | 409 ms: 1.13x faster                                                              |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                              |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                              |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                              |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                              |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                             |
| sympy_integrate            | 21.4 ms                                                | 19.2 ms: 1.12x faster                                                             |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                             |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                              |
| crypto_pyaes               | 81.9 ms                                                | 74.7 ms: 1.10x faster                                                             |
| logging_silent             | 104 ns                                                 | 95.9 ns: 1.09x faster                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                             |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                             |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                              |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                              |
| xml_etree_iterparse        | 107 ms                                                 | 99.5 ms: 1.07x faster                                                             |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 732 ms: 1.06x faster                                                              |
| pyflate                    | 482 ms                                                 | 456 ms: 1.06x faster                                                              |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                              |
| scimark_fft                | 382 ms                                                 | 363 ms: 1.05x faster                                                              |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.82 ms: 1.05x faster                                                             |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                              |
| richards                   | 45.8 ms                                                | 44.0 ms: 1.04x faster                                                             |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                              |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                             |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                             |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                             |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.25 ms: 1.03x faster                                                             |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                              |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                              |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                              |
| nqueens                    | 83.3 ms                                                | 82.1 ms: 1.01x faster                                                             |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                             |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                              |
| fannkuch                   | 417 ms                                                 | 423 ms: 1.01x slower                                                              |
| sqlite_synth               | 2.83 us                                                | 2.92 us: 1.03x slower                                                             |
| nbody                      | 97.0 ms                                                | 101 ms: 1.04x slower                                                              |
| json                       | 5.26 ms                                                | 5.52 ms: 1.05x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                                              |
| json_loads                 | 28.5 us                                                | 30.3 us: 1.06x slower                                                             |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                              |
| coroutines                 | 23.2 ms                                                | 25.4 ms: 1.10x slower                                                             |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                             |
| coverage                   | 72.7 ms                                                | 92.1 ms: 1.27x slower                                                             |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                             |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.70x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                      |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250501-3.14.0a7+-04539cc/bm-20250501-linux-x86_64-sergey%2dmiryanov-gh_132042_optimize_c-3.14.0a7+-04539cc.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x