# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: darwin-arm64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 181 ms: 1.06x faster                                                     |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                   |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                    |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 233 ms: 2.03x faster                                                     |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.01x faster                                                     |
| async_tree_io           | 980 ms                                                 | 529 ms: 1.85x faster                                                     |
| async_tree_cpu_io_mixed | 649 ms                                                 | 452 ms: 1.44x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 47.1 ms: 1.47x faster                                                    |
| nbody          | 93.0 ms                                                | 63.9 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                  | 1.29x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                    |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                                     |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                    |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                  | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 176 us: 1.60x faster                                                     |
| unpickle_pure_python | 194 us                                                 | 124 us: 1.57x faster                                                     |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 36.0 ms: 1.29x faster                                                    |
| json_dumps           | 8.11 ms                                                | 6.45 ms: 1.26x faster                                                    |
| xml_etree_generate   | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                    |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 14.5 ms: 1.84x slower                                                    |
| python_startup         | 10.9 ms                                                | 21.0 ms: 1.94x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.89x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                    |
| django_template | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                    |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                    |
| genshi_xml      | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.5 us: 3.31x faster                                                    |
| deltablue                | 4.91 ms                                                | 2.39 ms: 2.06x faster                                                    |
| async_tree_memoization   | 474 ms                                                 | 233 ms: 2.03x faster                                                     |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                    |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.01x faster                                                     |
| logging_silent           | 117 ns                                                 | 62.4 ns: 1.88x faster                                                    |
| async_tree_io            | 980 ms                                                 | 529 ms: 1.85x faster                                                     |
| raytrace                 | 301 ms                                                 | 165 ms: 1.82x faster                                                     |
| deepcopy                 | 272 us                                                 | 151 us: 1.80x faster                                                     |
| richards_super           | 57.8 ms                                                | 32.5 ms: 1.78x faster                                                    |
| richards                 | 48.7 ms                                                | 29.1 ms: 1.67x faster                                                    |
| chaos                    | 65.8 ms                                                | 39.8 ms: 1.65x faster                                                    |
| pickle_pure_python       | 281 us                                                 | 176 us: 1.60x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 124 us: 1.57x faster                                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                                    |
| mako                     | 9.87 ms                                                | 6.50 ms: 1.52x faster                                                    |
| sqlglot_parse            | 1.24 ms                                                | 833 us: 1.49x faster                                                     |
| scimark_monte_carlo      | 65.6 ms                                                | 44.2 ms: 1.48x faster                                                    |
| pylint                   | 277 ms                                                 | 187 ms: 1.48x faster                                                     |
| go                       | 151 ms                                                 | 102 ms: 1.47x faster                                                     |
| float                    | 69.0 ms                                                | 47.1 ms: 1.47x faster                                                    |
| asyncio_tcp              | 659 ms                                                 | 451 ms: 1.46x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                    |
| nbody                    | 93.0 ms                                                | 63.9 ms: 1.46x faster                                                    |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 452 ms: 1.44x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                    |
| logging_format           | 4.83 us                                                | 3.39 us: 1.43x faster                                                    |
| generators               | 32.3 ms                                                | 23.1 ms: 1.40x faster                                                    |
| hexiom                   | 6.19 ms                                                | 4.48 ms: 1.38x faster                                                    |
| crypto_pyaes             | 71.8 ms                                                | 52.0 ms: 1.38x faster                                                    |
| spectral_norm            | 94.8 ms                                                | 68.7 ms: 1.38x faster                                                    |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.37x faster                                                    |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 473 ms: 1.35x faster                                                     |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                    |
| pprint_pformat           | 1.30 sec                                               | 976 ms: 1.34x faster                                                     |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                                     |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                                     |
| pycparser                | 877 ms                                                 | 676 ms: 1.30x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 36.0 ms: 1.29x faster                                                    |
| regex_compile            | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                    |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                    |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                    |
| json_dumps               | 8.11 ms                                                | 6.45 ms: 1.26x faster                                                    |
| scimark_sor              | 128 ms                                                 | 103 ms: 1.24x faster                                                     |
| sympy_sum                | 92.2 ms                                                | 74.4 ms: 1.24x faster                                                    |
| scimark_lu               | 103 ms                                                 | 83.0 ms: 1.24x faster                                                    |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                                   |
| django_template          | 26.4 ms                                                | 21.5 ms: 1.23x faster                                                    |
| fannkuch                 | 303 ms                                                 | 249 ms: 1.21x faster                                                     |
| sympy_str                | 165 ms                                                 | 139 ms: 1.19x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.18x faster                                                    |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                     |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                                     |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.04 ms: 1.13x faster                                                    |
| dask                     | 253 ms                                                 | 228 ms: 1.11x faster                                                     |
| sympy_expand             | 269 ms                                                 | 243 ms: 1.11x faster                                                     |
| bench_thread_pool        | 527 us                                                 | 478 us: 1.10x faster                                                     |
| nqueens                  | 63.8 ms                                                | 58.6 ms: 1.09x faster                                                    |
| sqlglot_optimize         | 36.8 ms                                                | 33.8 ms: 1.09x faster                                                    |
| meteor_contest           | 77.7 ms                                                | 72.2 ms: 1.08x faster                                                    |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                    |
| sqlglot_normalize        | 190 ms                                                 | 180 ms: 1.06x faster                                                     |
| 2to3                     | 192 ms                                                 | 181 ms: 1.06x faster                                                     |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                    |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                    |
| xml_etree_generate       | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                    |
| xml_etree_iterparse      | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                    |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                    |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                    |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                    |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                    |
| create_gc_cycles         | 860 us                                                 | 906 us: 1.05x slower                                                     |
| coverage                 | 41.5 ms                                                | 46.9 ms: 1.13x slower                                                    |
| genshi_xml               | 33.8 ms                                                | 39.3 ms: 1.16x slower                                                    |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                     |
| telco                    | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                    |
| bench_mp_pool            | 37.4 ms                                                | 59.0 ms: 1.58x slower                                                    |
| python_startup_no_site   | 7.91 ms                                                | 14.5 ms: 1.84x slower                                                    |
| python_startup           | 10.9 ms                                                | 21.0 ms: 1.94x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.35x