# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 4953e8a
- commit date: 2025-03-28
- overall geometric mean: 1.121x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                      |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                     |
| nbody          | 97.0 ms                                                | 88.7 ms: 1.09x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                     |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.12x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                      |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                      |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                      |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                     |
| richards                   | 45.8 ms                                                | 34.9 ms: 1.31x faster                                                     |
| float                      | 84.7 ms                                                | 64.6 ms: 1.31x faster                                                     |
| richards_super             | 51.5 ms                                                | 39.7 ms: 1.30x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                    |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                     |
| deltablue                  | 3.72 ms                                                | 2.99 ms: 1.24x faster                                                     |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.23x faster                                                      |
| spectral_norm              | 115 ms                                                 | 93.9 ms: 1.22x faster                                                     |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                      |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                      |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                     |
| logging_simple             | 6.46 us                                                | 5.62 us: 1.15x faster                                                     |
| comprehensions             | 21.8 us                                                | 19.0 us: 1.15x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.16 ms: 1.14x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 60.4 ms: 1.14x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.12x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.12x faster                                                     |
| pyflate                    | 482 ms                                                 | 433 ms: 1.11x faster                                                      |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                     |
| async_generators           | 463 ms                                                 | 419 ms: 1.10x faster                                                      |
| go                         | 139 ms                                                 | 126 ms: 1.10x faster                                                      |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                     |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| nbody                      | 97.0 ms                                                | 88.7 ms: 1.09x faster                                                     |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                     |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                      |
| logging_silent             | 104 ns                                                 | 97.4 ns: 1.07x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                    |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.69 us: 1.05x faster                                                     |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                    |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 78.7 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 758 ms: 1.02x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                    |
| sympy_expand               | 478 ms                                                 | 470 ms: 1.02x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 84.4 ms: 1.01x slower                                                     |
| fannkuch                   | 417 ms                                                 | 423 ms: 1.01x slower                                                      |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                     |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 879 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                      |
| telco                      | 7.10 ms                                                | 7.85 ms: 1.11x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (6): pickle_pure_python, regex_v8, json, asyncio_websockets, coroutines, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250328-3.14.0a6+-4953e8a-JIT/bm-20250328-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-4953e8a.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.121x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x