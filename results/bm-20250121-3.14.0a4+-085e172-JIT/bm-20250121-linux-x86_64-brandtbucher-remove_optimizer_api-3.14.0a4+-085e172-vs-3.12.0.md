# Results vs. 3.12.0

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.104x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 589 ms: 2.01x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.78x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                        |
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                        |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.15x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 94.0 ms: 1.14x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 206 us: 1.12x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 328 us: 1.01x slower                                                         |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                        |
| django_template | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 589 ms: 2.01x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 466 ms: 1.56x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 485 ms: 1.50x faster                                                         |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                        |
| float                      | 84.7 ms                                                | 65.1 ms: 1.30x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                       |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                         |
| mako                       | 11.9 ms                                                | 9.83 ms: 1.21x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.2 ms: 1.21x faster                                                        |
| spectral_norm              | 115 ms                                                 | 95.1 ms: 1.21x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 68.4 ms: 1.20x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.15x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.42 ms: 1.14x faster                                                        |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 94.0 ms: 1.14x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                                        |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.13x faster                                                         |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 206 us: 1.12x faster                                                         |
| async_generators           | 463 ms                                                 | 415 ms: 1.12x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 80.3 ms: 1.11x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.30 ms: 1.09x faster                                                        |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                         |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                        |
| logging_format             | 7.23 us                                                | 6.71 us: 1.08x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| sympy_str                  | 300 ms                                                 | 281 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                        |
| fannkuch                   | 417 ms                                                 | 393 ms: 1.06x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                         |
| logging_simple             | 6.46 us                                                | 6.15 us: 1.05x faster                                                        |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                         |
| go                         | 139 ms                                                 | 133 ms: 1.05x faster                                                         |
| richards_super             | 51.5 ms                                                | 49.3 ms: 1.04x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.04x faster                                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| django_template            | 34.6 ms                                                | 33.5 ms: 1.03x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                       |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 67.9 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                         |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                         |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                        |
| pickle_pure_python         | 324 us                                                 | 328 us: 1.01x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                        |
| richards                   | 45.8 ms                                                | 47.1 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                         |
| logging_silent             | 104 ns                                                 | 111 ns: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.58 ms: 1.07x slower                                                        |
| nqueens                    | 83.3 ms                                                | 90.9 ms: 1.09x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.11 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| generators                 | 31.2 ms                                                | 37.2 ms: 1.19x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.60 ms: 1.21x slower                                                        |
| coverage                   | 72.7 ms                                                | 91.8 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, sqlglot_optimize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-085e172-JIT/bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.104x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x