# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-aarch64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 363 ms: 1.19x slower                                                       |
| docutils       | 3.10 sec                                                     | 3.55 sec: 1.14x slower                                                     |
| html5lib       | 66.1 ms                                                      | 69.4 ms: 1.05x slower                                                      |
| tornado_http   | 128 ms                                                       | 135 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 411 ms: 1.16x faster                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 537 ms: 1.13x faster                                                       |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                       |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 740 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 90.1 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                        | 1.00x faster                                                               |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 173 ms: 1.35x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x slower                                                               |

Benchmark hidden because not significant (3): regex_dna, regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                      |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                      |
| unpickle_pure_python | 251 us                                                       | 261 us: 1.04x slower                                                       |
| pickle_pure_python   | 359 us                                                       | 393 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                               |

Benchmark hidden because not significant (5): xml_etree_process, xml_etree_parse, tomli_loads, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                      |
| python_startup_no_site | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                      |
| django_template | 42.3 ms                                                      | 50.0 ms: 1.18x slower                                                      |
| genshi_text     | 27.4 ms                                                      | 32.6 ms: 1.19x slower                                                      |
| genshi_xml      | 60.4 ms                                                      | 75.7 ms: 1.25x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.4 us: 1.32x faster                                                      |
| deepcopy                   | 448 us                                                       | 377 us: 1.19x faster                                                       |
| async_tree_none_tg         | 476 ms                                                       | 411 ms: 1.16x faster                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.15x faster                                                     |
| async_tree_io_tg           | 1.27 sec                                                     | 1.12 sec: 1.14x faster                                                     |
| async_tree_memoization_tg  | 604 ms                                                       | 537 ms: 1.13x faster                                                       |
| async_tree_memoization     | 645 ms                                                       | 582 ms: 1.11x faster                                                       |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                       |
| richards                   | 55.9 ms                                                      | 51.4 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 740 ms: 1.07x faster                                                       |
| richards_super             | 62.3 ms                                                      | 58.7 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 724 ms: 1.05x faster                                                       |
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                      |
| gc_traversal               | 5.17 ms                                                      | 5.06 ms: 1.02x faster                                                      |
| float                      | 91.4 ms                                                      | 90.1 ms: 1.01x faster                                                      |
| mako                       | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                      |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                      |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.01x slower                                                       |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                     |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                      |
| logging_silent             | 133 ns                                                       | 137 ns: 1.02x slower                                                       |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                      |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                       |
| python_startup_no_site     | 8.60 ms                                                      | 8.85 ms: 1.03x slower                                                      |
| coroutines                 | 29.0 ms                                                      | 29.9 ms: 1.03x slower                                                      |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 5.83 sec                                                     | 6.04 sec: 1.04x slower                                                     |
| scimark_fft                | 445 ms                                                       | 462 ms: 1.04x slower                                                       |
| fannkuch                   | 451 ms                                                       | 468 ms: 1.04x slower                                                       |
| deepcopy_reduce            | 4.04 us                                                      | 4.19 us: 1.04x slower                                                      |
| unpickle_pure_python       | 251 us                                                       | 261 us: 1.04x slower                                                       |
| mdp                        | 3.33 sec                                                     | 3.46 sec: 1.04x slower                                                     |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 82.3 ms                                                      | 85.8 ms: 1.04x slower                                                      |
| asyncio_tcp                | 584 ms                                                       | 610 ms: 1.04x slower                                                       |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                      |
| html5lib                   | 66.1 ms                                                      | 69.4 ms: 1.05x slower                                                      |
| async_generators           | 488 ms                                                       | 515 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.91 ms: 1.06x slower                                                      |
| crypto_pyaes               | 82.0 ms                                                      | 86.5 ms: 1.06x slower                                                      |
| generators                 | 37.1 ms                                                      | 39.2 ms: 1.06x slower                                                      |
| tornado_http               | 128 ms                                                       | 135 ms: 1.06x slower                                                       |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.07x slower                                                       |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                       |
| pickle_pure_python         | 359 us                                                       | 393 us: 1.09x slower                                                       |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                       |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                     |
| pyflate                    | 557 ms                                                       | 612 ms: 1.10x slower                                                       |
| scimark_sor                | 159 ms                                                       | 175 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 62.6 ms                                                      | 69.2 ms: 1.10x slower                                                      |
| go                         | 161 ms                                                       | 178 ms: 1.11x slower                                                       |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                      |
| comprehensions             | 20.5 us                                                      | 23.4 us: 1.14x slower                                                      |
| docutils                   | 3.10 sec                                                     | 3.55 sec: 1.14x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.00 ms: 1.17x slower                                                      |
| django_template            | 42.3 ms                                                      | 50.0 ms: 1.18x slower                                                      |
| bench_mp_pool              | 7.03 ms                                                      | 8.33 ms: 1.19x slower                                                      |
| genshi_text                | 27.4 ms                                                      | 32.6 ms: 1.19x slower                                                      |
| 2to3                       | 305 ms                                                       | 363 ms: 1.19x slower                                                       |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                     |
| nqueens                    | 98.9 ms                                                      | 118 ms: 1.19x slower                                                       |
| sympy_expand               | 457 ms                                                       | 547 ms: 1.20x slower                                                       |
| pprint_pformat             | 1.93 sec                                                     | 2.32 sec: 1.20x slower                                                     |
| dulwich_log                | 58.5 ms                                                      | 70.6 ms: 1.21x slower                                                      |
| deltablue                  | 3.88 ms                                                      | 4.70 ms: 1.21x slower                                                      |
| sympy_str                  | 265 ms                                                       | 324 ms: 1.22x slower                                                       |
| pylint                     | 337 ms                                                       | 418 ms: 1.24x slower                                                       |
| genshi_xml                 | 60.4 ms                                                      | 75.7 ms: 1.25x slower                                                      |
| sympy_integrate            | 20.9 ms                                                      | 26.2 ms: 1.25x slower                                                      |
| chaos                      | 68.3 ms                                                      | 87.0 ms: 1.27x slower                                                      |
| sympy_sum                  | 144 ms                                                       | 184 ms: 1.28x slower                                                       |
| hexiom                     | 7.08 ms                                                      | 9.17 ms: 1.30x slower                                                      |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                       |
| regex_compile              | 128 ms                                                       | 173 ms: 1.35x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                               |

Benchmark hidden because not significant (16): xml_etree_process, regex_dna, regex_v8, pidigits, xml_etree_parse, regex_effbot, create_gc_cycles, tomli_loads, thrift, logging_simple, asyncio_websockets, nbody, json, logging_format, xml_etree_iterparse, xml_etree_generate
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x