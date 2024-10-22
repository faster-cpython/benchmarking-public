# Results vs. base

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: af5ed4b
- commit date: 2024-08-19
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 358 ms                                                                | 322 ms: 1.11x faster                                                         |
| docutils       | 3.41 sec                                                              | 3.26 sec: 1.05x faster                                                       |
| html5lib       | 79.4 ms                                                               | 75.5 ms: 1.05x faster                                                        |
| tornado_http   | 102 ms                                                                | 99.3 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 374 ms                                                                | 349 ms: 1.07x faster                                                         |
| async_tree_memoization  | 479 ms                                                                | 454 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed | 613 ms                                                                | 594 ms: 1.03x faster                                                         |
| async_tree_none_tg      | 323 ms                                                                | 313 ms: 1.03x faster                                                         |
| async_tree_io           | 963 ms                                                                | 935 ms: 1.03x faster                                                         |
| async_generators        | 477 ms                                                                | 467 ms: 1.02x faster                                                         |
| asyncio_tcp             | 502 ms                                                                | 501 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.82 sec: 1.00x slower                                                       |
| coroutines              | 23.4 ms                                                               | 23.9 ms: 1.02x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                                 |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 160 ms                                                                | 118 ms: 1.36x faster                                                         |
| float          | 105 ms                                                                | 84.9 ms: 1.24x faster                                                        |
| pidigits       | 190 ms                                                                | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 210 ms                                                                | 180 ms: 1.17x faster                                                         |
| regex_dna      | 231 ms                                                                | 221 ms: 1.05x faster                                                         |
| regex_v8       | 27.0 ms                                                               | 25.8 ms: 1.04x faster                                                        |
| regex_effbot   | 3.87 ms                                                               | 3.77 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.07 sec                                                              | 2.44 sec: 1.25x faster                                                       |
| xml_etree_generate   | 112 ms                                                                | 93.7 ms: 1.20x faster                                                        |
| xml_etree_process    | 79.2 ms                                                               | 66.1 ms: 1.20x faster                                                        |
| unpickle_pure_python | 294 us                                                                | 249 us: 1.18x faster                                                         |
| pickle_pure_python   | 434 us                                                                | 374 us: 1.16x faster                                                         |
| json_dumps           | 12.1 ms                                                               | 10.8 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 119 ms                                                                | 107 ms: 1.12x faster                                                         |
| xml_etree_parse      | 155 ms                                                                | 150 ms: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 17.8 ms                                                               | 13.5 ms: 1.32x faster                                                        |
| genshi_text     | 32.4 ms                                                               | 28.7 ms: 1.13x faster                                                        |
| django_template | 45.3 ms                                                               | 40.6 ms: 1.12x faster                                                        |
| genshi_xml      | 74.6 ms                                                               | 66.9 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.17x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators               | 59.6 ms                                                               | 40.8 ms: 1.46x faster                                                        |
| comprehensions           | 31.9 us                                                               | 22.8 us: 1.40x faster                                                        |
| deepcopy_memo            | 50.8 us                                                               | 36.6 us: 1.39x faster                                                        |
| logging_silent           | 172 ns                                                                | 124 ns: 1.38x faster                                                         |
| deltablue                | 6.11 ms                                                               | 4.48 ms: 1.37x faster                                                        |
| nbody                    | 160 ms                                                                | 118 ms: 1.36x faster                                                         |
| spectral_norm            | 184 ms                                                                | 135 ms: 1.36x faster                                                         |
| hexiom                   | 12.3 ms                                                               | 9.07 ms: 1.36x faster                                                        |
| fannkuch                 | 627 ms                                                                | 472 ms: 1.33x faster                                                         |
| richards                 | 89.7 ms                                                               | 67.7 ms: 1.32x faster                                                        |
| richards_super           | 100 ms                                                                | 76.0 ms: 1.32x faster                                                        |
| scimark_sor              | 197 ms                                                                | 149 ms: 1.32x faster                                                         |
| mako                     | 17.8 ms                                                               | 13.5 ms: 1.32x faster                                                        |
| scimark_sparse_mat_mult  | 7.73 ms                                                               | 5.98 ms: 1.29x faster                                                        |
| scimark_monte_carlo      | 104 ms                                                                | 80.2 ms: 1.29x faster                                                        |
| pyflate                  | 714 ms                                                                | 560 ms: 1.28x faster                                                         |
| crypto_pyaes             | 109 ms                                                                | 86.7 ms: 1.26x faster                                                        |
| tomli_loads              | 3.07 sec                                                              | 2.44 sec: 1.25x faster                                                       |
| pprint_safe_repr         | 1.11 sec                                                              | 890 ms: 1.25x faster                                                         |
| pprint_pformat           | 2.34 sec                                                              | 1.88 sec: 1.25x faster                                                       |
| nqueens                  | 129 ms                                                                | 104 ms: 1.25x faster                                                         |
| float                    | 105 ms                                                                | 84.9 ms: 1.24x faster                                                        |
| scimark_fft              | 524 ms                                                                | 423 ms: 1.24x faster                                                         |
| scimark_lu               | 164 ms                                                                | 134 ms: 1.22x faster                                                         |
| xml_etree_generate       | 112 ms                                                                | 93.7 ms: 1.20x faster                                                        |
| meteor_contest           | 145 ms                                                                | 121 ms: 1.20x faster                                                         |
| xml_etree_process        | 79.2 ms                                                               | 66.1 ms: 1.20x faster                                                        |
| unpickle_pure_python     | 294 us                                                                | 249 us: 1.18x faster                                                         |
| regex_compile            | 210 ms                                                                | 180 ms: 1.17x faster                                                         |
| sqlglot_parse            | 1.85 ms                                                               | 1.58 ms: 1.17x faster                                                        |
| bpe_tokeniser            | 6.35 sec                                                              | 5.44 sec: 1.17x faster                                                       |
| pickle_pure_python       | 434 us                                                                | 374 us: 1.16x faster                                                         |
| sqlglot_transpile        | 2.28 ms                                                               | 1.97 ms: 1.16x faster                                                        |
| chaos                    | 94.8 ms                                                               | 82.2 ms: 1.15x faster                                                        |
| deepcopy                 | 370 us                                                                | 321 us: 1.15x faster                                                         |
| go                       | 200 ms                                                                | 177 ms: 1.13x faster                                                         |
| genshi_text              | 32.4 ms                                                               | 28.7 ms: 1.13x faster                                                        |
| django_template          | 45.3 ms                                                               | 40.6 ms: 1.12x faster                                                        |
| sqlglot_optimize         | 74.2 ms                                                               | 66.5 ms: 1.12x faster                                                        |
| genshi_xml               | 74.6 ms                                                               | 66.9 ms: 1.12x faster                                                        |
| json_dumps               | 12.1 ms                                                               | 10.8 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 119 ms                                                                | 107 ms: 1.12x faster                                                         |
| sqlglot_normalize        | 148 ms                                                                | 134 ms: 1.11x faster                                                         |
| 2to3                     | 358 ms                                                                | 322 ms: 1.11x faster                                                         |
| sympy_integrate          | 27.1 ms                                                               | 24.5 ms: 1.11x faster                                                        |
| pycparser                | 1.60 sec                                                              | 1.45 sec: 1.10x faster                                                       |
| deepcopy_reduce          | 3.19 us                                                               | 2.94 us: 1.09x faster                                                        |
| telco                    | 9.54 ms                                                               | 8.80 ms: 1.08x faster                                                        |
| bench_thread_pool        | 934 us                                                                | 863 us: 1.08x faster                                                         |
| sympy_str                | 361 ms                                                                | 335 ms: 1.08x faster                                                         |
| typing_runtime_protocols | 201 us                                                                | 187 us: 1.07x faster                                                         |
| async_tree_none          | 374 ms                                                                | 349 ms: 1.07x faster                                                         |
| mdp                      | 2.94 sec                                                              | 2.75 sec: 1.07x faster                                                       |
| sympy_sum                | 195 ms                                                                | 183 ms: 1.06x faster                                                         |
| async_tree_memoization   | 479 ms                                                                | 454 ms: 1.06x faster                                                         |
| sympy_expand             | 597 ms                                                                | 566 ms: 1.05x faster                                                         |
| html5lib                 | 79.4 ms                                                               | 75.5 ms: 1.05x faster                                                        |
| regex_dna                | 231 ms                                                                | 221 ms: 1.05x faster                                                         |
| docutils                 | 3.41 sec                                                              | 3.26 sec: 1.05x faster                                                       |
| regex_v8                 | 27.0 ms                                                               | 25.8 ms: 1.04x faster                                                        |
| logging_simple           | 6.69 us                                                               | 6.42 us: 1.04x faster                                                        |
| pathlib                  | 17.2 ms                                                               | 16.5 ms: 1.04x faster                                                        |
| json                     | 5.76 ms                                                               | 5.53 ms: 1.04x faster                                                        |
| logging_format           | 7.56 us                                                               | 7.28 us: 1.04x faster                                                        |
| xml_etree_parse          | 155 ms                                                                | 150 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed  | 613 ms                                                                | 594 ms: 1.03x faster                                                         |
| tornado_http             | 102 ms                                                                | 99.3 ms: 1.03x faster                                                        |
| async_tree_none_tg       | 323 ms                                                                | 313 ms: 1.03x faster                                                         |
| async_tree_io            | 963 ms                                                                | 935 ms: 1.03x faster                                                         |
| regex_effbot             | 3.87 ms                                                               | 3.77 ms: 1.03x faster                                                        |
| async_generators         | 477 ms                                                                | 467 ms: 1.02x faster                                                         |
| coverage                 | 86.0 ms                                                               | 84.6 ms: 1.02x faster                                                        |
| pidigits                 | 190 ms                                                                | 189 ms: 1.01x faster                                                         |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| asyncio_tcp              | 502 ms                                                                | 501 ms: 1.00x faster                                                         |
| python_startup_no_site   | 7.10 ms                                                               | 7.08 ms: 1.00x faster                                                        |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.82 sec: 1.00x slower                                                       |
| gc_traversal             | 3.74 ms                                                               | 3.81 ms: 1.02x slower                                                        |
| coroutines               | 23.4 ms                                                               | 23.9 ms: 1.02x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                                 |

Benchmark hidden because not significant (9): pylint, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, json_loads, async_tree_io_tg, raytrace, bench_mp_pool, asyncio_websockets, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.00x