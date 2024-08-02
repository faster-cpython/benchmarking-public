# Results vs. base

- fork: python
- ref: 44995aab499b09a550de
- machine: linux-aarch64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 302 ms                                                                                                              | 362 ms: 1.20x slower                                                                                                    |
| chameleon      | 9.02 ms                                                                                                             | 9.14 ms: 1.01x slower                                                                                                   |
| docutils       | 3.13 sec                                                                                                            | 3.55 sec: 1.13x slower                                                                                                  |
| tornado_http   | 131 ms                                                                                                              | 141 ms: 1.07x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 90.5 ms                                                                                                             | 89.8 ms: 1.01x faster                                                                                                   |
| nbody          | 112 ms                                                                                                              | 116 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.01x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 256 ms                                                                                                              | 248 ms: 1.03x faster                                                                                                    |
| regex_v8       | 31.2 ms                                                                                                             | 30.2 ms: 1.03x faster                                                                                                   |
| regex_effbot   | 4.94 ms                                                                                                             | 4.87 ms: 1.02x faster                                                                                                   |
| regex_compile  | 128 ms                                                                                                              | 167 ms: 1.30x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| json_loads           | 32.6 us                                                                                                             | 32.1 us: 1.02x faster                                                                                                   |
| unpickle             | 19.7 us                                                                                                             | 19.6 us: 1.01x faster                                                                                                   |
| xml_etree_iterparse  | 149 ms                                                                                                              | 151 ms: 1.01x slower                                                                                                    |
| pickle_list          | 5.12 us                                                                                                             | 5.20 us: 1.02x slower                                                                                                   |
| pickle_dict          | 37.5 us                                                                                                             | 38.2 us: 1.02x slower                                                                                                   |
| unpickle_list        | 6.46 us                                                                                                             | 6.65 us: 1.03x slower                                                                                                   |
| xml_etree_generate   | 113 ms                                                                                                              | 118 ms: 1.04x slower                                                                                                    |
| tomli_loads          | 2.54 sec                                                                                                            | 2.65 sec: 1.04x slower                                                                                                  |
| pickle_pure_python   | 361 us                                                                                                              | 393 us: 1.09x slower                                                                                                    |
| unpickle_pure_python | 251 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                                                                             | 15.1 ms: 1.20x slower                                                                                                   |
| python_startup_no_site | 8.47 ms                                                                                                             | 10.8 ms: 1.27x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                               | 1.24x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.3 ms                                                                                                             | 49.5 ms: 1.20x slower                                                                                                   |
| genshi_text     | 27.9 ms                                                                                                             | 33.9 ms: 1.22x slower                                                                                                   |
| genshi_xml      | 61.0 ms                                                                                                             | 82.0 ms: 1.34x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                               | 1.18x slower                                                                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json | results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-arminc-aarch64-python-44995aab499b09a550de-3.13.0b1+-44995aa.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna                | 256 ms                                                                                                              | 248 ms: 1.03x faster                                                                                                    |
| regex_v8                 | 31.2 ms                                                                                                             | 30.2 ms: 1.03x faster                                                                                                   |
| json_loads               | 32.6 us                                                                                                             | 32.1 us: 1.02x faster                                                                                                   |
| regex_effbot             | 4.94 ms                                                                                                             | 4.87 ms: 1.02x faster                                                                                                   |
| json                     | 5.73 ms                                                                                                             | 5.65 ms: 1.01x faster                                                                                                   |
| unpickle                 | 19.7 us                                                                                                             | 19.6 us: 1.01x faster                                                                                                   |
| float                    | 90.5 ms                                                                                                             | 89.8 ms: 1.01x faster                                                                                                   |
| richards                 | 54.9 ms                                                                                                             | 55.2 ms: 1.01x slower                                                                                                   |
| chameleon                | 9.02 ms                                                                                                             | 9.14 ms: 1.01x slower                                                                                                   |
| xml_etree_iterparse      | 149 ms                                                                                                              | 151 ms: 1.01x slower                                                                                                    |
| pickle_list              | 5.12 us                                                                                                             | 5.20 us: 1.02x slower                                                                                                   |
| coverage                 | 97.5 ms                                                                                                             | 99.1 ms: 1.02x slower                                                                                                   |
| pickle_dict              | 37.5 us                                                                                                             | 38.2 us: 1.02x slower                                                                                                   |
| pathlib                  | 22.9 ms                                                                                                             | 23.4 ms: 1.02x slower                                                                                                   |
| telco                    | 164 ms                                                                                                              | 167 ms: 1.02x slower                                                                                                    |
| create_gc_cycles         | 2.40 ms                                                                                                             | 2.45 ms: 1.02x slower                                                                                                   |
| asyncio_tcp_ssl          | 2.22 sec                                                                                                            | 2.27 sec: 1.02x slower                                                                                                  |
| scimark_fft              | 446 ms                                                                                                              | 458 ms: 1.03x slower                                                                                                    |
| unpickle_list            | 6.46 us                                                                                                             | 6.65 us: 1.03x slower                                                                                                   |
| logging_simple           | 7.12 us                                                                                                             | 7.33 us: 1.03x slower                                                                                                   |
| gc_traversal             | 5.13 ms                                                                                                             | 5.30 ms: 1.03x slower                                                                                                   |
| fannkuch                 | 463 ms                                                                                                              | 479 ms: 1.03x slower                                                                                                    |
| nbody                    | 112 ms                                                                                                              | 116 ms: 1.04x slower                                                                                                    |
| xml_etree_generate       | 113 ms                                                                                                              | 118 ms: 1.04x slower                                                                                                    |
| mdp                      | 3.35 sec                                                                                                            | 3.48 sec: 1.04x slower                                                                                                  |
| meteor_contest           | 114 ms                                                                                                              | 119 ms: 1.04x slower                                                                                                    |
| spectral_norm            | 140 ms                                                                                                              | 146 ms: 1.04x slower                                                                                                    |
| bench_thread_pool        | 1.27 ms                                                                                                             | 1.32 ms: 1.04x slower                                                                                                   |
| tomli_loads              | 2.54 sec                                                                                                            | 2.65 sec: 1.04x slower                                                                                                  |
| typing_runtime_protocols | 197 us                                                                                                              | 207 us: 1.05x slower                                                                                                    |
| logging_silent           | 133 ns                                                                                                              | 140 ns: 1.05x slower                                                                                                    |
| dask                     | 377 ms                                                                                                              | 397 ms: 1.05x slower                                                                                                    |
| async_generators         | 488 ms                                                                                                              | 514 ms: 1.05x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.57 ms                                                                                                             | 6.97 ms: 1.06x slower                                                                                                   |
| scimark_monte_carlo      | 82.3 ms                                                                                                             | 87.6 ms: 1.06x slower                                                                                                   |
| crypto_pyaes             | 81.2 ms                                                                                                             | 86.6 ms: 1.07x slower                                                                                                   |
| tornado_http             | 131 ms                                                                                                              | 141 ms: 1.07x slower                                                                                                    |
| gunicorn                 | 1.21 ms                                                                                                             | 1.31 ms: 1.08x slower                                                                                                   |
| pickle_pure_python       | 361 us                                                                                                              | 393 us: 1.09x slower                                                                                                    |
| sqlglot_parse            | 1.45 ms                                                                                                             | 1.59 ms: 1.10x slower                                                                                                   |
| raytrace                 | 297 ms                                                                                                              | 327 ms: 1.10x slower                                                                                                    |
| asyncio_tcp              | 568 ms                                                                                                              | 624 ms: 1.10x slower                                                                                                    |
| pyflate                  | 557 ms                                                                                                              | 613 ms: 1.10x slower                                                                                                    |
| bench_mp_pool            | 7.16 ms                                                                                                             | 7.87 ms: 1.10x slower                                                                                                   |
| go                       | 162 ms                                                                                                              | 178 ms: 1.10x slower                                                                                                    |
| unpickle_pure_python     | 251 us                                                                                                              | 277 us: 1.10x slower                                                                                                    |
| scimark_sor              | 158 ms                                                                                                              | 175 ms: 1.11x slower                                                                                                    |
| pycparser                | 1.23 sec                                                                                                            | 1.36 sec: 1.11x slower                                                                                                  |
| aiohttp                  | 1.19 ms                                                                                                             | 1.34 ms: 1.13x slower                                                                                                   |
| deepcopy                 | 443 us                                                                                                              | 502 us: 1.13x slower                                                                                                    |
| docutils                 | 3.13 sec                                                                                                            | 3.55 sec: 1.13x slower                                                                                                  |
| sqlglot_optimize         | 62.6 ms                                                                                                             | 71.3 ms: 1.14x slower                                                                                                   |
| comprehensions           | 20.2 us                                                                                                             | 23.1 us: 1.14x slower                                                                                                   |
| sqlglot_normalize        | 128 ms                                                                                                              | 146 ms: 1.14x slower                                                                                                    |
| deepcopy_reduce          | 4.04 us                                                                                                             | 4.66 us: 1.15x slower                                                                                                   |
| pprint_safe_repr         | 953 ms                                                                                                              | 1.11 sec: 1.17x slower                                                                                                  |
| dulwich_log              | 58.7 ms                                                                                                             | 68.7 ms: 1.17x slower                                                                                                   |
| sqlglot_transpile        | 1.72 ms                                                                                                             | 2.03 ms: 1.18x slower                                                                                                   |
| sympy_expand             | 463 ms                                                                                                              | 548 ms: 1.18x slower                                                                                                    |
| nqueens                  | 99.0 ms                                                                                                             | 118 ms: 1.19x slower                                                                                                    |
| deltablue                | 3.88 ms                                                                                                             | 4.63 ms: 1.19x slower                                                                                                   |
| 2to3                     | 302 ms                                                                                                              | 362 ms: 1.20x slower                                                                                                    |
| python_startup           | 12.6 ms                                                                                                             | 15.1 ms: 1.20x slower                                                                                                   |
| django_template          | 41.3 ms                                                                                                             | 49.5 ms: 1.20x slower                                                                                                   |
| pprint_pformat           | 1.93 sec                                                                                                            | 2.32 sec: 1.20x slower                                                                                                  |
| sympy_str                | 270 ms                                                                                                              | 324 ms: 1.20x slower                                                                                                    |
| pylint                   | 340 ms                                                                                                              | 411 ms: 1.21x slower                                                                                                    |
| genshi_text              | 27.9 ms                                                                                                             | 33.9 ms: 1.22x slower                                                                                                   |
| sympy_integrate          | 21.0 ms                                                                                                             | 26.0 ms: 1.24x slower                                                                                                   |
| mypy2                    | 762 ms                                                                                                              | 946 ms: 1.24x slower                                                                                                    |
| sympy_sum                | 145 ms                                                                                                              | 182 ms: 1.25x slower                                                                                                    |
| python_startup_no_site   | 8.47 ms                                                                                                             | 10.8 ms: 1.27x slower                                                                                                   |
| hexiom                   | 7.01 ms                                                                                                             | 8.97 ms: 1.28x slower                                                                                                   |
| regex_compile            | 128 ms                                                                                                              | 167 ms: 1.30x slower                                                                                                    |
| chaos                    | 67.9 ms                                                                                                             | 89.2 ms: 1.31x slower                                                                                                   |
| scimark_lu               | 138 ms                                                                                                              | 184 ms: 1.34x slower                                                                                                    |
| genshi_xml               | 61.0 ms                                                                                                             | 82.0 ms: 1.34x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                               | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (24): xml_etree_parse, async_tree_memoization_tg, json_dumps, deepcopy_memo, coroutines, xml_etree_process, sqlite_synth, richards_super, asyncio_websockets, mako, async_tree_none_tg, pidigits, thrift, pickle, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, logging_format, html5lib, async_tree_cpu_io_mixed_tg, generators, flaskblogging

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x