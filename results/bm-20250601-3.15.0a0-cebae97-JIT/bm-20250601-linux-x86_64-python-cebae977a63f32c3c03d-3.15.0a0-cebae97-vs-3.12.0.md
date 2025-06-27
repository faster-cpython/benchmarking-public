# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.652x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 63.7 ms: 1.33x faster                                                 |
| nbody          | 97.0 ms                                                | 93.1 ms: 1.04x faster                                                 |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| regex_dna      | 212 ms                                                 | 197 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 97.1 ms: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                 |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.94 ms: 1.00x slower                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                 |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.57 sec                                               | 1.45 us: 1080528.20x faster                                           |
| pprint_safe_repr           | 776 ms                                                 | 837 ns: 927059.13x faster                                             |
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.84x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                 |
| richards                   | 45.8 ms                                                | 33.5 ms: 1.37x faster                                                 |
| float                      | 84.7 ms                                                | 63.7 ms: 1.33x faster                                                 |
| richards_super             | 51.5 ms                                                | 39.2 ms: 1.31x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.24x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 1.89 sec: 1.23x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.09 ms: 1.20x faster                                                 |
| pyflate                    | 482 ms                                                 | 412 ms: 1.17x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                  |
| scimark_fft                | 382 ms                                                 | 330 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                  |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| go                         | 139 ms                                                 | 123 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                 |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                 |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.5 ms: 1.11x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 97.1 ms: 1.10x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.29 ms: 1.10x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 56.3 ms: 1.10x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                                 |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                  |
| chaos                      | 67.0 ms                                                | 62.1 ms: 1.08x faster                                                 |
| regex_dna                  | 212 ms                                                 | 197 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| logging_format             | 7.23 us                                                | 6.78 us: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.11 us: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                |
| nbody                      | 97.0 ms                                                | 93.1 ms: 1.04x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                                 |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                  |
| generators                 | 31.2 ms                                                | 30.6 ms: 1.02x faster                                                 |
| fannkuch                   | 417 ms                                                 | 409 ms: 1.02x faster                                                  |
| nqueens                    | 83.3 ms                                                | 82.7 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.94 ms: 1.00x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.45 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 7.72 ms: 1.09x slower                                                 |
| coroutines                 | 23.2 ms                                                | 25.6 ms: 1.11x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.0 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.08 ms: 1.34x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                 |
| logging_silent             | 104 ns                                                 | 472 ns: 4.52x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.60x faster                                                          |

Benchmark hidden because not significant (5): json, pickle_pure_python, regex_v8, asyncio_websockets, scimark_lu
Ignored benchmarks (23) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.652x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.14x