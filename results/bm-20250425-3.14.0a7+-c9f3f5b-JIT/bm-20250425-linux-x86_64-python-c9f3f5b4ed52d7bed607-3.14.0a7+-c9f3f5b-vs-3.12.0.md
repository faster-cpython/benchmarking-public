# Results vs. 3.12.0

- fork: python
- ref: c9f3f5b4ed52d7bed607
- machine: linux-x86_64
- commit hash: c9f3f5b
- commit date: 2025-04-25
- overall geometric mean: 1.126x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 598 ms: 1.98x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                  |
| nbody          | 97.0 ms                                                | 87.3 ms: 1.11x faster                                                  |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                  |
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_dna      | 212 ms                                                 | 201 ms: 1.05x faster                                                   |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.28x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.13x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                  |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.18x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 598 ms: 1.98x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 594 ms: 1.95x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 306 ms: 1.88x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.46x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.28x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                                  |
| richards                   | 45.8 ms                                                | 36.6 ms: 1.25x faster                                                  |
| richards_super             | 51.5 ms                                                | 42.0 ms: 1.23x faster                                                  |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.22x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                                  |
| float                      | 84.7 ms                                                | 71.2 ms: 1.19x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                  |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.17x faster                                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                  |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.2 ms: 1.13x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.13x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 61.1 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                  |
| async_generators           | 463 ms                                                 | 415 ms: 1.11x faster                                                   |
| nbody                      | 97.0 ms                                                | 87.3 ms: 1.11x faster                                                  |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 80.4 ms: 1.11x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                   |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.8 ms: 1.09x faster                                                  |
| go                         | 139 ms                                                 | 128 ms: 1.09x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 56.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.67 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 725 ms: 1.07x faster                                                   |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                   |
| logging_silent             | 104 ns                                                 | 98.4 ns: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| pyflate                    | 482 ms                                                 | 457 ms: 1.05x faster                                                   |
| regex_dna                  | 212 ms                                                 | 201 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.76 us: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.03x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                                  |
| sympy_expand               | 478 ms                                                 | 469 ms: 1.02x faster                                                   |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                   |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                  |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                  |
| json                       | 5.26 ms                                                | 5.52 ms: 1.05x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 895 us: 1.06x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 173 us: 1.09x slower                                                   |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                  |
| coverage                   | 72.7 ms                                                | 94.0 ms: 1.29x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.39x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (3): pycparser, asyncio_websockets, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250425-3.14.0a7+-c9f3f5b-JIT/bm-20250425-linux-x86_64-python-c9f3f5b4ed52d7bed607-3.14.0a7+-c9f3f5b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.126x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x