# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_64
- machine: linux-x86_64
- commit hash: 48ade84
- commit date: 2024-11-08
- overall geometric mean: 1.058x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 277 ms: 1.01x slower                                              |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.05x slower                                            |
| Geometric mean | (ref)                                                  | 1.03x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                              |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                              |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                              |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                              |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.6 ms: 1.17x faster                                             |
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                             |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                              |
| regex_effbot   | 3.61 ms                                                | 3.62 ms: 1.00x slower                                             |
| regex_dna      | 212 ms                                                 | 214 ms: 1.01x slower                                              |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                            |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 79.1 ms: 1.13x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                              |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                             |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                              |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                              |
| json_dumps           | 10.4 ms                                                | 10.8 ms: 1.04x slower                                             |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                             |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                             |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                             |
| django_template | 34.6 ms                                                | 36.2 ms: 1.05x slower                                             |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 383 ms: 1.50x faster                                              |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                              |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                              |
| async_tree_memoization     | 578 ms                                                 | 418 ms: 1.38x faster                                              |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                             |
| deepcopy                   | 371 us                                                 | 271 us: 1.37x faster                                              |
| async_tree_io              | 1.16 sec                                               | 856 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                              |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                              |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.22x faster                                             |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 978 ms: 1.21x faster                                              |
| scimark_fft                | 382 ms                                                 | 320 ms: 1.19x faster                                              |
| crypto_pyaes               | 81.9 ms                                                | 68.7 ms: 1.19x faster                                             |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                            |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                             |
| nbody                      | 97.0 ms                                                | 82.6 ms: 1.17x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                              |
| scimark_monte_carlo        | 75.1 ms                                                | 64.7 ms: 1.16x faster                                             |
| logging_format             | 7.23 us                                                | 6.31 us: 1.15x faster                                             |
| chaos                      | 67.0 ms                                                | 59.0 ms: 1.13x faster                                             |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.13x faster                                             |
| xml_etree_generate         | 89.2 ms                                                | 79.1 ms: 1.13x faster                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                             |
| logging_simple             | 6.46 us                                                | 5.74 us: 1.13x faster                                             |
| xml_etree_process          | 61.7 ms                                                | 55.4 ms: 1.11x faster                                             |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                             |
| raytrace                   | 312 ms                                                 | 285 ms: 1.10x faster                                              |
| richards                   | 45.8 ms                                                | 42.4 ms: 1.08x faster                                             |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                              |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                              |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                              |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                              |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                             |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                              |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                              |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.06x faster                                             |
| json                       | 5.26 ms                                                | 4.99 ms: 1.05x faster                                             |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                              |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                              |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                            |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                            |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                              |
| async_generators           | 463 ms                                                 | 452 ms: 1.03x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                             |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                            |
| go                         | 139 ms                                                 | 137 ms: 1.02x faster                                              |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                             |
| dulwich_log                | 68.5 ms                                                | 67.8 ms: 1.01x faster                                             |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                              |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                              |
| regex_effbot               | 3.61 ms                                                | 3.62 ms: 1.00x slower                                             |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                              |
| regex_dna                  | 212 ms                                                 | 214 ms: 1.01x slower                                              |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                             |
| 2to3                       | 274 ms                                                 | 277 ms: 1.01x slower                                              |
| sympy_str                  | 300 ms                                                 | 303 ms: 1.01x slower                                              |
| sqlglot_normalize          | 110 ms                                                 | 113 ms: 1.02x slower                                              |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                             |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                              |
| json_dumps                 | 10.4 ms                                                | 10.8 ms: 1.04x slower                                             |
| django_template            | 34.6 ms                                                | 36.2 ms: 1.05x slower                                             |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                              |
| sympy_expand               | 478 ms                                                 | 502 ms: 1.05x slower                                              |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.05x slower                                            |
| nqueens                    | 83.3 ms                                                | 87.9 ms: 1.05x slower                                             |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                              |
| telco                      | 7.10 ms                                                | 7.61 ms: 1.07x slower                                             |
| sqlglot_optimize           | 54.8 ms                                                | 59.1 ms: 1.08x slower                                             |
| sympy_integrate            | 21.4 ms                                                | 23.2 ms: 1.08x slower                                             |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                             |
| hexiom                     | 6.41 ms                                                | 7.15 ms: 1.11x slower                                             |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                             |
| generators                 | 31.2 ms                                                | 36.2 ms: 1.16x slower                                             |
| gc_traversal               | 3.79 ms                                                | 4.81 ms: 1.27x slower                                             |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                             |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                             |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                             |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                      |

Benchmark hidden because not significant (2): sqlalchemy_declarative, spectral_norm
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241108-3.14.0a1+-48ade84-JIT/bm-20241108-linux-x86_64-brandtbucher-warmup_64-3.14.0a1+-48ade84.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.058x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.13x