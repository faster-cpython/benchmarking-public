# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-aarch64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.06x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 365 ms: 1.20x slower                                                       |
| docutils       | 3.10 sec                                                     | 3.67 sec: 1.19x slower                                                     |
| html5lib       | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                      |
| tornado_http   | 128 ms                                                       | 138 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                     |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                       |
| async_tree_memoization     | 645 ms                                                       | 576 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 700 ms: 1.09x faster                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 745 ms: 1.06x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                               |

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                       |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                      |
| regex_compile  | 128 ms                                                       | 181 ms: 1.41x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.8 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 147 ms                                                       | 146 ms: 1.01x faster                                                       |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.01x slower                                                      |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.03x slower                                                      |
| tomli_loads          | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                     |
| xml_etree_generate   | 114 ms                                                       | 119 ms: 1.05x slower                                                       |
| unpickle_pure_python | 251 us                                                       | 278 us: 1.11x slower                                                       |
| pickle_pure_python   | 359 us                                                       | 399 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.86 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                      |
| django_template | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                      |
| genshi_text     | 27.4 ms                                                      | 36.5 ms: 1.33x slower                                                      |
| genshi_xml      | 60.4 ms                                                      | 82.9 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.7 us: 1.31x faster                                                      |
| deepcopy                   | 448 us                                                       | 381 us: 1.18x faster                                                       |
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                     |
| async_tree_none            | 492 ms                                                       | 433 ms: 1.14x faster                                                       |
| async_tree_memoization     | 645 ms                                                       | 576 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                       |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 700 ms: 1.09x faster                                                       |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 745 ms: 1.06x faster                                                       |
| gc_traversal               | 5.17 ms                                                      | 4.91 ms: 1.05x faster                                                      |
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                       |
| pathlib                    | 22.8 ms                                                      | 22.0 ms: 1.04x faster                                                      |
| mako                       | 13.2 ms                                                      | 12.9 ms: 1.02x faster                                                      |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                      |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                      |
| xml_etree_process          | 80.8 ms                                                      | 79.8 ms: 1.01x faster                                                      |
| xml_etree_iterparse        | 147 ms                                                       | 146 ms: 1.01x faster                                                       |
| spectral_norm              | 141 ms                                                       | 143 ms: 1.01x slower                                                       |
| logging_format             | 7.82 us                                                      | 7.92 us: 1.01x slower                                                      |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                     |
| bpe_tokeniser              | 5.83 sec                                                     | 5.92 sec: 1.02x slower                                                     |
| logging_silent             | 133 ns                                                       | 136 ns: 1.02x slower                                                       |
| thrift                     | 962 us                                                       | 983 us: 1.02x slower                                                       |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.03x slower                                                      |
| scimark_fft                | 445 ms                                                       | 458 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.73 ms: 1.03x slower                                                      |
| python_startup_no_site     | 8.60 ms                                                      | 8.86 ms: 1.03x slower                                                      |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                      |
| tomli_loads                | 2.57 sec                                                     | 2.66 sec: 1.03x slower                                                     |
| meteor_contest             | 113 ms                                                       | 117 ms: 1.03x slower                                                       |
| async_generators           | 488 ms                                                       | 505 ms: 1.04x slower                                                       |
| fannkuch                   | 451 ms                                                       | 469 ms: 1.04x slower                                                       |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                     |
| xml_etree_generate         | 114 ms                                                       | 119 ms: 1.05x slower                                                       |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.05x slower                                                      |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                       |
| telco                      | 10.0 ms                                                      | 10.6 ms: 1.06x slower                                                      |
| crypto_pyaes               | 82.0 ms                                                      | 87.4 ms: 1.07x slower                                                      |
| html5lib                   | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                      |
| deepcopy_reduce            | 4.04 us                                                      | 4.32 us: 1.07x slower                                                      |
| asyncio_tcp                | 584 ms                                                       | 626 ms: 1.07x slower                                                       |
| tornado_http               | 128 ms                                                       | 138 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 193 us                                                       | 211 us: 1.09x slower                                                       |
| raytrace                   | 297 ms                                                       | 325 ms: 1.09x slower                                                       |
| scimark_monte_carlo        | 82.3 ms                                                      | 90.6 ms: 1.10x slower                                                      |
| unpickle_pure_python       | 251 us                                                       | 278 us: 1.11x slower                                                       |
| scimark_sor                | 159 ms                                                       | 177 ms: 1.11x slower                                                       |
| pickle_pure_python         | 359 us                                                       | 399 us: 1.11x slower                                                       |
| go                         | 161 ms                                                       | 180 ms: 1.12x slower                                                       |
| pyflate                    | 557 ms                                                       | 631 ms: 1.13x slower                                                       |
| bench_mp_pool              | 7.03 ms                                                      | 7.98 ms: 1.13x slower                                                      |
| sqlglot_parse              | 1.42 ms                                                      | 1.62 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 129 ms                                                       | 147 ms: 1.14x slower                                                       |
| sqlglot_optimize           | 62.6 ms                                                      | 71.9 ms: 1.15x slower                                                      |
| deltablue                  | 3.88 ms                                                      | 4.46 ms: 1.15x slower                                                      |
| comprehensions             | 20.5 us                                                      | 23.7 us: 1.15x slower                                                      |
| pycparser                  | 1.22 sec                                                     | 1.41 sec: 1.16x slower                                                     |
| docutils                   | 3.10 sec                                                     | 3.67 sec: 1.19x slower                                                     |
| sqlglot_transpile          | 1.71 ms                                                      | 2.04 ms: 1.19x slower                                                      |
| django_template            | 42.3 ms                                                      | 50.6 ms: 1.20x slower                                                      |
| 2to3                       | 305 ms                                                       | 365 ms: 1.20x slower                                                       |
| nqueens                    | 98.9 ms                                                      | 119 ms: 1.20x slower                                                       |
| pprint_safe_repr           | 933 ms                                                       | 1.12 sec: 1.20x slower                                                     |
| pprint_pformat             | 1.93 sec                                                     | 2.33 sec: 1.21x slower                                                     |
| sympy_expand               | 457 ms                                                       | 580 ms: 1.27x slower                                                       |
| pylint                     | 337 ms                                                       | 430 ms: 1.28x slower                                                       |
| sympy_str                  | 265 ms                                                       | 341 ms: 1.28x slower                                                       |
| sympy_integrate            | 20.9 ms                                                      | 26.8 ms: 1.29x slower                                                      |
| hexiom                     | 7.08 ms                                                      | 9.11 ms: 1.29x slower                                                      |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                       |
| chaos                      | 68.3 ms                                                      | 89.1 ms: 1.31x slower                                                      |
| genshi_text                | 27.4 ms                                                      | 36.5 ms: 1.33x slower                                                      |
| sympy_sum                  | 144 ms                                                       | 197 ms: 1.37x slower                                                       |
| genshi_xml                 | 60.4 ms                                                      | 82.9 ms: 1.37x slower                                                      |
| regex_compile              | 128 ms                                                       | 181 ms: 1.41x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                               |

Benchmark hidden because not significant (13): xml_etree_parse, richards, nbody, float, richards_super, python_startup, regex_v8, pidigits, create_gc_cycles, coverage, asyncio_websockets, generators, logging_simple
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.08x