# Results vs. 3.12.0

- fork: faster-cpython
- ref: current_executor
- machine: linux-x86_64
- commit hash: a30e444
- commit date: 2025-05-03
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.7 ms: 1.31x faster                                                        |
| nbody          | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.39 ms: 1.07x faster                                                        |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                        |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                                        |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                        |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.95x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.47x faster                                                         |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                        |
| float                      | 84.7 ms                                                | 64.7 ms: 1.31x faster                                                        |
| richards                   | 45.8 ms                                                | 35.4 ms: 1.29x faster                                                        |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.08 ms: 1.21x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.3 us: 1.19x faster                                                        |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.17x faster                                                         |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                        |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 60.9 ms: 1.12x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.76 us: 1.12x faster                                                        |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                        |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                         |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.10x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                         |
| async_generators           | 463 ms                                                 | 423 ms: 1.09x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.8 ms: 1.09x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.6 ms: 1.09x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                         |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                        |
| logging_silent             | 104 ns                                                 | 96.8 ns: 1.08x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.08x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 76.2 ms: 1.07x faster                                                        |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.39 ms: 1.07x faster                                                        |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                         |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 747 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| nbody                      | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.92 ms: 1.03x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                        |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                         |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                        |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                                         |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                        |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                        |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.02x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.74 ms: 1.05x slower                                                        |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 894 us: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.10x slower                                                         |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                        |
| telco                      | 7.10 ms                                                | 7.87 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 93.4 ms: 1.29x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250503-3.14.0a7+-a30e444-JIT/bm-20250503-linux-x86_64-faster%2dcpython-current_executor-3.14.0a7+-a30e444.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x