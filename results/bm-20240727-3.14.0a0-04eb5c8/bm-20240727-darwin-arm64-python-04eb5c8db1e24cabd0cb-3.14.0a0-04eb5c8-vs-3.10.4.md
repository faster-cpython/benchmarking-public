# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 163 ms: 1.18x faster                                                  |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.16x faster                                                |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.6 ms: 1.30x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 195 ms: 1.99x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 241 ms: 1.96x faster                                                  |
| async_tree_io           | 980 ms                                                 | 545 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 451 ms: 1.44x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 61.7 ms: 1.51x faster                                                 |
| float          | 69.0 ms                                                | 48.1 ms: 1.44x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 144 us: 1.35x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.37 ms: 1.27x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 53.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 72.6 ms: 1.01x slower                                                 |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.2 ms: 1.40x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.5 ms: 1.58x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.49x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.04 ms: 1.40x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.2 ms: 1.23x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.7 us: 3.45x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.11 ms: 2.33x faster                                                 |
| raytrace                 | 301 ms                                                 | 147 ms: 2.05x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.05x faster                                                 |
| async_tree_none          | 388 ms                                                 | 195 ms: 1.99x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 241 ms: 1.96x faster                                                  |
| logging_silent           | 117 ns                                                 | 59.7 ns: 1.96x faster                                                 |
| chaos                    | 65.8 ms                                                | 34.9 ms: 1.88x faster                                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.88x faster                                                  |
| async_tree_io            | 980 ms                                                 | 545 ms: 1.80x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 742 us: 1.68x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 905 us: 1.59x faster                                                  |
| generators               | 32.3 ms                                                | 20.6 ms: 1.57x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.49 us: 1.56x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.5 ms: 1.54x faster                                                 |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                  |
| go                       | 151 ms                                                 | 98.1 ms: 1.54x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 431 ms: 1.53x faster                                                  |
| nbody                    | 93.0 ms                                                | 61.7 ms: 1.51x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.12 ms: 1.50x faster                                                 |
| scimark_lu               | 103 ms                                                 | 69.5 ms: 1.48x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.08 us: 1.45x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 451 ms: 1.44x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 65.9 ms: 1.44x faster                                                 |
| float                    | 69.0 ms                                                | 48.1 ms: 1.44x faster                                                 |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 7.04 ms: 1.40x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 955 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 470 ms: 1.36x faster                                                  |
| pycparser                | 877 ms                                                 | 643 ms: 1.36x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 144 us: 1.35x faster                                                  |
| scimark_sor              | 128 ms                                                 | 95.1 ms: 1.35x faster                                                 |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                 |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                                  |
| thrift                   | 572 us                                                 | 432 us: 1.32x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 70.0 ms: 1.32x faster                                                 |
| tornado_http             | 86.7 ms                                                | 66.6 ms: 1.30x faster                                                 |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.37 ms: 1.27x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                 |
| sympy_str                | 165 ms                                                 | 133 ms: 1.24x faster                                                  |
| scimark_fft              | 224 ms                                                 | 182 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.2 ms: 1.23x faster                                                 |
| nqueens                  | 63.8 ms                                                | 53.6 ms: 1.19x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 449 us: 1.18x faster                                                  |
| 2to3                     | 192 ms                                                 | 163 ms: 1.18x faster                                                  |
| sympy_expand             | 269 ms                                                 | 229 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.16x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.16x faster                                                |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                  |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.9 ms: 1.08x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 53.0 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 72.6 ms: 1.01x slower                                                 |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                                 |
| async_generators         | 231 ms                                                 | 281 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.1 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.2 ms: 1.40x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.5 ms: 1.58x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.63x