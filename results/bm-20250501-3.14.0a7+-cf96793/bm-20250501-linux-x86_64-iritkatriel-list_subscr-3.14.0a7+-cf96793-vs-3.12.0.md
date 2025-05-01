# Results vs. 3.12.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: cf96793
- commit date: 2025-05-01
- overall geometric mean: 1.109x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                               |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.0 ms: 1.18x faster                                              |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                              |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                               |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 100 ms: 1.07x faster                                               |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 85.0 ms: 1.05x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 59.3 ms: 1.04x faster                                              |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                               |
| json_loads           | 28.5 us                                                | 30.5 us: 1.07x slower                                              |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.15x slower                                              |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                              |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                              |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                              |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                              |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                             |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.94x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                               |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                               |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.45x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                              |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                              |
| go                         | 139 ms                                                 | 113 ms: 1.24x faster                                               |
| float                      | 84.7 ms                                                | 72.0 ms: 1.18x faster                                              |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                               |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                               |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                              |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                              |
| dulwich_log                | 68.5 ms                                                | 59.8 ms: 1.15x faster                                              |
| async_generators           | 463 ms                                                 | 409 ms: 1.13x faster                                               |
| chaos                      | 67.0 ms                                                | 59.3 ms: 1.13x faster                                              |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.12x faster                                              |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                             |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                              |
| logging_silent             | 104 ns                                                 | 93.6 ns: 1.12x faster                                              |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.11x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.08x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                              |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                               |
| xml_etree_iterparse        | 107 ms                                                 | 100 ms: 1.07x faster                                               |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                               |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                              |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 77.1 ms: 1.06x faster                                              |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| richards                   | 45.8 ms                                                | 43.3 ms: 1.06x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                             |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                              |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 85.0 ms: 1.05x faster                                              |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 59.3 ms: 1.04x faster                                              |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                               |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                              |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                             |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.02x faster                                               |
| nqueens                    | 83.3 ms                                                | 81.8 ms: 1.02x faster                                              |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                               |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                               |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                              |
| scimark_fft                | 382 ms                                                 | 378 ms: 1.01x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.37 ms: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                               |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                              |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                               |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                              |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                              |
| json                       | 5.26 ms                                                | 5.45 ms: 1.04x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.05x slower                                               |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.37 ms: 1.06x slower                                              |
| json_loads                 | 28.5 us                                                | 30.5 us: 1.07x slower                                              |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                              |
| coroutines                 | 23.2 ms                                                | 26.3 ms: 1.13x slower                                              |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.15x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                              |
| coverage                   | 72.7 ms                                                | 93.2 ms: 1.28x slower                                              |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                              |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, nbody
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250501-3.14.0a7+-cf96793/bm-20250501-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-cf96793.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.109x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x