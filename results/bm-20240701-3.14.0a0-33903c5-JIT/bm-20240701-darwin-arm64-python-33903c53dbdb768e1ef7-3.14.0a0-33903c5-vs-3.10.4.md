# Results vs. 3.10.4

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: darwin-arm64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 177 ms: 1.08x faster                                                  |
| docutils       | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                |
| html5lib       | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                 |
| tornado_http   | 86.7 ms                                                | 68.4 ms: 1.27x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| async_tree_none         | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_io           | 980 ms                                                 | 508 ms: 1.93x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 47.2 ms: 1.46x faster                                                 |
| nbody          | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.6 ms: 1.29x faster                                                 |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 174 us: 1.61x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 36.2 ms: 1.29x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| xml_etree_generate   | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                 |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 14.1 ms: 1.78x slower                                                 |
| python_startup         | 10.9 ms                                                | 20.7 ms: 1.90x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.84x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.54 ms: 1.51x faster                                                 |
| django_template | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.05x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 40.7 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.4 us: 3.28x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.12x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 233 ms: 2.03x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                 |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_io            | 980 ms                                                 | 508 ms: 1.93x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.0 ns: 1.89x faster                                                 |
| raytrace                 | 301 ms                                                 | 163 ms: 1.85x faster                                                  |
| deepcopy                 | 272 us                                                 | 152 us: 1.78x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.1 ms: 1.69x faster                                                 |
| chaos                    | 65.8 ms                                                | 39.6 ms: 1.66x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 174 us: 1.61x faster                                                  |
| richards                 | 48.7 ms                                                | 30.6 ms: 1.59x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 430 ms: 1.53x faster                                                  |
| mako                     | 9.87 ms                                                | 6.54 ms: 1.51x faster                                                 |
| pylint                   | 277 ms                                                 | 184 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 828 us: 1.50x faster                                                  |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.57 us: 1.48x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 44.6 ms: 1.47x faster                                                 |
| float                    | 69.0 ms                                                | 47.2 ms: 1.46x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 994 us: 1.45x faster                                                  |
| nbody                    | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.36 us: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                  |
| generators               | 32.3 ms                                                | 23.1 ms: 1.40x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.43 ms: 1.40x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.7 ms: 1.38x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 52.1 ms: 1.38x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.9 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                |
| pyflate                  | 427 ms                                                 | 322 ms: 1.32x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 485 ms: 1.32x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 996 ms: 1.31x faster                                                  |
| thrift                   | 572 us                                                 | 437 us: 1.31x faster                                                  |
| pycparser                | 877 ms                                                 | 674 ms: 1.30x faster                                                  |
| regex_compile            | 95.3 ms                                                | 73.6 ms: 1.29x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.2 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 68.4 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.43 ms: 1.26x faster                                                 |
| scimark_sor              | 128 ms                                                 | 102 ms: 1.25x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 73.6 ms: 1.25x faster                                                 |
| django_template          | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                 |
| scimark_lu               | 103 ms                                                 | 83.0 ms: 1.24x faster                                                 |
| fannkuch                 | 303 ms                                                 | 245 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.19x faster                                                 |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                  |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                |
| dask                     | 253 ms                                                 | 225 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.05 ms: 1.12x faster                                                 |
| sympy_expand             | 269 ms                                                 | 240 ms: 1.12x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 478 us: 1.10x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.3 ms: 1.10x faster                                                 |
| nqueens                  | 63.8 ms                                                | 58.1 ms: 1.10x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                |
| 2to3                     | 192 ms                                                 | 177 ms: 1.08x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.3 ms: 1.07x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 178 ms: 1.07x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.2 ms: 1.01x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                  |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 46.7 ms: 1.13x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 40.7 ms: 1.20x slower                                                 |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                  |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 57.8 ms: 1.55x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 14.1 ms: 1.78x slower                                                 |
| python_startup           | 10.9 ms                                                | 20.7 ms: 1.90x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_iterparse, asyncio_websockets, pidigits, xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-darwin-arm64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.30x