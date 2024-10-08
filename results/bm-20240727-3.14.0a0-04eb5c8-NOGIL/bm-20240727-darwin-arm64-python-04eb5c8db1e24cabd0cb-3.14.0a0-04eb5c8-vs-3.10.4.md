# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 248 ms: 1.29x slower                                                  |
| docutils       | 1.73 sec                                               | 1.79 sec: 1.03x slower                                                |
| html5lib       | 42.4 ms                                                | 51.2 ms: 1.21x slower                                                 |
| tornado_http   | 86.7 ms                                                | 94.5 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 522 ms: 1.88x faster                                                  |
| async_tree_none         | 388 ms                                                 | 229 ms: 1.70x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 284 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 483 ms: 1.35x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.64x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 69.0 ms                                                | 93.2 ms: 1.35x slower                                                 |
| nbody          | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| Geometric mean | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 138 ms: 1.26x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| regex_compile  | 95.3 ms                                                | 122 ms: 1.28x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.90 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 75.8 ms: 1.05x slower                                                 |
| json_loads           | 16.4 us                                                | 19.1 us: 1.16x slower                                                 |
| tomli_loads          | 1.71 sec                                               | 2.03 sec: 1.19x slower                                                |
| pickle_pure_python   | 281 us                                                 | 342 us: 1.22x slower                                                  |
| xml_etree_process    | 46.5 ms                                                | 59.5 ms: 1.28x slower                                                 |
| xml_etree_generate   | 53.5 ms                                                | 69.1 ms: 1.29x slower                                                 |
| unpickle_pure_python | 194 us                                                 | 268 us: 1.38x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.8 ms: 1.74x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| mako            | 9.87 ms                                                | 13.6 ms: 1.38x slower                                                 |
| genshi_text     | 17.3 ms                                                | 25.4 ms: 1.46x slower                                                 |
| genshi_xml      | 33.8 ms                                                | 50.6 ms: 1.50x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.42x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 145 us: 2.23x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 350 ms: 1.89x faster                                                  |
| async_tree_io            | 980 ms                                                 | 522 ms: 1.88x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 106 ms: 1.79x faster                                                  |
| async_tree_none          | 388 ms                                                 | 229 ms: 1.70x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 284 ms: 1.67x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 483 ms: 1.35x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 656 us: 1.31x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.31x faster                                                |
| pylint                   | 277 ms                                                 | 218 ms: 1.27x faster                                                  |
| regex_dna                | 174 ms                                                 | 138 ms: 1.26x faster                                                  |
| gc_traversal             | 2.36 ms                                                | 2.03 ms: 1.17x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 31.3 us: 1.11x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 97.3 ms: 1.11x faster                                                 |
| deepcopy                 | 272 us                                                 | 249 us: 1.09x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.90 ms: 1.03x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 403 ms: 1.02x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.5 ms: 1.02x slower                                                 |
| docutils                 | 1.73 sec                                               | 1.79 sec: 1.03x slower                                                |
| xml_etree_iterparse      | 72.1 ms                                                | 75.8 ms: 1.05x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                                 |
| pathlib                  | 24.5 ms                                                | 25.9 ms: 1.06x slower                                                 |
| pycparser                | 877 ms                                                 | 933 ms: 1.06x slower                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.53 us: 1.09x slower                                                 |
| crypto_pyaes             | 71.8 ms                                                | 78.3 ms: 1.09x slower                                                 |
| tornado_http             | 86.7 ms                                                | 94.5 ms: 1.09x slower                                                 |
| json                     | 3.08 ms                                                | 3.37 ms: 1.09x slower                                                 |
| richards_super           | 57.8 ms                                                | 63.6 ms: 1.10x slower                                                 |
| logging_silent           | 117 ns                                                 | 130 ns: 1.11x slower                                                  |
| richards                 | 48.7 ms                                                | 54.2 ms: 1.11x slower                                                 |
| coroutines               | 20.7 ms                                                | 23.1 ms: 1.11x slower                                                 |
| comprehensions           | 16.9 us                                                | 18.9 us: 1.12x slower                                                 |
| generators               | 32.3 ms                                                | 36.2 ms: 1.12x slower                                                 |
| pyflate                  | 427 ms                                                 | 482 ms: 1.13x slower                                                  |
| deltablue                | 4.91 ms                                                | 5.55 ms: 1.13x slower                                                 |
| mdp                      | 1.63 sec                                               | 1.85 sec: 1.14x slower                                                |
| meteor_contest           | 77.7 ms                                                | 88.8 ms: 1.14x slower                                                 |
| chaos                    | 65.8 ms                                                | 75.5 ms: 1.15x slower                                                 |
| dulwich_log              | 35.3 ms                                                | 41.0 ms: 1.16x slower                                                 |
| json_loads               | 16.4 us                                                | 19.1 us: 1.16x slower                                                 |
| sympy_integrate          | 13.1 ms                                                | 15.5 ms: 1.18x slower                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 77.4 ms: 1.18x slower                                                 |
| scimark_fft              | 224 ms                                                 | 266 ms: 1.19x slower                                                  |
| tomli_loads              | 1.71 sec                                               | 2.03 sec: 1.19x slower                                                |
| fannkuch                 | 303 ms                                                 | 362 ms: 1.20x slower                                                  |
| thrift                   | 572 us                                                 | 687 us: 1.20x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 4.13 ms: 1.21x slower                                                 |
| html5lib                 | 42.4 ms                                                | 51.2 ms: 1.21x slower                                                 |
| nqueens                  | 63.8 ms                                                | 77.5 ms: 1.22x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 342 us: 1.22x slower                                                  |
| raytrace                 | 301 ms                                                 | 368 ms: 1.22x slower                                                  |
| scimark_sor              | 128 ms                                                 | 157 ms: 1.22x slower                                                  |
| go                       | 151 ms                                                 | 192 ms: 1.27x slower                                                  |
| hexiom                   | 6.19 ms                                                | 7.89 ms: 1.27x slower                                                 |
| xml_etree_process        | 46.5 ms                                                | 59.5 ms: 1.28x slower                                                 |
| regex_compile            | 95.3 ms                                                | 122 ms: 1.28x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 69.1 ms: 1.29x slower                                                 |
| 2to3                     | 192 ms                                                 | 248 ms: 1.29x slower                                                  |
| coverage                 | 41.5 ms                                                | 54.1 ms: 1.30x slower                                                 |
| pprint_safe_repr         | 641 ms                                                 | 836 ms: 1.30x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.70 sec: 1.31x slower                                                |
| sqlglot_transpile        | 1.44 ms                                                | 1.89 ms: 1.31x slower                                                 |
| sqlglot_parse            | 1.24 ms                                                | 1.66 ms: 1.33x slower                                                 |
| spectral_norm            | 94.8 ms                                                | 128 ms: 1.35x slower                                                  |
| float                    | 69.0 ms                                                | 93.2 ms: 1.35x slower                                                 |
| django_template          | 26.4 ms                                                | 35.9 ms: 1.36x slower                                                 |
| logging_format           | 4.83 us                                                | 6.58 us: 1.36x slower                                                 |
| logging_simple           | 4.45 us                                                | 6.07 us: 1.36x slower                                                 |
| unpickle_pure_python     | 194 us                                                 | 268 us: 1.38x slower                                                  |
| mako                     | 9.87 ms                                                | 13.6 ms: 1.38x slower                                                 |
| sympy_str                | 165 ms                                                 | 234 ms: 1.41x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 53.2 ms: 1.45x slower                                                 |
| async_generators         | 231 ms                                                 | 336 ms: 1.45x slower                                                  |
| genshi_text              | 17.3 ms                                                | 25.4 ms: 1.46x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 55.4 ms: 1.48x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 50.6 ms: 1.50x slower                                                 |
| bench_thread_pool        | 527 us                                                 | 791 us: 1.50x slower                                                  |
| scimark_lu               | 103 ms                                                 | 155 ms: 1.51x slower                                                  |
| sympy_sum                | 92.2 ms                                                | 139 ms: 1.51x slower                                                  |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                 |
| telco                    | 3.49 ms                                                | 5.65 ms: 1.62x slower                                                 |
| sympy_expand             | 269 ms                                                 | 438 ms: 1.63x slower                                                  |
| nbody                    | 93.0 ms                                                | 154 ms: 1.66x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.8 ms: 1.74x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.12x slower                                                          |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.65x