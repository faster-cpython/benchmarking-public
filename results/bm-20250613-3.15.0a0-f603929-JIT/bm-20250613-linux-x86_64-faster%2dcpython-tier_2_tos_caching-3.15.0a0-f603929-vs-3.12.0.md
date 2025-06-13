# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                          |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.9 ms: 1.28x faster                                                         |
| nbody          | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                         |
| regex_dna      | 212 ms                                                 | 196 ms: 1.08x faster                                                          |
| regex_v8       | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 203 us: 1.13x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 56.4 ms: 1.10x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 99.4 ms: 1.07x faster                                                         |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                         |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                         |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                         |
| django_template | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 603 ms: 1.92x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 315 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                          |
| deepcopy                   | 371 us                                                 | 258 us: 1.44x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                         |
| richards                   | 45.8 ms                                                | 35.0 ms: 1.31x faster                                                         |
| richards_super             | 51.5 ms                                                | 40.0 ms: 1.29x faster                                                         |
| float                      | 84.7 ms                                                | 65.9 ms: 1.28x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.24x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.91 sec: 1.22x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.77 us: 1.21x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                         |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                          |
| scimark_fft                | 382 ms                                                 | 336 ms: 1.14x faster                                                          |
| pyflate                    | 482 ms                                                 | 425 ms: 1.13x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 203 us: 1.13x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                          |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.2 ms: 1.12x faster                                                         |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 61.4 ms: 1.12x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                         |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                                          |
| nbody                      | 97.0 ms                                                | 88.2 ms: 1.10x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 56.4 ms: 1.10x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 81.9 ms: 1.09x faster                                                         |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                         |
| regex_dna                  | 212 ms                                                 | 196 ms: 1.08x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.4 ms: 1.07x faster                                                         |
| chaos                      | 67.0 ms                                                | 62.6 ms: 1.07x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 76.5 ms: 1.07x faster                                                         |
| async_generators           | 463 ms                                                 | 434 ms: 1.07x faster                                                          |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                          |
| django_template            | 34.6 ms                                                | 32.7 ms: 1.06x faster                                                         |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                          |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                          |
| logging_format             | 7.23 us                                                | 6.88 us: 1.05x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                        |
| logging_simple             | 6.46 us                                                | 6.18 us: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                          |
| generators                 | 31.2 ms                                                | 30.2 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.18 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.79 us: 1.01x faster                                                         |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 6.93 ms: 1.00x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                          |
| nqueens                    | 83.3 ms                                                | 84.2 ms: 1.01x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.4 ms: 1.01x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.52 ms: 1.02x slower                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.23 ms: 1.03x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                          |
| pprint_safe_repr           | 776 ms                                                 | 850 ms: 1.10x slower                                                          |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                         |
| coroutines                 | 23.2 ms                                                | 25.9 ms: 1.12x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.78 sec: 1.14x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                         |
| logging_silent             | 104 ns                                                 | 480 ns: 4.59x slower                                                          |
| coverage                   | 72.7 ms                                                | 424 ms: 5.84x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (4): scimark_lu, asyncio_websockets, pickle_pure_python, fannkuch
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.095x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.16x