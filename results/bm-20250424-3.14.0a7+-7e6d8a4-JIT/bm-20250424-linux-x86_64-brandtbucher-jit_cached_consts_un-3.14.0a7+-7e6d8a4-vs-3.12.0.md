# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_cached_consts_un
- machine: linux-x86_64
- commit hash: 7e6d8a4
- commit date: 2025-04-24
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                        |
| nbody          | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                        |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.18 ms: 1.14x faster                                                        |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 208 us: 1.11x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.08x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.01x faster                                                         |
| json_loads           | 28.5 us                                                | 30.2 us: 1.06x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.27 ms: 1.19x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                        |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.18x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 253 us: 1.47x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                       |
| richards                   | 45.8 ms                                                | 36.2 ms: 1.27x faster                                                        |
| richards_super             | 51.5 ms                                                | 41.1 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.00 ms: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                         |
| float                      | 84.7 ms                                                | 69.5 ms: 1.22x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.6 us: 1.17x faster                                                        |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                        |
| logging_format             | 7.23 us                                                | 6.24 us: 1.16x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                        |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                         |
| chaos                      | 67.0 ms                                                | 58.8 ms: 1.14x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.18 ms: 1.14x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 61.2 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.7 ms: 1.12x faster                                                        |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                         |
| pyflate                    | 482 ms                                                 | 433 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                        |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 208 us: 1.11x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                        |
| async_generators           | 463 ms                                                 | 422 ms: 1.10x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.09x faster                                                         |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                        |
| nbody                      | 97.0 ms                                                | 89.3 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.08x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                        |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                        |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                         |
| 2to3                       | 274 ms                                                 | 260 ms: 1.05x faster                                                         |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                         |
| generators                 | 31.2 ms                                                | 30.4 ms: 1.03x faster                                                        |
| logging_silent             | 104 ns                                                 | 102 ns: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.01x faster                                                         |
| nqueens                    | 83.3 ms                                                | 82.3 ms: 1.01x faster                                                        |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                         |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.8 ms: 1.03x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                        |
| json                       | 5.26 ms                                                | 5.49 ms: 1.04x slower                                                        |
| json_loads                 | 28.5 us                                                | 30.2 us: 1.06x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 894 us: 1.06x slower                                                         |
| coroutines                 | 23.2 ms                                                | 24.7 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                         |
| telco                      | 7.10 ms                                                | 7.70 ms: 1.09x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.27 ms: 1.19x slower                                                        |
| coverage                   | 72.7 ms                                                | 93.7 ms: 1.29x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.03 ms: 1.33x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250424-3.14.0a7+-7e6d8a4-JIT/bm-20250424-linux-x86_64-brandtbucher-jit_cached_consts_un-3.14.0a7+-7e6d8a4.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.12x