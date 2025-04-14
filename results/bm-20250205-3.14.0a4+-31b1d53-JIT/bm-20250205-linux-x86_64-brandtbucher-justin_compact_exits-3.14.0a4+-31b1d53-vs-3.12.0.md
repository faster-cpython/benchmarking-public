# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 31b1d53
- commit date: 2025-02-05
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                        |
| nbody          | 97.0 ms                                                | 94.8 ms: 1.02x faster                                                        |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_compile  | 148 ms                                                 | 130 ms: 1.15x faster                                                         |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 194 us: 1.18x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 95.7 ms: 1.12x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                         |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 32.8 ms: 1.05x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 331 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 501 ms: 1.45x faster                                                         |
| deepcopy                   | 371 us                                                 | 269 us: 1.38x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                        |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.31x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.81 sec: 1.29x faster                                                       |
| float                      | 84.7 ms                                                | 67.6 ms: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                        |
| pathlib                    | 19.3 ms                                                | 15.9 ms: 1.22x faster                                                        |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 63.0 ms: 1.19x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 194 us: 1.18x faster                                                         |
| logging_format             | 7.23 us                                                | 6.12 us: 1.18x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| spectral_norm              | 115 ms                                                 | 98.0 ms: 1.17x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 70.0 ms: 1.17x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.12 ms: 1.16x faster                                                        |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                                        |
| regex_compile              | 148 ms                                                 | 130 ms: 1.15x faster                                                         |
| scimark_sor                | 129 ms                                                 | 113 ms: 1.14x faster                                                         |
| async_generators           | 463 ms                                                 | 406 ms: 1.14x faster                                                         |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.12x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                         |
| richards_super             | 51.5 ms                                                | 46.1 ms: 1.12x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 95.7 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.56 ms: 1.11x faster                                                        |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.40 ms: 1.09x faster                                                        |
| raytrace                   | 312 ms                                                 | 286 ms: 1.09x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 57.0 ms: 1.08x faster                                                        |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                        |
| fannkuch                   | 417 ms                                                 | 386 ms: 1.08x faster                                                         |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                        |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.06x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                       |
| django_template            | 34.6 ms                                                | 32.8 ms: 1.05x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                         |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 746 ms: 1.04x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| sqlglot_optimize           | 54.8 ms                                                | 53.1 ms: 1.03x faster                                                        |
| sqlglot_normalize          | 110 ms                                                 | 108 ms: 1.03x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                        |
| nbody                      | 97.0 ms                                                | 94.8 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                         |
| json                       | 5.26 ms                                                | 5.18 ms: 1.01x faster                                                        |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                         |
| meteor_contest             | 112 ms                                                 | 112 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                                         |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.02x slower                                                         |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                        |
| logging_silent             | 104 ns                                                 | 110 ns: 1.05x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                        |
| telco                      | 7.10 ms                                                | 7.49 ms: 1.06x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                                         |
| nqueens                    | 83.3 ms                                                | 90.7 ms: 1.09x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.28 ms: 1.14x slower                                                        |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                                        |
| coverage                   | 72.7 ms                                                | 89.8 ms: 1.24x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.5 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250205-3.14.0a4+-31b1d53-JIT/bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x