# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: darwin-arm64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 258 ms: 1.35x slower                                                  |
| docutils       | 1.73 sec                                               | 1.88 sec: 1.08x slower                                                |
| html5lib       | 42.4 ms                                                | 54.3 ms: 1.28x slower                                                 |
| tornado_http   | 86.7 ms                                                | 109 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.24x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 566 ms: 1.73x faster                                                  |
| async_tree_none         | 388 ms                                                 | 243 ms: 1.59x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 307 ms: 1.54x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 503 ms: 1.29x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.53x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 69.0 ms                                                | 103 ms: 1.50x slower                                                  |
| nbody          | 93.0 ms                                                | 158 ms: 1.70x slower                                                  |
| Geometric mean | (ref)                                                  | 1.36x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 139 ms: 1.25x faster                                                  |
| regex_v8       | 17.1 ms                                                | 18.0 ms: 1.05x slower                                                 |
| regex_compile  | 95.3 ms                                                | 137 ms: 1.44x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| json_dumps           | 8.11 ms                                                | 8.50 ms: 1.05x slower                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 84.8 ms: 1.18x slower                                                 |
| json_loads           | 16.4 us                                                | 19.5 us: 1.19x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 2.19 sec: 1.28x slower                                                |
| pickle_pure_python   | 281 us                                                 | 375 us: 1.34x slower                                                  |
| xml_etree_process    | 46.5 ms                                                | 66.5 ms: 1.43x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                | 77.8 ms: 1.45x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 293 us: 1.50x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.26x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.64x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 14.5 ms: 1.47x slower                                                 |
| django_template | 26.4 ms                                                | 39.3 ms: 1.49x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 55.9 ms: 1.65x slower                                                 |
| genshi_text     | 17.3 ms                                                | 31.2 ms: 1.80x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.60x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 172 us: 1.88x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 352 ms: 1.87x faster                                                  |
| async_tree_io            | 980 ms                                                 | 566 ms: 1.73x faster                                                  |
| async_tree_none          | 388 ms                                                 | 243 ms: 1.59x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 121 ms: 1.57x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 307 ms: 1.54x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 503 ms: 1.29x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.25 sec: 1.28x faster                                                |
| create_gc_cycles         | 860 us                                                 | 673 us: 1.28x faster                                                  |
| regex_dna                | 174 ms                                                 | 139 ms: 1.25x faster                                                  |
| pylint                   | 277 ms                                                 | 228 ms: 1.22x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.04 ms: 1.16x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 405 ms: 1.01x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 18.0 ms: 1.05x slower                                                 |
| json_dumps               | 8.11 ms                                                | 8.50 ms: 1.05x slower                                                 |
| deepcopy                 | 272 us                                                 | 285 us: 1.05x slower                                                  |
| deepcopy_memo            | 34.7 us                                                | 36.6 us: 1.05x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.88 sec: 1.08x slower                                                |
| pathlib                  | 24.5 ms                                                | 26.6 ms: 1.08x slower                                                 |
| generators               | 32.3 ms                                                | 35.1 ms: 1.09x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 79.5 ms: 1.11x slower                                                 |
| pycparser                | 877 ms                                                 | 974 ms: 1.11x slower                                                  |
| json                     | 3.08 ms                                                | 3.45 ms: 1.12x slower                                                 |
| comprehensions           | 16.9 us                                                | 19.4 us: 1.15x slower                                                 |
| mdp                      | 1.63 sec                                               | 1.88 sec: 1.16x slower                                                |
| logging_silent           | 117 ns                                                 | 136 ns: 1.16x slower                                                  |
| pyflate                  | 427 ms                                                 | 498 ms: 1.17x slower                                                  |
| fannkuch                 | 303 ms                                                 | 355 ms: 1.17x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 84.8 ms: 1.18x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 92.3 ms: 1.19x slower                                                 |
| json_loads               | 16.4 us                                                | 19.5 us: 1.19x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.90 ms: 1.20x slower                                                 |
| dulwich_log              | 35.3 ms                                                | 42.7 ms: 1.21x slower                                                 |
| richards_super           | 57.8 ms                                                | 70.3 ms: 1.22x slower                                                 |
| chaos                    | 65.8 ms                                                | 80.1 ms: 1.22x slower                                                 |
| scimark_fft              | 224 ms                                                 | 276 ms: 1.23x slower                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.87 us: 1.23x slower                                                 |
| coroutines               | 20.7 ms                                                | 25.6 ms: 1.24x slower                                                 |
| sympy_integrate          | 13.1 ms                                                | 16.3 ms: 1.24x slower                                                 |
| nqueens                  | 63.8 ms                                                | 79.1 ms: 1.24x slower                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 81.3 ms: 1.24x slower                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.26 ms: 1.25x slower                                                 |
| tornado_http             | 86.7 ms                                                | 109 ms: 1.25x slower                                                  |
| richards                 | 48.7 ms                                                | 61.8 ms: 1.27x slower                                                 |
| html5lib                 | 42.4 ms                                                | 54.3 ms: 1.28x slower                                                 |
| tomli_loads              | 1.71 sec                                               | 2.19 sec: 1.28x slower                                                |
| raytrace                 | 301 ms                                                 | 387 ms: 1.29x slower                                                  |
| scimark_sor              | 128 ms                                                 | 165 ms: 1.29x slower                                                  |
| thrift                   | 572 us                                                 | 738 us: 1.29x slower                                                  |
| hexiom                   | 6.19 ms                                                | 8.06 ms: 1.30x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 375 us: 1.34x slower                                                  |
| 2to3                     | 192 ms                                                 | 258 ms: 1.35x slower                                                  |
| go                       | 151 ms                                                 | 205 ms: 1.36x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 2.01 ms: 1.40x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.75 ms: 1.41x slower                                                 |
| coverage                 | 41.5 ms                                                | 59.2 ms: 1.43x slower                                                 |
| xml_etree_process        | 46.5 ms                                                | 66.5 ms: 1.43x slower                                                 |
| regex_compile            | 95.3 ms                                                | 137 ms: 1.44x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.89 sec: 1.45x slower                                                |
| pprint_safe_repr         | 641 ms                                                 | 930 ms: 1.45x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 77.8 ms: 1.45x slower                                                 |
| mako                     | 9.87 ms                                                | 14.5 ms: 1.47x slower                                                 |
| logging_format           | 4.83 us                                                | 7.12 us: 1.47x slower                                                 |
| logging_simple           | 4.45 us                                                | 6.57 us: 1.48x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 55.6 ms: 1.49x slower                                                 |
| async_generators         | 231 ms                                                 | 345 ms: 1.49x slower                                                  |
| django_template          | 26.4 ms                                                | 39.3 ms: 1.49x slower                                                 |
| sympy_str                | 165 ms                                                 | 247 ms: 1.50x slower                                                  |
| float                    | 69.0 ms                                                | 103 ms: 1.50x slower                                                  |
| unpickle_pure_python     | 194 us                                                 | 293 us: 1.50x slower                                                  |
| spectral_norm            | 94.8 ms                                                | 143 ms: 1.51x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 811 us: 1.54x slower                                                  |
| python_startup           | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                 |
| sympy_sum                | 92.2 ms                                                | 145 ms: 1.58x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 55.9 ms: 1.65x slower                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 60.9 ms: 1.66x slower                                                 |
| scimark_lu               | 103 ms                                                 | 174 ms: 1.69x slower                                                  |
| telco                    | 3.49 ms                                                | 5.91 ms: 1.69x slower                                                 |
| nbody                    | 93.0 ms                                                | 158 ms: 1.70x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.6 ms: 1.72x slower                                                 |
| sympy_expand             | 269 ms                                                 | 464 ms: 1.72x slower                                                  |
| genshi_text              | 17.3 ms                                                | 31.2 ms: 1.80x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.19x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240817-3.14.0a0-79c542b-NOGIL/bm-20240817-darwin-arm64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.19x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 0.52x