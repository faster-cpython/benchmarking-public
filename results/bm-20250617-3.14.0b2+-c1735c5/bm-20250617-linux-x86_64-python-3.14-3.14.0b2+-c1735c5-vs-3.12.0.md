# Results vs. 3.12.0

- fork: python
- ref: 3.14
- machine: linux-x86_64
- commit hash: c1735c5
- commit date: 2025-06-17
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                   |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                 |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 592 ms: 1.95x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.94x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                   |
| Geometric mean             | (ref)                                                  | 1.77x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                   |
| nbody          | 97.0 ms                                                | 100 ms: 1.03x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                   |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.13x faster                                  |
| regex_dna      | 212 ms                                                 | 207 ms: 1.02x faster                                   |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                 |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 107 ms                                                 | 99.0 ms: 1.08x faster                                  |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                   |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                  |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                  |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.02x faster                                   |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                  |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                  |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.13x faster                                 |
| async_tree_io              | 1.16 sec                                               | 592 ms: 1.95x faster                                   |
| async_tree_io_tg           | 1.18 sec                                               | 608 ms: 1.94x faster                                   |
| async_tree_memoization     | 578 ms                                                 | 308 ms: 1.88x faster                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 310 ms: 1.85x faster                                   |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.84x faster                                   |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                   |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                   |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                  |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                  |
| go                         | 139 ms                                                 | 112 ms: 1.24x faster                                   |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                  |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                   |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                 |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                   |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                  |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                   |
| async_generators           | 463 ms                                                 | 408 ms: 1.14x faster                                   |
| pyflate                    | 482 ms                                                 | 426 ms: 1.13x faster                                   |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                  |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.13x faster                                  |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                   |
| pathlib                    | 19.3 ms                                                | 17.3 ms: 1.12x faster                                  |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                  |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                  |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 134 ms: 1.10x faster                                   |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.0 ms: 1.08x faster                                  |
| richards                   | 45.8 ms                                                | 42.6 ms: 1.08x faster                                  |
| logging_format             | 7.23 us                                                | 6.77 us: 1.07x faster                                  |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                   |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.6 ms: 1.06x faster                                  |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                   |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                  |
| logging_simple             | 6.46 us                                                | 6.13 us: 1.05x faster                                  |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                   |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                   |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                  |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                   |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                  |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                   |
| pprint_pformat             | 1.57 sec                                               | 1.52 sec: 1.03x faster                                 |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                  |
| nqueens                    | 83.3 ms                                                | 81.0 ms: 1.03x faster                                  |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                  |
| regex_dna                  | 212 ms                                                 | 207 ms: 1.02x faster                                   |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.02x faster                                   |
| scimark_fft                | 382 ms                                                 | 373 ms: 1.02x faster                                   |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                 |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                   |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.02 ms: 1.01x faster                                  |
| fannkuch                   | 417 ms                                                 | 416 ms: 1.00x faster                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                   |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                  |
| generators                 | 31.2 ms                                                | 31.4 ms: 1.01x slower                                  |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                  |
| nbody                      | 97.0 ms                                                | 100 ms: 1.03x slower                                   |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                  |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                   |
| coroutines                 | 23.2 ms                                                | 24.8 ms: 1.07x slower                                  |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                  |
| coverage                   | 72.7 ms                                                | 87.1 ms: 1.20x slower                                  |
| gc_traversal               | 3.79 ms                                                | 4.74 ms: 1.25x slower                                  |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.58 ms: 1.74x slower                                  |
| logging_silent             | 104 ns                                                 | 471 ns: 4.51x slower                                   |
| Geometric mean             | (ref)                                                  | 1.09x faster                                           |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (20) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250617-3.14.0b2+-c1735c5/bm-20250617-linux-x86_64-python-3.14-3.14.0b2+-c1735c5.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x