# Results vs. 3.12.0

- fork: python
- ref: cc39b19f0fca8db0f881
- machine: linux-x86_64
- commit hash: cc39b19
- commit date: 2025-04-30
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                  |
| pidigits       | 187 ms                                                 | 195 ms: 1.04x slower                                                   |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                  |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                   |
| json_loads           | 28.5 us                                                | 30.7 us: 1.08x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                  |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.11x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 596 ms: 1.94x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                  |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                  |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 71.5 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                   |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                 |
| logging_format             | 7.23 us                                                | 6.32 us: 1.14x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.14x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.13x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                   |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                                   |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.12x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                  |
| logging_silent             | 104 ns                                                 | 96.5 ns: 1.08x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                                  |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 76.1 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                                  |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                                  |
| generators                 | 31.2 ms                                                | 29.2 ms: 1.07x faster                                                  |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.06x faster                                                   |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                   |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                  |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.5 ms: 1.03x faster                                                  |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                   |
| nqueens                    | 83.3 ms                                                | 81.9 ms: 1.02x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                   |
| scimark_fft                | 382 ms                                                 | 380 ms: 1.01x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                  |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                   |
| pidigits                   | 187 ms                                                 | 195 ms: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.27 ms: 1.04x slower                                                  |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                                   |
| json                       | 5.26 ms                                                | 5.56 ms: 1.06x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                   |
| json_loads                 | 28.5 us                                                | 30.7 us: 1.08x slower                                                  |
| telco                      | 7.10 ms                                                | 8.01 ms: 1.13x slower                                                  |
| coroutines                 | 23.2 ms                                                | 26.1 ms: 1.13x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                  |
| coverage                   | 72.7 ms                                                | 93.2 ms: 1.28x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.31x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (3): pycparser, asyncio_websockets, sqlite_synth
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-cc39b19/bm-20250430-linux-x86_64-python-cc39b19f0fca8db0f881-3.14.0a7+-cc39b19.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x