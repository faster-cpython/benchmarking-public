# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.246x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.12x faster                                                   |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.20x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 254 ms: 1.86x faster                                                   |
| async_tree_io           | 980 ms                                                 | 590 ms: 1.66x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 469 ms: 1.39x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 68.1 ms: 1.36x faster                                                  |
| float          | 69.0 ms                                                | 53.1 ms: 1.30x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 71.9 ms: 1.32x faster                                                  |
| regex_dna      | 174 ms                                                 | 137 ms: 1.28x faster                                                   |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.32 ms: 1.06x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 208 us: 1.35x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 154 us: 1.27x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 39.5 ms: 1.18x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.22 ms: 1.12x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.54 sec: 1.11x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 54.5 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.9 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.0 ms: 1.65x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 13.4 ms: 1.70x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.67x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.13 ms: 1.39x faster                                                  |
| django_template | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.21x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 31.0 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.6 us: 3.31x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.47 ms: 1.99x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 18.3 us: 1.89x faster                                                  |
| async_tree_none          | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 254 ms: 1.86x faster                                                   |
| deepcopy                 | 272 us                                                 | 153 us: 1.77x faster                                                   |
| raytrace                 | 301 ms                                                 | 170 ms: 1.77x faster                                                   |
| go                       | 151 ms                                                 | 87.3 ms: 1.73x faster                                                  |
| logging_silent           | 117 ns                                                 | 68.5 ns: 1.71x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| chaos                    | 65.8 ms                                                | 39.1 ms: 1.68x faster                                                  |
| async_tree_io            | 980 ms                                                 | 590 ms: 1.66x faster                                                   |
| richards_super           | 57.8 ms                                                | 37.4 ms: 1.55x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 803 us: 1.55x faster                                                   |
| pylint                   | 277 ms                                                 | 186 ms: 1.49x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 975 us: 1.48x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.59 us: 1.47x faster                                                  |
| richards                 | 48.7 ms                                                | 33.8 ms: 1.44x faster                                                  |
| generators               | 32.3 ms                                                | 22.5 ms: 1.44x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 46.1 ms: 1.42x faster                                                  |
| scimark_lu               | 103 ms                                                 | 73.9 ms: 1.39x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.47 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 469 ms: 1.39x faster                                                   |
| mako                     | 9.87 ms                                                | 7.13 ms: 1.39x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.25 us: 1.37x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.37x faster                                                  |
| nbody                    | 93.0 ms                                                | 68.1 ms: 1.36x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.50 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 208 us: 1.35x faster                                                   |
| logging_format           | 4.83 us                                                | 3.57 us: 1.35x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 53.6 ms: 1.34x faster                                                  |
| pycparser                | 877 ms                                                 | 656 ms: 1.34x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 981 ms: 1.33x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 482 ms: 1.33x faster                                                   |
| regex_compile            | 95.3 ms                                                | 71.9 ms: 1.32x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 71.9 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                                   |
| float                    | 69.0 ms                                                | 53.1 ms: 1.30x faster                                                  |
| scimark_sor              | 128 ms                                                 | 99.8 ms: 1.28x faster                                                  |
| regex_dna                | 174 ms                                                 | 137 ms: 1.28x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 154 us: 1.27x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 73.0 ms: 1.26x faster                                                  |
| pyflate                  | 427 ms                                                 | 338 ms: 1.26x faster                                                   |
| django_template          | 26.4 ms                                                | 21.1 ms: 1.25x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.3 ms: 1.25x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.7 ms: 1.25x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.21x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.20x faster                                                 |
| coroutines               | 20.7 ms                                                | 17.5 ms: 1.18x faster                                                  |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 39.5 ms: 1.18x faster                                                  |
| scimark_fft              | 224 ms                                                 | 193 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.98 ms: 1.15x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.15x faster                                                  |
| fannkuch                 | 303 ms                                                 | 265 ms: 1.14x faster                                                   |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 465 us: 1.13x faster                                                   |
| 2to3                     | 192 ms                                                 | 170 ms: 1.12x faster                                                   |
| json_dumps               | 8.11 ms                                                | 7.22 ms: 1.12x faster                                                  |
| pathlib                  | 24.5 ms                                                | 21.9 ms: 1.12x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.0 ms: 1.11x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.54 sec: 1.11x faster                                                 |
| nqueens                  | 63.8 ms                                                | 57.9 ms: 1.10x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 31.0 ms: 1.09x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.51 sec: 1.08x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 178 ms: 1.07x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 72.8 ms: 1.07x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.32 ms: 1.06x faster                                                  |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 54.5 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.9 ms: 1.04x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.4 ms: 1.07x slower                                                  |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.92 ms: 1.24x slower                                                  |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.30 ms: 1.52x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 60.7 ms: 1.62x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.0 ms: 1.65x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.4 ms: 1.70x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.246x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x