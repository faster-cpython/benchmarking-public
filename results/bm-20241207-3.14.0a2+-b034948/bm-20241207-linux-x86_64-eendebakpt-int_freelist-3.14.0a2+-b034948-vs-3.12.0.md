# Results vs. 3.12.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b034948
- commit date: 2024-12-07
- overall geometric mean: 1.100x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                               |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                               |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 329 ms: 1.74x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.72x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 264 ms: 1.70x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                               |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                              |
| nbody          | 97.0 ms                                                | 93.5 ms: 1.04x faster                                              |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| regex_effbot   | 3.61 ms                                                | 3.30 ms: 1.10x faster                                              |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                               |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                               |
| xml_etree_iterparse  | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| json_loads           | 28.5 us                                                | 26.4 us: 1.08x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.05x faster                                              |
| xml_etree_process    | 61.7 ms                                                | 59.4 ms: 1.04x faster                                              |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                               |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                               |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                              |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                              |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                              |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                               |
| async_tree_none            | 472 ms                                                 | 270 ms: 1.75x faster                                               |
| async_tree_memoization_tg  | 575 ms                                                 | 329 ms: 1.74x faster                                               |
| async_tree_memoization     | 578 ms                                                 | 337 ms: 1.72x faster                                               |
| async_tree_none_tg         | 450 ms                                                 | 264 ms: 1.70x faster                                               |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 485 ms: 1.50x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 491 ms: 1.48x faster                                               |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                               |
| deepcopy_memo              | 40.7 us                                                | 31.3 us: 1.30x faster                                              |
| comprehensions             | 21.8 us                                                | 17.0 us: 1.28x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                              |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                              |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                               |
| logging_format             | 7.23 us                                                | 6.19 us: 1.17x faster                                              |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                               |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                               |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                              |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                               |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                             |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                               |
| deltablue                  | 3.72 ms                                                | 3.24 ms: 1.15x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.6 ms: 1.13x faster                                              |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                               |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                               |
| json                       | 5.26 ms                                                | 4.78 ms: 1.10x faster                                              |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                              |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                              |
| chaos                      | 67.0 ms                                                | 61.1 ms: 1.10x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.30 ms: 1.10x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                               |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 98.4 ms: 1.09x faster                                              |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                             |
| json_loads                 | 28.5 us                                                | 26.4 us: 1.08x faster                                              |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                              |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                               |
| scimark_fft                | 382 ms                                                 | 356 ms: 1.07x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                              |
| pyflate                    | 482 ms                                                 | 452 ms: 1.07x faster                                               |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                              |
| spectral_norm              | 115 ms                                                 | 108 ms: 1.07x faster                                               |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                              |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.06x faster                                               |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.05x faster                                              |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 59.4 ms: 1.04x faster                                              |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                               |
| nbody                      | 97.0 ms                                                | 93.5 ms: 1.04x faster                                              |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.03x faster                                               |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                               |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                              |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                              |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                               |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                             |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                              |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                               |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                              |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                               |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                               |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                               |
| richards_super             | 51.5 ms                                                | 52.0 ms: 1.01x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                              |
| mdp                        | 2.63 sec                                               | 2.68 sec: 1.02x slower                                             |
| bench_thread_pool          | 842 us                                                 | 861 us: 1.02x slower                                               |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 163 us: 1.03x slower                                               |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                              |
| telco                      | 7.10 ms                                                | 7.81 ms: 1.10x slower                                              |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                              |
| mypy2                      | 830 ms                                                 | 943 ms: 1.14x slower                                               |
| coverage                   | 72.7 ms                                                | 83.5 ms: 1.15x slower                                              |
| gc_traversal               | 3.79 ms                                                | 4.50 ms: 1.19x slower                                              |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                              |
| create_gc_cycles           | 1.48 ms                                                | 2.22 ms: 1.50x slower                                              |
| bench_mp_pool              | 24.0 ms                                                | 78.6 ms: 3.27x slower                                              |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                       |

Benchmark hidden because not significant (3): richards, sqlite_synth, scimark_lu
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241207-3.14.0a2+-b034948/bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.100x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x