# Results vs. 3.10.4

- fork: faster-cpython
- ref: binary_subscr_getite
- machine: linux-x86_64
- commit hash: d4df441
- commit date: 2024-08-01
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                            |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                          |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                           |
| tornado_http   | 136 ms                                                 | 92.3 ms: 1.48x faster                                                           |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 908 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                           |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                           |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.89 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| django_template | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.7 ms: 1.25x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                            |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.49 ms: 2.27x faster                                                           |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 28.5 us: 2.05x faster                                                           |
| richards_super           | 94.7 ms                                                | 46.9 ms: 2.02x faster                                                           |
| chaos                    | 115 ms                                                 | 57.4 ms: 2.01x faster                                                           |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.98x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 60.1 ms: 1.97x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 908 ms: 1.95x faster                                                            |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                                            |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                           |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 67.5 ms: 1.89x faster                                                           |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 499 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                           |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                           |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.65x faster                                                          |
| mako                     | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                            |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                            |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                           |
| pylint                   | 551 ms                                                 | 354 ms: 1.56x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                           |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                           |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.38 ms: 1.48x faster                                                           |
| tornado_http             | 136 ms                                                 | 92.3 ms: 1.48x faster                                                           |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 55.5 ms: 1.42x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                          |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                            |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                            |
| django_template          | 48.2 ms                                                | 35.6 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                          |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                           |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 52.7 ms: 1.25x faster                                                           |
| nqueens                  | 106 ms                                                 | 84.6 ms: 1.25x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                           |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 815 us: 1.21x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                           |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                            |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                          |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.13x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                           |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                                          |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.02x slower                                                           |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.89 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                           |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                           |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240801-3.14.0a0-d4df441-JIT/bm-20240801-linux-x86_64-faster%2dcpython-binary_subscr_getite-3.14.0a0-d4df441.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x