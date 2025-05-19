# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.064x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 352 ms: 1.13x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                  |
| html5lib       | 65.6 ms                                                  | 68.6 ms: 1.05x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.30 sec: 1.08x slower                                                  |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 452 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 841 ms: 1.38x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 482 ms: 1.38x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 638 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 684 ms: 1.15x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 231 ms: 1.03x faster                                                    |
| nbody          | 118 ms                                                   | 170 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.96 ms: 1.29x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                   |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| regex_compile  | 134 ms                                                   | 151 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 128 ms: 1.24x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.84 sec: 1.06x slower                                                  |
| unpickle_pure_python | 265 us                                                   | 302 us: 1.14x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 428 us: 1.15x slower                                                    |
| json_loads           | 32.8 us                                                  | 39.0 us: 1.19x slower                                                   |
| xml_etree_generate   | 118 ms                                                   | 142 ms: 1.20x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 72.1 ms: 1.17x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 35.0 ms: 1.23x slower                                                   |
| django_template | 39.4 ms                                                  | 50.6 ms: 1.29x slower                                                   |
| mako            | 14.0 ms                                                  | 21.3 ms: 1.53x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.30x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.88 ms: 2.06x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.97 sec: 1.75x faster                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 2.30 ms: 1.47x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 452 ms: 1.46x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 841 ms: 1.38x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 482 ms: 1.38x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 372 ms: 1.30x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.96 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 638 ms: 1.26x faster                                                    |
| deepcopy                   | 479 us                                                   | 386 us: 1.24x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 128 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 409 ms: 1.23x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.5 ms: 1.18x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.46 us: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 684 ms: 1.15x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.11x faster                                                    |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 48.1 us: 1.10x faster                                                   |
| go                         | 164 ms                                                   | 158 ms: 1.04x faster                                                    |
| pidigits                   | 238 ms                                                   | 231 ms: 1.03x faster                                                    |
| pyflate                    | 582 ms                                                   | 600 ms: 1.03x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 68.6 ms: 1.05x slower                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.84 sec: 1.06x slower                                                  |
| sphinx                     | 1.20 sec                                                 | 1.30 sec: 1.08x slower                                                  |
| k_core                     | 2.99 sec                                                 | 3.24 sec: 1.08x slower                                                  |
| telco                      | 10.5 ms                                                  | 11.3 ms: 1.08x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.24 sec: 1.09x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.20 sec: 1.11x slower                                                  |
| nqueens                    | 105 ms                                                   | 116 ms: 1.11x slower                                                    |
| pylint                     | 345 ms                                                   | 383 ms: 1.11x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.07 sec: 1.11x slower                                                  |
| chaos                      | 70.7 ms                                                  | 78.9 ms: 1.12x slower                                                   |
| json                       | 5.94 ms                                                  | 6.63 ms: 1.12x slower                                                   |
| hexiom                     | 7.34 ms                                                  | 8.24 ms: 1.12x slower                                                   |
| 2to3                       | 313 ms                                                   | 352 ms: 1.13x slower                                                    |
| regex_compile              | 134 ms                                                   | 151 ms: 1.13x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 302 us: 1.14x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 428 us: 1.15x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.16 ms: 1.15x slower                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 6.93 sec: 1.15x slower                                                  |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.67 ms: 1.15x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 72.1 ms: 1.17x slower                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 103 ms: 1.18x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.68 ms: 1.18x slower                                                   |
| json_loads                 | 32.8 us                                                  | 39.0 us: 1.19x slower                                                   |
| connected_components       | 547 ms                                                   | 653 ms: 1.19x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 175 ms: 1.20x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 142 ms: 1.20x slower                                                    |
| shortest_path              | 565 ms                                                   | 681 ms: 1.20x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 25.9 ms: 1.21x slower                                                   |
| genshi_text                | 28.6 ms                                                  | 35.0 ms: 1.23x slower                                                   |
| xml_etree_process          | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| sympy_expand               | 472 ms                                                   | 581 ms: 1.23x slower                                                    |
| raytrace                   | 310 ms                                                   | 383 ms: 1.24x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 188 ms: 1.24x slower                                                    |
| logging_simple             | 7.25 us                                                  | 9.07 us: 1.25x slower                                                   |
| logging_format             | 8.10 us                                                  | 10.1 us: 1.25x slower                                                   |
| richards                   | 54.5 ms                                                  | 68.3 ms: 1.25x slower                                                   |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                   |
| django_template            | 39.4 ms                                                  | 50.6 ms: 1.29x slower                                                   |
| richards_super             | 60.8 ms                                                  | 78.3 ms: 1.29x slower                                                   |
| meteor_contest             | 117 ms                                                   | 151 ms: 1.29x slower                                                    |
| fannkuch                   | 478 ms                                                   | 618 ms: 1.29x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 110 ms: 1.29x slower                                                    |
| comprehensions             | 20.8 us                                                  | 27.0 us: 1.30x slower                                                   |
| sympy_str                  | 265 ms                                                   | 343 ms: 1.30x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.81 ms: 1.35x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 271 us: 1.38x slower                                                    |
| coverage                   | 106 ms                                                   | 146 ms: 1.38x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| nbody                      | 118 ms                                                   | 170 ms: 1.44x slower                                                    |
| mako                       | 14.0 ms                                                  | 21.3 ms: 1.53x slower                                                   |
| many_optionals             | 626 us                                                   | 1.05 ms: 1.67x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 35.0 ms: 1.72x slower                                                   |
| logging_silent             | 135 ns                                                   | 765 ns: 5.69x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 62.3 ms: 7.73x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (12): pathlib, scimark_sor, spectral_norm, deepcopy_reduce, asyncio_websockets, scimark_fft, async_generators, float, generators, pycparser, coroutines, json_dumps
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250518-3.15.0a0-009e7b3-NOGIL/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.29x