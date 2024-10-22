# Results vs. 3.10.4

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: darwin-arm64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.75x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.34x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 236 ms: 2.00x faster                                                  |
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| async_tree_io           | 980 ms                                                 | 532 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 457 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| float          | 69.0 ms                                                | 49.4 ms: 1.40x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.8 ms: 1.04x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.36 ms: 1.28x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 52.7 ms: 1.01x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.1 ms: 1.39x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.47x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.19 ms: 1.37x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 90.8 us: 3.56x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.12 ms: 2.32x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.05x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 236 ms: 2.00x faster                                                  |
| logging_silent           | 117 ns                                                 | 59.3 ns: 1.98x faster                                                 |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                  |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                  |
| async_tree_io            | 980 ms                                                 | 532 ms: 1.84x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.9 ms: 1.83x faster                                                 |
| richards_super           | 57.8 ms                                                | 34.4 ms: 1.68x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 746 us: 1.67x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.6 us: 1.60x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 909 us: 1.59x faster                                                  |
| richards                 | 48.7 ms                                                | 31.3 ms: 1.56x faster                                                 |
| generators               | 32.3 ms                                                | 20.9 ms: 1.55x faster                                                 |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.1 ms: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.54x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                 |
| go                       | 151 ms                                                 | 98.3 ms: 1.53x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.8 ms: 1.53x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.08 ms: 1.52x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 437 ms: 1.51x faster                                                  |
| scimark_lu               | 103 ms                                                 | 69.8 ms: 1.47x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.38 us: 1.43x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 66.4 ms: 1.43x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 457 ms: 1.42x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 49.4 ms: 1.40x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                 |
| mako                     | 9.87 ms                                                | 7.19 ms: 1.37x faster                                                 |
| pycparser                | 877 ms                                                 | 640 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 960 ms: 1.36x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 473 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.34x faster                                                 |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| scimark_sor              | 128 ms                                                 | 96.1 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 322 ms: 1.33x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 70.3 ms: 1.31x faster                                                 |
| thrift                   | 572 us                                                 | 438 us: 1.31x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.36 ms: 1.28x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| sympy_str                | 165 ms                                                 | 134 ms: 1.24x faster                                                  |
| scimark_fft              | 224 ms                                                 | 183 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.81 ms: 1.22x faster                                                 |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                  |
| nqueens                  | 63.8 ms                                                | 54.0 ms: 1.18x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                |
| sympy_expand             | 269 ms                                                 | 230 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 452 us: 1.17x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                                |
| fannkuch                 | 303 ms                                                 | 263 ms: 1.15x faster                                                  |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.0 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 3.01 ms: 1.02x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 52.7 ms: 1.01x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.8 ms: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 899 us: 1.05x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.2 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 281 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 47.2 ms: 1.26x slower                                                 |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.1 ms: 1.39x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-darwin-arm64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.75x