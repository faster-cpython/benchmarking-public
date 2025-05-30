# Results vs. 3.12.0

- fork: iritkatriel
- ref: list_subscr
- machine: linux-x86_64
- commit hash: c52d9d2
- commit date: 2025-04-16
- overall geometric mean: 1.126x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                               |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                               |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                               |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                               |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.2 ms: 1.24x faster                                              |
| nbody          | 97.0 ms                                                | 95.4 ms: 1.02x faster                                              |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                              |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                              |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                               |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.05x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 58.5 ms: 1.05x faster                                              |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                               |
| json_loads           | 28.5 us                                                | 30.1 us: 1.05x slower                                              |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                              |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                              |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                              |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                              |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                               |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                               |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                               |
| deepcopy                   | 371 us                                                 | 248 us: 1.50x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                              |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.64 us: 1.27x faster                                              |
| float                      | 84.7 ms                                                | 68.2 ms: 1.24x faster                                              |
| go                         | 139 ms                                                 | 112 ms: 1.24x faster                                               |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                               |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                              |
| chaos                      | 67.0 ms                                                | 56.0 ms: 1.20x faster                                              |
| logging_simple             | 6.46 us                                                | 5.45 us: 1.18x faster                                              |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                             |
| async_generators           | 463 ms                                                 | 396 ms: 1.17x faster                                               |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                              |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                               |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                              |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                              |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.3 ms: 1.12x faster                                              |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                               |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                              |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                              |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.39 ms: 1.10x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                             |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                              |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                              |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                               |
| richards                   | 45.8 ms                                                | 42.8 ms: 1.07x faster                                              |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                               |
| pyflate                    | 482 ms                                                 | 453 ms: 1.07x faster                                               |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                               |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                             |
| scimark_fft                | 382 ms                                                 | 360 ms: 1.06x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                               |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                              |
| logging_silent             | 104 ns                                                 | 98.8 ns: 1.06x faster                                              |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                              |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.05x faster                                              |
| xml_etree_process          | 61.7 ms                                                | 58.5 ms: 1.05x faster                                              |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                              |
| hexiom                     | 6.41 ms                                                | 6.17 ms: 1.04x faster                                              |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.88 ms: 1.04x faster                                              |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                              |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                               |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                             |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                              |
| nbody                      | 97.0 ms                                                | 95.4 ms: 1.02x faster                                              |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                               |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                               |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                              |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                               |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                               |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.05x slower                                              |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                              |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                               |
| telco                      | 7.10 ms                                                | 7.69 ms: 1.08x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                              |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.26x slower                                              |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 81.9 ms: 3.41x slower                                              |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, regex_v8
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-c52d9d2/bm-20250416-linux-x86_64-iritkatriel-list_subscr-3.14.0a7+-c52d9d2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.126x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x