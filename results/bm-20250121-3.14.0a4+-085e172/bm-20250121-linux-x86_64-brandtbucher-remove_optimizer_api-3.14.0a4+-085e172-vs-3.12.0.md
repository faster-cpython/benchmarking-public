# Results vs. 3.12.0

- fork: brandtbucher
- ref: remove_optimizer_api
- machine: linux-x86_64
- commit hash: 085e172
- commit date: 2025-01-21
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 256 ms: 1.07x faster                                                         |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 591 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                        |
| nbody          | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                        |
| regex_dna      | 212 ms                                                 | 208 ms: 1.02x faster                                                         |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 97.2 ms: 1.10x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 61.4 ms: 1.00x faster                                                        |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| pickle_pure_python   | 324 us                                                 | 331 us: 1.02x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 591 ms: 2.00x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                                         |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 31.2 us: 1.30x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                        |
| go                         | 139 ms                                                 | 116 ms: 1.21x faster                                                         |
| float                      | 84.7 ms                                                | 70.7 ms: 1.20x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                        |
| async_generators           | 463 ms                                                 | 388 ms: 1.19x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.16 ms: 1.17x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                                       |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                         |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                         |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                        |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                         |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.12x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 73.0 ms: 1.12x faster                                                        |
| generators                 | 31.2 ms                                                | 28.2 ms: 1.11x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 68.3 ms: 1.10x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 97.2 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.61 ms: 1.10x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                        |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                        |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                        |
| 2to3                       | 274 ms                                                 | 256 ms: 1.07x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 727 ms: 1.07x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.8 ms: 1.06x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                        |
| nqueens                    | 83.3 ms                                                | 78.7 ms: 1.06x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                       |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                         |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 105 ms: 1.05x faster                                                         |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                        |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                                        |
| logging_silent             | 104 ns                                                 | 100.0 ns: 1.04x faster                                                       |
| nbody                      | 97.0 ms                                                | 92.9 ms: 1.04x faster                                                        |
| pyflate                    | 482 ms                                                 | 466 ms: 1.04x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.0 ms: 1.03x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                         |
| richards_super             | 51.5 ms                                                | 50.2 ms: 1.03x faster                                                        |
| fannkuch                   | 417 ms                                                 | 407 ms: 1.02x faster                                                         |
| regex_dna                  | 212 ms                                                 | 208 ms: 1.02x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                                         |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 61.4 ms: 1.00x faster                                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                        |
| pickle_pure_python         | 324 us                                                 | 331 us: 1.02x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 864 us: 1.03x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                        |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.9 ms: 1.15x slower                                                        |
| coverage                   | 72.7 ms                                                | 89.8 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.77 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-085e172/bm-20250121-linux-x86_64-brandtbucher-remove_optimizer_api-3.14.0a4+-085e172.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x