# Results vs. 3.12.0

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.004x faster
- HPT reliability: 72.40%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 283 ms: 1.01x faster                                                     |
| docutils       | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                     |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 325 ms: 1.33x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                     |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 850 ms: 1.23x faster                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                     |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                                     |
| nbody          | 88.0 ms                                                      | 91.3 ms: 1.04x slower                                                    |
| float          | 76.6 ms                                                      | 80.5 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                     |
| regex_effbot   | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                    |
| regex_dna      | 239 ms                                                       | 242 ms: 1.02x slower                                                     |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                        | 1.02x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 87.3 ms: 1.01x slower                                                    |
| unpickle_pure_python | 210 us                                                       | 215 us: 1.02x slower                                                     |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                    |
| xml_etree_parse      | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| pickle_pure_python   | 318 us                                                       | 333 us: 1.05x slower                                                     |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                                    |
| tomli_loads          | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                                   |
| json_dumps           | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                    |
| python_startup         | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 37.3 ms: 1.02x faster                                                    |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 380 ms: 1.42x faster                                                     |
| async_tree_none            | 452 ms                                                       | 334 ms: 1.35x faster                                                     |
| async_tree_none_tg         | 431 ms                                                       | 325 ms: 1.33x faster                                                     |
| async_tree_memoization     | 544 ms                                                       | 413 ms: 1.32x faster                                                     |
| deepcopy                   | 368 us                                                       | 286 us: 1.29x faster                                                     |
| generators                 | 37.4 ms                                                      | 29.3 ms: 1.28x faster                                                    |
| comprehensions             | 21.9 us                                                      | 17.5 us: 1.25x faster                                                    |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                     |
| async_tree_io              | 1.04 sec                                                     | 850 ms: 1.23x faster                                                     |
| async_tree_io_tg           | 1.05 sec                                                     | 871 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 580 ms: 1.20x faster                                                     |
| pathlib                    | 18.9 ms                                                      | 16.3 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                    |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                     |
| go                         | 150 ms                                                       | 136 ms: 1.10x faster                                                     |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.08x faster                                                    |
| raytrace                   | 298 ms                                                       | 278 ms: 1.07x faster                                                     |
| crypto_pyaes               | 80.3 ms                                                      | 75.1 ms: 1.07x faster                                                    |
| logging_format             | 7.48 us                                                      | 7.03 us: 1.07x faster                                                    |
| sympy_sum                  | 162 ms                                                       | 152 ms: 1.06x faster                                                     |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                                     |
| spectral_norm              | 91.6 ms                                                      | 87.3 ms: 1.05x faster                                                    |
| mdp                        | 2.57 sec                                                     | 2.47 sec: 1.04x faster                                                   |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                     |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.5 ms: 1.04x faster                                                    |
| chaos                      | 64.0 ms                                                      | 61.9 ms: 1.03x faster                                                    |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.2 ms: 1.03x faster                                                    |
| bench_thread_pool          | 950 us                                                       | 924 us: 1.03x faster                                                     |
| sympy_str                  | 302 ms                                                       | 294 ms: 1.03x faster                                                     |
| logging_simple             | 6.71 us                                                      | 6.54 us: 1.03x faster                                                    |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.03x faster                                                     |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                                   |
| django_template            | 38.2 ms                                                      | 37.3 ms: 1.02x faster                                                    |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                   |
| nqueens                    | 89.9 ms                                                      | 88.6 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 807 ms                                                       | 798 ms: 1.01x faster                                                     |
| 2to3                       | 285 ms                                                       | 283 ms: 1.01x faster                                                     |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                    |
| json                       | 5.12 ms                                                      | 5.17 ms: 1.01x slower                                                    |
| regex_effbot               | 3.57 ms                                                      | 3.61 ms: 1.01x slower                                                    |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                    |
| xml_etree_generate         | 86.1 ms                                                      | 87.3 ms: 1.01x slower                                                    |
| regex_dna                  | 239 ms                                                       | 242 ms: 1.02x slower                                                     |
| scimark_fft                | 301 ms                                                       | 306 ms: 1.02x slower                                                     |
| docutils                   | 2.87 sec                                                     | 2.92 sec: 1.02x slower                                                   |
| dulwich_log                | 65.4 ms                                                      | 66.7 ms: 1.02x slower                                                    |
| unpickle_pure_python       | 210 us                                                       | 215 us: 1.02x slower                                                     |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 57.5 ms                                                      | 59.0 ms: 1.03x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.03x slower                                                    |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                     |
| nbody                      | 88.0 ms                                                      | 91.3 ms: 1.04x slower                                                    |
| xml_etree_parse            | 144 ms                                                       | 150 ms: 1.04x slower                                                     |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                     |
| pickle_pure_python         | 318 us                                                       | 333 us: 1.05x slower                                                     |
| python_startup_no_site     | 8.64 ms                                                      | 9.04 ms: 1.05x slower                                                    |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                                    |
| float                      | 76.6 ms                                                      | 80.5 ms: 1.05x slower                                                    |
| hexiom                     | 5.96 ms                                                      | 6.28 ms: 1.05x slower                                                    |
| logging_silent             | 94.4 ns                                                      | 100.0 ns: 1.06x slower                                                   |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                    |
| fannkuch                   | 350 ms                                                       | 376 ms: 1.07x slower                                                     |
| richards                   | 45.7 ms                                                      | 49.3 ms: 1.08x slower                                                    |
| richards_super             | 51.3 ms                                                      | 55.6 ms: 1.08x slower                                                    |
| deltablue                  | 3.24 ms                                                      | 3.52 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.61 ms: 1.10x slower                                                    |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                                    |
| pyflate                    | 439 ms                                                       | 488 ms: 1.11x slower                                                     |
| async_generators           | 390 ms                                                       | 436 ms: 1.12x slower                                                     |
| tomli_loads                | 2.16 sec                                                     | 2.42 sec: 1.12x slower                                                   |
| json_dumps                 | 10.2 ms                                                      | 11.5 ms: 1.12x slower                                                    |
| telco                      | 6.96 ms                                                      | 7.88 ms: 1.13x slower                                                    |
| scimark_sor                | 109 ms                                                       | 126 ms: 1.16x slower                                                     |
| typing_runtime_protocols   | 152 us                                                       | 177 us: 1.17x slower                                                     |
| coverage                   | 66.7 ms                                                      | 83.7 ms: 1.26x slower                                                    |
| python_startup             | 11.6 ms                                                      | 16.0 ms: 1.38x slower                                                    |
| gc_traversal               | 3.48 ms                                                      | 6.15 ms: 1.77x slower                                                    |
| create_gc_cycles           | 1.59 ms                                                      | 3.00 ms: 1.89x slower                                                    |
| bench_mp_pool              | 4.76 ms                                                      | 1.22 sec: 256.57x slower                                                 |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                             |

Benchmark hidden because not significant (3): scimark_lu, asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-pythonperf2-x86_64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 72.40% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x