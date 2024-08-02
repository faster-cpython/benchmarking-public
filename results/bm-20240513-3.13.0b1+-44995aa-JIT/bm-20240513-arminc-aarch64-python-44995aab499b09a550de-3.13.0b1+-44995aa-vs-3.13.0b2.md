# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.11x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 362 ms: 1.19x slower                                                     |
| chameleon      | 8.95 ms                                                      | 9.14 ms: 1.02x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.55 sec: 1.15x slower                                                   |
| html5lib       | 66.1 ms                                                      | 70.2 ms: 1.06x slower                                                    |
| tornado_http   | 128 ms                                                       | 141 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                        | 1.10x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 817 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.8 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                     |
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 167 ms: 1.31x slower                                                     |
| Geometric mean | (ref)                                                        | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_list          | 5.27 us                                                      | 5.20 us: 1.01x faster                                                    |
| unpickle             | 19.8 us                                                      | 19.6 us: 1.01x faster                                                    |
| pickle_dict          | 37.6 us                                                      | 38.2 us: 1.01x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.65 us: 1.02x slower                                                    |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 151 ms: 1.03x slower                                                     |
| xml_etree_generate   | 114 ms                                                       | 118 ms: 1.03x slower                                                     |
| pickle_pure_python   | 359 us                                                       | 393 us: 1.10x slower                                                     |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                             |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.1 ms: 1.16x slower                                                    |
| python_startup_no_site | 8.60 ms                                                      | 10.8 ms: 1.25x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 49.5 ms: 1.17x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 33.9 ms: 1.24x slower                                                    |
| genshi_xml      | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                             |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                     |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 49.8 us: 1.02x faster                                                    |
| float                      | 91.4 ms                                                      | 89.8 ms: 1.02x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.20 us: 1.01x faster                                                    |
| unpickle                   | 19.8 us                                                      | 19.6 us: 1.01x faster                                                    |
| coverage                   | 98.4 ms                                                      | 99.1 ms: 1.01x slower                                                    |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                     |
| pickle_dict                | 37.6 us                                                      | 38.2 us: 1.01x slower                                                    |
| chameleon                  | 8.95 ms                                                      | 9.14 ms: 1.02x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.65 us: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.30 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                   |
| pathlib                    | 22.8 ms                                                      | 23.4 ms: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.05 us: 1.03x slower                                                    |
| scimark_fft                | 445 ms                                                       | 458 ms: 1.03x slower                                                     |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 151 ms: 1.03x slower                                                     |
| xml_etree_generate         | 114 ms                                                       | 118 ms: 1.03x slower                                                     |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.04x slower                                                     |
| generators                 | 37.1 ms                                                      | 38.8 ms: 1.04x slower                                                    |
| logging_silent             | 133 ns                                                       | 140 ns: 1.05x slower                                                     |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.05x slower                                                   |
| meteor_contest             | 113 ms                                                       | 119 ms: 1.05x slower                                                     |
| create_gc_cycles           | 2.33 ms                                                      | 2.45 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                    |
| async_generators           | 488 ms                                                       | 514 ms: 1.05x slower                                                     |
| crypto_pyaes               | 82.0 ms                                                      | 86.6 ms: 1.06x slower                                                    |
| fannkuch                   | 451 ms                                                       | 479 ms: 1.06x slower                                                     |
| html5lib                   | 66.1 ms                                                      | 70.2 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.97 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.6 ms: 1.06x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 624 ms: 1.07x slower                                                     |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                     |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 817 ms: 1.07x slower                                                     |
| dask                       | 370 ms                                                       | 397 ms: 1.07x slower                                                     |
| flaskblogging              | 4.70 ms                                                      | 5.06 ms: 1.08x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 393 us: 1.10x slower                                                     |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                     |
| tornado_http               | 128 ms                                                       | 141 ms: 1.10x slower                                                     |
| pyflate                    | 557 ms                                                       | 613 ms: 1.10x slower                                                     |
| raytrace                   | 297 ms                                                       | 327 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                     |
| gunicorn                   | 1.19 ms                                                      | 1.31 ms: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 178 ms: 1.11x slower                                                     |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                    |
| deepcopy                   | 448 us                                                       | 502 us: 1.12x slower                                                     |
| bench_mp_pool              | 7.03 ms                                                      | 7.87 ms: 1.12x slower                                                    |
| comprehensions             | 20.5 us                                                      | 23.1 us: 1.12x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 146 ms: 1.13x slower                                                     |
| aiohttp                    | 1.18 ms                                                      | 1.34 ms: 1.14x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 71.3 ms: 1.14x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.55 sec: 1.15x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.66 us: 1.16x slower                                                    |
| python_startup             | 13.0 ms                                                      | 15.1 ms: 1.16x slower                                                    |
| django_template            | 42.3 ms                                                      | 49.5 ms: 1.17x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 68.7 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.03 ms: 1.19x slower                                                    |
| 2to3                       | 305 ms                                                       | 362 ms: 1.19x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                     |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.63 ms: 1.19x slower                                                    |
| sympy_expand               | 457 ms                                                       | 548 ms: 1.20x slower                                                     |
| pprint_pformat             | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                   |
| pylint                     | 337 ms                                                       | 411 ms: 1.22x slower                                                     |
| sympy_str                  | 265 ms                                                       | 324 ms: 1.22x slower                                                     |
| mypy2                      | 767 ms                                                       | 946 ms: 1.23x slower                                                     |
| genshi_text                | 27.4 ms                                                      | 33.9 ms: 1.24x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 26.0 ms: 1.25x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 10.8 ms: 1.25x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 182 ms: 1.27x slower                                                     |
| hexiom                     | 7.08 ms                                                      | 8.97 ms: 1.27x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                     |
| chaos                      | 68.3 ms                                                      | 89.2 ms: 1.31x slower                                                    |
| regex_compile              | 128 ms                                                       | 167 ms: 1.31x slower                                                     |
| genshi_xml                 | 60.4 ms                                                      | 82.0 ms: 1.36x slower                                                    |
| telco                      | 10.0 ms                                                      | 167 ms: 16.66x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.11x slower                                                             |

Benchmark hidden because not significant (21): xml_etree_parse, async_tree_io_tg, richards, sqlite_synth, async_tree_none_tg, coroutines, xml_etree_process, json_dumps, json_loads, richards_super, json, mako, async_tree_none, pidigits, thrift, nbody, async_tree_memoization, async_tree_memoization_tg, logging_simple, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x