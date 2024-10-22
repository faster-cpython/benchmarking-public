# Results vs. 3.10.4

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: darwin-arm64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                                            |
| docutils       | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                          |
| html5lib       | 42.4 ms                                                | 29.4 ms: 1.44x faster                                                           |
| tornado_http   | 86.7 ms                                                | 66.7 ms: 1.30x faster                                                           |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 189 ms: 2.06x faster                                                            |
| async_tree_memoization  | 474 ms                                                 | 236 ms: 2.01x faster                                                            |
| async_tree_io           | 980 ms                                                 | 538 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 448 ms: 1.45x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                           |
| nbody          | 93.0 ms                                                | 62.9 ms: 1.48x faster                                                           |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                           |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                            |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                           |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 170 us: 1.65x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 128 us: 1.52x faster                                                            |
| tomli_loads          | 1.71 sec                                               | 1.21 sec: 1.41x faster                                                          |
| xml_etree_process    | 46.5 ms                                                | 34.8 ms: 1.33x faster                                                           |
| json_dumps           | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                           |
| xml_etree_generate   | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                           |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                           |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                           |
| django_template | 26.4 ms                                                | 21.4 ms: 1.23x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 33.3 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.1 us: 3.51x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.17 ms: 2.27x faster                                                           |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                                           |
| async_tree_none          | 388 ms                                                 | 189 ms: 2.06x faster                                                            |
| async_tree_memoization   | 474 ms                                                 | 236 ms: 2.01x faster                                                            |
| logging_silent           | 117 ns                                                 | 61.0 ns: 1.92x faster                                                           |
| raytrace                 | 301 ms                                                 | 161 ms: 1.88x faster                                                            |
| async_tree_io            | 980 ms                                                 | 538 ms: 1.82x faster                                                            |
| deepcopy                 | 272 us                                                 | 154 us: 1.77x faster                                                            |
| chaos                    | 65.8 ms                                                | 38.5 ms: 1.71x faster                                                           |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.68x faster                                                           |
| pickle_pure_python       | 281 us                                                 | 170 us: 1.65x faster                                                            |
| richards                 | 48.7 ms                                                | 30.0 ms: 1.62x faster                                                           |
| scimark_sor              | 128 ms                                                 | 79.6 ms: 1.61x faster                                                           |
| go                       | 151 ms                                                 | 94.0 ms: 1.60x faster                                                           |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                           |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                           |
| asyncio_tcp              | 659 ms                                                 | 432 ms: 1.53x faster                                                            |
| logging_simple           | 4.45 us                                                | 2.93 us: 1.52x faster                                                           |
| unpickle_pure_python     | 194 us                                                 | 128 us: 1.52x faster                                                            |
| scimark_monte_carlo      | 65.6 ms                                                | 43.5 ms: 1.51x faster                                                           |
| logging_format           | 4.83 us                                                | 3.24 us: 1.49x faster                                                           |
| sqlglot_parse            | 1.24 ms                                                | 836 us: 1.49x faster                                                            |
| float                    | 69.0 ms                                                | 46.6 ms: 1.48x faster                                                           |
| nbody                    | 93.0 ms                                                | 62.9 ms: 1.48x faster                                                           |
| pylint                   | 277 ms                                                 | 191 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 448 ms: 1.45x faster                                                            |
| html5lib                 | 42.4 ms                                                | 29.4 ms: 1.44x faster                                                           |
| coroutines               | 20.7 ms                                                | 14.4 ms: 1.43x faster                                                           |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                           |
| tomli_loads              | 1.71 sec                                               | 1.21 sec: 1.41x faster                                                          |
| crypto_pyaes             | 71.8 ms                                                | 51.7 ms: 1.39x faster                                                           |
| hexiom                   | 6.19 ms                                                | 4.46 ms: 1.39x faster                                                           |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.38x faster                                                           |
| spectral_norm            | 94.8 ms                                                | 68.6 ms: 1.38x faster                                                           |
| pyflate                  | 427 ms                                                 | 309 ms: 1.38x faster                                                            |
| xml_etree_process        | 46.5 ms                                                | 34.8 ms: 1.33x faster                                                           |
| pycparser                | 877 ms                                                 | 662 ms: 1.32x faster                                                            |
| regex_compile            | 95.3 ms                                                | 72.1 ms: 1.32x faster                                                           |
| generators               | 32.3 ms                                                | 24.5 ms: 1.32x faster                                                           |
| json_dumps               | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                           |
| thrift                   | 572 us                                                 | 438 us: 1.31x faster                                                            |
| pprint_safe_repr         | 641 ms                                                 | 491 ms: 1.31x faster                                                            |
| tornado_http             | 86.7 ms                                                | 66.7 ms: 1.30x faster                                                           |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.30x faster                                                          |
| scimark_lu               | 103 ms                                                 | 79.9 ms: 1.29x faster                                                           |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                           |
| dulwich_log              | 35.3 ms                                                | 28.0 ms: 1.26x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                          |
| sympy_sum                | 92.2 ms                                                | 73.4 ms: 1.26x faster                                                           |
| django_template          | 26.4 ms                                                | 21.4 ms: 1.23x faster                                                           |
| fannkuch                 | 303 ms                                                 | 254 ms: 1.19x faster                                                            |
| scimark_fft              | 224 ms                                                 | 189 ms: 1.19x faster                                                            |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                            |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                            |
| sympy_integrate          | 13.1 ms                                                | 11.3 ms: 1.16x faster                                                           |
| dask                     | 253 ms                                                 | 221 ms: 1.14x faster                                                            |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.00 ms: 1.14x faster                                                           |
| docutils                 | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                          |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                                            |
| bench_thread_pool        | 527 us                                                 | 469 us: 1.12x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 32.9 ms: 1.12x faster                                                           |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.12x faster                                                          |
| sympy_expand             | 269 ms                                                 | 242 ms: 1.11x faster                                                            |
| nqueens                  | 63.8 ms                                                | 57.7 ms: 1.11x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 71.7 ms: 1.08x faster                                                           |
| sqlglot_normalize        | 190 ms                                                 | 176 ms: 1.08x faster                                                            |
| json                     | 3.08 ms                                                | 2.92 ms: 1.05x faster                                                           |
| xml_etree_generate       | 53.5 ms                                                | 51.1 ms: 1.05x faster                                                           |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                           |
| genshi_xml               | 33.8 ms                                                | 33.3 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                           |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                            |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                           |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                           |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                           |
| gc_traversal             | 2.36 ms                                                | 2.48 ms: 1.05x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 902 us: 1.05x slower                                                            |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                                           |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                            |
| telco                    | 3.49 ms                                                | 4.59 ms: 1.32x slower                                                           |
| bench_mp_pool            | 37.4 ms                                                | 50.9 ms: 1.36x slower                                                           |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 0.74x