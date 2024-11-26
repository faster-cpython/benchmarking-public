# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.352x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 508 ms: 1.67x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 118 ms: 1.78x slower                                                    |
| tornado_http   | 128 ms                                                   | 203 ms: 1.59x slower                                                    |
| Geometric mean | (ref)                                                    | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 676 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 689 ms: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 862 ms: 1.12x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 735 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 897 ms: 1.17x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.34 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 565 ms: 1.20x slower                                                    |
| async_tree_none            | 497 ms                                                   | 604 ms: 1.22x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.23x slower                                                  |
| async_generators           | 489 ms                                                   | 653 ms: 1.34x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 39.3 ms: 1.38x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 205 ms: 2.20x slower                                                    |
| nbody          | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                    | 1.75x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.42 ms: 1.11x faster                                                   |
| regex_v8       | 31.8 ms                                                  | 32.5 ms: 1.02x slower                                                   |
| regex_compile  | 127 ms                                                   | 248 ms: 1.95x slower                                                    |
| Geometric mean | (ref)                                                    | 1.16x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 182 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 152 ms: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 37.9 us: 1.20x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 17.8 ms: 1.32x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 125 ms: 1.56x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 4.11 sec: 1.62x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 526 us: 2.10x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 754 us: 2.11x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.41x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 18.1 ms: 1.18x slower                                                   |
| python_startup_no_site | 8.73 ms                                                  | 12.1 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.28x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 101 ms: 1.67x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 52.1 ms: 1.88x slower                                                   |
| django_template | 41.6 ms                                                  | 79.0 ms: 1.90x slower                                                   |
| mako            | 13.4 ms                                                  | 28.4 ms: 2.12x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.89x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.61 ms: 2.07x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 3.44 ms: 1.68x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 6.69 ms: 1.15x faster                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.42 ms: 1.11x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 182 ms: 1.08x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 152 ms: 1.02x slower                                                    |
| regex_v8                   | 31.8 ms                                                  | 32.5 ms: 1.02x slower                                                   |
| asyncio_websockets         | 659 ms                                                   | 676 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 689 ms: 1.06x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 862 ms: 1.12x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 735 ms: 1.13x slower                                                    |
| pathlib                    | 22.7 ms                                                  | 25.7 ms: 1.13x slower                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 897 ms: 1.17x slower                                                    |
| python_startup             | 15.4 ms                                                  | 18.1 ms: 1.18x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.34 sec: 1.18x slower                                                  |
| json                       | 5.73 ms                                                  | 6.77 ms: 1.18x slower                                                   |
| deepcopy                   | 447 us                                                   | 531 us: 1.19x slower                                                    |
| json_loads                 | 31.7 us                                                  | 37.9 us: 1.20x slower                                                   |
| async_tree_none_tg         | 470 ms                                                   | 565 ms: 1.20x slower                                                    |
| async_tree_none            | 497 ms                                                   | 604 ms: 1.22x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.23x slower                                                  |
| mdp                        | 3.34 sec                                                 | 4.28 sec: 1.28x slower                                                  |
| scimark_fft                | 447 ms                                                   | 574 ms: 1.28x slower                                                    |
| json_dumps                 | 13.6 ms                                                  | 17.8 ms: 1.32x slower                                                   |
| telco                      | 9.74 ms                                                  | 12.9 ms: 1.32x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.66 ms: 1.33x slower                                                   |
| async_generators           | 489 ms                                                   | 653 ms: 1.34x slower                                                    |
| coverage                   | 99.1 ms                                                  | 133 ms: 1.34x slower                                                    |
| deepcopy_memo              | 50.4 us                                                  | 67.9 us: 1.35x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| xml_etree_generate         | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 39.3 ms: 1.38x slower                                                   |
| python_startup_no_site     | 8.73 ms                                                  | 12.1 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.76 us: 1.42x slower                                                   |
| meteor_contest             | 114 ms                                                   | 166 ms: 1.46x slower                                                    |
| pylint                     | 342 ms                                                   | 499 ms: 1.46x slower                                                    |
| nqueens                    | 100 ms                                                   | 149 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.8 ms: 1.54x slower                                                   |
| xml_etree_process          | 80.5 ms                                                  | 125 ms: 1.56x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 2.00 sec: 1.57x slower                                                  |
| spectral_norm              | 143 ms                                                   | 225 ms: 1.58x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 9.28 sec: 1.58x slower                                                  |
| bench_thread_pool          | 1.27 ms                                                  | 2.01 ms: 1.58x slower                                                   |
| tornado_http               | 128 ms                                                   | 203 ms: 1.59x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 4.11 sec: 1.62x slower                                                  |
| fannkuch                   | 461 ms                                                   | 753 ms: 1.63x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 139 ms: 1.66x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 34.6 ms: 1.66x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 101 ms: 1.67x slower                                                    |
| 2to3                       | 304 ms                                                   | 508 ms: 1.67x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 324 us: 1.68x slower                                                    |
| thrift                     | 968 us                                                   | 1.62 ms: 1.68x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 217 ms: 1.72x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 110 ms: 1.77x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 118 ms: 1.78x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.67 sec: 1.80x slower                                                  |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.43 sec: 1.81x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 52.1 ms: 1.88x slower                                                   |
| django_template            | 41.6 ms                                                  | 79.0 ms: 1.90x slower                                                   |
| sympy_str                  | 264 ms                                                   | 504 ms: 1.91x slower                                                    |
| regex_compile              | 127 ms                                                   | 248 ms: 1.95x slower                                                    |
| logging_format             | 7.82 us                                                  | 15.4 us: 1.97x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.2 us: 1.97x slower                                                   |
| logging_simple             | 7.07 us                                                  | 14.1 us: 1.99x slower                                                   |
| sympy_expand               | 457 ms                                                   | 936 ms: 2.05x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 526 us: 2.10x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 176 ms: 2.11x slower                                                    |
| scimark_sor                | 160 ms                                                   | 337 ms: 2.11x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 754 us: 2.11x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.4 ms: 2.12x slower                                                   |
| logging_silent             | 133 ns                                                   | 284 ns: 2.13x slower                                                    |
| richards                   | 53.6 ms                                                  | 115 ms: 2.15x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 310 ms: 2.16x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 15.4 ms: 2.16x slower                                                   |
| float                      | 93.3 ms                                                  | 205 ms: 2.20x slower                                                    |
| richards_super             | 60.1 ms                                                  | 135 ms: 2.25x slower                                                    |
| chaos                      | 68.0 ms                                                  | 161 ms: 2.37x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 330 ms: 2.37x slower                                                    |
| go                         | 160 ms                                                   | 384 ms: 2.40x slower                                                    |
| nbody                      | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.28 ms: 2.47x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.72 ms: 2.70x slower                                                   |
| raytrace                   | 300 ms                                                   | 821 ms: 2.74x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 12.4 ms: 3.24x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.54x slower                                                            |

Benchmark hidden because not significant (2): pidigits, regex_dna
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.352x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.06x