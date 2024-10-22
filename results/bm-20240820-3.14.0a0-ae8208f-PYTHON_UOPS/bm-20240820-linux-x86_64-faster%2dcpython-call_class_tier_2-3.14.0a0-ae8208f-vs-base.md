# Results vs. base

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: ae8208f
- commit date: 2024-08-20
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 358 ms                                                                | 327 ms: 1.10x faster                                                         |
| docutils       | 3.41 sec                                                              | 3.26 sec: 1.04x faster                                                       |
| html5lib       | 79.4 ms                                                               | 75.9 ms: 1.05x faster                                                        |
| tornado_http   | 102 ms                                                                | 98.6 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 374 ms                                                                | 351 ms: 1.07x faster                                                         |
| async_tree_memoization  | 479 ms                                                                | 456 ms: 1.05x faster                                                         |
| async_tree_io           | 963 ms                                                                | 931 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed | 613 ms                                                                | 595 ms: 1.03x faster                                                         |
| async_tree_io_tg        | 895 ms                                                                | 875 ms: 1.02x faster                                                         |
| async_generators        | 477 ms                                                                | 467 ms: 1.02x faster                                                         |
| async_tree_none_tg      | 323 ms                                                                | 319 ms: 1.01x faster                                                         |
| asyncio_tcp             | 502 ms                                                                | 500 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl         | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| coroutines              | 23.4 ms                                                               | 23.9 ms: 1.02x slower                                                        |
| Geometric mean          | (ref)                                                                 | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 160 ms                                                                | 120 ms: 1.34x faster                                                         |
| float          | 105 ms                                                                | 84.3 ms: 1.25x faster                                                        |
| pidigits       | 190 ms                                                                | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 210 ms                                                                | 183 ms: 1.15x faster                                                         |
| regex_effbot   | 3.87 ms                                                               | 3.65 ms: 1.06x faster                                                        |
| regex_dna      | 231 ms                                                                | 226 ms: 1.02x faster                                                         |
| regex_v8       | 27.0 ms                                                               | 26.6 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.07 sec                                                              | 2.54 sec: 1.21x faster                                                       |
| xml_etree_generate   | 112 ms                                                                | 94.2 ms: 1.19x faster                                                        |
| xml_etree_process    | 79.2 ms                                                               | 66.5 ms: 1.19x faster                                                        |
| unpickle_pure_python | 294 us                                                                | 253 us: 1.16x faster                                                         |
| pickle_pure_python   | 434 us                                                                | 384 us: 1.13x faster                                                         |
| xml_etree_iterparse  | 119 ms                                                                | 108 ms: 1.10x faster                                                         |
| json_dumps           | 12.1 ms                                                               | 11.4 ms: 1.06x faster                                                        |
| xml_etree_parse      | 155 ms                                                                | 150 ms: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                        |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 17.8 ms                                                               | 13.6 ms: 1.31x faster                                                        |
| genshi_text     | 32.4 ms                                                               | 28.6 ms: 1.13x faster                                                        |
| django_template | 45.3 ms                                                               | 40.9 ms: 1.11x faster                                                        |
| genshi_xml      | 74.6 ms                                                               | 67.6 ms: 1.10x faster                                                        |
| Geometric mean  | (ref)                                                                 | 1.16x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240819-linux-x86_64-python-e077b201f49a6007ddad-3.14.0a0-e077b20 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators               | 59.6 ms                                                               | 40.2 ms: 1.48x faster                                                        |
| nbody                    | 160 ms                                                                | 120 ms: 1.34x faster                                                         |
| scimark_sparse_mat_mult  | 7.73 ms                                                               | 5.82 ms: 1.33x faster                                                        |
| comprehensions           | 31.9 us                                                               | 24.2 us: 1.32x faster                                                        |
| spectral_norm            | 184 ms                                                                | 139 ms: 1.32x faster                                                         |
| fannkuch                 | 627 ms                                                                | 478 ms: 1.31x faster                                                         |
| mako                     | 17.8 ms                                                               | 13.6 ms: 1.31x faster                                                        |
| deepcopy_memo            | 50.8 us                                                               | 38.8 us: 1.31x faster                                                        |
| deltablue                | 6.11 ms                                                               | 4.70 ms: 1.30x faster                                                        |
| logging_silent           | 172 ns                                                                | 132 ns: 1.30x faster                                                         |
| hexiom                   | 12.3 ms                                                               | 9.54 ms: 1.29x faster                                                        |
| scimark_monte_carlo      | 104 ms                                                                | 80.8 ms: 1.28x faster                                                        |
| pyflate                  | 714 ms                                                                | 558 ms: 1.28x faster                                                         |
| crypto_pyaes             | 109 ms                                                                | 87.0 ms: 1.26x faster                                                        |
| scimark_sor              | 197 ms                                                                | 157 ms: 1.25x faster                                                         |
| float                    | 105 ms                                                                | 84.3 ms: 1.25x faster                                                        |
| nqueens                  | 129 ms                                                                | 104 ms: 1.25x faster                                                         |
| richards                 | 89.7 ms                                                               | 72.0 ms: 1.25x faster                                                        |
| richards_super           | 100 ms                                                                | 80.7 ms: 1.24x faster                                                        |
| pprint_safe_repr         | 1.11 sec                                                              | 911 ms: 1.22x faster                                                         |
| scimark_lu               | 164 ms                                                                | 134 ms: 1.22x faster                                                         |
| pprint_pformat           | 2.34 sec                                                              | 1.93 sec: 1.22x faster                                                       |
| scimark_fft              | 524 ms                                                                | 433 ms: 1.21x faster                                                         |
| tomli_loads              | 3.07 sec                                                              | 2.54 sec: 1.21x faster                                                       |
| xml_etree_generate       | 112 ms                                                                | 94.2 ms: 1.19x faster                                                        |
| meteor_contest           | 145 ms                                                                | 122 ms: 1.19x faster                                                         |
| xml_etree_process        | 79.2 ms                                                               | 66.5 ms: 1.19x faster                                                        |
| bpe_tokeniser            | 6.35 sec                                                              | 5.46 sec: 1.16x faster                                                       |
| unpickle_pure_python     | 294 us                                                                | 253 us: 1.16x faster                                                         |
| sqlglot_parse            | 1.85 ms                                                               | 1.60 ms: 1.16x faster                                                        |
| regex_compile            | 210 ms                                                                | 183 ms: 1.15x faster                                                         |
| deepcopy                 | 370 us                                                                | 323 us: 1.14x faster                                                         |
| sqlglot_transpile        | 2.28 ms                                                               | 2.00 ms: 1.14x faster                                                        |
| go                       | 200 ms                                                                | 175 ms: 1.14x faster                                                         |
| chaos                    | 94.8 ms                                                               | 83.4 ms: 1.14x faster                                                        |
| genshi_text              | 32.4 ms                                                               | 28.6 ms: 1.13x faster                                                        |
| pickle_pure_python       | 434 us                                                                | 384 us: 1.13x faster                                                         |
| sqlglot_optimize         | 74.2 ms                                                               | 67.0 ms: 1.11x faster                                                        |
| django_template          | 45.3 ms                                                               | 40.9 ms: 1.11x faster                                                        |
| genshi_xml               | 74.6 ms                                                               | 67.6 ms: 1.10x faster                                                        |
| sympy_integrate          | 27.1 ms                                                               | 24.5 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 119 ms                                                                | 108 ms: 1.10x faster                                                         |
| 2to3                     | 358 ms                                                                | 327 ms: 1.10x faster                                                         |
| sqlglot_normalize        | 148 ms                                                                | 136 ms: 1.09x faster                                                         |
| telco                    | 9.54 ms                                                               | 8.76 ms: 1.09x faster                                                        |
| pycparser                | 1.60 sec                                                              | 1.47 sec: 1.09x faster                                                       |
| bench_thread_pool        | 934 us                                                                | 866 us: 1.08x faster                                                         |
| typing_runtime_protocols | 201 us                                                                | 187 us: 1.08x faster                                                         |
| sympy_str                | 361 ms                                                                | 338 ms: 1.07x faster                                                         |
| sympy_sum                | 195 ms                                                                | 183 ms: 1.07x faster                                                         |
| async_tree_none          | 374 ms                                                                | 351 ms: 1.07x faster                                                         |
| json_dumps               | 12.1 ms                                                               | 11.4 ms: 1.06x faster                                                        |
| regex_effbot             | 3.87 ms                                                               | 3.65 ms: 1.06x faster                                                        |
| sympy_expand             | 597 ms                                                                | 563 ms: 1.06x faster                                                         |
| deepcopy_reduce          | 3.19 us                                                               | 3.02 us: 1.06x faster                                                        |
| async_tree_memoization   | 479 ms                                                                | 456 ms: 1.05x faster                                                         |
| html5lib                 | 79.4 ms                                                               | 75.9 ms: 1.05x faster                                                        |
| docutils                 | 3.41 sec                                                              | 3.26 sec: 1.04x faster                                                       |
| tornado_http             | 102 ms                                                                | 98.6 ms: 1.04x faster                                                        |
| async_tree_io            | 963 ms                                                                | 931 ms: 1.03x faster                                                         |
| xml_etree_parse          | 155 ms                                                                | 150 ms: 1.03x faster                                                         |
| json                     | 5.76 ms                                                               | 5.59 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed  | 613 ms                                                                | 595 ms: 1.03x faster                                                         |
| async_tree_io_tg         | 895 ms                                                                | 875 ms: 1.02x faster                                                         |
| async_generators         | 477 ms                                                                | 467 ms: 1.02x faster                                                         |
| regex_dna                | 231 ms                                                                | 226 ms: 1.02x faster                                                         |
| pathlib                  | 17.2 ms                                                               | 16.8 ms: 1.02x faster                                                        |
| mdp                      | 2.94 sec                                                              | 2.89 sec: 1.02x faster                                                       |
| regex_v8                 | 27.0 ms                                                               | 26.6 ms: 1.01x faster                                                        |
| async_tree_none_tg       | 323 ms                                                                | 319 ms: 1.01x faster                                                         |
| logging_format           | 7.56 us                                                               | 7.48 us: 1.01x faster                                                        |
| logging_simple           | 6.69 us                                                               | 6.63 us: 1.01x faster                                                        |
| pidigits                 | 190 ms                                                                | 189 ms: 1.01x faster                                                         |
| asyncio_tcp              | 502 ms                                                                | 500 ms: 1.01x faster                                                         |
| gc_traversal             | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl          | 1.81 sec                                                              | 1.81 sec: 1.00x faster                                                       |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                        |
| python_startup_no_site   | 7.10 ms                                                               | 7.11 ms: 1.00x slower                                                        |
| thrift                   | 801 us                                                                | 807 us: 1.01x slower                                                         |
| raytrace                 | 345 ms                                                                | 349 ms: 1.01x slower                                                         |
| create_gc_cycles         | 1.76 ms                                                               | 1.78 ms: 1.01x slower                                                        |
| coroutines               | 23.4 ms                                                               | 23.9 ms: 1.02x slower                                                        |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                                 |

Benchmark hidden because not significant (7): pylint, async_tree_memoization_tg, coverage, async_tree_cpu_io_mixed_tg, json_loads, bench_mp_pool, asyncio_websockets

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.00x