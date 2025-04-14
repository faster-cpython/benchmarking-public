# Results vs. 3.12.0

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: dda3d1f
- commit date: 2025-02-06
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                       |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.20x faster                                                      |
| nbody          | 97.0 ms                                                | 91.2 ms: 1.06x faster                                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                      |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                       |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.19x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                       |
| json_loads           | 28.5 us                                                | 29.3 us: 1.03x slower                                                      |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                      |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                       |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 322 ms: 1.79x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                       |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                                      |
| spectral_norm              | 115 ms                                                 | 94.5 ms: 1.22x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.21x faster                                                      |
| float                      | 84.7 ms                                                | 70.3 ms: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                      |
| async_generators           | 463 ms                                                 | 390 ms: 1.19x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.19x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                      |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                       |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                       |
| crypto_pyaes               | 81.9 ms                                                | 69.9 ms: 1.17x faster                                                      |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.15x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                       |
| chaos                      | 67.0 ms                                                | 58.3 ms: 1.15x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                       |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                       |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                                      |
| scimark_fft                | 382 ms                                                 | 341 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.53 ms: 1.12x faster                                                      |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 709 ms: 1.09x faster                                                       |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.32 ms: 1.09x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.25 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                     |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                     |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                       |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                       |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                      |
| sqlglot_normalize          | 110 ms                                                 | 103 ms: 1.07x faster                                                       |
| sympy_expand               | 478 ms                                                 | 448 ms: 1.07x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 83.7 ms: 1.06x faster                                                      |
| nbody                      | 97.0 ms                                                | 91.2 ms: 1.06x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 51.8 ms: 1.06x faster                                                      |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                       |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.16 ms: 1.04x faster                                                      |
| nqueens                    | 83.3 ms                                                | 80.1 ms: 1.04x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                       |
| richards                   | 45.8 ms                                                | 44.9 ms: 1.02x faster                                                      |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                      |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                     |
| richards_super             | 51.5 ms                                                | 50.7 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 158 us                                                 | 156 us: 1.01x faster                                                       |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                       |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.00 ms: 1.01x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 861 us: 1.02x slower                                                       |
| json_loads                 | 28.5 us                                                | 29.3 us: 1.03x slower                                                      |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.13x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.60 ms: 1.21x slower                                                      |
| coverage                   | 72.7 ms                                                | 92.7 ms: 1.27x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250206-3.14.0a4+-dda3d1f/bm-20250206-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-dda3d1f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.09x