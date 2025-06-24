# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_threshold_64
- machine: linux-x86_64
- commit hash: 539b80a
- commit date: 2025-06-23
- overall geometric mean: 1.122x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 635 ms: 1.86x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                    |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                    |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.6 ms: 1.29x faster                                                   |
| nbody          | 97.0 ms                                                | 90.9 ms: 1.07x faster                                                   |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                    |
| regex_effbot   | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                   |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                   |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 199 us: 1.16x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                    |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                                   |
| json_loads           | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                    |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                   |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.6 ms: 1.13x faster                                                   |
| django_template | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 604 ms: 1.91x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 635 ms: 1.86x faster                                                    |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                    |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                    |
| async_tree_none            | 472 ms                                                 | 263 ms: 1.79x faster                                                    |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                    |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 498 ms: 1.46x faster                                                    |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                    |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                   |
| float                      | 84.7 ms                                                | 65.6 ms: 1.29x faster                                                   |
| richards                   | 45.8 ms                                                | 36.9 ms: 1.24x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                   |
| richards_super             | 51.5 ms                                                | 42.0 ms: 1.23x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                   |
| scimark_fft                | 382 ms                                                 | 328 ms: 1.16x faster                                                    |
| unpickle_pure_python       | 230 us                                                 | 199 us: 1.16x faster                                                    |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                    |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                                    |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                    |
| go                         | 139 ms                                                 | 122 ms: 1.14x faster                                                    |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                    |
| mako                       | 11.9 ms                                                | 10.6 ms: 1.13x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 67.0 ms: 1.12x faster                                                   |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.11x faster                                                    |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 80.6 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.8 ms: 1.09x faster                                                   |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                                   |
| async_generators           | 463 ms                                                 | 429 ms: 1.08x faster                                                    |
| chaos                      | 67.0 ms                                                | 62.2 ms: 1.08x faster                                                   |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                                   |
| nbody                      | 97.0 ms                                                | 90.9 ms: 1.07x faster                                                   |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.06x faster                                                   |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                                    |
| regex_effbot               | 3.61 ms                                                | 3.43 ms: 1.05x faster                                                   |
| logging_simple             | 6.46 us                                                | 6.18 us: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                    |
| logging_format             | 7.23 us                                                | 6.94 us: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                   |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                  |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.03x faster                                                   |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                   |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                   |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                    |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                 | 270 ms: 1.01x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                    |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                    |
| nqueens                    | 83.3 ms                                                | 82.9 ms: 1.00x faster                                                   |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                   |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                    |
| hexiom                     | 6.41 ms                                                | 6.53 ms: 1.02x slower                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                    |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                                   |
| pprint_safe_repr           | 776 ms                                                 | 816 ms: 1.05x slower                                                    |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                    |
| telco                      | 7.10 ms                                                | 7.74 ms: 1.09x slower                                                   |
| coroutines                 | 23.2 ms                                                | 25.6 ms: 1.11x slower                                                   |
| coverage                   | 72.7 ms                                                | 88.4 ms: 1.22x slower                                                   |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                   |
| gc_traversal               | 3.79 ms                                                | 4.97 ms: 1.31x slower                                                   |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.77x slower                                                   |
| logging_silent             | 104 ns                                                 | 477 ns: 4.57x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-539b80a-JIT/bm-20250623-linux-x86_64-brandtbucher-jit_threshold_64-3.15.0a0-539b80a.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.122x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.18x