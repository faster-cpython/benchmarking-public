# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.5 ms: 1.19x faster                                                 |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| nbody          | 97.0 ms                                                | 103 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.07 ms: 1.18x faster                                                 |
| regex_dna      | 212 ms                                                 | 182 ms: 1.17x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                  |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.91x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.63 us: 1.27x faster                                                 |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                  |
| float                      | 84.7 ms                                                | 71.5 ms: 1.19x faster                                                 |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.07 ms: 1.18x faster                                                 |
| regex_dna                  | 212 ms                                                 | 182 ms: 1.17x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 58.9 ms: 1.16x faster                                                 |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.12x faster                                                  |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.1 ms: 1.10x faster                                                 |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                  |
| pyflate                    | 482 ms                                                 | 443 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.47 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.78 us: 1.07x faster                                                 |
| richards                   | 45.8 ms                                                | 43.0 ms: 1.07x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.6 ms: 1.06x faster                                                 |
| logging_simple             | 6.46 us                                                | 6.11 us: 1.06x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.07 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                  |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| richards_super             | 51.5 ms                                                | 48.9 ms: 1.05x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                 |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                  |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                                 |
| scimark_fft                | 382 ms                                                 | 379 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.00x faster                                                 |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.86 us: 1.01x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 785 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                |
| nbody                      | 97.0 ms                                                | 103 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                 |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                 |
| coverage                   | 72.7 ms                                                | 89.2 ms: 1.23x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.56 ms: 1.73x slower                                                 |
| logging_silent             | 104 ns                                                 | 475 ns: 4.54x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x