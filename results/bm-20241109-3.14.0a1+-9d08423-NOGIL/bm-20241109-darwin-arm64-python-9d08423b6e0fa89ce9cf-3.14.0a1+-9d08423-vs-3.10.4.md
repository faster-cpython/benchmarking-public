# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.096x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 244 ms: 1.27x slower                                                   |
| docutils       | 1.73 sec                                               | 1.69 sec: 1.03x faster                                                 |
| html5lib       | 42.4 ms                                                | 49.7 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 520 ms: 1.88x faster                                                   |
| async_tree_none         | 388 ms                                                 | 228 ms: 1.71x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 284 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 487 ms: 1.33x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| float          | 69.0 ms                                                | 90.9 ms: 1.32x slower                                                  |
| nbody          | 93.0 ms                                                | 134 ms: 1.44x slower                                                   |
| Geometric mean | (ref)                                                  | 1.24x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 138 ms: 1.26x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.42 ms: 1.02x faster                                                  |
| regex_compile  | 95.3 ms                                                | 116 ms: 1.22x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| json_dumps           | 8.11 ms                                                | 8.58 ms: 1.06x slower                                                  |
| json_loads           | 16.4 us                                                | 17.8 us: 1.08x slower                                                  |
| tomli_loads          | 1.71 sec                                               | 1.88 sec: 1.10x slower                                                 |
| xml_etree_process    | 46.5 ms                                                | 52.9 ms: 1.14x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 64.7 ms: 1.21x slower                                                  |
| pickle_pure_python   | 281 us                                                 | 347 us: 1.24x slower                                                   |
| unpickle_pure_python | 194 us                                                 | 256 us: 1.32x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 20.6 ms: 1.89x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.0 ms: 2.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.96x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 34.8 ms: 1.32x slower                                                  |
| genshi_text     | 17.3 ms                                                | 23.5 ms: 1.35x slower                                                  |
| mako            | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                  |
| genshi_xml      | 33.8 ms                                                | 47.4 ms: 1.40x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.36x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 140 us: 2.30x faster                                                   |
| async_tree_io            | 980 ms                                                 | 520 ms: 1.88x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 238 ms: 1.72x faster                                                   |
| async_tree_none          | 388 ms                                                 | 228 ms: 1.71x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 284 ms: 1.67x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 487 ms: 1.33x faster                                                   |
| pylint                   | 277 ms                                                 | 209 ms: 1.33x faster                                                   |
| regex_dna                | 174 ms                                                 | 138 ms: 1.26x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 29.0 us: 1.20x faster                                                  |
| deepcopy                 | 272 us                                                 | 230 us: 1.18x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| generators               | 32.3 ms                                                | 30.6 ms: 1.06x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.69 sec: 1.03x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.42 ms: 1.02x faster                                                  |
| pathlib                  | 24.5 ms                                                | 24.1 ms: 1.02x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.32 us: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                   |
| json                     | 3.08 ms                                                | 3.16 ms: 1.03x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| scimark_fft              | 224 ms                                                 | 233 ms: 1.04x slower                                                   |
| pycparser                | 877 ms                                                 | 909 ms: 1.04x slower                                                   |
| chaos                    | 65.8 ms                                                | 69.6 ms: 1.06x slower                                                  |
| json_dumps               | 8.11 ms                                                | 8.58 ms: 1.06x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.51 ms: 1.06x slower                                                  |
| spectral_norm            | 94.8 ms                                                | 102 ms: 1.07x slower                                                   |
| richards_super           | 57.8 ms                                                | 62.2 ms: 1.08x slower                                                  |
| crypto_pyaes             | 71.8 ms                                                | 77.6 ms: 1.08x slower                                                  |
| json_loads               | 16.4 us                                                | 17.8 us: 1.08x slower                                                  |
| pyflate                  | 427 ms                                                 | 464 ms: 1.09x slower                                                   |
| richards                 | 48.7 ms                                                | 53.3 ms: 1.09x slower                                                  |
| tomli_loads              | 1.71 sec                                               | 1.88 sec: 1.10x slower                                                 |
| nqueens                  | 63.8 ms                                                | 70.4 ms: 1.10x slower                                                  |
| fannkuch                 | 303 ms                                                 | 334 ms: 1.10x slower                                                   |
| logging_silent           | 117 ns                                                 | 130 ns: 1.11x slower                                                   |
| mdp                      | 1.63 sec                                               | 1.80 sec: 1.11x slower                                                 |
| deltablue                | 4.91 ms                                                | 5.45 ms: 1.11x slower                                                  |
| dulwich_log              | 35.3 ms                                                | 39.6 ms: 1.12x slower                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 9.97 ms: 1.13x slower                                                  |
| meteor_contest           | 77.7 ms                                                | 87.9 ms: 1.13x slower                                                  |
| raytrace                 | 301 ms                                                 | 340 ms: 1.13x slower                                                   |
| comprehensions           | 16.9 us                                                | 19.2 us: 1.14x slower                                                  |
| xml_etree_process        | 46.5 ms                                                | 52.9 ms: 1.14x slower                                                  |
| thrift                   | 572 us                                                 | 656 us: 1.15x slower                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 76.3 ms: 1.16x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.99 ms: 1.17x slower                                                  |
| go                       | 151 ms                                                 | 177 ms: 1.17x slower                                                   |
| html5lib                 | 42.4 ms                                                | 49.7 ms: 1.17x slower                                                  |
| scimark_sor              | 128 ms                                                 | 151 ms: 1.18x slower                                                   |
| sympy_integrate          | 13.1 ms                                                | 15.8 ms: 1.21x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 64.7 ms: 1.21x slower                                                  |
| regex_compile            | 95.3 ms                                                | 116 ms: 1.22x slower                                                   |
| hexiom                   | 6.19 ms                                                | 7.55 ms: 1.22x slower                                                  |
| pprint_safe_repr         | 641 ms                                                 | 784 ms: 1.22x slower                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 89.8 ms: 1.23x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.60 sec: 1.23x slower                                                 |
| pickle_pure_python       | 281 us                                                 | 347 us: 1.24x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.08 ms: 1.25x slower                                                  |
| 2to3                     | 192 ms                                                 | 244 ms: 1.27x slower                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.84 ms: 1.28x slower                                                  |
| sqlglot_parse            | 1.24 ms                                                | 1.61 ms: 1.29x slower                                                  |
| coverage                 | 41.5 ms                                                | 54.1 ms: 1.30x slower                                                  |
| unpickle_pure_python     | 194 us                                                 | 256 us: 1.32x slower                                                   |
| float                    | 69.0 ms                                                | 90.9 ms: 1.32x slower                                                  |
| django_template          | 26.4 ms                                                | 34.8 ms: 1.32x slower                                                  |
| logging_simple           | 4.45 us                                                | 5.89 us: 1.32x slower                                                  |
| logging_format           | 4.83 us                                                | 6.44 us: 1.33x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 49.7 ms: 1.35x slower                                                  |
| genshi_text              | 17.3 ms                                                | 23.5 ms: 1.35x slower                                                  |
| mako                     | 9.87 ms                                                | 13.4 ms: 1.36x slower                                                  |
| async_generators         | 231 ms                                                 | 316 ms: 1.37x slower                                                   |
| sympy_str                | 165 ms                                                 | 226 ms: 1.37x slower                                                   |
| scimark_lu               | 103 ms                                                 | 141 ms: 1.37x slower                                                   |
| sqlglot_normalize        | 190 ms                                                 | 262 ms: 1.38x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 47.4 ms: 1.40x slower                                                  |
| nbody                    | 93.0 ms                                                | 134 ms: 1.44x slower                                                   |
| sympy_sum                | 92.2 ms                                                | 137 ms: 1.49x slower                                                   |
| telco                    | 3.49 ms                                                | 5.30 ms: 1.52x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 811 us: 1.54x slower                                                   |
| sympy_expand             | 269 ms                                                 | 417 ms: 1.55x slower                                                   |
| python_startup           | 10.9 ms                                                | 20.6 ms: 1.89x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 72.9 ms: 1.95x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.0 ms: 2.03x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.12x slower                                                           |

Benchmark hidden because not significant (2): sqlite_synth, coroutines
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.096x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.49x