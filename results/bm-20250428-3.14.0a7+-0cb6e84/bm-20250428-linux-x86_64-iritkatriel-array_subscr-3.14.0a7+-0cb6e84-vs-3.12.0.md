# Results vs. 3.12.0

- fork: iritkatriel
- ref: array_subscr
- machine: linux-x86_64
- commit hash: 0cb6e84
- commit date: 2025-04-28
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 602 ms: 1.96x faster                                                |
| async_tree_io              | 1.16 sec                                               | 590 ms: 1.96x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.4 ms: 1.22x faster                                               |
| nbody          | 97.0 ms                                                | 97.8 ms: 1.01x slower                                               |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                               |
| regex_v8       | 23.1 ms                                                | 22.2 ms: 1.04x faster                                               |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                               |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.3 ms: 1.06x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                               |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                |
| json_loads           | 28.5 us                                                | 30.4 us: 1.07x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                               |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| mako            | 11.9 ms                                                | 11.6 ms: 1.03x faster                                               |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 602 ms: 1.96x faster                                                |
| async_tree_io              | 1.16 sec                                               | 590 ms: 1.96x faster                                                |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 482 ms: 1.51x faster                                                |
| deepcopy                   | 371 us                                                 | 252 us: 1.47x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                               |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                               |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                |
| float                      | 84.7 ms                                                | 69.4 ms: 1.22x faster                                               |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                               |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                               |
| async_generators           | 463 ms                                                 | 396 ms: 1.17x faster                                                |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.3 ms: 1.16x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                               |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.12x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.32 ms: 1.12x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                               |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                                |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 713 ms: 1.09x faster                                                |
| logging_silent             | 104 ns                                                 | 96.3 ns: 1.08x faster                                               |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                                |
| pyflate                    | 482 ms                                                 | 454 ms: 1.06x faster                                                |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                               |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 84.3 ms: 1.06x faster                                               |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                              |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.2 ms: 1.04x faster                                               |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                               |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                               |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.03x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                              |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                               |
| nbody                      | 97.0 ms                                                | 97.8 ms: 1.01x slower                                               |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                               |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                               |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                                |
| scimark_lu                 | 118 ms                                                 | 124 ms: 1.05x slower                                                |
| json_loads                 | 28.5 us                                                | 30.4 us: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.50 ms: 1.09x slower                                               |
| telco                      | 7.10 ms                                                | 7.79 ms: 1.10x slower                                               |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                               |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                               |
| coverage                   | 72.7 ms                                                | 92.3 ms: 1.27x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.98 ms: 1.31x slower                                               |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                        |

Benchmark hidden because not significant (3): asyncio_websockets, fannkuch, scimark_fft
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250428-3.14.0a7+-0cb6e84/bm-20250428-linux-x86_64-iritkatriel-array_subscr-3.14.0a7+-0cb6e84.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x