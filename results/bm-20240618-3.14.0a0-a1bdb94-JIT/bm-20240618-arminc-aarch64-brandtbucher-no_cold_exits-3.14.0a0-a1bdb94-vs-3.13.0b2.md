# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                   |
| docutils       | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                 |
| html5lib       | 66.1 ms                                                      | 73.3 ms: 1.11x slower                                                  |
| tornado_http   | 128 ms                                                       | 141 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                        | 1.13x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 811 ms: 1.02x slower                                                   |
| async_tree_none            | 492 ms                                                       | 506 ms: 1.03x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 667 ms: 1.03x slower                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 626 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                           |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 116 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                  |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                  |
| regex_compile  | 128 ms                                                       | 175 ms: 1.36x slower                                                   |
| Geometric mean | (ref)                                                        | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.2 ms: 1.02x faster                                                  |
| pickle_dict          | 37.6 us                                                      | 37.3 us: 1.01x faster                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                  |
| unpickle_list        | 6.52 us                                                      | 6.61 us: 1.01x slower                                                  |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                  |
| json_loads           | 32.1 us                                                      | 32.8 us: 1.02x slower                                                  |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                 |
| pickle_pure_python   | 359 us                                                       | 393 us: 1.10x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 278 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_generate, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                  |
| genshi_text     | 27.4 ms                                                      | 35.2 ms: 1.28x slower                                                  |
| genshi_xml      | 60.4 ms                                                      | 82.2 ms: 1.36x slower                                                  |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.7 us: 1.35x faster                                                  |
| deepcopy                   | 448 us                                                       | 381 us: 1.18x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.85 ms: 1.07x faster                                                  |
| richards                   | 55.9 ms                                                      | 53.8 ms: 1.04x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 22.1 ms: 1.03x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.24 sec: 1.03x faster                                                 |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.2 ms: 1.02x faster                                                  |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                  |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                  |
| richards_super             | 62.3 ms                                                      | 61.4 ms: 1.01x faster                                                  |
| pickle_dict                | 37.6 us                                                      | 37.3 us: 1.01x faster                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                  |
| nbody                      | 114 ms                                                       | 116 ms: 1.01x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 6.61 us: 1.01x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                  |
| fannkuch                   | 451 ms                                                       | 459 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                 |
| json_loads                 | 32.1 us                                                      | 32.8 us: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 811 ms: 1.02x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.02 us: 1.03x slower                                                  |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                 |
| async_tree_none            | 492 ms                                                       | 506 ms: 1.03x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 6.01 sec: 1.03x slower                                                 |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.44 sec: 1.03x slower                                                 |
| async_tree_memoization     | 645 ms                                                       | 667 ms: 1.03x slower                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 626 ms: 1.04x slower                                                   |
| dask                       | 370 ms                                                       | 385 ms: 1.04x slower                                                   |
| scimark_fft                | 445 ms                                                       | 463 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.21 us: 1.04x slower                                                  |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                   |
| generators                 | 37.1 ms                                                      | 38.8 ms: 1.05x slower                                                  |
| async_generators           | 488 ms                                                       | 512 ms: 1.05x slower                                                   |
| json                       | 5.64 ms                                                      | 5.92 ms: 1.05x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.90 ms: 1.05x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 617 ms: 1.06x slower                                                   |
| logging_silent             | 133 ns                                                       | 141 ns: 1.06x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.34 ms: 1.07x slower                                                  |
| crypto_pyaes               | 82.0 ms                                                      | 88.0 ms: 1.07x slower                                                  |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.2 ms: 1.08x slower                                                  |
| bench_mp_pool              | 7.03 ms                                                      | 7.66 ms: 1.09x slower                                                  |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 212 us: 1.10x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 393 us: 1.10x slower                                                   |
| tornado_http               | 128 ms                                                       | 141 ms: 1.10x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 69.2 ms: 1.11x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 278 us: 1.11x slower                                                   |
| go                         | 161 ms                                                       | 178 ms: 1.11x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 73.3 ms: 1.11x slower                                                  |
| pyflate                    | 557 ms                                                       | 619 ms: 1.11x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 144 ms: 1.11x slower                                                   |
| scimark_sor                | 159 ms                                                       | 178 ms: 1.12x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.12x slower                                                 |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                  |
| comprehensions             | 20.5 us                                                      | 23.1 us: 1.13x slower                                                  |
| docutils                   | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                 |
| deltablue                  | 3.88 ms                                                      | 4.48 ms: 1.16x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.18x slower                                                  |
| django_template            | 42.3 ms                                                      | 49.8 ms: 1.18x slower                                                  |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                   |
| sympy_expand               | 457 ms                                                       | 543 ms: 1.19x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.12 sec: 1.21x slower                                                 |
| pylint                     | 337 ms                                                       | 410 ms: 1.22x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.35 sec: 1.22x slower                                                 |
| sympy_str                  | 265 ms                                                       | 326 ms: 1.23x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 72.4 ms: 1.24x slower                                                  |
| hexiom                     | 7.08 ms                                                      | 8.96 ms: 1.27x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 26.5 ms: 1.27x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 35.2 ms: 1.28x slower                                                  |
| scimark_lu                 | 141 ms                                                       | 183 ms: 1.30x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 187 ms: 1.30x slower                                                   |
| chaos                      | 68.3 ms                                                      | 89.5 ms: 1.31x slower                                                  |
| genshi_xml                 | 60.4 ms                                                      | 82.2 ms: 1.36x slower                                                  |
| regex_compile              | 128 ms                                                       | 175 ms: 1.36x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                           |

Benchmark hidden because not significant (17): float, sqlite_synth, xml_etree_parse, create_gc_cycles, xml_etree_generate, thrift, unpickle, pickle_list, async_tree_none_tg, pidigits, python_startup, coroutines, mako, asyncio_websockets, telco, logging_simple, async_tree_io
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x