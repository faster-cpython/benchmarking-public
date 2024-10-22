# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 362 ms: 1.19x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.63 sec: 1.25x slower                                                  |
| html5lib       | 64.3 ms                                                  | 70.9 ms: 1.10x slower                                                   |
| tornado_http   | 131 ms                                                   | 136 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 573 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 742 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 666 ms: 1.02x slower                                                    |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 612 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| regex_dna      | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| regex_compile  | 128 ms                                                   | 176 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| xml_etree_parse      | 188 ms                                                   | 195 ms: 1.04x slower                                                    |
| json_loads           | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| unpickle_pure_python | 254 us                                                   | 272 us: 1.07x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 385 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.85 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 50.3 ms: 1.19x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.5 ms: 1.25x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 81.2 ms: 1.35x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.8 us: 1.35x faster                                                   |
| deepcopy                   | 451 us                                                   | 376 us: 1.20x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 547 ms: 1.19x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 573 ms: 1.09x faster                                                    |
| float                      | 94.4 ms                                                  | 90.5 ms: 1.04x faster                                                   |
| generators                 | 37.8 ms                                                  | 36.5 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 742 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.7 ms: 1.03x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| logging_silent             | 135 ns                                                   | 133 ns: 1.02x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 725 ms: 1.02x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 4.02 us: 1.01x faster                                                   |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| logging_simple             | 7.04 us                                                  | 7.12 us: 1.01x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.85 ms: 1.01x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.29 ms: 1.01x slower                                                   |
| meteor_contest             | 113 ms                                                   | 115 ms: 1.01x slower                                                    |
| asyncio_websockets         | 656 ms                                                   | 666 ms: 1.02x slower                                                    |
| coverage                   | 98.5 ms                                                  | 100 ms: 1.02x slower                                                    |
| regex_effbot               | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                                   |
| thrift                     | 946 us                                                   | 963 us: 1.02x slower                                                    |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                    |
| scimark_fft                | 447 ms                                                   | 456 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.74 ms: 1.02x slower                                                   |
| mdp                        | 3.36 sec                                                 | 3.45 sec: 1.02x slower                                                  |
| fannkuch                   | 452 ms                                                   | 464 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| tomli_loads                | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| tornado_http               | 131 ms                                                   | 136 ms: 1.04x slower                                                    |
| regex_dna                  | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| xml_etree_parse            | 188 ms                                                   | 195 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.14 sec: 1.04x slower                                                  |
| json                       | 5.61 ms                                                  | 5.85 ms: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                   | 147 ms: 1.04x slower                                                    |
| json_loads                 | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| pyflate                    | 556 ms                                                   | 589 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.4 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 254 us                                                   | 272 us: 1.07x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 385 us: 1.07x slower                                                    |
| telco                      | 9.73 ms                                                  | 10.4 ms: 1.07x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 1.36 sec: 1.07x slower                                                  |
| bench_mp_pool              | 7.30 ms                                                  | 7.86 ms: 1.08x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 612 ms: 1.08x slower                                                    |
| raytrace                   | 298 ms                                                   | 323 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 209 us: 1.09x slower                                                    |
| go                         | 163 ms                                                   | 177 ms: 1.09x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 90.3 ms: 1.09x slower                                                   |
| scimark_sor                | 159 ms                                                   | 175 ms: 1.10x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 70.9 ms: 1.10x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 142 ms: 1.11x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.35 ms: 1.11x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 70.0 ms: 1.12x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.09 ms: 1.12x slower                                                   |
| dask                       | 350 ms                                                   | 396 ms: 1.13x slower                                                    |
| comprehensions             | 20.4 us                                                  | 23.3 us: 1.14x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 4.40 ms: 1.14x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.60 ms: 1.16x slower                                                   |
| pylint                     | 343 ms                                                   | 403 ms: 1.17x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 116 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.05 ms: 1.18x slower                                                   |
| 2to3                       | 306 ms                                                   | 362 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                  | 50.3 ms: 1.19x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.13 sec: 1.22x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 2.33 sec: 1.23x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 34.5 ms: 1.25x slower                                                   |
| docutils                   | 2.91 sec                                                 | 3.63 sec: 1.25x slower                                                  |
| sympy_expand               | 455 ms                                                   | 569 ms: 1.25x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 26.7 ms: 1.27x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 9.12 ms: 1.28x slower                                                   |
| chaos                      | 68.8 ms                                                  | 89.1 ms: 1.29x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 181 ms: 1.30x slower                                                    |
| sympy_str                  | 264 ms                                                   | 343 ms: 1.30x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 81.2 ms: 1.35x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 197 ms: 1.37x slower                                                    |
| regex_compile              | 128 ms                                                   | 176 ms: 1.37x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                            |

Benchmark hidden because not significant (12): xml_etree_generate, pathlib, bpe_tokeniser, xml_etree_process, nbody, logging_format, json_dumps, pidigits, richards, richards_super, async_tree_io, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097-JIT/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x