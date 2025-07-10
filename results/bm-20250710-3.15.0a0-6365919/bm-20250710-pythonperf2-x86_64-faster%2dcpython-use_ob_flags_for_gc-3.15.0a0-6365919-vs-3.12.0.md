# Results vs. 3.12.0

- fork: faster-cpython
- ref: use_ob_flags_for_gc
- machine: linux-x86_64
- commit hash: 6365919
- commit date: 2025-07-10
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 281 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 496 ms: 1.40x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                 |
| Geometric mean             | (ref)                                                        | 1.59x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.4 ms: 1.09x faster                                                                |
| pidigits       | 265 ms                                                       | 256 ms: 1.04x faster                                                                 |
| nbody          | 88.0 ms                                                      | 94.7 ms: 1.08x slower                                                                |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 131 ms: 1.10x faster                                                                 |
| regex_dna      | 239 ms                                                       | 225 ms: 1.06x faster                                                                 |
| regex_effbot   | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                                |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                               |
| xml_etree_iterparse  | 103 ms                                                       | 98.1 ms: 1.05x faster                                                                |
| xml_etree_parse      | 144 ms                                                       | 138 ms: 1.04x faster                                                                 |
| xml_etree_generate   | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                                |
| unpickle_pure_python | 210 us                                                       | 208 us: 1.01x faster                                                                 |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.02x slower                                                                |
| pickle_pure_python   | 318 us                                                       | 328 us: 1.03x slower                                                                 |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.77 ms: 1.02x slower                                                                |
| python_startup         | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                                |
| Geometric mean         | (ref)                                                        | 1.15x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 35.2 ms: 1.09x faster                                                                |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mdp                        | 2.57 sec                                                     | 1.28 sec: 2.00x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 614 ms: 1.70x faster                                                                 |
| async_tree_io_tg           | 1.05 sec                                                     | 627 ms: 1.68x faster                                                                 |
| async_tree_none            | 452 ms                                                       | 269 ms: 1.68x faster                                                                 |
| async_tree_memoization     | 544 ms                                                       | 325 ms: 1.67x faster                                                                 |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                                 |
| async_tree_none_tg         | 431 ms                                                       | 271 ms: 1.59x faster                                                                 |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 496 ms: 1.40x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 507 ms: 1.38x faster                                                                 |
| deepcopy                   | 368 us                                                       | 268 us: 1.37x faster                                                                 |
| deepcopy_memo              | 36.8 us                                                      | 27.1 us: 1.36x faster                                                                |
| comprehensions             | 21.9 us                                                      | 16.5 us: 1.33x faster                                                                |
| go                         | 150 ms                                                       | 118 ms: 1.26x faster                                                                 |
| generators                 | 37.4 ms                                                      | 30.0 ms: 1.25x faster                                                                |
| deepcopy_reduce            | 3.37 us                                                      | 2.93 us: 1.15x faster                                                                |
| scimark_monte_carlo        | 69.0 ms                                                      | 60.2 ms: 1.15x faster                                                                |
| logging_format             | 7.48 us                                                      | 6.63 us: 1.13x faster                                                                |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                                |
| logging_simple             | 6.71 us                                                      | 6.03 us: 1.11x faster                                                                |
| dulwich_log                | 65.4 ms                                                      | 59.2 ms: 1.10x faster                                                                |
| regex_compile              | 144 ms                                                       | 131 ms: 1.10x faster                                                                 |
| chaos                      | 64.0 ms                                                      | 58.2 ms: 1.10x faster                                                                |
| sympy_integrate            | 23.9 ms                                                      | 22.0 ms: 1.09x faster                                                                |
| float                      | 76.6 ms                                                      | 70.4 ms: 1.09x faster                                                                |
| django_template            | 38.2 ms                                                      | 35.2 ms: 1.09x faster                                                                |
| pprint_pformat             | 1.65 sec                                                     | 1.53 sec: 1.08x faster                                                               |
| pprint_safe_repr           | 807 ms                                                       | 748 ms: 1.08x faster                                                                 |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                                 |
| spectral_norm              | 91.6 ms                                                      | 85.2 ms: 1.08x faster                                                                |
| crypto_pyaes               | 80.3 ms                                                      | 74.9 ms: 1.07x faster                                                                |
| meteor_contest             | 128 ms                                                       | 120 ms: 1.07x faster                                                                 |
| pyflate                    | 439 ms                                                       | 409 ms: 1.07x faster                                                                 |
| tomli_loads                | 2.16 sec                                                     | 2.02 sec: 1.07x faster                                                               |
| scimark_sor                | 109 ms                                                       | 103 ms: 1.06x faster                                                                 |
| regex_dna                  | 239 ms                                                       | 225 ms: 1.06x faster                                                                 |
| raytrace                   | 298 ms                                                       | 282 ms: 1.06x faster                                                                 |
| sympy_str                  | 302 ms                                                       | 286 ms: 1.06x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                       | 98.1 ms: 1.05x faster                                                                |
| xml_etree_parse            | 144 ms                                                       | 138 ms: 1.04x faster                                                                 |
| scimark_lu                 | 98.8 ms                                                      | 95.3 ms: 1.04x faster                                                                |
| pidigits                   | 265 ms                                                       | 256 ms: 1.04x faster                                                                 |
| deltablue                  | 3.24 ms                                                      | 3.15 ms: 1.03x faster                                                                |
| xml_etree_generate         | 86.1 ms                                                      | 84.4 ms: 1.02x faster                                                                |
| regex_effbot               | 3.57 ms                                                      | 3.50 ms: 1.02x faster                                                                |
| hexiom                     | 5.96 ms                                                      | 5.87 ms: 1.02x faster                                                                |
| 2to3                       | 285 ms                                                       | 281 ms: 1.01x faster                                                                 |
| richards                   | 45.7 ms                                                      | 45.1 ms: 1.01x faster                                                                |
| logging_silent             | 94.4 ns                                                      | 93.1 ns: 1.01x faster                                                                |
| asyncio_websockets         | 387 ms                                                       | 383 ms: 1.01x faster                                                                 |
| unpickle_pure_python       | 210 us                                                       | 208 us: 1.01x faster                                                                 |
| coroutines                 | 23.0 ms                                                      | 22.9 ms: 1.01x faster                                                                |
| sympy_expand               | 484 ms                                                       | 487 ms: 1.01x slower                                                                 |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                               |
| python_startup_no_site     | 8.64 ms                                                      | 8.77 ms: 1.02x slower                                                                |
| scimark_fft                | 301 ms                                                       | 307 ms: 1.02x slower                                                                 |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.02x slower                                                                |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                                |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                                |
| pickle_pure_python         | 318 us                                                       | 328 us: 1.03x slower                                                                 |
| nqueens                    | 89.9 ms                                                      | 92.8 ms: 1.03x slower                                                                |
| fannkuch                   | 350 ms                                                       | 371 ms: 1.06x slower                                                                 |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                                |
| nbody                      | 88.0 ms                                                      | 94.7 ms: 1.08x slower                                                                |
| typing_runtime_protocols   | 152 us                                                       | 166 us: 1.10x slower                                                                 |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                                |
| async_generators           | 390 ms                                                       | 435 ms: 1.11x slower                                                                 |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.87 ms: 1.16x slower                                                                |
| coverage                   | 66.7 ms                                                      | 80.3 ms: 1.20x slower                                                                |
| python_startup             | 11.6 ms                                                      | 15.2 ms: 1.31x slower                                                                |
| gc_traversal               | 3.48 ms                                                      | 5.88 ms: 1.69x slower                                                                |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                                |
| telco                      | 6.96 ms                                                      | 158 ms: 22.65x slower                                                                |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                         |

Benchmark hidden because not significant (4): richards_super, xml_etree_process, docutils, regex_v8
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250710-3.15.0a0-6365919/bm-20250710-pythonperf2-x86_64-faster%2dcpython-use_ob_flags_for_gc-3.15.0a0-6365919.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.13x