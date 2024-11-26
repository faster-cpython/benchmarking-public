# Results vs. 3.10.4

- fork: diegorusso
- ref: pthread
- machine: darwin-arm64
- commit hash: f74cd79
- commit date: 2024-10-18
- overall geometric mean: 1.237x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 182 ms: 1.06x faster                                          |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.11x faster                                        |
| html5lib       | 42.4 ms                                                | 34.0 ms: 1.25x faster                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                          |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                          |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                          |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                          |
| Geometric mean          | (ref)                                                  | 1.70x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.4 ms: 1.43x faster                                         |
| nbody          | 93.0 ms                                                | 65.3 ms: 1.42x faster                                         |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                  | 1.27x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.4 ms: 1.28x faster                                         |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                          |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                         |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                          |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                          |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                        |
| xml_etree_process    | 46.5 ms                                                | 34.8 ms: 1.34x faster                                         |
| json_dumps           | 8.11 ms                                                | 7.08 ms: 1.15x faster                                         |
| xml_etree_generate   | 53.5 ms                                                | 50.5 ms: 1.06x faster                                         |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                         |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.7 ms: 1.45x slower                                         |
| python_startup_no_site | 7.91 ms                                                | 11.9 ms: 1.51x slower                                         |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.46 ms: 1.53x faster                                         |
| django_template | 26.4 ms                                                | 22.6 ms: 1.17x faster                                         |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                         |
| genshi_xml      | 33.8 ms                                                | 41.0 ms: 1.21x slower                                         |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.4 us: 3.32x faster                                         |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.06x faster                                         |
| deltablue                | 4.91 ms                                                | 2.39 ms: 2.05x faster                                         |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                          |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                          |
| deepcopy                 | 272 us                                                 | 152 us: 1.79x faster                                          |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                          |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                          |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                          |
| logging_silent           | 117 ns                                                 | 70.1 ns: 1.67x faster                                         |
| scimark_lu               | 103 ms                                                 | 65.0 ms: 1.58x faster                                         |
| chaos                    | 65.8 ms                                                | 41.7 ms: 1.58x faster                                         |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                          |
| pylint                   | 277 ms                                                 | 178 ms: 1.56x faster                                          |
| go                       | 151 ms                                                 | 98.4 ms: 1.53x faster                                         |
| mako                     | 9.87 ms                                                | 6.46 ms: 1.53x faster                                         |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                         |
| scimark_sor              | 128 ms                                                 | 86.1 ms: 1.49x faster                                         |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                          |
| richards_super           | 57.8 ms                                                | 39.5 ms: 1.46x faster                                         |
| sqlglot_parse            | 1.24 ms                                                | 865 us: 1.44x faster                                          |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                         |
| scimark_monte_carlo      | 65.6 ms                                                | 45.8 ms: 1.43x faster                                         |
| logging_format           | 4.83 us                                                | 3.38 us: 1.43x faster                                         |
| float                    | 69.0 ms                                                | 48.4 ms: 1.43x faster                                         |
| nbody                    | 93.0 ms                                                | 65.3 ms: 1.42x faster                                         |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                          |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                        |
| spectral_norm            | 94.8 ms                                                | 69.3 ms: 1.37x faster                                         |
| sqlglot_transpile        | 1.44 ms                                                | 1.05 ms: 1.37x faster                                         |
| richards                 | 48.7 ms                                                | 35.7 ms: 1.37x faster                                         |
| thrift                   | 572 us                                                 | 420 us: 1.36x faster                                          |
| xml_etree_process        | 46.5 ms                                                | 34.8 ms: 1.34x faster                                         |
| crypto_pyaes             | 71.8 ms                                                | 53.9 ms: 1.33x faster                                         |
| pyflate                  | 427 ms                                                 | 325 ms: 1.31x faster                                          |
| comprehensions           | 16.9 us                                                | 13.1 us: 1.29x faster                                         |
| pprint_pformat           | 1.30 sec                                               | 1.01 sec: 1.29x faster                                        |
| pycparser                | 877 ms                                                 | 680 ms: 1.29x faster                                          |
| regex_compile            | 95.3 ms                                                | 74.4 ms: 1.28x faster                                         |
| generators               | 32.3 ms                                                | 25.3 ms: 1.28x faster                                         |
| pprint_safe_repr         | 641 ms                                                 | 504 ms: 1.27x faster                                          |
| coroutines               | 20.7 ms                                                | 16.5 ms: 1.26x faster                                         |
| hexiom                   | 6.19 ms                                                | 4.96 ms: 1.25x faster                                         |
| html5lib                 | 42.4 ms                                                | 34.0 ms: 1.25x faster                                         |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                         |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.18x faster                                          |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                          |
| sympy_sum                | 92.2 ms                                                | 78.8 ms: 1.17x faster                                         |
| django_template          | 26.4 ms                                                | 22.6 ms: 1.17x faster                                         |
| json_dumps               | 8.11 ms                                                | 7.08 ms: 1.15x faster                                         |
| fannkuch                 | 303 ms                                                 | 268 ms: 1.13x faster                                          |
| bench_thread_pool        | 527 us                                                 | 476 us: 1.11x faster                                          |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.11x faster                                        |
| pathlib                  | 24.5 ms                                                | 22.2 ms: 1.10x faster                                         |
| sympy_str                | 165 ms                                                 | 151 ms: 1.10x faster                                          |
| sympy_expand             | 269 ms                                                 | 247 ms: 1.09x faster                                          |
| json                     | 3.08 ms                                                | 2.84 ms: 1.09x faster                                         |
| nqueens                  | 63.8 ms                                                | 58.7 ms: 1.09x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.18 ms: 1.08x faster                                         |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                         |
| xml_etree_generate       | 53.5 ms                                                | 50.5 ms: 1.06x faster                                         |
| 2to3                     | 192 ms                                                 | 182 ms: 1.06x faster                                          |
| mdp                      | 1.63 sec                                               | 1.55 sec: 1.05x faster                                        |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                         |
| meteor_contest           | 77.7 ms                                                | 74.5 ms: 1.04x faster                                         |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                          |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                         |
| sqlglot_optimize         | 36.8 ms                                                | 36.7 ms: 1.00x faster                                         |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                          |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                         |
| coverage                 | 41.5 ms                                                | 43.5 ms: 1.05x slower                                         |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                         |
| genshi_xml               | 33.8 ms                                                | 41.0 ms: 1.21x slower                                         |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.25x slower                                         |
| async_generators         | 231 ms                                                 | 293 ms: 1.27x slower                                          |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                         |
| python_startup           | 10.9 ms                                                | 15.7 ms: 1.45x slower                                         |
| python_startup_no_site   | 7.91 ms                                                | 11.9 ms: 1.51x slower                                         |
| create_gc_cycles         | 860 us                                                 | 1.33 ms: 1.54x slower                                         |
| bench_mp_pool            | 37.4 ms                                                | 60.5 ms: 1.62x slower                                         |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                  |

Benchmark hidden because not significant (3): tornado_http, xml_etree_parse, json_loads
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241018-3.14.0a1+-f74cd79-JIT/bm-20241018-darwin-arm64-diegorusso-pthread-3.14.0a1+-f74cd79.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.237x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.43x