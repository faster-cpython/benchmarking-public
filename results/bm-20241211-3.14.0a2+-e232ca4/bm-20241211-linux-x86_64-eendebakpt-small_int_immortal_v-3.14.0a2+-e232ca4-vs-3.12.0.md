# Results vs. 3.12.0

- fork: eendebakpt
- ref: small_int_immortal_v
- machine: linux-x86_64
- commit hash: e232ca4
- commit date: 2024-12-11
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.07x faster                                                       |
| docutils       | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 631 ms: 1.88x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                       |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.3 ms: 1.11x faster                                                      |
| nbody          | 97.0 ms                                                | 94.0 ms: 1.03x faster                                                      |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| regex_effbot   | 3.61 ms                                                | 3.52 ms: 1.03x faster                                                      |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                       |
| regex_v8       | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 97.3 ms: 1.10x faster                                                      |
| json_loads           | 28.5 us                                                | 26.8 us: 1.06x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                       |
| xml_etree_generate   | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                      |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                      |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                      |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 631 ms: 1.88x faster                                                       |
| async_tree_io              | 1.16 sec                                               | 626 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                       |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                       |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                       |
| async_tree_memoization     | 578 ms                                                 | 339 ms: 1.70x faster                                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 489 ms: 1.48x faster                                                       |
| deepcopy                   | 371 us                                                 | 259 us: 1.43x faster                                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 507 ms: 1.43x faster                                                       |
| deepcopy_memo              | 40.7 us                                                | 30.9 us: 1.32x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                      |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                      |
| go                         | 139 ms                                                 | 119 ms: 1.18x faster                                                       |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 70.4 ms: 1.16x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.58 us: 1.16x faster                                                      |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                      |
| sqlalchemy_declarative     | 147 ms                                                 | 127 ms: 1.16x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.3 ms: 1.15x faster                                                      |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                       |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                       |
| generators                 | 31.2 ms                                                | 27.3 ms: 1.14x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.27 ms: 1.14x faster                                                      |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                     |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                       |
| float                      | 84.7 ms                                                | 76.3 ms: 1.11x faster                                                      |
| async_generators           | 463 ms                                                 | 421 ms: 1.10x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.3 ms: 1.10x faster                                                      |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 68.9 ms: 1.09x faster                                                      |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                      |
| 2to3                       | 274 ms                                                 | 255 ms: 1.07x faster                                                       |
| json_loads                 | 28.5 us                                                | 26.8 us: 1.06x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                     |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.05x faster                                                      |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                      |
| dulwich_log                | 68.5 ms                                                | 65.2 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                     |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                       |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                       |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                      |
| nbody                      | 97.0 ms                                                | 94.0 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.90 ms: 1.03x faster                                                      |
| fannkuch                   | 417 ms                                                 | 405 ms: 1.03x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                     |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                       |
| xml_etree_generate         | 89.2 ms                                                | 86.8 ms: 1.03x faster                                                      |
| json                       | 5.26 ms                                                | 5.13 ms: 1.03x faster                                                      |
| regex_effbot               | 3.61 ms                                                | 3.52 ms: 1.03x faster                                                      |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                     |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.02x faster                                                       |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                                      |
| xml_etree_process          | 61.7 ms                                                | 60.6 ms: 1.02x faster                                                      |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                      |
| scimark_fft                | 382 ms                                                 | 376 ms: 1.02x faster                                                       |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                       |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                       |
| richards                   | 45.8 ms                                                | 46.2 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                      |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                       |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                      |
| richards_super             | 51.5 ms                                                | 52.3 ms: 1.02x slower                                                      |
| bench_thread_pool          | 842 us                                                 | 857 us: 1.02x slower                                                       |
| pyflate                    | 482 ms                                                 | 496 ms: 1.03x slower                                                       |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                       |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                       |
| telco                      | 7.10 ms                                                | 7.78 ms: 1.10x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.9 ms: 1.12x slower                                                      |
| mypy2                      | 830 ms                                                 | 948 ms: 1.14x slower                                                       |
| coverage                   | 72.7 ms                                                | 83.1 ms: 1.14x slower                                                      |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.26x slower                                                      |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241211-3.14.0a2+-e232ca4/bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x