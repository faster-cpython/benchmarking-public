# Results vs. 3.12.0

- fork: brandtbucher
- ref: negative_subscr
- machine: linux-x86_64
- commit hash: 6a93886
- commit date: 2025-04-03
- overall geometric mean: 1.135x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                    |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                    |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 62.0 ms: 1.37x faster                                                   |
| nbody          | 97.0 ms                                                | 89.7 ms: 1.08x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                   |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                    |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 206 us: 1.12x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.10x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.0 ms: 1.09x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                    |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                   |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                   |
| django_template | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.17x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                    |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                    |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                    |
| deepcopy                   | 371 us                                                 | 252 us: 1.47x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.0 us: 1.40x faster                                                   |
| float                      | 84.7 ms                                                | 62.0 ms: 1.37x faster                                                   |
| richards                   | 45.8 ms                                                | 34.7 ms: 1.32x faster                                                   |
| richards_super             | 51.5 ms                                                | 39.8 ms: 1.30x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.62 us: 1.28x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                  |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                                   |
| comprehensions             | 21.8 us                                                | 18.2 us: 1.20x faster                                                   |
| spectral_norm              | 115 ms                                                 | 96.9 ms: 1.19x faster                                                   |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                    |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                    |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.56 us: 1.16x faster                                                   |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                   |
| pyflate                    | 482 ms                                                 | 416 ms: 1.16x faster                                                    |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                    |
| scimark_monte_carlo        | 75.1 ms                                                | 65.8 ms: 1.14x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 60.5 ms: 1.13x faster                                                   |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                    |
| go                         | 139 ms                                                 | 124 ms: 1.13x faster                                                    |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 206 us: 1.12x faster                                                    |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.11x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                    |
| logging_silent             | 104 ns                                                 | 94.9 ns: 1.10x faster                                                   |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.10x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 75.0 ms: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                 | 98.0 ms: 1.09x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                   |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                   |
| nbody                      | 97.0 ms                                                | 89.7 ms: 1.08x faster                                                   |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.70 ms: 1.08x faster                                                   |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.08x faster                                                   |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.05x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                                  |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                    |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                   |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.03x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                    |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 761 ms: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                    |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                    |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                    |
| json                       | 5.26 ms                                                | 5.30 ms: 1.01x slower                                                   |
| coroutines                 | 23.2 ms                                                | 23.7 ms: 1.02x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.76 ms: 1.05x slower                                                   |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                    |
| telco                      | 7.10 ms                                                | 7.82 ms: 1.10x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.89 ms: 1.29x slower                                                   |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.70x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                            |

Benchmark hidden because not significant (2): pprint_pformat, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250403-3.14.0a6+-6a93886-JIT/bm-20250403-linux-x86_64-brandtbucher-negative_subscr-3.14.0a6+-6a93886.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.12x