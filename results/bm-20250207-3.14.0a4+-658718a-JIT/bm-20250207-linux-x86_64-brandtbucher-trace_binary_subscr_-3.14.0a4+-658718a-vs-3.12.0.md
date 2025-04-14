# Results vs. 3.12.0

- fork: brandtbucher
- ref: trace_binary_subscr_
- machine: linux-x86_64
- commit hash: 658718a
- commit date: 2025-02-07
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                         |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                        |
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_dna      | 212 ms                                                 | 199 ms: 1.07x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.5 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.5 ms: 1.12x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                        |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 625 ms: 1.89x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 624 ms: 1.85x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 327 ms: 1.77x faster                                                         |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 258 ms: 1.74x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 491 ms: 1.48x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                         |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.6 us: 1.24x faster                                                        |
| spectral_norm              | 115 ms                                                 | 93.4 ms: 1.23x faster                                                        |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                         |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                        |
| float                      | 84.7 ms                                                | 71.0 ms: 1.19x faster                                                        |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.47 us: 1.18x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 69.8 ms: 1.17x faster                                                        |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                        |
| go                         | 139 ms                                                 | 120 ms: 1.16x faster                                                         |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                                         |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                        |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.5 ms: 1.13x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.31 ms: 1.12x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.5 ms: 1.12x faster                                                        |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 95.5 ms: 1.12x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                                        |
| pyflate                    | 482 ms                                                 | 439 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                        |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                         |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| regex_dna                  | 212 ms                                                 | 199 ms: 1.07x faster                                                         |
| fannkuch                   | 417 ms                                                 | 392 ms: 1.06x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.2 ms: 1.06x faster                                                        |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.0 ms: 1.04x faster                                                        |
| richards                   | 45.8 ms                                                | 44.2 ms: 1.04x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 750 ms: 1.03x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.02x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                       |
| richards_super             | 51.5 ms                                                | 50.4 ms: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                       |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                        |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 54.1 ms: 1.01x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                         |
| sympy_expand               | 478 ms                                                 | 473 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.02x slower                                                       |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.66 ms: 1.04x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                                         |
| logging_silent             | 104 ns                                                 | 111 ns: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.68 ms: 1.08x slower                                                        |
| nqueens                    | 83.3 ms                                                | 91.1 ms: 1.09x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.8 ms: 1.14x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.0 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.77 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (2): nbody, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250207-3.14.0a4+-658718a-JIT/bm-20250207-linux-x86_64-brandtbucher-trace_binary_subscr_-3.14.0a4+-658718a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x