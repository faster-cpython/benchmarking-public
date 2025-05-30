# Results vs. 3.12.0

- fork: brandtbucher
- ref: call_self_or_null
- machine: linux-x86_64
- commit hash: 39daf97
- commit date: 2025-04-15
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 248 ms: 1.11x faster                                                      |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                     |
| nbody          | 97.0 ms                                                | 88.7 ms: 1.09x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                     |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                     |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 57.4 ms: 1.07x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 316 us: 1.03x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                                      |
| json_loads           | 28.5 us                                                | 30.0 us: 1.05x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                     |
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.19 sec: 2.20x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.92x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 619 ms: 1.87x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 319 ms: 1.80x faster                                                      |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                      |
| deepcopy                   | 371 us                                                 | 242 us: 1.53x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 483 ms: 1.50x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.4 us: 1.43x faster                                                     |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.60 us: 1.29x faster                                                     |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                    |
| spectral_norm              | 115 ms                                                 | 95.5 ms: 1.20x faster                                                     |
| async_generators           | 463 ms                                                 | 389 ms: 1.19x faster                                                      |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                      |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 64.5 ms: 1.17x faster                                                     |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.16x faster                                                      |
| float                      | 84.7 ms                                                | 72.9 ms: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 59.1 ms: 1.16x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                      |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 71.6 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.7 ms: 1.14x faster                                                     |
| sympy_str                  | 300 ms                                                 | 263 ms: 1.14x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                      |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.12x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.24 ms: 1.11x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.35 ms: 1.11x faster                                                     |
| raytrace                   | 312 ms                                                 | 282 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.57 ms: 1.11x faster                                                     |
| 2to3                       | 274 ms                                                 | 248 ms: 1.11x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.4 ms: 1.11x faster                                                     |
| logging_silent             | 104 ns                                                 | 95.2 ns: 1.10x faster                                                     |
| django_template            | 34.6 ms                                                | 31.5 ms: 1.10x faster                                                     |
| richards                   | 45.8 ms                                                | 41.9 ms: 1.10x faster                                                     |
| nbody                      | 97.0 ms                                                | 88.7 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 98.1 ms: 1.09x faster                                                     |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 82.6 ms: 1.08x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                    |
| richards_super             | 51.5 ms                                                | 47.9 ms: 1.08x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 722 ms: 1.07x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 57.4 ms: 1.07x faster                                                     |
| sympy_expand               | 478 ms                                                 | 445 ms: 1.07x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                                    |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| hexiom                     | 6.41 ms                                                | 6.06 ms: 1.06x faster                                                     |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                     |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                                     |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 316 us: 1.03x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                                      |
| coroutines                 | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                     |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                      |
| json                       | 5.26 ms                                                | 5.47 ms: 1.04x slower                                                     |
| json_loads                 | 28.5 us                                                | 30.0 us: 1.05x slower                                                     |
| telco                      | 7.10 ms                                                | 7.55 ms: 1.06x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                     |
| coverage                   | 72.7 ms                                                | 83.3 ms: 1.15x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.16 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.66x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.12x faster                                                              |

Benchmark hidden because not significant (2): typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-39daf97/bm-20250415-linux-x86_64-brandtbucher-call_self_or_null-3.14.0a7+-39daf97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x