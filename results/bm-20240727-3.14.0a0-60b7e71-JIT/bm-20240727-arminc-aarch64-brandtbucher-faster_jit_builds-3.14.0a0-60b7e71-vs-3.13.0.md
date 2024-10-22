# Results vs. 3.13.0

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-aarch64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 365 ms: 1.19x slower                                                       |
| docutils       | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                                     |
| html5lib       | 64.3 ms                                                  | 70.5 ms: 1.10x slower                                                      |
| tornado_http   | 131 ms                                                   | 138 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                    | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 467 ms                                                   | 410 ms: 1.14x faster                                                       |
| async_tree_none            | 493 ms                                                   | 433 ms: 1.14x faster                                                       |
| async_tree_memoization     | 626 ms                                                   | 576 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 700 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 745 ms: 1.02x faster                                                       |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                       |
| coroutines                 | 28.2 ms                                                  | 28.4 ms: 1.01x slower                                                      |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                       |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                     |
| asyncio_tcp                | 568 ms                                                   | 626 ms: 1.10x slower                                                       |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                               |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 246 ms                                                   | 248 ms: 1.01x slower                                                       |
| regex_compile  | 128 ms                                                   | 181 ms: 1.41x slower                                                       |
| Geometric mean | (ref)                                                    | 1.09x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                   | 146 ms: 1.01x faster                                                       |
| json_loads           | 31.4 us                                                  | 32.6 us: 1.04x slower                                                      |
| tomli_loads          | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                     |
| xml_etree_generate   | 113 ms                                                   | 119 ms: 1.05x slower                                                       |
| unpickle_pure_python | 254 us                                                   | 278 us: 1.09x slower                                                       |
| pickle_pure_python   | 359 us                                                   | 399 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.04x slower                                                               |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                      |
| python_startup_no_site | 8.75 ms                                                  | 8.86 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.04x faster                                                      |
| django_template | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                      |
| genshi_text     | 27.7 ms                                                  | 36.5 ms: 1.32x slower                                                      |
| genshi_xml      | 60.2 ms                                                  | 82.9 ms: 1.38x slower                                                      |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.7 us: 1.32x faster                                                      |
| async_tree_memoization_tg  | 649 ms                                                   | 541 ms: 1.20x faster                                                       |
| deepcopy                   | 451 us                                                   | 381 us: 1.18x faster                                                       |
| async_tree_none_tg         | 467 ms                                                   | 410 ms: 1.14x faster                                                       |
| async_tree_none            | 493 ms                                                   | 433 ms: 1.14x faster                                                       |
| async_tree_memoization     | 626 ms                                                   | 576 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 700 ms: 1.05x faster                                                       |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.04x faster                                                      |
| float                      | 94.4 ms                                                  | 91.2 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 745 ms: 1.02x faster                                                       |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                      |
| pathlib                    | 22.4 ms                                                  | 22.0 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 147 ms                                                   | 146 ms: 1.01x faster                                                       |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                       |
| coroutines                 | 28.2 ms                                                  | 28.4 ms: 1.01x slower                                                      |
| regex_dna                  | 246 ms                                                   | 248 ms: 1.01x slower                                                       |
| spectral_norm              | 141 ms                                                   | 143 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.75 ms                                                  | 8.86 ms: 1.01x slower                                                      |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                       |
| scimark_fft                | 447 ms                                                   | 458 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.73 ms: 1.02x slower                                                      |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                     |
| richards_super             | 60.3 ms                                                  | 62.2 ms: 1.03x slower                                                      |
| richards                   | 53.5 ms                                                  | 55.2 ms: 1.03x slower                                                      |
| meteor_contest             | 113 ms                                                   | 117 ms: 1.03x slower                                                       |
| json                       | 5.61 ms                                                  | 5.81 ms: 1.04x slower                                                      |
| json_loads                 | 31.4 us                                                  | 32.6 us: 1.04x slower                                                      |
| fannkuch                   | 452 ms                                                   | 469 ms: 1.04x slower                                                       |
| mdp                        | 3.36 sec                                                 | 3.49 sec: 1.04x slower                                                     |
| bench_thread_pool          | 1.28 ms                                                  | 1.33 ms: 1.04x slower                                                      |
| thrift                     | 946 us                                                   | 983 us: 1.04x slower                                                       |
| logging_simple             | 7.04 us                                                  | 7.32 us: 1.04x slower                                                      |
| tomli_loads                | 2.53 sec                                                 | 2.66 sec: 1.05x slower                                                     |
| tornado_http               | 131 ms                                                   | 138 ms: 1.05x slower                                                       |
| xml_etree_generate         | 113 ms                                                   | 119 ms: 1.05x slower                                                       |
| crypto_pyaes               | 82.7 ms                                                  | 87.4 ms: 1.06x slower                                                      |
| deepcopy_reduce            | 4.07 us                                                  | 4.32 us: 1.06x slower                                                      |
| scimark_monte_carlo        | 83.8 ms                                                  | 90.6 ms: 1.08x slower                                                      |
| gc_traversal               | 4.53 ms                                                  | 4.91 ms: 1.08x slower                                                      |
| telco                      | 9.73 ms                                                  | 10.6 ms: 1.09x slower                                                      |
| raytrace                   | 298 ms                                                   | 325 ms: 1.09x slower                                                       |
| bench_mp_pool              | 7.30 ms                                                  | 7.98 ms: 1.09x slower                                                      |
| unpickle_pure_python       | 254 us                                                   | 278 us: 1.09x slower                                                       |
| html5lib                   | 64.3 ms                                                  | 70.5 ms: 1.10x slower                                                      |
| create_gc_cycles           | 2.12 ms                                                  | 2.34 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 192 us                                                   | 211 us: 1.10x slower                                                       |
| asyncio_tcp                | 568 ms                                                   | 626 ms: 1.10x slower                                                       |
| go                         | 163 ms                                                   | 180 ms: 1.11x slower                                                       |
| pickle_pure_python         | 359 us                                                   | 399 us: 1.11x slower                                                       |
| scimark_sor                | 159 ms                                                   | 177 ms: 1.12x slower                                                       |
| dask                       | 350 ms                                                   | 392 ms: 1.12x slower                                                       |
| pycparser                  | 1.26 sec                                                 | 1.41 sec: 1.12x slower                                                     |
| pyflate                    | 556 ms                                                   | 631 ms: 1.14x slower                                                       |
| sqlglot_normalize          | 128 ms                                                   | 147 ms: 1.15x slower                                                       |
| sqlglot_optimize           | 62.4 ms                                                  | 71.9 ms: 1.15x slower                                                      |
| deltablue                  | 3.85 ms                                                  | 4.46 ms: 1.16x slower                                                      |
| comprehensions             | 20.4 us                                                  | 23.7 us: 1.16x slower                                                      |
| sqlglot_parse              | 1.38 ms                                                  | 1.62 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 1.73 ms                                                  | 2.04 ms: 1.18x slower                                                      |
| 2to3                       | 306 ms                                                   | 365 ms: 1.19x slower                                                       |
| django_template            | 42.3 ms                                                  | 50.6 ms: 1.20x slower                                                      |
| nqueens                    | 98.7 ms                                                  | 119 ms: 1.20x slower                                                       |
| pprint_safe_repr           | 926 ms                                                   | 1.12 sec: 1.21x slower                                                     |
| pprint_pformat             | 1.90 sec                                                 | 2.33 sec: 1.23x slower                                                     |
| pylint                     | 343 ms                                                   | 430 ms: 1.25x slower                                                       |
| docutils                   | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                                     |
| sympy_expand               | 455 ms                                                   | 580 ms: 1.28x slower                                                       |
| hexiom                     | 7.13 ms                                                  | 9.11 ms: 1.28x slower                                                      |
| sympy_integrate            | 21.0 ms                                                  | 26.8 ms: 1.28x slower                                                      |
| sympy_str                  | 264 ms                                                   | 341 ms: 1.29x slower                                                       |
| chaos                      | 68.8 ms                                                  | 89.1 ms: 1.30x slower                                                      |
| genshi_text                | 27.7 ms                                                  | 36.5 ms: 1.32x slower                                                      |
| scimark_lu                 | 139 ms                                                   | 184 ms: 1.32x slower                                                       |
| sympy_sum                  | 143 ms                                                   | 197 ms: 1.37x slower                                                       |
| genshi_xml                 | 60.2 ms                                                  | 82.9 ms: 1.38x slower                                                      |
| regex_compile              | 128 ms                                                   | 181 ms: 1.41x slower                                                       |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                               |

Benchmark hidden because not significant (14): regex_v8, nbody, generators, xml_etree_process, pidigits, coverage, bpe_tokeniser, xml_etree_parse, json_dumps, logging_silent, regex_effbot, async_tree_io_tg, logging_format, async_tree_io
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x