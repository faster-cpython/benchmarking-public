# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 32ebfed
- commit date: 2025-03-19
- overall geometric mean: 1.117x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                      |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                      |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.2 ms: 1.30x faster                                                     |
| nbody          | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                     |
| regex_dna      | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                      |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                     |
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.87x faster                                                      |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 319 ms: 1.81x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 496 ms: 1.46x faster                                                      |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                     |
| richards                   | 45.8 ms                                                | 34.9 ms: 1.31x faster                                                     |
| float                      | 84.7 ms                                                | 65.2 ms: 1.30x faster                                                     |
| richards_super             | 51.5 ms                                                | 40.3 ms: 1.28x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                    |
| deltablue                  | 3.72 ms                                                | 3.01 ms: 1.24x faster                                                     |
| scimark_fft                | 382 ms                                                 | 311 ms: 1.23x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                     |
| spectral_norm              | 115 ms                                                 | 95.8 ms: 1.20x faster                                                     |
| logging_format             | 7.23 us                                                | 6.16 us: 1.17x faster                                                     |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                     |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                      |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                     |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                      |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 60.9 ms: 1.12x faster                                                     |
| generators                 | 31.2 ms                                                | 27.8 ms: 1.12x faster                                                     |
| nbody                      | 97.0 ms                                                | 86.9 ms: 1.12x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 67.6 ms: 1.11x faster                                                     |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                     |
| scimark_sor                | 129 ms                                                 | 117 ms: 1.10x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.10x faster                                                      |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                                      |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.10x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                                     |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                     |
| pyflate                    | 482 ms                                                 | 444 ms: 1.09x faster                                                      |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                      |
| logging_silent             | 104 ns                                                 | 98.1 ns: 1.06x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.69 us: 1.05x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 78.2 ms: 1.05x faster                                                     |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.45 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                                     |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                    |
| pprint_safe_repr           | 776 ms                                                 | 767 ms: 1.01x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| nqueens                    | 83.3 ms                                                | 84.1 ms: 1.01x slower                                                     |
| fannkuch                   | 417 ms                                                 | 424 ms: 1.02x slower                                                      |
| coroutines                 | 23.2 ms                                                | 23.8 ms: 1.03x slower                                                     |
| regex_dna                  | 212 ms                                                 | 221 ms: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.79 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.92 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.8 ms: 1.17x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.83 ms: 1.27x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.50 ms: 1.69x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (6): pycparser, pprint_pformat, asyncio_websockets, regex_v8, scimark_lu, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-32ebfed-JIT/bm-20250319-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-32ebfed.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x