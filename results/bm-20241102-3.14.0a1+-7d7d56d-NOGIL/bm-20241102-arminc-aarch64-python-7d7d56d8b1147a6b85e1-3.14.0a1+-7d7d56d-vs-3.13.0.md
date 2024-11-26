# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: linux-aarch64
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.374x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.38x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 532 ms: 1.75x slower                                                     |
| docutils       | 2.89 sec                                                 | 4.17 sec: 1.44x slower                                                   |
| html5lib       | 66.4 ms                                                  | 120 ms: 1.80x slower                                                     |
| sphinx         | 1.17 sec                                                 | 1.69 sec: 1.45x slower                                                   |
| tornado_http   | 128 ms                                                   | 196 ms: 1.53x slower                                                     |
| Geometric mean | (ref)                                                    | 1.59x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 693 ms: 1.05x slower                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 755 ms: 1.16x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 917 ms: 1.19x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 780 ms: 1.20x slower                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 950 ms: 1.24x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.42 sec: 1.25x slower                                                   |
| async_tree_none            | 497 ms                                                   | 636 ms: 1.28x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 609 ms: 1.30x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.46 sec: 1.32x slower                                                   |
| async_generators           | 489 ms                                                   | 684 ms: 1.40x slower                                                     |
| coroutines                 | 28.5 ms                                                  | 40.3 ms: 1.41x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.25x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 234 ms                                                   | 242 ms: 1.04x slower                                                     |
| float          | 93.3 ms                                                  | 213 ms: 2.28x slower                                                     |
| nbody          | 114 ms                                                   | 295 ms: 2.58x slower                                                     |
| Geometric mean | (ref)                                                    | 1.83x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.63 ms: 1.06x faster                                                    |
| regex_dna      | 253 ms                                                   | 268 ms: 1.06x slower                                                     |
| regex_v8       | 31.8 ms                                                  | 34.2 ms: 1.08x slower                                                    |
| regex_compile  | 127 ms                                                   | 260 ms: 2.04x slower                                                     |
| Geometric mean | (ref)                                                    | 1.22x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 149 ms                                                   | 157 ms: 1.05x slower                                                     |
| json_loads           | 31.7 us                                                  | 39.1 us: 1.23x slower                                                    |
| json_dumps           | 13.6 ms                                                  | 20.0 ms: 1.47x slower                                                    |
| xml_etree_generate   | 113 ms                                                   | 170 ms: 1.50x slower                                                     |
| xml_etree_process    | 80.5 ms                                                  | 135 ms: 1.67x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 4.33 sec: 1.70x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 566 us: 2.26x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 828 us: 2.32x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.51x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 20.8 ms: 1.35x slower                                                    |
| python_startup_no_site | 8.73 ms                                                  | 12.3 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 109 ms: 1.81x slower                                                     |
| genshi_text     | 27.7 ms                                                  | 54.0 ms: 1.95x slower                                                    |
| django_template | 41.6 ms                                                  | 85.1 ms: 2.04x slower                                                    |
| mako            | 13.4 ms                                                  | 29.7 ms: 2.22x slower                                                    |
| Geometric mean  | (ref)                                                    | 2.00x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.77 ms                                                  | 4.59 ms: 1.26x faster                                                    |
| create_gc_cycles           | 3.35 ms                                                  | 2.71 ms: 1.24x faster                                                    |
| regex_effbot               | 4.89 ms                                                  | 4.63 ms: 1.06x faster                                                    |
| pidigits                   | 234 ms                                                   | 242 ms: 1.04x slower                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 157 ms: 1.05x slower                                                     |
| asyncio_websockets         | 659 ms                                                   | 693 ms: 1.05x slower                                                     |
| regex_dna                  | 253 ms                                                   | 268 ms: 1.06x slower                                                     |
| regex_v8                   | 31.8 ms                                                  | 34.2 ms: 1.08x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 755 ms: 1.16x slower                                                     |
| k_core                     | 2.96 sec                                                 | 3.52 sec: 1.19x slower                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 917 ms: 1.19x slower                                                     |
| json                       | 5.73 ms                                                  | 6.87 ms: 1.20x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 780 ms: 1.20x slower                                                     |
| deepcopy                   | 447 us                                                   | 551 us: 1.23x slower                                                     |
| json_loads                 | 31.7 us                                                  | 39.1 us: 1.23x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 950 ms: 1.24x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.42 sec: 1.25x slower                                                   |
| pathlib                    | 22.7 ms                                                  | 29.0 ms: 1.28x slower                                                    |
| async_tree_none            | 497 ms                                                   | 636 ms: 1.28x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 609 ms: 1.30x slower                                                     |
| shortest_path              | 565 ms                                                   | 736 ms: 1.30x slower                                                     |
| connected_components       | 533 ms                                                   | 701 ms: 1.32x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.46 sec: 1.32x slower                                                   |
| scimark_fft                | 447 ms                                                   | 593 ms: 1.33x slower                                                     |
| telco                      | 9.74 ms                                                  | 13.0 ms: 1.34x slower                                                    |
| mdp                        | 3.34 sec                                                 | 4.48 sec: 1.34x slower                                                   |
| python_startup             | 15.4 ms                                                  | 20.8 ms: 1.35x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.97 ms: 1.38x slower                                                    |
| async_generators           | 489 ms                                                   | 684 ms: 1.40x slower                                                     |
| python_startup_no_site     | 8.73 ms                                                  | 12.3 ms: 1.41x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 40.3 ms: 1.41x slower                                                    |
| coverage                   | 99.1 ms                                                  | 142 ms: 1.44x slower                                                     |
| docutils                   | 2.89 sec                                                 | 4.17 sec: 1.44x slower                                                   |
| sphinx                     | 1.17 sec                                                 | 1.69 sec: 1.45x slower                                                   |
| json_dumps                 | 13.6 ms                                                  | 20.0 ms: 1.47x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.10 us: 1.50x slower                                                    |
| xml_etree_generate         | 113 ms                                                   | 170 ms: 1.50x slower                                                     |
| meteor_contest             | 114 ms                                                   | 172 ms: 1.51x slower                                                     |
| deepcopy_memo              | 50.4 us                                                  | 76.2 us: 1.51x slower                                                    |
| pylint                     | 342 ms                                                   | 522 ms: 1.53x slower                                                     |
| tornado_http               | 128 ms                                                   | 196 ms: 1.53x slower                                                     |
| nqueens                    | 100 ms                                                   | 157 ms: 1.56x slower                                                     |
| bench_thread_pool          | 1.27 ms                                                  | 2.03 ms: 1.59x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 9.40 sec: 1.60x slower                                                   |
| spectral_norm              | 143 ms                                                   | 231 ms: 1.62x slower                                                     |
| generators                 | 37.6 ms                                                  | 61.5 ms: 1.64x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 135 ms: 1.67x slower                                                     |
| pycparser                  | 1.27 sec                                                 | 2.14 sec: 1.68x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 4.33 sec: 1.70x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 145 ms: 1.73x slower                                                     |
| fannkuch                   | 461 ms                                                   | 797 ms: 1.73x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 36.3 ms: 1.74x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 338 us: 1.75x slower                                                     |
| 2to3                       | 304 ms                                                   | 532 ms: 1.75x slower                                                     |
| sqlalchemy_declarative     | 150 ms                                                   | 271 ms: 1.80x slower                                                     |
| html5lib                   | 66.4 ms                                                  | 120 ms: 1.80x slower                                                     |
| genshi_xml                 | 60.3 ms                                                  | 109 ms: 1.81x slower                                                     |
| sqlglot_normalize          | 127 ms                                                   | 234 ms: 1.84x slower                                                     |
| thrift                     | 968 us                                                   | 1.79 ms: 1.85x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.04 sec: 1.87x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.61 sec: 1.90x slower                                                   |
| sqlglot_optimize           | 62.2 ms                                                  | 118 ms: 1.90x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.77 sec: 1.91x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 54.0 ms: 1.95x slower                                                    |
| sqlalchemy_imperative      | 15.1 ms                                                  | 30.0 ms: 1.98x slower                                                    |
| sympy_str                  | 264 ms                                                   | 530 ms: 2.00x slower                                                     |
| regex_compile              | 127 ms                                                   | 260 ms: 2.04x slower                                                     |
| django_template            | 41.6 ms                                                  | 85.1 ms: 2.04x slower                                                    |
| logging_simple             | 7.07 us                                                  | 14.5 us: 2.05x slower                                                    |
| logging_format             | 7.82 us                                                  | 16.3 us: 2.09x slower                                                    |
| comprehensions             | 20.4 us                                                  | 42.9 us: 2.11x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 177 ms: 2.12x slower                                                     |
| sympy_expand               | 457 ms                                                   | 980 ms: 2.15x slower                                                     |
| logging_silent             | 133 ns                                                   | 290 ns: 2.18x slower                                                     |
| mako                       | 13.4 ms                                                  | 29.7 ms: 2.22x slower                                                    |
| scimark_sor                | 160 ms                                                   | 359 ms: 2.25x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 566 us: 2.26x slower                                                     |
| hexiom                     | 7.11 ms                                                  | 16.1 ms: 2.27x slower                                                    |
| float                      | 93.3 ms                                                  | 213 ms: 2.28x slower                                                     |
| sympy_sum                  | 144 ms                                                   | 329 ms: 2.29x slower                                                     |
| richards                   | 53.6 ms                                                  | 124 ms: 2.31x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 828 us: 2.32x slower                                                     |
| richards_super             | 60.1 ms                                                  | 139 ms: 2.32x slower                                                     |
| chaos                      | 68.0 ms                                                  | 161 ms: 2.37x slower                                                     |
| scimark_lu                 | 139 ms                                                   | 347 ms: 2.49x slower                                                     |
| go                         | 160 ms                                                   | 407 ms: 2.55x slower                                                     |
| nbody                      | 114 ms                                                   | 295 ms: 2.58x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 4.51 ms: 2.61x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.80 ms: 2.76x slower                                                    |
| raytrace                   | 300 ms                                                   | 891 ms: 2.97x slower                                                     |
| deltablue                  | 3.82 ms                                                  | 12.8 ms: 3.35x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 63.9 ms: 8.31x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.66x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2
Ignored benchmarks (2) of results/bm-20241102-3.14.0a1+-7d7d56d-NOGIL/bm-20241102-arminc-aarch64-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: dulwich_log, sqlite_synth

- Geometric mean (including insignificant results): 1.374x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.38x

# Memory
- memory change: 1.18x