# Results vs. 3.12.0

- fork: brandtbucher
- ref: faster_pprint
- machine: linux-x86_64
- commit hash: ccfdf31
- commit date: 2025-06-17
- overall geometric mean: 1.112x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                 |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.9 ms: 1.15x faster                                                |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                 |
| nbody          | 97.0 ms                                                | 99.9 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                |
| regex_dna      | 212 ms                                                 | 201 ms: 1.06x faster                                                 |
| regex_v8       | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.99 sec: 1.17x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.03x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                |
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                               |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 633 ms: 1.87x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 497 ms: 1.46x faster                                                 |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                |
| go                         | 139 ms                                                 | 114 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.99 sec: 1.17x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                                |
| float                      | 84.7 ms                                                | 73.9 ms: 1.15x faster                                                |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                 |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.12x faster                                                 |
| async_generators           | 463 ms                                                 | 415 ms: 1.11x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                |
| pyflate                    | 482 ms                                                 | 440 ms: 1.10x faster                                                 |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                |
| chaos                      | 67.0 ms                                                | 61.9 ms: 1.08x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                                |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                               |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.03 ms: 1.06x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                 |
| logging_format             | 7.23 us                                                | 6.83 us: 1.06x faster                                                |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                |
| regex_dna                  | 212 ms                                                 | 201 ms: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.0 ms: 1.05x faster                                                |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                |
| logging_simple             | 6.46 us                                                | 6.16 us: 1.05x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.58 ms: 1.04x faster                                                |
| generators                 | 31.2 ms                                                | 30.1 ms: 1.04x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.03x faster                                                 |
| richards_super             | 51.5 ms                                                | 50.1 ms: 1.03x faster                                                |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                                |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.01x faster                                                |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                |
| fannkuch                   | 417 ms                                                 | 415 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                |
| sqlite_synth               | 2.83 us                                                | 2.90 us: 1.02x slower                                                |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                 |
| nbody                      | 97.0 ms                                                | 99.9 ms: 1.03x slower                                                |
| scimark_lu                 | 118 ms                                                 | 122 ms: 1.03x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                |
| coroutines                 | 23.2 ms                                                | 25.9 ms: 1.12x slower                                                |
| telco                      | 7.10 ms                                                | 7.96 ms: 1.12x slower                                                |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.75x slower                                                |
| logging_silent             | 104 ns                                                 | 474 ns: 4.54x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (2): pickle_pure_python, json_loads
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250617-3.15.0a0-ccfdf31/bm-20250617-linux-x86_64-brandtbucher-faster_pprint-3.15.0a0-ccfdf31.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.112x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x