# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: darwin-arm64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 163 ms: 1.18x faster                                                            |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                          |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                           |
| tornado_http   | 86.7 ms                                                | 66.3 ms: 1.31x faster                                                           |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 195 ms: 1.99x faster                                                            |
| async_tree_memoization  | 474 ms                                                 | 241 ms: 1.96x faster                                                            |
| async_tree_io           | 980 ms                                                 | 544 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 452 ms: 1.44x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.1 ms: 1.57x faster                                                           |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                           |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.1 ms: 1.38x faster                                                           |
| regex_dna      | 174 ms                                                 | 150 ms: 1.17x faster                                                            |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                           |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 185 us: 1.52x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 145 us: 1.35x faster                                                            |
| json_dumps           | 8.11 ms                                                | 6.45 ms: 1.26x faster                                                           |
| xml_etree_process    | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                           |
| tomli_loads          | 1.71 sec                                               | 1.50 sec: 1.14x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                | 53.7 ms: 1.00x slower                                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                           |
| json_loads           | 16.4 us                                                | 17.4 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.5 ms: 1.42x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.98 ms: 1.41x faster                                                           |
| django_template | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                           |
| genshi_text     | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 30.5 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.2 us: 3.50x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.13 ms: 2.31x faster                                                           |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                           |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                            |
| async_tree_none          | 388 ms                                                 | 195 ms: 1.99x faster                                                            |
| logging_silent           | 117 ns                                                 | 59.5 ns: 1.97x faster                                                           |
| async_tree_memoization   | 474 ms                                                 | 241 ms: 1.96x faster                                                            |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                            |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                           |
| async_tree_io            | 980 ms                                                 | 544 ms: 1.80x faster                                                            |
| sqlglot_parse            | 1.24 ms                                                | 748 us: 1.66x faster                                                            |
| richards_super           | 57.8 ms                                                | 34.8 ms: 1.66x faster                                                           |
| comprehensions           | 16.9 us                                                | 10.4 us: 1.62x faster                                                           |
| sqlglot_transpile        | 1.44 ms                                                | 908 us: 1.59x faster                                                            |
| nbody                    | 93.0 ms                                                | 59.1 ms: 1.57x faster                                                           |
| generators               | 32.3 ms                                                | 20.6 ms: 1.57x faster                                                           |
| asyncio_tcp              | 659 ms                                                 | 423 ms: 1.56x faster                                                            |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.55x faster                                                           |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                           |
| go                       | 151 ms                                                 | 98.8 ms: 1.53x faster                                                           |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                            |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                           |
| pickle_pure_python       | 281 us                                                 | 185 us: 1.52x faster                                                            |
| hexiom                   | 6.19 ms                                                | 4.12 ms: 1.50x faster                                                           |
| scimark_lu               | 103 ms                                                 | 70.5 ms: 1.46x faster                                                           |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                           |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 452 ms: 1.44x faster                                                            |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                           |
| mako                     | 9.87 ms                                                | 6.98 ms: 1.41x faster                                                           |
| crypto_pyaes             | 71.8 ms                                                | 51.1 ms: 1.41x faster                                                           |
| spectral_norm            | 94.8 ms                                                | 67.6 ms: 1.40x faster                                                           |
| regex_compile            | 95.3 ms                                                | 69.1 ms: 1.38x faster                                                           |
| pycparser                | 877 ms                                                 | 641 ms: 1.37x faster                                                            |
| pprint_pformat           | 1.30 sec                                               | 967 ms: 1.35x faster                                                            |
| pprint_safe_repr         | 641 ms                                                 | 475 ms: 1.35x faster                                                            |
| unpickle_pure_python     | 194 us                                                 | 145 us: 1.35x faster                                                            |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                           |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                           |
| pyflate                  | 427 ms                                                 | 324 ms: 1.32x faster                                                            |
| scimark_sor              | 128 ms                                                 | 97.4 ms: 1.32x faster                                                           |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                                            |
| tornado_http             | 86.7 ms                                                | 66.3 ms: 1.31x faster                                                           |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                           |
| sympy_sum                | 92.2 ms                                                | 71.6 ms: 1.29x faster                                                           |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                          |
| json_dumps               | 8.11 ms                                                | 6.45 ms: 1.26x faster                                                           |
| sympy_integrate          | 13.1 ms                                                | 10.5 ms: 1.25x faster                                                           |
| genshi_text              | 17.3 ms                                                | 14.1 ms: 1.23x faster                                                           |
| xml_etree_process        | 46.5 ms                                                | 37.9 ms: 1.23x faster                                                           |
| sympy_str                | 165 ms                                                 | 135 ms: 1.23x faster                                                            |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.84 ms: 1.21x faster                                                           |
| scimark_fft              | 224 ms                                                 | 187 ms: 1.20x faster                                                            |
| nqueens                  | 63.8 ms                                                | 53.8 ms: 1.19x faster                                                           |
| 2to3                     | 192 ms                                                 | 163 ms: 1.18x faster                                                            |
| sympy_expand             | 269 ms                                                 | 230 ms: 1.17x faster                                                            |
| regex_dna                | 174 ms                                                 | 150 ms: 1.17x faster                                                            |
| bench_thread_pool        | 527 us                                                 | 453 us: 1.16x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 31.6 ms: 1.16x faster                                                           |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                          |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                            |
| tomli_loads              | 1.71 sec                                               | 1.50 sec: 1.14x faster                                                          |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                            |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                          |
| sqlglot_normalize        | 190 ms                                                 | 171 ms: 1.11x faster                                                            |
| genshi_xml               | 33.8 ms                                                | 30.5 ms: 1.11x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 72.8 ms: 1.07x faster                                                           |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                           |
| json                     | 3.08 ms                                                | 3.01 ms: 1.02x faster                                                           |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                            |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                            |
| xml_etree_generate       | 53.5 ms                                                | 53.7 ms: 1.00x slower                                                           |
| xml_etree_iterparse      | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                           |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                           |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 906 us: 1.05x slower                                                            |
| json_loads               | 16.4 us                                                | 17.4 us: 1.06x slower                                                           |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                           |
| coverage                 | 41.5 ms                                                | 45.6 ms: 1.10x slower                                                           |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                                            |
| bench_mp_pool            | 37.4 ms                                                | 49.0 ms: 1.31x slower                                                           |
| telco                    | 3.49 ms                                                | 4.79 ms: 1.37x slower                                                           |
| python_startup           | 10.9 ms                                                | 15.5 ms: 1.42x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240731-3.14.0a0-1a2b0b8/bm-20240731-darwin-arm64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.01x