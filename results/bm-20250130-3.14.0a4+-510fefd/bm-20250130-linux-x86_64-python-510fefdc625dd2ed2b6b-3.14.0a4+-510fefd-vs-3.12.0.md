# Results vs. 3.12.0

- fork: python
- ref: 510fefdc625dd2ed2b6b
- machine: linux-x86_64
- commit hash: 510fefd
- commit date: 2025-01-30
- overall geometric mean: 1.119x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                   |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.96x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                  |
| nbody          | 97.0 ms                                                | 91.6 ms: 1.06x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.18x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.3 ms: 1.09x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                   |
| xml_etree_process    | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 605 ms: 1.96x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.80x faster                                                   |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 257 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 30.2 us: 1.35x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.3 us: 1.34x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                  |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 70.1 ms: 1.21x faster                                                  |
| async_generators           | 463 ms                                                 | 385 ms: 1.20x faster                                                   |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                                   |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.96 sec: 1.19x faster                                                 |
| regex_compile              | 148 ms                                                 | 125 ms: 1.18x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                  |
| spectral_norm              | 115 ms                                                 | 98.0 ms: 1.17x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 145 ms: 1.17x faster                                                   |
| raytrace                   | 312 ms                                                 | 270 ms: 1.16x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 70.8 ms: 1.16x faster                                                  |
| chaos                      | 67.0 ms                                                | 58.0 ms: 1.15x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.23 ms: 1.15x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.41 ms: 1.15x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                   |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                   |
| scimark_fft                | 382 ms                                                 | 337 ms: 1.13x faster                                                   |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                  |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                  |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 98.3 ms: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                   |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                   |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 83.6 ms: 1.07x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.47 sec: 1.07x faster                                                 |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                 |
| nbody                      | 97.0 ms                                                | 91.6 ms: 1.06x faster                                                  |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 51.9 ms: 1.06x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.13 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 59.2 ms: 1.04x faster                                                  |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                   |
| json                       | 5.26 ms                                                | 5.09 ms: 1.03x faster                                                  |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                  |
| richards                   | 45.8 ms                                                | 45.1 ms: 1.02x faster                                                  |
| nqueens                    | 83.3 ms                                                | 82.0 ms: 1.02x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 857 us: 1.02x slower                                                   |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.8 ms: 1.07x slower                                                  |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.21x slower                                                  |
| coverage                   | 72.7 ms                                                | 90.2 ms: 1.24x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.66x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (5): richards_super, regex_dna, typing_runtime_protocols, json_loads, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250130-3.14.0a4+-510fefd/bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x