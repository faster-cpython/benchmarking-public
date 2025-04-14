# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: aa6e11c
- commit date: 2025-02-06
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.9 ms: 1.27x faster                                                        |
| nbody          | 97.0 ms                                                | 94.6 ms: 1.03x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                        |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.79 sec: 1.30x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.2 ms: 1.12x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                        |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 620 ms: 1.86x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 325 ms: 1.78x faster                                                         |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| deepcopy                   | 371 us                                                 | 265 us: 1.40x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.79 sec: 1.30x faster                                                       |
| float                      | 84.7 ms                                                | 66.9 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                                        |
| spectral_norm              | 115 ms                                                 | 95.4 ms: 1.20x faster                                                        |
| mako                       | 11.9 ms                                                | 10.0 ms: 1.19x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 63.5 ms: 1.18x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                         |
| logging_format             | 7.23 us                                                | 6.21 us: 1.16x faster                                                        |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 77.5 ms: 1.15x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 71.3 ms: 1.15x faster                                                        |
| async_generators           | 463 ms                                                 | 408 ms: 1.13x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                                        |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.13x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                        |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 95.2 ms: 1.12x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.54 ms: 1.11x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                        |
| richards                   | 45.8 ms                                                | 41.2 ms: 1.11x faster                                                        |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                         |
| pyflate                    | 482 ms                                                 | 438 ms: 1.10x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                         |
| richards_super             | 51.5 ms                                                | 47.2 ms: 1.09x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                        |
| fannkuch                   | 417 ms                                                 | 382 ms: 1.09x faster                                                         |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                        |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                        |
| sympy_str                  | 300 ms                                                 | 280 ms: 1.07x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.49 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 737 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                       |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                        |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 66.7 ms: 1.03x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                        |
| nbody                      | 97.0 ms                                                | 94.6 ms: 1.03x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                        |
| sympy_expand               | 478 ms                                                 | 476 ms: 1.00x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| nqueens                    | 83.3 ms                                                | 87.1 ms: 1.05x slower                                                        |
| logging_silent             | 104 ns                                                 | 109 ns: 1.05x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 893 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.65 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.22 ms: 1.13x slower                                                        |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.17x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.22x slower                                                        |
| coverage                   | 72.7 ms                                                | 89.3 ms: 1.23x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.3 ms: 3.34x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (3): regex_dna, asyncio_websockets, meteor_contest
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250206-3.14.0a4+-aa6e11c-JIT/bm-20250206-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-aa6e11c.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x