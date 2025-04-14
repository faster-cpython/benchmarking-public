# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.121x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 376 ms: 1.20x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.33 sec: 1.12x slower                                                   |
| html5lib       | 65.6 ms                                                  | 77.0 ms: 1.17x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.37 sec: 1.14x slower                                                   |
| Geometric mean | (ref)                                                    | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 532 ms: 1.25x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 968 ms: 1.18x faster                                                     |
| async_tree_none            | 504 ms                                                   | 434 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 709 ms: 1.11x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 31.0 ms: 1.05x slower                                                    |
| async_generators           | 500 ms                                                   | 540 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.13x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 103 ms: 1.07x slower                                                     |
| nbody          | 118 ms                                                   | 185 ms: 1.57x slower                                                     |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                    |
| regex_dna      | 263 ms                                                   | 252 ms: 1.04x faster                                                     |
| regex_compile  | 134 ms                                                   | 163 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 131 ms: 1.21x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.15 sec: 1.18x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 17.0 ms: 1.20x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 323 us: 1.22x slower                                                     |
| json_loads           | 32.8 us                                                  | 40.5 us: 1.23x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 462 us: 1.24x slower                                                     |
| xml_etree_generate   | 118 ms                                                   | 146 ms: 1.24x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 104 ms: 1.26x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.13x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.3 ms: 1.40x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 79.5 ms: 1.29x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 38.0 ms: 1.33x slower                                                    |
| django_template | 39.4 ms                                                  | 54.3 ms: 1.38x slower                                                    |
| mako            | 14.0 ms                                                  | 22.6 ms: 1.62x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.40x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.67 ms: 2.22x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.09 ms: 1.62x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 919 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.08 ms: 1.25x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 532 ms: 1.25x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 131 ms: 1.21x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 403 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 669 ms: 1.20x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 968 ms: 1.18x faster                                                     |
| async_tree_none            | 504 ms                                                   | 434 ms: 1.16x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.62 us: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| deepcopy                   | 479 us                                                   | 430 us: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 709 ms: 1.11x faster                                                     |
| regex_dna                  | 263 ms                                                   | 252 ms: 1.04x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 31.0 ms: 1.05x slower                                                    |
| k_core                     | 2.99 sec                                                 | 3.20 sec: 1.07x slower                                                   |
| float                      | 95.8 ms                                                  | 103 ms: 1.07x slower                                                     |
| generators                 | 40.3 ms                                                  | 43.2 ms: 1.07x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                                   |
| go                         | 164 ms                                                   | 177 ms: 1.07x slower                                                     |
| scimark_fft                | 463 ms                                                   | 498 ms: 1.08x slower                                                     |
| async_generators           | 500 ms                                                   | 540 ms: 1.08x slower                                                     |
| scimark_sor                | 164 ms                                                   | 178 ms: 1.09x slower                                                     |
| logging_silent             | 135 ns                                                   | 149 ns: 1.11x slower                                                     |
| json                       | 5.94 ms                                                  | 6.63 ms: 1.12x slower                                                    |
| pyflate                    | 582 ms                                                   | 651 ms: 1.12x slower                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 4.75 us: 1.12x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.33 sec: 1.12x slower                                                   |
| pylint                     | 345 ms                                                   | 389 ms: 1.13x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.92 sec: 1.14x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.37 sec: 1.14x slower                                                   |
| telco                      | 10.5 ms                                                  | 12.1 ms: 1.16x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 77.0 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 154 ms: 1.18x slower                                                     |
| tomli_loads                | 2.67 sec                                                 | 3.15 sec: 1.18x slower                                                   |
| json_dumps                 | 14.2 ms                                                  | 17.0 ms: 1.20x slower                                                    |
| 2to3                       | 313 ms                                                   | 376 ms: 1.20x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.20x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.40 sec: 1.21x slower                                                   |
| logging_format             | 8.10 us                                                  | 9.79 us: 1.21x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 323 us: 1.22x slower                                                     |
| regex_compile              | 134 ms                                                   | 163 ms: 1.22x slower                                                     |
| connected_components       | 547 ms                                                   | 669 ms: 1.22x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 80.2 ms: 1.23x slower                                                    |
| shortest_path              | 565 ms                                                   | 696 ms: 1.23x slower                                                     |
| thrift                     | 1.01 ms                                                  | 1.25 ms: 1.23x slower                                                    |
| json_loads                 | 32.8 us                                                  | 40.5 us: 1.23x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 462 us: 1.24x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 146 ms: 1.24x slower                                                     |
| logging_simple             | 7.25 us                                                  | 9.01 us: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.30 ms: 1.25x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 190 ms: 1.26x slower                                                     |
| chaos                      | 70.7 ms                                                  | 89.0 ms: 1.26x slower                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 194 ms: 1.26x slower                                                     |
| xml_etree_process          | 82.1 ms                                                  | 104 ms: 1.26x slower                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 7.60 sec: 1.26x slower                                                   |
| nqueens                    | 105 ms                                                   | 133 ms: 1.27x slower                                                     |
| comprehensions             | 20.8 us                                                  | 26.4 us: 1.27x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.37 ms: 1.28x slower                                                    |
| coverage                   | 106 ms                                                   | 135 ms: 1.28x slower                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 113 ms: 1.29x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 79.5 ms: 1.29x slower                                                    |
| sympy_expand               | 472 ms                                                   | 613 ms: 1.30x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 192 ms: 1.31x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 112 ms: 1.32x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.43 ms: 1.32x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 5.24 ms: 1.32x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 38.0 ms: 1.33x slower                                                    |
| meteor_contest             | 117 ms                                                   | 157 ms: 1.34x slower                                                     |
| raytrace                   | 310 ms                                                   | 416 ms: 1.34x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 28.8 ms: 1.34x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 21.8 ms: 1.35x slower                                                    |
| richards                   | 54.5 ms                                                  | 73.9 ms: 1.36x slower                                                    |
| richards_super             | 60.8 ms                                                  | 83.7 ms: 1.38x slower                                                    |
| django_template            | 39.4 ms                                                  | 54.3 ms: 1.38x slower                                                    |
| sympy_str                  | 265 ms                                                   | 367 ms: 1.38x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 12.3 ms: 1.40x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.88 ms: 1.41x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 2.02 ms: 1.41x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 281 us: 1.43x slower                                                     |
| fannkuch                   | 478 ms                                                   | 681 ms: 1.43x slower                                                     |
| nbody                      | 118 ms                                                   | 185 ms: 1.57x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 32.5 ms: 1.60x slower                                                    |
| mako                       | 14.0 ms                                                  | 22.6 ms: 1.62x slower                                                    |
| many_optionals             | 626 us                                                   | 1.10 ms: 1.75x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 56.7 ms: 7.03x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.16x slower                                                             |

Benchmark hidden because not significant (6): regex_v8, spectral_norm, pathlib, deepcopy_memo, pidigits, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.121x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.23x