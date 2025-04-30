# Results vs. 3.12.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: 638a892
- commit date: 2025-04-29
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                               |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.2 ms: 1.22x faster                                              |
| nbody          | 97.0 ms                                                | 96.3 ms: 1.01x faster                                              |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.14 ms: 1.15x faster                                              |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                              |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.06x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 87.6 ms: 1.02x faster                                              |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                               |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.87 ms: 1.01x faster                                              |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                              |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                              |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                             |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 612 ms: 1.93x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.83x faster                                               |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 487 ms: 1.49x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 492 ms: 1.48x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 28.3 us: 1.44x faster                                              |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                               |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                              |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                               |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                              |
| float                      | 84.7 ms                                                | 69.2 ms: 1.22x faster                                              |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                              |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                             |
| chaos                      | 67.0 ms                                                | 56.9 ms: 1.18x faster                                              |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                              |
| async_generators           | 463 ms                                                 | 401 ms: 1.15x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.14 ms: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                              |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                              |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.12x faster                                               |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                              |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.10x faster                                               |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                              |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.3 ms: 1.08x faster                                              |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                               |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 723 ms: 1.07x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                             |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.06x faster                                               |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                              |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                              |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                               |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                              |
| richards_super             | 51.5 ms                                                | 49.7 ms: 1.04x faster                                              |
| nqueens                    | 83.3 ms                                                | 80.4 ms: 1.04x faster                                              |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                               |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 87.6 ms: 1.02x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                              |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                               |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.87 ms: 1.01x faster                                              |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                               |
| nbody                      | 97.0 ms                                                | 96.3 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                               |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.16 ms: 1.02x slower                                              |
| json                       | 5.26 ms                                                | 5.50 ms: 1.05x slower                                              |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                               |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                               |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                              |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                              |
| coverage                   | 72.7 ms                                                | 92.8 ms: 1.28x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.85 ms: 1.28x slower                                              |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.41x slower                                              |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                       |

Benchmark hidden because not significant (2): pycparser, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250429-3.14.0a7+-638a892/bm-20250429-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-638a892.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.11x