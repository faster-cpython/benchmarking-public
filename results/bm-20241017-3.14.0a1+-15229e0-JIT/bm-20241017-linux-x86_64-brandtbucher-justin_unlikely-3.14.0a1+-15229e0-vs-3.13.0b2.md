# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-x86_64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.01x faster
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.01x slower                                                    |
| docutils       | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                  |
| html5lib       | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                   |
| tornado_http   | 94.6 ms                                                    | 95.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 374 ms: 1.19x faster                                                    |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                    |
| async_tree_io              | 939 ms                                                     | 859 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 318 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 559 ms: 1.05x faster                                                    |
| async_tree_io_tg           | 936 ms                                                     | 974 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                      | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                   |
| float          | 78.9 ms                                                    | 75.3 ms: 1.05x faster                                                   |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                      | 1.05x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 216 ms: 1.03x faster                                                    |
| regex_v8       | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| regex_effbot   | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                   |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                      | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 78.5 ms: 1.11x faster                                                   |
| xml_etree_process    | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                   |
| tomli_loads          | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                  |
| xml_etree_parse      | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| json_loads           | 28.9 us                                                    | 26.6 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                     | 99.1 ms: 1.08x faster                                                   |
| unpickle_pure_python | 218 us                                                     | 215 us: 1.01x faster                                                    |
| unpickle_list        | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| pickle_pure_python   | 305 us                                                     | 309 us: 1.01x slower                                                    |
| pickle_list          | 5.11 us                                                    | 5.16 us: 1.01x slower                                                   |
| json_dumps           | 10.7 ms                                                    | 10.9 ms: 1.02x slower                                                   |
| pickle_dict          | 34.8 us                                                    | 35.8 us: 1.03x slower                                                   |
| pickle               | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                      | 1.04x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| python_startup         | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.93 ms: 1.13x faster                                                   |
| django_template | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                   |
| genshi_text     | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                   |
| genshi_xml      | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 270 us: 1.36x faster                                                    |
| deepcopy_memo              | 39.7 us                                                    | 29.3 us: 1.36x faster                                                   |
| scimark_fft                | 392 ms                                                     | 317 ms: 1.24x faster                                                    |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                    | 2.71 us: 1.23x faster                                                   |
| richards_super             | 57.4 ms                                                    | 47.0 ms: 1.22x faster                                                   |
| async_tree_memoization_tg  | 444 ms                                                     | 374 ms: 1.19x faster                                                    |
| crypto_pyaes               | 77.5 ms                                                    | 66.4 ms: 1.17x faster                                                   |
| async_tree_none            | 378 ms                                                     | 328 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.62 ms: 1.14x faster                                                   |
| mako                       | 11.2 ms                                                    | 9.93 ms: 1.13x faster                                                   |
| bpe_tokeniser              | 5.02 sec                                                   | 4.45 sec: 1.13x faster                                                  |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 78.5 ms: 1.11x faster                                                   |
| xml_etree_process          | 61.2 ms                                                    | 55.0 ms: 1.11x faster                                                   |
| tomli_loads                | 2.12 sec                                                   | 1.91 sec: 1.11x faster                                                  |
| coverage                   | 93.1 ms                                                    | 84.0 ms: 1.11x faster                                                   |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                    |
| mdp                        | 2.79 sec                                                   | 2.54 sec: 1.10x faster                                                  |
| async_tree_io              | 939 ms                                                     | 859 ms: 1.09x faster                                                    |
| nbody                      | 88.3 ms                                                    | 80.9 ms: 1.09x faster                                                   |
| go                         | 145 ms                                                     | 132 ms: 1.09x faster                                                    |
| json_loads                 | 28.9 us                                                    | 26.6 us: 1.09x faster                                                   |
| xml_etree_iterparse        | 107 ms                                                     | 99.1 ms: 1.08x faster                                                   |
| telco                      | 8.41 ms                                                    | 7.79 ms: 1.08x faster                                                   |
| scimark_monte_carlo        | 69.2 ms                                                    | 64.1 ms: 1.08x faster                                                   |
| json                       | 5.31 ms                                                    | 4.92 ms: 1.08x faster                                                   |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                    |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                   |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                    |
| pyflate                    | 484 ms                                                     | 452 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 574 ms: 1.07x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 63.4 ms: 1.06x faster                                                   |
| chaos                      | 61.3 ms                                                    | 57.9 ms: 1.06x faster                                                   |
| async_tree_none_tg         | 336 ms                                                     | 318 ms: 1.06x faster                                                    |
| logging_format             | 6.47 us                                                    | 6.12 us: 1.06x faster                                                   |
| pprint_safe_repr           | 758 ms                                                     | 719 ms: 1.05x faster                                                    |
| sqlite_synth               | 2.99 us                                                    | 2.84 us: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 559 ms: 1.05x faster                                                    |
| thrift                     | 823 us                                                     | 783 us: 1.05x faster                                                    |
| float                      | 78.9 ms                                                    | 75.3 ms: 1.05x faster                                                   |
| logging_silent             | 105 ns                                                     | 100 ns: 1.05x faster                                                    |
| pprint_pformat             | 1.56 sec                                                   | 1.51 sec: 1.03x faster                                                  |
| logging_simple             | 5.74 us                                                    | 5.59 us: 1.03x faster                                                   |
| regex_dna                  | 221 ms                                                     | 216 ms: 1.03x faster                                                    |
| regex_v8                   | 25.1 ms                                                    | 24.5 ms: 1.03x faster                                                   |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                  |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                    |
| fannkuch                   | 402 ms                                                     | 395 ms: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                   |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                    |
| unpickle_pure_python       | 218 us                                                     | 215 us: 1.01x faster                                                    |
| meteor_contest             | 110 ms                                                     | 109 ms: 1.01x faster                                                    |
| unpickle_list              | 5.34 us                                                    | 5.30 us: 1.01x faster                                                   |
| python_startup_no_site     | 7.11 ms                                                    | 7.09 ms: 1.00x faster                                                   |
| tornado_http               | 94.6 ms                                                    | 95.4 ms: 1.01x slower                                                   |
| pickle_pure_python         | 305 us                                                     | 309 us: 1.01x slower                                                    |
| pickle_list                | 5.11 us                                                    | 5.16 us: 1.01x slower                                                   |
| 2to3                       | 274 ms                                                     | 278 ms: 1.01x slower                                                    |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.01x slower                                                  |
| comprehensions             | 16.6 us                                                    | 16.9 us: 1.02x slower                                                   |
| json_dumps                 | 10.7 ms                                                    | 10.9 ms: 1.02x slower                                                   |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                   |
| pickle_dict                | 34.8 us                                                    | 35.8 us: 1.03x slower                                                   |
| pickle                     | 11.5 us                                                    | 11.8 us: 1.03x slower                                                   |
| regex_effbot               | 3.67 ms                                                    | 3.78 ms: 1.03x slower                                                   |
| docutils                   | 2.83 sec                                                   | 2.92 sec: 1.03x slower                                                  |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                    |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 936 ms                                                     | 974 ms: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 115 ms: 1.04x slower                                                    |
| async_generators           | 442 ms                                                     | 461 ms: 1.04x slower                                                    |
| bench_thread_pool          | 834 us                                                     | 878 us: 1.05x slower                                                    |
| sympy_expand               | 473 ms                                                     | 499 ms: 1.06x slower                                                    |
| django_template            | 34.8 ms                                                    | 36.9 ms: 1.06x slower                                                   |
| sympy_str                  | 282 ms                                                     | 301 ms: 1.07x slower                                                    |
| genshi_text                | 23.7 ms                                                    | 25.5 ms: 1.08x slower                                                   |
| sqlglot_optimize           | 55.5 ms                                                    | 59.9 ms: 1.08x slower                                                   |
| nqueens                    | 81.4 ms                                                    | 88.4 ms: 1.09x slower                                                   |
| python_startup             | 10.8 ms                                                    | 11.9 ms: 1.11x slower                                                   |
| hexiom                     | 6.30 ms                                                    | 6.98 ms: 1.11x slower                                                   |
| gc_traversal               | 3.98 ms                                                    | 4.45 ms: 1.12x slower                                                   |
| sympy_sum                  | 156 ms                                                     | 177 ms: 1.14x slower                                                    |
| sympy_integrate            | 20.5 ms                                                    | 23.5 ms: 1.15x slower                                                   |
| genshi_xml                 | 51.6 ms                                                    | 59.7 ms: 1.16x slower                                                   |
| pylint                     | 317 ms                                                     | 376 ms: 1.19x slower                                                    |
| generators                 | 29.6 ms                                                    | 35.3 ms: 1.19x slower                                                   |
| create_gc_cycles           | 1.82 ms                                                    | 2.67 ms: 1.47x slower                                                   |
| bench_mp_pool              | 23.9 ms                                                    | 84.2 ms: 3.53x slower                                                   |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (6): unpickle, dulwich_log, deltablue, sqlglot_parse, typing_runtime_protocols, spectral_norm
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-linux-x86_64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.03% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x