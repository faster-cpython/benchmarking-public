# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: af5ed4b
- commit date: 2024-08-19
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 322 ms: 1.18x slower                                                         |
| docutils       | 2.83 sec                                                   | 3.26 sec: 1.15x slower                                                       |
| html5lib       | 67.2 ms                                                    | 75.5 ms: 1.12x slower                                                        |
| tornado_http   | 94.6 ms                                                    | 99.3 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                      | 1.12x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 349 ms: 1.08x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                                         |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 189 ms: 1.01x faster                                                         |
| float          | 78.9 ms                                                    | 84.9 ms: 1.08x slower                                                        |
| nbody          | 88.3 ms                                                    | 118 ms: 1.33x slower                                                         |
| Geometric mean | (ref)                                                      | 1.12x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 221 ms: 1.00x faster                                                         |
| regex_effbot   | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                        |
| regex_v8       | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                        |
| regex_compile  | 137 ms                                                     | 180 ms: 1.31x slower                                                         |
| Geometric mean | (ref)                                                      | 1.08x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 162 ms                                                     | 150 ms: 1.08x faster                                                         |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                        |
| json_dumps           | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                        |
| xml_etree_generate   | 87.4 ms                                                    | 93.7 ms: 1.07x slower                                                        |
| xml_etree_process    | 61.2 ms                                                    | 66.1 ms: 1.08x slower                                                        |
| unpickle_pure_python | 218 us                                                     | 249 us: 1.14x slower                                                         |
| tomli_loads          | 2.12 sec                                                   | 2.44 sec: 1.15x slower                                                       |
| pickle_pure_python   | 305 us                                                     | 374 us: 1.22x slower                                                         |
| Geometric mean       | (ref)                                                      | 1.06x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                      | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.8 ms                                                    | 40.6 ms: 1.17x slower                                                        |
| mako            | 11.2 ms                                                    | 13.5 ms: 1.20x slower                                                        |
| genshi_text     | 23.7 ms                                                    | 28.7 ms: 1.21x slower                                                        |
| genshi_xml      | 51.6 ms                                                    | 66.9 ms: 1.30x slower                                                        |
| Geometric mean  | (ref)                                                      | 1.22x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 321 us: 1.14x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                    | 2.94 us: 1.14x faster                                                        |
| coverage                   | 93.1 ms                                                    | 84.6 ms: 1.10x faster                                                        |
| deepcopy_memo              | 39.7 us                                                    | 36.6 us: 1.09x faster                                                        |
| async_tree_none            | 378 ms                                                     | 349 ms: 1.08x faster                                                         |
| async_tree_memoization_tg  | 444 ms                                                     | 410 ms: 1.08x faster                                                         |
| xml_etree_parse            | 162 ms                                                     | 150 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 336 ms                                                     | 313 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 552 ms: 1.06x faster                                                         |
| async_tree_io_tg           | 936 ms                                                     | 890 ms: 1.05x faster                                                         |
| pathlib                    | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                        |
| gc_traversal               | 3.98 ms                                                    | 3.81 ms: 1.04x faster                                                        |
| create_gc_cycles           | 1.82 ms                                                    | 1.76 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 594 ms: 1.03x faster                                                         |
| python_startup             | 10.8 ms                                                    | 10.5 ms: 1.03x faster                                                        |
| thrift                     | 823 us                                                     | 803 us: 1.02x faster                                                         |
| asyncio_websockets         | 567 ms                                                     | 556 ms: 1.02x faster                                                         |
| mdp                        | 2.79 sec                                                   | 2.75 sec: 1.02x faster                                                       |
| pidigits                   | 191 ms                                                     | 189 ms: 1.01x faster                                                         |
| asyncio_tcp                | 508 ms                                                     | 501 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.82 sec: 1.01x faster                                                       |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                        |
| regex_dna                  | 221 ms                                                     | 221 ms: 1.00x faster                                                         |
| python_startup_no_site     | 7.11 ms                                                    | 7.08 ms: 1.00x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                        |
| json_dumps                 | 10.7 ms                                                    | 10.8 ms: 1.01x slower                                                        |
| regex_effbot               | 3.67 ms                                                    | 3.77 ms: 1.03x slower                                                        |
| regex_v8                   | 25.1 ms                                                    | 25.8 ms: 1.03x slower                                                        |
| coroutines                 | 23.2 ms                                                    | 23.9 ms: 1.03x slower                                                        |
| bench_thread_pool          | 834 us                                                     | 863 us: 1.03x slower                                                         |
| json                       | 5.31 ms                                                    | 5.53 ms: 1.04x slower                                                        |
| telco                      | 8.41 ms                                                    | 8.80 ms: 1.05x slower                                                        |
| tornado_http               | 94.6 ms                                                    | 99.3 ms: 1.05x slower                                                        |
| async_generators           | 442 ms                                                     | 467 ms: 1.06x slower                                                         |
| xml_etree_generate         | 87.4 ms                                                    | 93.7 ms: 1.07x slower                                                        |
| float                      | 78.9 ms                                                    | 84.9 ms: 1.08x slower                                                        |
| scimark_fft                | 392 ms                                                     | 423 ms: 1.08x slower                                                         |
| xml_etree_process          | 61.2 ms                                                    | 66.1 ms: 1.08x slower                                                        |
| bpe_tokeniser              | 5.02 sec                                                   | 5.44 sec: 1.08x slower                                                       |
| scimark_lu                 | 122 ms                                                     | 134 ms: 1.10x slower                                                         |
| meteor_contest             | 110 ms                                                     | 121 ms: 1.10x slower                                                         |
| logging_simple             | 5.74 us                                                    | 6.42 us: 1.12x slower                                                        |
| crypto_pyaes               | 77.5 ms                                                    | 86.7 ms: 1.12x slower                                                        |
| html5lib                   | 67.2 ms                                                    | 75.5 ms: 1.12x slower                                                        |
| logging_format             | 6.47 us                                                    | 7.28 us: 1.13x slower                                                        |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 5.98 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 165 us                                                     | 187 us: 1.14x slower                                                         |
| unpickle_pure_python       | 218 us                                                     | 249 us: 1.14x slower                                                         |
| tomli_loads                | 2.12 sec                                                   | 2.44 sec: 1.15x slower                                                       |
| docutils                   | 2.83 sec                                                   | 3.26 sec: 1.15x slower                                                       |
| pyflate                    | 484 ms                                                     | 560 ms: 1.16x slower                                                         |
| scimark_monte_carlo        | 69.2 ms                                                    | 80.2 ms: 1.16x slower                                                        |
| spectral_norm              | 116 ms                                                     | 135 ms: 1.16x slower                                                         |
| django_template            | 34.8 ms                                                    | 40.6 ms: 1.17x slower                                                        |
| scimark_sor                | 127 ms                                                     | 149 ms: 1.17x slower                                                         |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                         |
| pprint_safe_repr           | 758 ms                                                     | 890 ms: 1.17x slower                                                         |
| fannkuch                   | 402 ms                                                     | 472 ms: 1.17x slower                                                         |
| sympy_sum                  | 156 ms                                                     | 183 ms: 1.17x slower                                                         |
| 2to3                       | 274 ms                                                     | 322 ms: 1.18x slower                                                         |
| logging_silent             | 105 ns                                                     | 124 ns: 1.18x slower                                                         |
| sympy_str                  | 282 ms                                                     | 335 ms: 1.19x slower                                                         |
| sympy_integrate            | 20.5 ms                                                    | 24.5 ms: 1.19x slower                                                        |
| sqlglot_parse              | 1.32 ms                                                    | 1.58 ms: 1.20x slower                                                        |
| sqlglot_optimize           | 55.5 ms                                                    | 66.5 ms: 1.20x slower                                                        |
| sympy_expand               | 473 ms                                                     | 566 ms: 1.20x slower                                                         |
| mako                       | 11.2 ms                                                    | 13.5 ms: 1.20x slower                                                        |
| sqlglot_transpile          | 1.63 ms                                                    | 1.97 ms: 1.21x slower                                                        |
| pprint_pformat             | 1.56 sec                                                   | 1.88 sec: 1.21x slower                                                       |
| genshi_text                | 23.7 ms                                                    | 28.7 ms: 1.21x slower                                                        |
| sqlglot_normalize          | 110 ms                                                     | 134 ms: 1.21x slower                                                         |
| go                         | 145 ms                                                     | 177 ms: 1.22x slower                                                         |
| pickle_pure_python         | 305 us                                                     | 374 us: 1.22x slower                                                         |
| pycparser                  | 1.16 sec                                                   | 1.45 sec: 1.25x slower                                                       |
| nqueens                    | 81.4 ms                                                    | 104 ms: 1.28x slower                                                         |
| raytrace                   | 267 ms                                                     | 344 ms: 1.29x slower                                                         |
| genshi_xml                 | 51.6 ms                                                    | 66.9 ms: 1.30x slower                                                        |
| regex_compile              | 137 ms                                                     | 180 ms: 1.31x slower                                                         |
| richards_super             | 57.4 ms                                                    | 76.0 ms: 1.32x slower                                                        |
| richards                   | 50.9 ms                                                    | 67.7 ms: 1.33x slower                                                        |
| nbody                      | 88.3 ms                                                    | 118 ms: 1.33x slower                                                         |
| chaos                      | 61.3 ms                                                    | 82.2 ms: 1.34x slower                                                        |
| comprehensions             | 16.6 us                                                    | 22.8 us: 1.37x slower                                                        |
| generators                 | 29.6 ms                                                    | 40.8 ms: 1.38x slower                                                        |
| deltablue                  | 3.25 ms                                                    | 4.48 ms: 1.38x slower                                                        |
| hexiom                     | 6.30 ms                                                    | 9.07 ms: 1.44x slower                                                        |
| Geometric mean             | (ref)                                                      | 1.10x slower                                                                 |

Benchmark hidden because not significant (3): async_tree_memoization, xml_etree_iterparse, async_tree_io
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.02x