# Results vs. 3.13.0

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-aarch64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.369x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 512 ms: 1.69x slower                                                     |
| docutils       | 2.89 sec                                                 | 4.09 sec: 1.41x slower                                                   |
| html5lib       | 66.4 ms                                                  | 119 ms: 1.79x slower                                                     |
| sphinx         | 1.17 sec                                                 | 1.64 sec: 1.41x slower                                                   |
| tornado_http   | 128 ms                                                   | 205 ms: 1.60x slower                                                     |
| Geometric mean | (ref)                                                    | 1.57x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 673 ms: 1.02x slower                                                     |
| async_tree_memoization_tg  | 649 ms                                                   | 710 ms: 1.09x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 742 ms: 1.14x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 884 ms: 1.15x slower                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 917 ms: 1.20x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                   |
| async_tree_none            | 497 ms                                                   | 608 ms: 1.22x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 583 ms: 1.24x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.25x slower                                                   |
| async_generators           | 489 ms                                                   | 658 ms: 1.35x slower                                                     |
| coroutines                 | 28.5 ms                                                  | 40.0 ms: 1.41x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 209 ms: 2.24x slower                                                     |
| nbody          | 114 ms                                                   | 286 ms: 2.50x slower                                                     |
| Geometric mean | (ref)                                                    | 1.78x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.48 ms: 1.09x faster                                                    |
| regex_dna      | 253 ms                                                   | 251 ms: 1.01x faster                                                     |
| regex_v8       | 31.8 ms                                                  | 32.9 ms: 1.03x slower                                                    |
| regex_compile  | 127 ms                                                   | 250 ms: 1.97x slower                                                     |
| Geometric mean | (ref)                                                    | 1.17x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 182 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 149 ms                                                   | 153 ms: 1.02x slower                                                     |
| json_loads           | 31.7 us                                                  | 37.3 us: 1.18x slower                                                    |
| json_dumps           | 13.6 ms                                                  | 18.9 ms: 1.39x slower                                                    |
| xml_etree_generate   | 113 ms                                                   | 158 ms: 1.40x slower                                                     |
| xml_etree_process    | 80.5 ms                                                  | 127 ms: 1.58x slower                                                     |
| tomli_loads          | 2.54 sec                                                 | 4.19 sec: 1.65x slower                                                   |
| unpickle_pure_python | 251 us                                                   | 532 us: 2.12x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 778 us: 2.18x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.44x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 20.4 ms: 1.32x slower                                                    |
| python_startup_no_site | 8.73 ms                                                  | 12.1 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.36x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 101 ms: 1.68x slower                                                     |
| genshi_text     | 27.7 ms                                                  | 51.4 ms: 1.86x slower                                                    |
| django_template | 41.6 ms                                                  | 80.6 ms: 1.94x slower                                                    |
| mako            | 13.4 ms                                                  | 29.2 ms: 2.18x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.91x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.56 ms: 1.31x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 4.43 ms: 1.30x faster                                                    |
| regex_effbot               | 4.89 ms                                                  | 4.48 ms: 1.09x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 182 ms: 1.08x faster                                                     |
| regex_dna                  | 253 ms                                                   | 251 ms: 1.01x faster                                                     |
| asyncio_websockets         | 659 ms                                                   | 673 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 149 ms                                                   | 153 ms: 1.02x slower                                                     |
| regex_v8                   | 31.8 ms                                                  | 32.9 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 710 ms: 1.09x slower                                                     |
| async_tree_memoization     | 651 ms                                                   | 742 ms: 1.14x slower                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 884 ms: 1.15x slower                                                     |
| pathlib                    | 22.7 ms                                                  | 26.1 ms: 1.15x slower                                                    |
| json_loads                 | 31.7 us                                                  | 37.3 us: 1.18x slower                                                    |
| json                       | 5.73 ms                                                  | 6.75 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 917 ms: 1.20x slower                                                     |
| deepcopy                   | 447 us                                                   | 536 us: 1.20x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                   |
| async_tree_none            | 497 ms                                                   | 608 ms: 1.22x slower                                                     |
| async_tree_none_tg         | 470 ms                                                   | 583 ms: 1.24x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.25x slower                                                   |
| scimark_fft                | 447 ms                                                   | 569 ms: 1.27x slower                                                     |
| mdp                        | 3.34 sec                                                 | 4.31 sec: 1.29x slower                                                   |
| telco                      | 9.74 ms                                                  | 12.6 ms: 1.30x slower                                                    |
| python_startup             | 15.4 ms                                                  | 20.4 ms: 1.32x slower                                                    |
| coverage                   | 99.1 ms                                                  | 133 ms: 1.34x slower                                                     |
| async_generators           | 489 ms                                                   | 658 ms: 1.35x slower                                                     |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.82 ms: 1.35x slower                                                    |
| deepcopy_memo              | 50.4 us                                                  | 69.5 us: 1.38x slower                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 12.1 ms: 1.39x slower                                                    |
| json_dumps                 | 13.6 ms                                                  | 18.9 ms: 1.39x slower                                                    |
| xml_etree_generate         | 113 ms                                                   | 158 ms: 1.40x slower                                                     |
| coroutines                 | 28.5 ms                                                  | 40.0 ms: 1.41x slower                                                    |
| sphinx                     | 1.17 sec                                                 | 1.64 sec: 1.41x slower                                                   |
| docutils                   | 2.89 sec                                                 | 4.09 sec: 1.41x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.84 us: 1.44x slower                                                    |
| meteor_contest             | 114 ms                                                   | 166 ms: 1.46x slower                                                     |
| pylint                     | 342 ms                                                   | 507 ms: 1.48x slower                                                     |
| nqueens                    | 100 ms                                                   | 153 ms: 1.53x slower                                                     |
| bench_thread_pool          | 1.27 ms                                                  | 1.96 ms: 1.54x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 9.17 sec: 1.56x slower                                                   |
| generators                 | 37.6 ms                                                  | 59.3 ms: 1.58x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 127 ms: 1.58x slower                                                     |
| tornado_http               | 128 ms                                                   | 205 ms: 1.60x slower                                                     |
| pycparser                  | 1.27 sec                                                 | 2.05 sec: 1.61x slower                                                   |
| spectral_norm              | 143 ms                                                   | 231 ms: 1.62x slower                                                     |
| fannkuch                   | 461 ms                                                   | 751 ms: 1.63x slower                                                     |
| tomli_loads                | 2.54 sec                                                 | 4.19 sec: 1.65x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 140 ms: 1.68x slower                                                     |
| genshi_xml                 | 60.3 ms                                                  | 101 ms: 1.68x slower                                                     |
| typing_runtime_protocols   | 193 us                                                   | 325 us: 1.68x slower                                                     |
| 2to3                       | 304 ms                                                   | 512 ms: 1.69x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 35.2 ms: 1.69x slower                                                    |
| thrift                     | 968 us                                                   | 1.69 ms: 1.75x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 222 ms: 1.75x slower                                                     |
| sqlalchemy_declarative     | 150 ms                                                   | 268 ms: 1.78x slower                                                     |
| html5lib                   | 66.4 ms                                                  | 119 ms: 1.79x slower                                                     |
| sqlglot_optimize           | 62.2 ms                                                  | 113 ms: 1.81x slower                                                     |
| pprint_safe_repr           | 926 ms                                                   | 1.69 sec: 1.82x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.47 sec: 1.83x slower                                                   |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 51.4 ms: 1.86x slower                                                    |
| sympy_str                  | 264 ms                                                   | 506 ms: 1.91x slower                                                     |
| django_template            | 41.6 ms                                                  | 80.6 ms: 1.94x slower                                                    |
| sqlalchemy_imperative      | 15.1 ms                                                  | 29.7 ms: 1.96x slower                                                    |
| regex_compile              | 127 ms                                                   | 250 ms: 1.97x slower                                                     |
| logging_format             | 7.82 us                                                  | 15.7 us: 2.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 41.2 us: 2.02x slower                                                    |
| logging_simple             | 7.07 us                                                  | 14.4 us: 2.04x slower                                                    |
| sympy_expand               | 457 ms                                                   | 948 ms: 2.08x slower                                                     |
| unpickle_pure_python       | 251 us                                                   | 532 us: 2.12x slower                                                     |
| logging_silent             | 133 ns                                                   | 285 ns: 2.14x slower                                                     |
| scimark_sor                | 160 ms                                                   | 346 ms: 2.17x slower                                                     |
| sympy_sum                  | 144 ms                                                   | 311 ms: 2.17x slower                                                     |
| scimark_monte_carlo        | 83.6 ms                                                  | 181 ms: 2.17x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 778 us: 2.18x slower                                                     |
| mako                       | 13.4 ms                                                  | 29.2 ms: 2.18x slower                                                    |
| richards                   | 53.6 ms                                                  | 118 ms: 2.20x slower                                                     |
| hexiom                     | 7.11 ms                                                  | 15.7 ms: 2.21x slower                                                    |
| float                      | 93.3 ms                                                  | 209 ms: 2.24x slower                                                     |
| chaos                      | 68.0 ms                                                  | 159 ms: 2.34x slower                                                     |
| richards_super             | 60.1 ms                                                  | 141 ms: 2.35x slower                                                     |
| scimark_lu                 | 139 ms                                                   | 333 ms: 2.39x slower                                                     |
| go                         | 160 ms                                                   | 391 ms: 2.45x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 4.26 ms: 2.46x slower                                                    |
| nbody                      | 114 ms                                                   | 286 ms: 2.50x slower                                                     |
| sqlglot_parse              | 1.38 ms                                                  | 3.72 ms: 2.70x slower                                                    |
| raytrace                   | 300 ms                                                   | 821 ms: 2.74x slower                                                     |
| deltablue                  | 3.82 ms                                                  | 12.6 ms: 3.30x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 61.1 ms: 7.95x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.62x slower                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path
Ignored benchmarks (1) of results/bm-20241026-3.14.0a1+-f6cc7c8-NOGIL/bm-20241026-arminc-aarch64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: dulwich_log

- Geometric mean (including insignificant results): 1.369x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.18x