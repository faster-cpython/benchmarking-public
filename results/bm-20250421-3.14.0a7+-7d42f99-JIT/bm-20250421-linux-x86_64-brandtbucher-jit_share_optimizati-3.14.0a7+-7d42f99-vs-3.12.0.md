# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_share_optimizati
- machine: linux-x86_64
- commit hash: 7d42f99
- commit date: 2025-04-21
- overall geometric mean: 1.128x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                        |
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_dna      | 212 ms                                                 | 199 ms: 1.07x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 207 us: 1.11x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.25 ms: 1.19x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                        |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                         |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 28.3 us: 1.44x faster                                                        |
| richards                   | 45.8 ms                                                | 33.0 ms: 1.39x faster                                                        |
| richards_super             | 51.5 ms                                                | 38.2 ms: 1.35x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.04 ms: 1.22x faster                                                        |
| scimark_fft                | 382 ms                                                 | 315 ms: 1.21x faster                                                         |
| float                      | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                        |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                         |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                         |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                                        |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                                        |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| comprehensions             | 21.8 us                                                | 19.2 us: 1.13x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 66.5 ms: 1.13x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 60.7 ms: 1.13x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                                        |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 207 us: 1.11x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                        |
| logging_silent             | 104 ns                                                 | 94.5 ns: 1.11x faster                                                        |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                         |
| async_generators           | 463 ms                                                 | 420 ms: 1.10x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                        |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 135 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                        |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 718 ms: 1.08x faster                                                         |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.4 ms: 1.07x faster                                                        |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                       |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                        |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                        |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                         |
| nqueens                    | 83.3 ms                                                | 83.8 ms: 1.01x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                        |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                        |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 897 us: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.12x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.25 ms: 1.19x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                                        |
| coverage                   | 72.7 ms                                                | 93.0 ms: 1.28x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, fannkuch
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250421-3.14.0a7+-7d42f99-JIT/bm-20250421-linux-x86_64-brandtbucher-jit_share_optimizati-3.14.0a7+-7d42f99.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.128x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x