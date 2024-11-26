# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.365x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 518 ms: 1.71x slower                                                    |
| docutils       | 2.89 sec                                                 | 4.08 sec: 1.41x slower                                                  |
| html5lib       | 66.4 ms                                                  | 121 ms: 1.82x slower                                                    |
| tornado_http   | 128 ms                                                   | 208 ms: 1.63x slower                                                    |
| Geometric mean | (ref)                                                    | 1.64x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 675 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 731 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 869 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 570 ms: 1.21x slower                                                    |
| async_tree_none            | 497 ms                                                   | 606 ms: 1.22x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.25x slower                                                  |
| async_generators           | 489 ms                                                   | 652 ms: 1.33x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 40.6 ms: 1.43x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 206 ms: 2.21x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| Geometric mean | (ref)                                                    | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.46 ms: 1.10x faster                                                   |
| regex_v8       | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                   |
| regex_compile  | 127 ms                                                   | 257 ms: 2.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 185 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 156 ms: 1.05x slower                                                    |
| json_loads           | 31.7 us                                                  | 38.6 us: 1.22x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 18.2 ms: 1.34x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 163 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 132 ms: 1.63x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 4.22 sec: 1.66x slower                                                  |
| pickle_pure_python   | 357 us                                                   | 773 us: 2.17x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 546 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 18.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 8.73 ms                                                  | 12.3 ms: 1.40x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 52.9 ms: 1.91x slower                                                   |
| django_template | 41.6 ms                                                  | 82.7 ms: 1.99x slower                                                   |
| mako            | 13.4 ms                                                  | 28.7 ms: 2.15x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.93x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.62 ms: 2.07x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 3.50 ms: 1.65x faster                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.46 ms: 1.10x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 185 ms: 1.06x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.51 ms: 1.02x faster                                                   |
| asyncio_websockets         | 659 ms                                                   | 675 ms: 1.02x slower                                                    |
| regex_v8                   | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 149 ms                                                   | 156 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 731 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 869 ms: 1.13x slower                                                    |
| pathlib                    | 22.7 ms                                                  | 26.4 ms: 1.16x slower                                                   |
| python_startup             | 15.4 ms                                                  | 18.2 ms: 1.18x slower                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                  |
| json                       | 5.73 ms                                                  | 6.93 ms: 1.21x slower                                                   |
| async_tree_none_tg         | 470 ms                                                   | 570 ms: 1.21x slower                                                    |
| json_loads                 | 31.7 us                                                  | 38.6 us: 1.22x slower                                                   |
| async_tree_none            | 497 ms                                                   | 606 ms: 1.22x slower                                                    |
| deepcopy                   | 447 us                                                   | 557 us: 1.25x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.25x slower                                                  |
| scimark_fft                | 447 ms                                                   | 576 ms: 1.29x slower                                                    |
| mdp                        | 3.34 sec                                                 | 4.33 sec: 1.30x slower                                                  |
| telco                      | 9.74 ms                                                  | 12.8 ms: 1.31x slower                                                   |
| async_generators           | 489 ms                                                   | 652 ms: 1.33x slower                                                    |
| json_dumps                 | 13.6 ms                                                  | 18.2 ms: 1.34x slower                                                   |
| coverage                   | 99.1 ms                                                  | 135 ms: 1.36x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.94 ms: 1.37x slower                                                   |
| python_startup_no_site     | 8.73 ms                                                  | 12.3 ms: 1.40x slower                                                   |
| docutils                   | 2.89 sec                                                 | 4.08 sec: 1.41x slower                                                  |
| coroutines                 | 28.5 ms                                                  | 40.6 ms: 1.43x slower                                                   |
| deepcopy_memo              | 50.4 us                                                  | 72.3 us: 1.43x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 163 ms: 1.43x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 5.94 us: 1.46x slower                                                   |
| meteor_contest             | 114 ms                                                   | 168 ms: 1.48x slower                                                    |
| pylint                     | 342 ms                                                   | 514 ms: 1.50x slower                                                    |
| nqueens                    | 100 ms                                                   | 151 ms: 1.51x slower                                                    |
| generators                 | 37.6 ms                                                  | 58.4 ms: 1.55x slower                                                   |
| pycparser                  | 1.27 sec                                                 | 2.03 sec: 1.59x slower                                                  |
| fannkuch                   | 461 ms                                                   | 736 ms: 1.60x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 9.42 sec: 1.60x slower                                                  |
| spectral_norm              | 143 ms                                                   | 231 ms: 1.62x slower                                                    |
| tornado_http               | 128 ms                                                   | 208 ms: 1.63x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 132 ms: 1.63x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 139 ms: 1.66x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 4.22 sec: 1.66x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 34.8 ms: 1.67x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 2.13 ms: 1.67x slower                                                   |
| 2to3                       | 304 ms                                                   | 518 ms: 1.71x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 104 ms: 1.72x slower                                                    |
| thrift                     | 968 us                                                   | 1.67 ms: 1.73x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 337 us: 1.74x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 121 ms: 1.82x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                  |
| sqlglot_normalize          | 127 ms                                                   | 234 ms: 1.84x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 116 ms: 1.86x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.76 sec: 1.90x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 52.9 ms: 1.91x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.63 sec: 1.91x slower                                                  |
| sympy_str                  | 264 ms                                                   | 516 ms: 1.95x slower                                                    |
| django_template            | 41.6 ms                                                  | 82.7 ms: 1.99x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.9 us: 2.01x slower                                                   |
| regex_compile              | 127 ms                                                   | 257 ms: 2.02x slower                                                    |
| logging_format             | 7.82 us                                                  | 16.1 us: 2.05x slower                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 174 ms: 2.08x slower                                                    |
| sympy_expand               | 457 ms                                                   | 959 ms: 2.10x slower                                                    |
| logging_simple             | 7.07 us                                                  | 14.9 us: 2.11x slower                                                   |
| scimark_sor                | 160 ms                                                   | 342 ms: 2.14x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.7 ms: 2.15x slower                                                   |
| logging_silent             | 133 ns                                                   | 287 ns: 2.16x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 773 us: 2.17x slower                                                    |
| richards                   | 53.6 ms                                                  | 117 ms: 2.17x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 546 us: 2.18x slower                                                    |
| float                      | 93.3 ms                                                  | 206 ms: 2.21x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 317 ms: 2.21x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 15.8 ms: 2.23x slower                                                   |
| richards_super             | 60.1 ms                                                  | 138 ms: 2.29x slower                                                    |
| chaos                      | 68.0 ms                                                  | 159 ms: 2.34x slower                                                    |
| go                         | 160 ms                                                   | 389 ms: 2.43x slower                                                    |
| nbody                      | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.27 ms: 2.47x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 353 ms: 2.54x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.65 ms: 2.65x slower                                                   |
| raytrace                   | 300 ms                                                   | 812 ms: 2.71x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 12.8 ms: 3.35x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.57x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, pidigits
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (3) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log

- Geometric mean (including insignificant results): 1.365x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.06x