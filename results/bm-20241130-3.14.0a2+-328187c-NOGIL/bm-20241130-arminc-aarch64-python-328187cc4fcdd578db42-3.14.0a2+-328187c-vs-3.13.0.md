# Results vs. 3.13.0

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-aarch64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.332x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 494 ms: 1.63x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                   |
| html5lib       | 66.4 ms                                                  | 117 ms: 1.76x slower                                                     |
| sphinx         | 1.17 sec                                                 | 1.58 sec: 1.35x slower                                                   |
| Geometric mean | (ref)                                                    | 1.52x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 684 ms: 1.04x slower                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 738 ms: 1.14x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 759 ms: 1.17x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 915 ms: 1.19x slower                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 928 ms: 1.21x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.38 sec: 1.22x slower                                                   |
| async_tree_none            | 497 ms                                                   | 618 ms: 1.24x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                   |
| async_tree_none_tg         | 470 ms                                                   | 603 ms: 1.28x slower                                                     |
| async_generators           | 489 ms                                                   | 670 ms: 1.37x slower                                                     |
| coroutines                 | 28.5 ms                                                  | 39.3 ms: 1.38x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.22x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 199 ms: 1.74x slower                                                     |
| float          | 93.3 ms                                                  | 203 ms: 2.18x slower                                                     |
| Geometric mean | (ref)                                                    | 1.56x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.20 ms: 1.16x faster                                                    |
| regex_dna      | 253 ms                                                   | 266 ms: 1.05x slower                                                     |
| regex_v8       | 31.8 ms                                                  | 33.6 ms: 1.06x slower                                                    |
| regex_compile  | 127 ms                                                   | 224 ms: 1.76x slower                                                     |
| Geometric mean | (ref)                                                    | 1.14x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 182 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 140 ms: 1.06x faster                                                     |
| json_loads           | 31.7 us                                                  | 37.9 us: 1.20x slower                                                    |
| xml_etree_generate   | 113 ms                                                   | 150 ms: 1.33x slower                                                     |
| json_dumps           | 13.6 ms                                                  | 19.3 ms: 1.42x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 121 ms: 1.51x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 3.99 sec: 1.57x slower                                                   |
| pickle_pure_python   | 357 us                                                   | 735 us: 2.06x slower                                                     |
| unpickle_pure_python | 251 us                                                   | 518 us: 2.07x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.39x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 21.4 ms: 1.39x slower                                                    |
| python_startup_no_site | 8.73 ms                                                  | 12.7 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.43x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 89.7 ms: 1.49x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 45.8 ms: 1.65x slower                                                    |
| django_template | 41.6 ms                                                  | 73.6 ms: 1.77x slower                                                    |
| mako            | 13.4 ms                                                  | 28.6 ms: 2.14x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.75x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 4.89 ms                                                  | 4.20 ms: 1.16x faster                                                    |
| create_gc_cycles           | 3.35 ms                                                  | 2.94 ms: 1.14x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.10 ms: 1.13x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 182 ms: 1.08x faster                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 140 ms: 1.06x faster                                                     |
| asyncio_websockets         | 659 ms                                                   | 684 ms: 1.04x slower                                                     |
| regex_dna                  | 253 ms                                                   | 266 ms: 1.05x slower                                                     |
| regex_v8                   | 31.8 ms                                                  | 33.6 ms: 1.06x slower                                                    |
| deepcopy                   | 447 us                                                   | 482 us: 1.08x slower                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 738 ms: 1.14x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 759 ms: 1.17x slower                                                     |
| k_core                     | 2.96 sec                                                 | 3.46 sec: 1.17x slower                                                   |
| pathlib                    | 22.7 ms                                                  | 26.6 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 915 ms: 1.19x slower                                                     |
| scimark_fft                | 447 ms                                                   | 533 ms: 1.19x slower                                                     |
| json_loads                 | 31.7 us                                                  | 37.9 us: 1.20x slower                                                    |
| json                       | 5.73 ms                                                  | 6.87 ms: 1.20x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 928 ms: 1.21x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.38 sec: 1.22x slower                                                   |
| async_tree_none            | 497 ms                                                   | 618 ms: 1.24x slower                                                     |
| deepcopy_memo              | 50.4 us                                                  | 62.9 us: 1.25x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                   |
| spectral_norm              | 143 ms                                                   | 181 ms: 1.27x slower                                                     |
| mdp                        | 3.34 sec                                                 | 4.26 sec: 1.28x slower                                                   |
| async_tree_none_tg         | 470 ms                                                   | 603 ms: 1.28x slower                                                     |
| shortest_path              | 565 ms                                                   | 741 ms: 1.31x slower                                                     |
| connected_components       | 533 ms                                                   | 700 ms: 1.31x slower                                                     |
| xml_etree_generate         | 113 ms                                                   | 150 ms: 1.33x slower                                                     |
| telco                      | 9.74 ms                                                  | 13.0 ms: 1.33x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.81 ms: 1.35x slower                                                    |
| sphinx                     | 1.17 sec                                                 | 1.58 sec: 1.35x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.53 us: 1.36x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                   |
| async_generators           | 489 ms                                                   | 670 ms: 1.37x slower                                                     |
| coroutines                 | 28.5 ms                                                  | 39.3 ms: 1.38x slower                                                    |
| python_startup             | 15.4 ms                                                  | 21.4 ms: 1.39x slower                                                    |
| meteor_contest             | 114 ms                                                   | 161 ms: 1.42x slower                                                     |
| json_dumps                 | 13.6 ms                                                  | 19.3 ms: 1.42x slower                                                    |
| pylint                     | 342 ms                                                   | 495 ms: 1.45x slower                                                     |
| coverage                   | 99.1 ms                                                  | 145 ms: 1.46x slower                                                     |
| python_startup_no_site     | 8.73 ms                                                  | 12.7 ms: 1.46x slower                                                    |
| nqueens                    | 100 ms                                                   | 148 ms: 1.48x slower                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 8.72 sec: 1.48x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 89.7 ms: 1.49x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 121 ms: 1.51x slower                                                     |
| typing_runtime_protocols   | 193 us                                                   | 296 us: 1.53x slower                                                     |
| sqlglot_optimize           | 62.2 ms                                                  | 97.1 ms: 1.56x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 2.00 sec: 1.57x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 3.99 sec: 1.57x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 2.01 ms: 1.57x slower                                                    |
| generators                 | 37.6 ms                                                  | 59.5 ms: 1.58x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 202 ms: 1.59x slower                                                     |
| crypto_pyaes               | 83.7 ms                                                  | 134 ms: 1.61x slower                                                     |
| fannkuch                   | 461 ms                                                   | 746 ms: 1.62x slower                                                     |
| 2to3                       | 304 ms                                                   | 494 ms: 1.63x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.51 sec: 1.63x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.10 sec: 1.63x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 45.8 ms: 1.65x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 35.1 ms: 1.69x slower                                                    |
| sqlalchemy_declarative     | 150 ms                                                   | 259 ms: 1.72x slower                                                     |
| nbody                      | 114 ms                                                   | 199 ms: 1.74x slower                                                     |
| thrift                     | 968 us                                                   | 1.70 ms: 1.75x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 117 ms: 1.76x slower                                                     |
| regex_compile              | 127 ms                                                   | 224 ms: 1.76x slower                                                     |
| django_template            | 41.6 ms                                                  | 73.6 ms: 1.77x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.01 sec: 1.81x slower                                                   |
| sympy_str                  | 264 ms                                                   | 486 ms: 1.84x slower                                                     |
| sqlalchemy_imperative      | 15.1 ms                                                  | 28.6 ms: 1.89x slower                                                    |
| logging_simple             | 7.07 us                                                  | 13.6 us: 1.92x slower                                                    |
| logging_format             | 7.82 us                                                  | 15.3 us: 1.95x slower                                                    |
| sympy_expand               | 457 ms                                                   | 895 ms: 1.96x slower                                                     |
| scimark_sor                | 160 ms                                                   | 316 ms: 1.98x slower                                                     |
| comprehensions             | 20.4 us                                                  | 41.3 us: 2.03x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 292 ms: 2.03x slower                                                     |
| scimark_monte_carlo        | 83.6 ms                                                  | 170 ms: 2.04x slower                                                     |
| scimark_lu                 | 139 ms                                                   | 287 ms: 2.06x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 735 us: 2.06x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 518 us: 2.07x slower                                                     |
| hexiom                     | 7.11 ms                                                  | 14.7 ms: 2.07x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.6 ms: 2.14x slower                                                    |
| float                      | 93.3 ms                                                  | 203 ms: 2.18x slower                                                     |
| logging_silent             | 133 ns                                                   | 293 ns: 2.20x slower                                                     |
| richards                   | 53.6 ms                                                  | 119 ms: 2.22x slower                                                     |
| richards_super             | 60.1 ms                                                  | 136 ms: 2.27x slower                                                     |
| chaos                      | 68.0 ms                                                  | 158 ms: 2.32x slower                                                     |
| go                         | 160 ms                                                   | 387 ms: 2.42x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 4.20 ms: 2.42x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.52 ms: 2.56x slower                                                    |
| raytrace                   | 300 ms                                                   | 811 ms: 2.71x slower                                                     |
| deltablue                  | 3.82 ms                                                  | 12.3 ms: 3.23x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 65.5 ms: 8.52x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.56x slower                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241130-3.14.0a2+-328187c-NOGIL/bm-20241130-arminc-aarch64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json: dulwich_log, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.332x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.36x
- 95% likely to have a slowdown of 1.34x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.21x