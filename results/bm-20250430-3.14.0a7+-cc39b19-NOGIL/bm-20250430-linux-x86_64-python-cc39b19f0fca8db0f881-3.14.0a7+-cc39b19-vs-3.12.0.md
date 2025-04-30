# Results vs. 3.12.0

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.025x faster
- HPT reliability: 83.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 292 ms: 1.06x slower                                                   |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 514 ms: 2.30x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 548 ms: 2.11x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 228 ms: 1.97x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 294 ms: 1.95x faster                                                   |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.84x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                  |
| pidigits       | 187 ms                                                 | 181 ms: 1.04x faster                                                   |
| nbody          | 97.0 ms                                                | 129 ms: 1.33x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                  |
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                   |
| tomli_loads          | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 239 us: 1.04x slower                                                   |
| pickle_pure_python   | 324 us                                                 | 345 us: 1.07x slower                                                   |
| xml_etree_generate   | 89.2 ms                                                | 96.3 ms: 1.08x slower                                                  |
| xml_etree_process    | 61.7 ms                                                | 68.1 ms: 1.10x slower                                                  |
| json_loads           | 28.5 us                                                | 32.6 us: 1.14x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.1 ms: 1.26x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.12 ms: 1.31x slower                                                  |
| python_startup         | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 39.3 ms: 1.14x slower                                                  |
| mako            | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.24x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 514 ms: 2.30x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 548 ms: 2.11x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 228 ms: 1.97x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 294 ms: 1.95x faster                                                   |
| mdp                        | 2.63 sec                                               | 1.39 sec: 1.89x faster                                                 |
| async_tree_none            | 472 ms                                                 | 266 ms: 1.77x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 330 ms: 1.75x faster                                                   |
| gc_traversal               | 3.79 ms                                                | 2.29 ms: 1.66x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 459 ms: 1.58x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 500 ms: 1.45x faster                                                   |
| deepcopy                   | 371 us                                                 | 298 us: 1.24x faster                                                   |
| float                      | 84.7 ms                                                | 70.9 ms: 1.20x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.17 ms: 1.14x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 36.4 us: 1.12x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.5 ms: 1.11x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.7 us: 1.10x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 62.4 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.6 ms: 1.09x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 3.16 us: 1.06x faster                                                  |
| async_generators           | 463 ms                                                 | 442 ms: 1.05x faster                                                   |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 2.24 sec: 1.04x faster                                                 |
| pidigits                   | 187 ms                                                 | 181 ms: 1.04x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                  |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                 |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.70 ms: 1.00x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.01x slower                                                 |
| chaos                      | 67.0 ms                                                | 67.7 ms: 1.01x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 171 ms: 1.01x slower                                                   |
| sympy_str                  | 300 ms                                                 | 305 ms: 1.02x slower                                                   |
| logging_simple             | 6.46 us                                                | 6.58 us: 1.02x slower                                                  |
| logging_format             | 7.23 us                                                | 7.38 us: 1.02x slower                                                  |
| raytrace                   | 312 ms                                                 | 321 ms: 1.03x slower                                                   |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.03x slower                                                   |
| pprint_safe_repr           | 776 ms                                                 | 806 ms: 1.04x slower                                                   |
| unpickle_pure_python       | 230 us                                                 | 239 us: 1.04x slower                                                   |
| pyflate                    | 482 ms                                                 | 503 ms: 1.04x slower                                                   |
| sympy_integrate            | 21.4 ms                                                | 22.3 ms: 1.04x slower                                                  |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.67 sec: 1.06x slower                                                 |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                   |
| 2to3                       | 274 ms                                                 | 292 ms: 1.06x slower                                                   |
| pickle_pure_python         | 324 us                                                 | 345 us: 1.07x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 157 ms: 1.07x slower                                                   |
| coroutines                 | 23.2 ms                                                | 24.9 ms: 1.07x slower                                                  |
| json                       | 5.26 ms                                                | 5.66 ms: 1.08x slower                                                  |
| scimark_fft                | 382 ms                                                 | 411 ms: 1.08x slower                                                   |
| xml_etree_generate         | 89.2 ms                                                | 96.3 ms: 1.08x slower                                                  |
| sympy_expand               | 478 ms                                                 | 516 ms: 1.08x slower                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.4 ms: 1.09x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 89.4 ms: 1.09x slower                                                  |
| nqueens                    | 83.3 ms                                                | 91.7 ms: 1.10x slower                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 82.8 ms: 1.10x slower                                                  |
| xml_etree_process          | 61.7 ms                                                | 68.1 ms: 1.10x slower                                                  |
| richards                   | 45.8 ms                                                | 50.6 ms: 1.10x slower                                                  |
| django_template            | 34.6 ms                                                | 39.3 ms: 1.14x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.29 ms: 1.14x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 1.69 ms: 1.14x slower                                                  |
| json_loads                 | 28.5 us                                                | 32.6 us: 1.14x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.87 ms: 1.16x slower                                                  |
| richards_super             | 51.5 ms                                                | 60.0 ms: 1.16x slower                                                  |
| meteor_contest             | 112 ms                                                 | 132 ms: 1.18x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 139 ms: 1.18x slower                                                   |
| fannkuch                   | 417 ms                                                 | 503 ms: 1.21x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 13.1 ms: 1.26x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 202 us: 1.28x slower                                                   |
| telco                      | 7.10 ms                                                | 9.08 ms: 1.28x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.12 ms: 1.31x slower                                                  |
| nbody                      | 97.0 ms                                                | 129 ms: 1.33x slower                                                   |
| mako                       | 11.9 ms                                                | 16.2 ms: 1.36x slower                                                  |
| python_startup             | 9.55 ms                                                | 15.5 ms: 1.62x slower                                                  |
| coverage                   | 72.7 ms                                                | 123 ms: 1.69x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 90.6 ms: 3.77x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 3.27 ms: 3.89x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, regex_dna
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-cc39b19-NOGIL/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 83.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.32x