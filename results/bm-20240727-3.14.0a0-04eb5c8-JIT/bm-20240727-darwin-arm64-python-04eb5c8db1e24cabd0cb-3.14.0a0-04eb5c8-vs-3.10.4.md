# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                  |
| docutils       | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                |
| html5lib       | 42.4 ms                                                | 30.6 ms: 1.38x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 195 ms: 2.00x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 241 ms: 1.96x faster                                                  |
| async_tree_io           | 980 ms                                                 | 544 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 454 ms: 1.43x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 45.9 ms: 1.50x faster                                                 |
| nbody          | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.8 ms: 1.31x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 171 us: 1.64x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                |
| xml_etree_process    | 46.5 ms                                                | 35.4 ms: 1.31x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 70.9 ms: 1.02x faster                                                 |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.39 ms: 1.54x faster                                                 |
| django_template | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                 |
| genshi_text     | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 40.4 ms: 1.19x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.1 us: 3.40x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.27 ms: 2.16x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.5 us: 2.11x faster                                                 |
| async_tree_none          | 388 ms                                                 | 195 ms: 2.00x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 241 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.0 ns: 1.92x faster                                                 |
| raytrace                 | 301 ms                                                 | 160 ms: 1.89x faster                                                  |
| async_tree_io            | 980 ms                                                 | 544 ms: 1.80x faster                                                  |
| deepcopy                 | 272 us                                                 | 151 us: 1.80x faster                                                  |
| chaos                    | 65.8 ms                                                | 38.5 ms: 1.71x faster                                                 |
| richards_super           | 57.8 ms                                                | 33.9 ms: 1.70x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 171 us: 1.64x faster                                                  |
| richards                 | 48.7 ms                                                | 30.2 ms: 1.61x faster                                                 |
| mako                     | 9.87 ms                                                | 6.39 ms: 1.54x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.7 ms: 1.53x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 820 us: 1.52x faster                                                  |
| logging_simple           | 4.45 us                                                | 2.94 us: 1.51x faster                                                 |
| go                       | 151 ms                                                 | 99.7 ms: 1.51x faster                                                 |
| generators               | 32.3 ms                                                | 21.5 ms: 1.50x faster                                                 |
| float                    | 69.0 ms                                                | 45.9 ms: 1.50x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.49x faster                                                 |
| logging_format           | 4.83 us                                                | 3.24 us: 1.49x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 444 ms: 1.48x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                 |
| pylint                   | 277 ms                                                 | 189 ms: 1.47x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 996 us: 1.45x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 454 ms: 1.43x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 66.9 ms: 1.42x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.38 ms: 1.41x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.4 ms: 1.40x faster                                                 |
| html5lib                 | 42.4 ms                                                | 30.6 ms: 1.38x faster                                                 |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.38x faster                                                |
| pyflate                  | 427 ms                                                 | 310 ms: 1.38x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 477 ms: 1.34x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 974 ms: 1.34x faster                                                  |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.4 ms: 1.31x faster                                                 |
| pycparser                | 877 ms                                                 | 670 ms: 1.31x faster                                                  |
| regex_compile            | 95.3 ms                                                | 72.8 ms: 1.31x faster                                                 |
| scimark_lu               | 103 ms                                                 | 79.6 ms: 1.29x faster                                                 |
| scimark_sor              | 128 ms                                                 | 99.6 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.38 ms: 1.27x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 73.1 ms: 1.26x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 28.2 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| django_template          | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| fannkuch                 | 303 ms                                                 | 249 ms: 1.21x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.87 ms: 1.19x faster                                                 |
| sympy_str                | 165 ms                                                 | 139 ms: 1.19x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.18x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                |
| docutils                 | 1.73 sec                                               | 1.53 sec: 1.13x faster                                                |
| dask                     | 253 ms                                                 | 224 ms: 1.13x faster                                                  |
| nqueens                  | 63.8 ms                                                | 56.6 ms: 1.13x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 470 us: 1.12x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 32.8 ms: 1.12x faster                                                 |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 240 ms: 1.12x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 71.0 ms: 1.10x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 175 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                                 |
| genshi_text              | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 52.0 ms: 1.03x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.9 ms: 1.02x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 907 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.1 ms: 1.09x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 40.4 ms: 1.19x slower                                                 |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                  |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                 |
| bench_mp_pool            | 37.4 ms                                                | 50.9 ms: 1.36x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.54x