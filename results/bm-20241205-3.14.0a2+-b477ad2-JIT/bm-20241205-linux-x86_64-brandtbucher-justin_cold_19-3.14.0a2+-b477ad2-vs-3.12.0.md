# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_19
- machine: linux-x86_64
- commit hash: b477ad2
- commit date: 2024-12-05
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                  |
| float          | 84.7 ms                                                | 75.8 ms: 1.12x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 195 us: 1.18x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 94.5 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                  |
| json_loads           | 28.5 us                                                | 26.0 us: 1.10x faster                                                  |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                  |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 626 ms: 1.89x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.79x faster                                                   |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 479 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                  |
| deepcopy                   | 371 us                                                 | 268 us: 1.39x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                                  |
| richards                   | 45.8 ms                                                | 36.6 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                 |
| richards_super             | 51.5 ms                                                | 43.1 ms: 1.20x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 68.5 ms: 1.19x faster                                                  |
| mako                       | 11.9 ms                                                | 9.98 ms: 1.19x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.19x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 195 us: 1.18x faster                                                   |
| scimark_fft                | 382 ms                                                 | 325 ms: 1.18x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.2 ms: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.20 ms: 1.16x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| logging_format             | 7.23 us                                                | 6.34 us: 1.14x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.14x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 94.5 ms: 1.13x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 54.7 ms: 1.13x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| logging_simple             | 6.46 us                                                | 5.73 us: 1.13x faster                                                  |
| nbody                      | 97.0 ms                                                | 86.0 ms: 1.13x faster                                                  |
| float                      | 84.7 ms                                                | 75.8 ms: 1.12x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| chaos                      | 67.0 ms                                                | 60.1 ms: 1.11x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.25 ms: 1.11x faster                                                  |
| json                       | 5.26 ms                                                | 4.74 ms: 1.11x faster                                                  |
| json_loads                 | 28.5 us                                                | 26.0 us: 1.10x faster                                                  |
| fannkuch                   | 417 ms                                                 | 381 ms: 1.09x faster                                                   |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                   |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                                 |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| sympy_str                  | 300 ms                                                 | 283 ms: 1.06x faster                                                   |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                                  |
| sqlglot_transpile          | 1.68 ms                                                | 1.63 ms: 1.03x faster                                                  |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                   |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                   |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 67.6 ms: 1.01x faster                                                  |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                   |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.6 ms: 1.01x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.02x slower                                                  |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| pycparser                  | 1.18 sec                                               | 1.20 sec: 1.02x slower                                                 |
| sympy_expand               | 478 ms                                                 | 490 ms: 1.02x slower                                                   |
| bench_thread_pool          | 842 us                                                 | 875 us: 1.04x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.74 sec: 1.04x slower                                                 |
| telco                      | 7.10 ms                                                | 7.51 ms: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                   |
| nqueens                    | 83.3 ms                                                | 90.3 ms: 1.08x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.04 ms: 1.10x slower                                                  |
| coverage                   | 72.7 ms                                                | 84.5 ms: 1.16x slower                                                  |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.74 ms: 1.25x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.44 ms: 1.65x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (6): scimark_sparse_mat_mult, sqlite_synth, pickle_pure_python, sqlglot_normalize, coroutines, docutils
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241205-3.14.0a2+-b477ad2-JIT/bm-20241205-linux-x86_64-brandtbucher-justin_cold_19-3.14.0a2+-b477ad2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.103x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x