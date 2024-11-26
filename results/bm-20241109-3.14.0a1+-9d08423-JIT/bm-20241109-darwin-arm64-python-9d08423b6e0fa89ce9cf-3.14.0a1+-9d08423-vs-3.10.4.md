# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.216x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.44x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 212 ms: 1.11x slower                                                   |
| docutils       | 1.73 sec                                               | 1.58 sec: 1.09x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 254 ms: 1.86x faster                                                   |
| async_tree_io           | 980 ms                                                 | 592 ms: 1.65x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 472 ms: 1.38x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.68x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                  |
| float          | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 137 ms: 1.27x faster                                                   |
| regex_compile  | 95.3 ms                                                | 76.7 ms: 1.24x faster                                                  |
| regex_v8       | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.33 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 194 us: 1.45x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.10 ms: 1.14x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 49.5 ms: 1.08x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.8 ms: 1.73x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 14.0 ms: 1.76x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.75x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.24 ms: 1.58x faster                                                  |
| django_template | 26.4 ms                                                | 23.5 ms: 1.12x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 39.7 ms: 1.17x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 101 us: 3.21x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 17.6 us: 1.97x faster                                                  |
| async_tree_none          | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.61 ms: 1.88x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 254 ms: 1.86x faster                                                   |
| deepcopy                 | 272 us                                                 | 157 us: 1.72x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| async_tree_io            | 980 ms                                                 | 592 ms: 1.65x faster                                                   |
| raytrace                 | 301 ms                                                 | 184 ms: 1.64x faster                                                   |
| logging_silent           | 117 ns                                                 | 73.5 ns: 1.59x faster                                                  |
| mako                     | 9.87 ms                                                | 6.24 ms: 1.58x faster                                                  |
| richards_super           | 57.8 ms                                                | 37.8 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                  |
| chaos                    | 65.8 ms                                                | 43.5 ms: 1.51x faster                                                  |
| pylint                   | 277 ms                                                 | 184 ms: 1.51x faster                                                   |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                   |
| scimark_lu               | 103 ms                                                 | 68.7 ms: 1.50x faster                                                  |
| scimark_sor              | 128 ms                                                 | 87.0 ms: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 45.0 ms: 1.46x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 194 us: 1.45x faster                                                   |
| richards                 | 48.7 ms                                                | 34.0 ms: 1.43x faster                                                  |
| float                    | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 882 us: 1.41x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 472 ms: 1.38x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 69.8 ms: 1.36x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.29 us: 1.35x faster                                                  |
| logging_format           | 4.83 us                                                | 3.61 us: 1.34x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.08 ms: 1.33x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.71 ms: 1.32x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.5 ms: 1.32x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 487 ms: 1.32x faster                                                   |
| pyflate                  | 427 ms                                                 | 327 ms: 1.31x faster                                                   |
| thrift                   | 572 us                                                 | 442 us: 1.29x faster                                                   |
| pycparser                | 877 ms                                                 | 680 ms: 1.29x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.28x faster                                                 |
| html5lib                 | 42.4 ms                                                | 33.0 ms: 1.28x faster                                                  |
| regex_dna                | 174 ms                                                 | 137 ms: 1.27x faster                                                   |
| comprehensions           | 16.9 us                                                | 13.5 us: 1.25x faster                                                  |
| regex_compile            | 95.3 ms                                                | 76.7 ms: 1.24x faster                                                  |
| hexiom                   | 6.19 ms                                                | 5.05 ms: 1.23x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                  |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                   |
| generators               | 32.3 ms                                                | 26.9 ms: 1.20x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.5 ms: 1.18x faster                                                  |
| fannkuch                 | 303 ms                                                 | 257 ms: 1.18x faster                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 63.2 ms: 1.16x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.10 ms: 1.14x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 80.9 ms: 1.14x faster                                                  |
| django_template          | 26.4 ms                                                | 23.5 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.06 ms: 1.12x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.58 sec: 1.09x faster                                                 |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 488 us: 1.08x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 49.5 ms: 1.08x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.8 ms: 1.07x faster                                                  |
| sympy_str                | 165 ms                                                 | 155 ms: 1.07x faster                                                   |
| json                     | 3.08 ms                                                | 2.91 ms: 1.06x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.33 ms: 1.05x faster                                                  |
| sympy_expand             | 269 ms                                                 | 256 ms: 1.05x faster                                                   |
| nqueens                  | 63.8 ms                                                | 61.7 ms: 1.03x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.58 sec: 1.03x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 12.8 ms: 1.02x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| sqlglot_normalize        | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 38.1 ms: 1.04x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.6 ms: 1.08x slower                                                  |
| 2to3                     | 192 ms                                                 | 212 ms: 1.11x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 39.7 ms: 1.17x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.93 ms: 1.24x slower                                                  |
| telco                    | 3.49 ms                                                | 4.43 ms: 1.27x slower                                                  |
| async_generators         | 231 ms                                                 | 306 ms: 1.32x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.54x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 64.2 ms: 1.72x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.8 ms: 1.73x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.0 ms: 1.76x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): genshi_text
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.216x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.44x