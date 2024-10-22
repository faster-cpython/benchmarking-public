# Results vs. 3.13.0

- fork: colesbury
- ref: gh_117376_pydecref_m
- machine: linux-aarch64
- commit hash: 4b27f3a
- commit date: 2024-08-13
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 513 ms: 1.68x slower                                                       |
| docutils       | 2.91 sec                                                 | 4.09 sec: 1.41x slower                                                     |
| html5lib       | 64.3 ms                                                  | 120 ms: 1.87x slower                                                       |
| tornado_http   | 131 ms                                                   | 206 ms: 1.57x slower                                                       |
| Geometric mean | (ref)                                                    | 1.62x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 668 ms: 1.02x slower                                                       |
| async_tree_memoization_tg  | 649 ms                                                   | 683 ms: 1.05x slower                                                       |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.43 sec: 1.12x slower                                                     |
| asyncio_tcp                | 568 ms                                                   | 661 ms: 1.16x slower                                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 867 ms: 1.18x slower                                                       |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                       |
| async_tree_none_tg         | 467 ms                                                   | 557 ms: 1.19x slower                                                       |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 914 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.23x slower                                                     |
| async_tree_none            | 493 ms                                                   | 607 ms: 1.23x slower                                                       |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.26x slower                                                     |
| async_generators           | 496 ms                                                   | 668 ms: 1.35x slower                                                       |
| coroutines                 | 28.2 ms                                                  | 39.1 ms: 1.39x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 208 ms: 2.20x slower                                                       |
| nbody          | 114 ms                                                   | 281 ms: 2.46x slower                                                       |
| Geometric mean | (ref)                                                    | 1.76x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.51 ms: 1.08x faster                                                      |
| regex_dna      | 246 ms                                                   | 259 ms: 1.05x slower                                                       |
| regex_v8       | 31.5 ms                                                  | 33.4 ms: 1.06x slower                                                      |
| regex_compile  | 128 ms                                                   | 254 ms: 1.97x slower                                                       |
| Geometric mean | (ref)                                                    | 1.19x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 183 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 147 ms                                                   | 158 ms: 1.08x slower                                                       |
| json_loads           | 31.4 us                                                  | 39.1 us: 1.24x slower                                                      |
| json_dumps           | 13.4 ms                                                  | 17.8 ms: 1.33x slower                                                      |
| xml_etree_generate   | 113 ms                                                   | 161 ms: 1.43x slower                                                       |
| xml_etree_process    | 80.1 ms                                                  | 131 ms: 1.64x slower                                                       |
| tomli_loads          | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                     |
| unpickle_pure_python | 254 us                                                   | 541 us: 2.13x slower                                                       |
| pickle_pure_python   | 359 us                                                   | 783 us: 2.18x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.47x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 17.8 ms: 1.34x slower                                                      |
| python_startup_no_site | 8.75 ms                                                  | 11.9 ms: 1.36x slower                                                      |
| Geometric mean         | (ref)                                                    | 1.35x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 104 ms: 1.73x slower                                                       |
| django_template | 42.3 ms                                                  | 82.2 ms: 1.94x slower                                                      |
| genshi_text     | 27.7 ms                                                  | 53.9 ms: 1.95x slower                                                      |
| mako            | 13.3 ms                                                  | 29.0 ms: 2.18x slower                                                      |
| Geometric mean  | (ref)                                                    | 1.94x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-colesbury-gh_117376_pydecref_m-3.14.0a0-4b27f3a |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.61 ms: 1.32x faster                                                      |
| gc_traversal               | 4.53 ms                                                  | 3.44 ms: 1.32x faster                                                      |
| regex_effbot               | 4.87 ms                                                  | 4.51 ms: 1.08x faster                                                      |
| bench_mp_pool              | 7.30 ms                                                  | 6.91 ms: 1.06x faster                                                      |
| xml_etree_parse            | 188 ms                                                   | 183 ms: 1.03x faster                                                       |
| asyncio_websockets         | 656 ms                                                   | 668 ms: 1.02x slower                                                       |
| regex_dna                  | 246 ms                                                   | 259 ms: 1.05x slower                                                       |
| async_tree_memoization_tg  | 649 ms                                                   | 683 ms: 1.05x slower                                                       |
| regex_v8                   | 31.5 ms                                                  | 33.4 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 147 ms                                                   | 158 ms: 1.08x slower                                                       |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.43 sec: 1.12x slower                                                     |
| asyncio_tcp                | 568 ms                                                   | 661 ms: 1.16x slower                                                       |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 867 ms: 1.18x slower                                                       |
| pathlib                    | 22.4 ms                                                  | 26.4 ms: 1.18x slower                                                      |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                       |
| async_tree_none_tg         | 467 ms                                                   | 557 ms: 1.19x slower                                                       |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 914 ms: 1.20x slower                                                       |
| async_tree_io_tg           | 1.09 sec                                                 | 1.34 sec: 1.23x slower                                                     |
| async_tree_none            | 493 ms                                                   | 607 ms: 1.23x slower                                                       |
| deepcopy                   | 451 us                                                   | 560 us: 1.24x slower                                                       |
| json_loads                 | 31.4 us                                                  | 39.1 us: 1.24x slower                                                      |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.26x slower                                                     |
| json                       | 5.61 ms                                                  | 7.09 ms: 1.26x slower                                                      |
| scimark_fft                | 447 ms                                                   | 572 ms: 1.28x slower                                                       |
| mdp                        | 3.36 sec                                                 | 4.32 sec: 1.29x slower                                                     |
| telco                      | 9.73 ms                                                  | 12.8 ms: 1.31x slower                                                      |
| json_dumps                 | 13.4 ms                                                  | 17.8 ms: 1.33x slower                                                      |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.79 ms: 1.34x slower                                                      |
| python_startup             | 13.3 ms                                                  | 17.8 ms: 1.34x slower                                                      |
| coverage                   | 98.5 ms                                                  | 132 ms: 1.34x slower                                                       |
| async_generators           | 496 ms                                                   | 668 ms: 1.35x slower                                                       |
| python_startup_no_site     | 8.75 ms                                                  | 11.9 ms: 1.36x slower                                                      |
| coroutines                 | 28.2 ms                                                  | 39.1 ms: 1.39x slower                                                      |
| docutils                   | 2.91 sec                                                 | 4.09 sec: 1.41x slower                                                     |
| deepcopy_memo              | 51.0 us                                                  | 72.5 us: 1.42x slower                                                      |
| xml_etree_generate         | 113 ms                                                   | 161 ms: 1.43x slower                                                       |
| deepcopy_reduce            | 4.07 us                                                  | 6.00 us: 1.48x slower                                                      |
| pylint                     | 343 ms                                                   | 507 ms: 1.48x slower                                                       |
| meteor_contest             | 113 ms                                                   | 169 ms: 1.49x slower                                                       |
| generators                 | 37.8 ms                                                  | 56.6 ms: 1.50x slower                                                      |
| nqueens                    | 98.7 ms                                                  | 151 ms: 1.53x slower                                                       |
| tornado_http               | 131 ms                                                   | 206 ms: 1.57x slower                                                       |
| spectral_norm              | 141 ms                                                   | 227 ms: 1.61x slower                                                       |
| bpe_tokeniser              | 5.90 sec                                                 | 9.51 sec: 1.61x slower                                                     |
| pycparser                  | 1.26 sec                                                 | 2.06 sec: 1.63x slower                                                     |
| fannkuch                   | 452 ms                                                   | 738 ms: 1.63x slower                                                       |
| xml_etree_process          | 80.1 ms                                                  | 131 ms: 1.64x slower                                                       |
| crypto_pyaes               | 82.7 ms                                                  | 136 ms: 1.65x slower                                                       |
| bench_thread_pool          | 1.28 ms                                                  | 2.11 ms: 1.65x slower                                                      |
| sympy_integrate            | 21.0 ms                                                  | 34.8 ms: 1.66x slower                                                      |
| tomli_loads                | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                     |
| 2to3                       | 306 ms                                                   | 513 ms: 1.68x slower                                                       |
| genshi_xml                 | 60.2 ms                                                  | 104 ms: 1.73x slower                                                       |
| sqlglot_normalize          | 128 ms                                                   | 230 ms: 1.80x slower                                                       |
| thrift                     | 946 us                                                   | 1.70 ms: 1.80x slower                                                      |
| typing_runtime_protocols   | 192 us                                                   | 347 us: 1.81x slower                                                       |
| pyflate                    | 556 ms                                                   | 1.01 sec: 1.81x slower                                                     |
| sqlglot_optimize           | 62.4 ms                                                  | 116 ms: 1.86x slower                                                       |
| html5lib                   | 64.3 ms                                                  | 120 ms: 1.87x slower                                                       |
| pprint_safe_repr           | 926 ms                                                   | 1.75 sec: 1.89x slower                                                     |
| pprint_pformat             | 1.90 sec                                                 | 3.61 sec: 1.90x slower                                                     |
| django_template            | 42.3 ms                                                  | 82.2 ms: 1.94x slower                                                      |
| genshi_text                | 27.7 ms                                                  | 53.9 ms: 1.95x slower                                                      |
| sympy_str                  | 264 ms                                                   | 516 ms: 1.96x slower                                                       |
| regex_compile              | 128 ms                                                   | 254 ms: 1.97x slower                                                       |
| logging_format             | 7.83 us                                                  | 15.6 us: 1.99x slower                                                      |
| comprehensions             | 20.4 us                                                  | 41.0 us: 2.01x slower                                                      |
| logging_simple             | 7.04 us                                                  | 14.4 us: 2.04x slower                                                      |
| logging_silent             | 135 ns                                                   | 279 ns: 2.06x slower                                                       |
| scimark_monte_carlo        | 83.8 ms                                                  | 173 ms: 2.06x slower                                                       |
| sympy_expand               | 455 ms                                                   | 952 ms: 2.09x slower                                                       |
| scimark_sor                | 159 ms                                                   | 336 ms: 2.12x slower                                                       |
| unpickle_pure_python       | 254 us                                                   | 541 us: 2.13x slower                                                       |
| richards                   | 53.5 ms                                                  | 116 ms: 2.16x slower                                                       |
| mako                       | 13.3 ms                                                  | 29.0 ms: 2.18x slower                                                      |
| pickle_pure_python         | 359 us                                                   | 783 us: 2.18x slower                                                       |
| hexiom                     | 7.13 ms                                                  | 15.6 ms: 2.19x slower                                                      |
| float                      | 94.4 ms                                                  | 208 ms: 2.20x slower                                                       |
| sympy_sum                  | 143 ms                                                   | 316 ms: 2.20x slower                                                       |
| chaos                      | 68.8 ms                                                  | 158 ms: 2.29x slower                                                       |
| richards_super             | 60.3 ms                                                  | 140 ms: 2.32x slower                                                       |
| nbody                      | 114 ms                                                   | 281 ms: 2.46x slower                                                       |
| sqlglot_transpile          | 1.73 ms                                                  | 4.30 ms: 2.48x slower                                                      |
| scimark_lu                 | 139 ms                                                   | 353 ms: 2.53x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                  | 3.59 ms: 2.60x slower                                                      |
| raytrace                   | 298 ms                                                   | 803 ms: 2.69x slower                                                       |
| go                         | 163 ms                                                   | 442 ms: 2.72x slower                                                       |
| deltablue                  | 3.85 ms                                                  | 12.5 ms: 3.26x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.58x slower                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.39x

# Memory
- memory change: 1.16x