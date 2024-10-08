# Results vs. 3.10.4

- fork: mdboom
- ref: rc1_mdboom
- machine: darwin-arm64
- commit hash: 2a88001
- commit date: 2024-08-26
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 0.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 200 ms: 1.04x slower                                         |
| chameleon      | 6.26 ms                                                | 4.65 ms: 1.35x faster                                        |
| docutils       | 1.73 sec                                               | 1.54 sec: 1.13x faster                                       |
| html5lib       | 42.4 ms                                                | 33.3 ms: 1.27x faster                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 227 ms: 1.71x faster                                         |
| async_tree_memoization  | 474 ms                                                 | 279 ms: 1.70x faster                                         |
| async_tree_io           | 980 ms                                                 | 587 ms: 1.67x faster                                         |
| async_tree_cpu_io_mixed | 649 ms                                                 | 488 ms: 1.33x faster                                         |
| Geometric mean          | (ref)                                                  | 1.59x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 66.0 ms: 1.41x faster                                        |
| float          | 69.0 ms                                                | 51.4 ms: 1.34x faster                                        |
| Geometric mean | (ref)                                                  | 1.24x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.9 ms: 1.29x faster                                        |
| regex_dna      | 174 ms                                                 | 144 ms: 1.21x faster                                         |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                        |
| regex_effbot   | 2.46 ms                                                | 2.55 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 191 us: 1.47x faster                                         |
| unpickle_pure_python | 194 us                                                 | 152 us: 1.28x faster                                         |
| json_dumps           | 8.11 ms                                                | 6.65 ms: 1.22x faster                                        |
| xml_etree_process    | 46.5 ms                                                | 42.2 ms: 1.10x faster                                        |
| tomli_loads          | 1.71 sec                                               | 1.56 sec: 1.09x faster                                       |
| xml_etree_iterparse  | 72.1 ms                                                | 74.4 ms: 1.03x slower                                        |
| json_loads           | 16.4 us                                                | 17.8 us: 1.08x slower                                        |
| xml_etree_generate   | 53.5 ms                                                | 59.9 ms: 1.12x slower                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.9 ms: 1.46x slower                                        |
| python_startup_no_site | 7.91 ms                                                | 13.0 ms: 1.64x slower                                        |
| Geometric mean         | (ref)                                                  | 1.55x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.37 ms: 1.34x faster                                        |
| django_template | 26.4 ms                                                | 22.2 ms: 1.19x faster                                        |
| genshi_text     | 17.3 ms                                                | 14.7 ms: 1.18x faster                                        |
| genshi_xml      | 33.8 ms                                                | 31.9 ms: 1.06x faster                                        |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 108 us: 2.98x faster                                         |
| deltablue                | 4.91 ms                                                | 2.29 ms: 2.15x faster                                        |
| raytrace                 | 301 ms                                                 | 168 ms: 1.79x faster                                         |
| logging_silent           | 117 ns                                                 | 67.8 ns: 1.73x faster                                        |
| chaos                    | 65.8 ms                                                | 38.1 ms: 1.73x faster                                        |
| async_tree_none          | 388 ms                                                 | 227 ms: 1.71x faster                                         |
| async_tree_memoization   | 474 ms                                                 | 279 ms: 1.70x faster                                         |
| async_tree_io            | 980 ms                                                 | 587 ms: 1.67x faster                                         |
| asyncio_tcp              | 659 ms                                                 | 415 ms: 1.59x faster                                         |
| sqlglot_parse            | 1.24 ms                                                | 784 us: 1.58x faster                                         |
| richards_super           | 57.8 ms                                                | 37.0 ms: 1.57x faster                                        |
| sqlglot_transpile        | 1.44 ms                                                | 958 us: 1.51x faster                                         |
| hexiom                   | 6.19 ms                                                | 4.20 ms: 1.48x faster                                        |
| pickle_pure_python       | 281 us                                                 | 191 us: 1.47x faster                                         |
| scimark_monte_carlo      | 65.6 ms                                                | 44.6 ms: 1.47x faster                                        |
| go                       | 151 ms                                                 | 103 ms: 1.46x faster                                         |
| pylint                   | 277 ms                                                 | 190 ms: 1.45x faster                                         |
| richards                 | 48.7 ms                                                | 33.5 ms: 1.45x faster                                        |
| comprehensions           | 16.9 us                                                | 11.8 us: 1.44x faster                                        |
| deepcopy_memo            | 34.7 us                                                | 24.3 us: 1.43x faster                                        |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                        |
| nbody                    | 93.0 ms                                                | 66.0 ms: 1.41x faster                                        |
| generators               | 32.3 ms                                                | 23.7 ms: 1.37x faster                                        |
| chameleon                | 6.26 ms                                                | 4.65 ms: 1.35x faster                                        |
| float                    | 69.0 ms                                                | 51.4 ms: 1.34x faster                                        |
| scimark_lu               | 103 ms                                                 | 76.7 ms: 1.34x faster                                        |
| mako                     | 9.87 ms                                                | 7.37 ms: 1.34x faster                                        |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 488 ms: 1.33x faster                                         |
| spectral_norm            | 94.8 ms                                                | 72.5 ms: 1.31x faster                                        |
| logging_simple           | 4.45 us                                                | 3.42 us: 1.30x faster                                        |
| logging_format           | 4.83 us                                                | 3.74 us: 1.29x faster                                        |
| regex_compile            | 95.3 ms                                                | 73.9 ms: 1.29x faster                                        |
| pycparser                | 877 ms                                                 | 682 ms: 1.29x faster                                         |
| unpickle_pure_python     | 194 us                                                 | 152 us: 1.28x faster                                         |
| html5lib                 | 42.4 ms                                                | 33.3 ms: 1.27x faster                                        |
| pyflate                  | 427 ms                                                 | 336 ms: 1.27x faster                                         |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.26x faster                                       |
| pprint_safe_repr         | 641 ms                                                 | 511 ms: 1.25x faster                                         |
| dulwich_log              | 35.3 ms                                                | 28.2 ms: 1.25x faster                                        |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                       |
| scimark_sor              | 128 ms                                                 | 104 ms: 1.24x faster                                         |
| mypy2                    | 607 ms                                                 | 494 ms: 1.23x faster                                         |
| json_dumps               | 8.11 ms                                                | 6.65 ms: 1.22x faster                                        |
| regex_dna                | 174 ms                                                 | 144 ms: 1.21x faster                                         |
| deepcopy                 | 272 us                                                 | 227 us: 1.20x faster                                         |
| sympy_sum                | 92.2 ms                                                | 77.1 ms: 1.20x faster                                        |
| django_template          | 26.4 ms                                                | 22.2 ms: 1.19x faster                                        |
| genshi_text              | 17.3 ms                                                | 14.7 ms: 1.18x faster                                        |
| sympy_integrate          | 13.1 ms                                                | 11.2 ms: 1.17x faster                                        |
| thrift                   | 572 us                                                 | 493 us: 1.16x faster                                         |
| deepcopy_reduce          | 2.33 us                                                | 2.03 us: 1.15x faster                                        |
| scimark_fft              | 224 ms                                                 | 197 ms: 1.14x faster                                         |
| docutils                 | 1.73 sec                                               | 1.54 sec: 1.13x faster                                       |
| sympy_str                | 165 ms                                                 | 147 ms: 1.12x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.08 ms: 1.11x faster                                        |
| nqueens                  | 63.8 ms                                                | 57.8 ms: 1.10x faster                                        |
| xml_etree_process        | 46.5 ms                                                | 42.2 ms: 1.10x faster                                        |
| tomli_loads              | 1.71 sec                                               | 1.56 sec: 1.09x faster                                       |
| bench_thread_pool        | 527 us                                                 | 486 us: 1.09x faster                                         |
| genshi_xml               | 33.8 ms                                                | 31.9 ms: 1.06x faster                                        |
| meteor_contest           | 77.7 ms                                                | 73.6 ms: 1.06x faster                                        |
| coroutines               | 20.7 ms                                                | 19.8 ms: 1.05x faster                                        |
| sympy_expand             | 269 ms                                                 | 257 ms: 1.04x faster                                         |
| dask                     | 253 ms                                                 | 243 ms: 1.04x faster                                         |
| sqlglot_optimize         | 36.8 ms                                                | 35.8 ms: 1.03x faster                                        |
| fannkuch                 | 303 ms                                                 | 296 ms: 1.02x faster                                         |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                        |
| mdp                      | 1.63 sec                                               | 1.60 sec: 1.02x faster                                       |
| json                     | 3.08 ms                                                | 3.06 ms: 1.01x faster                                        |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                         |
| sqlglot_normalize        | 190 ms                                                 | 193 ms: 1.01x slower                                         |
| create_gc_cycles         | 860 us                                                 | 882 us: 1.03x slower                                         |
| xml_etree_iterparse      | 72.1 ms                                                | 74.4 ms: 1.03x slower                                        |
| regex_effbot             | 2.46 ms                                                | 2.55 ms: 1.04x slower                                        |
| pathlib                  | 24.5 ms                                                | 25.5 ms: 1.04x slower                                        |
| 2to3                     | 192 ms                                                 | 200 ms: 1.04x slower                                         |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                        |
| json_loads               | 16.4 us                                                | 17.8 us: 1.08x slower                                        |
| xml_etree_generate       | 53.5 ms                                                | 59.9 ms: 1.12x slower                                        |
| coverage                 | 41.5 ms                                                | 50.8 ms: 1.22x slower                                        |
| bench_mp_pool            | 37.4 ms                                                | 48.8 ms: 1.30x slower                                        |
| async_generators         | 231 ms                                                 | 323 ms: 1.40x slower                                         |
| telco                    | 3.49 ms                                                | 4.95 ms: 1.42x slower                                        |
| python_startup           | 10.9 ms                                                | 15.9 ms: 1.46x slower                                        |
| python_startup_no_site   | 7.91 ms                                                | 13.0 ms: 1.64x slower                                        |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                 |

Benchmark hidden because not significant (3): tornado_http, pidigits, xml_etree_parse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240826-3.13.0rc1-2a88001/bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 0.57x