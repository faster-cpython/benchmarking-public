# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_cached_consts
- machine: linux-x86_64
- commit hash: 6510018
- commit date: 2025-03-17
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 609 ms: 1.90x faster                                                      |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                     |
| nbody          | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                     |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                     |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                    |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                      |
| xml_etree_generate   | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.6 ms: 1.09x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.08x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                      |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 609 ms: 1.90x faster                                                      |
| async_tree_none            | 472 ms                                                 | 255 ms: 1.85x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 314 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 475 ms: 1.53x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                      |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                     |
| richards                   | 45.8 ms                                                | 34.6 ms: 1.32x faster                                                     |
| float                      | 84.7 ms                                                | 64.8 ms: 1.31x faster                                                     |
| richards_super             | 51.5 ms                                                | 39.7 ms: 1.30x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.26x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                    |
| deltablue                  | 3.72 ms                                                | 2.97 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                      |
| spectral_norm              | 115 ms                                                 | 94.3 ms: 1.22x faster                                                     |
| logging_format             | 7.23 us                                                | 6.05 us: 1.19x faster                                                     |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.48 us: 1.18x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                     |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| comprehensions             | 21.8 us                                                | 18.8 us: 1.16x faster                                                     |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 60.0 ms: 1.14x faster                                                     |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.14x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 66.9 ms: 1.12x faster                                                     |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                      |
| async_generators           | 463 ms                                                 | 415 ms: 1.11x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 55.5 ms: 1.11x faster                                                     |
| scimark_sor                | 129 ms                                                 | 116 ms: 1.11x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.11x faster                                                     |
| nbody                      | 97.0 ms                                                | 88.5 ms: 1.10x faster                                                     |
| django_template            | 34.6 ms                                                | 31.6 ms: 1.09x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 97.6 ms: 1.09x faster                                                     |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                      |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.08x faster                                                      |
| logging_silent             | 104 ns                                                 | 96.7 ns: 1.08x faster                                                     |
| pyflate                    | 482 ms                                                 | 449 ms: 1.07x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                     |
| mdp                        | 2.63 sec                                               | 2.46 sec: 1.07x faster                                                    |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                     |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                     |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                      |
| sqlite_synth               | 2.83 us                                                | 2.70 us: 1.05x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 78.1 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 776 ms                                                 | 745 ms: 1.04x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.47 ms: 1.04x faster                                                     |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                    |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                      |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                      |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                      |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                     |
| nqueens                    | 83.3 ms                                                | 84.4 ms: 1.01x slower                                                     |
| fannkuch                   | 417 ms                                                 | 430 ms: 1.03x slower                                                      |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                     |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 874 us: 1.04x slower                                                      |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                                     |
| hexiom                     | 6.41 ms                                                | 6.77 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                      |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                     |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.20 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.91 ms: 1.29x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 82.9 ms: 3.45x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (4): pycparser, pprint_pformat, asyncio_websockets, regex_v8
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250317-3.14.0a6+-6510018-JIT/bm-20250317-linux-x86_64-brandtbucher-jit_cached_consts-3.14.0a6+-6510018.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x