# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: bb15287
- commit date: 2025-01-29
- overall geometric mean: 1.120x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.5 ms: 1.27x faster                                                        |
| nbody          | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                        |
| regex_dna      | 212 ms                                                 | 213 ms: 1.01x slower                                                         |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.79 sec: 1.30x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 188 us: 1.22x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 94.9 ms: 1.12x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                         |
| json_loads           | 28.5 us                                                | 28.8 us: 1.01x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                        |
| django_template | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 628 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 329 ms: 1.75x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| deepcopy                   | 371 us                                                 | 266 us: 1.39x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.37x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.32x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.79 sec: 1.30x faster                                                       |
| float                      | 84.7 ms                                                | 66.5 ms: 1.27x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 188 us: 1.22x faster                                                         |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                        |
| spectral_norm              | 115 ms                                                 | 94.4 ms: 1.22x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.0 ms: 1.21x faster                                                        |
| mako                       | 11.9 ms                                                | 9.95 ms: 1.20x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 69.1 ms: 1.18x faster                                                        |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                         |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                        |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                         |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                         |
| richards                   | 45.8 ms                                                | 40.0 ms: 1.15x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 78.0 ms: 1.14x faster                                                        |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                         |
| scimark_sor                | 129 ms                                                 | 114 ms: 1.14x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.47 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 94.9 ms: 1.12x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 54.9 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                        |
| nbody                      | 97.0 ms                                                | 86.7 ms: 1.12x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                        |
| richards_super             | 51.5 ms                                                | 46.3 ms: 1.11x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 707 ms: 1.10x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                         |
| fannkuch                   | 417 ms                                                 | 382 ms: 1.09x faster                                                         |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                         |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.09x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                        |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                        |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.69 us: 1.05x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                        |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                         |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                         |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                                        |
| json                       | 5.26 ms                                                | 5.18 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| regex_dna                  | 212 ms                                                 | 213 ms: 1.01x slower                                                         |
| json_loads                 | 28.5 us                                                | 28.8 us: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.11 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.02x slower                                                         |
| logging_silent             | 104 ns                                                 | 107 ns: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                | 24.0 ms: 1.03x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                         |
| nqueens                    | 83.3 ms                                                | 89.2 ms: 1.07x slower                                                        |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| generators                 | 31.2 ms                                                | 36.5 ms: 1.17x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.8 ms: 1.25x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.88 ms: 1.29x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250129-3.14.0a4+-bb15287-JIT/bm-20250129-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-bb15287.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.120x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x