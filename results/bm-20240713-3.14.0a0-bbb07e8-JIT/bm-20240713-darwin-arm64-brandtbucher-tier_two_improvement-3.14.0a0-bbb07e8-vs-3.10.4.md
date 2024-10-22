# Results vs. 3.10.4

- fork: brandtbucher
- ref: tier_two_improvement
- machine: darwin-arm64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 171 ms: 1.12x faster                                                        |
| docutils       | 1.73 sec                                               | 1.51 sec: 1.14x faster                                                      |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                       |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 232 ms: 2.04x faster                                                        |
| async_tree_none         | 388 ms                                                 | 195 ms: 1.99x faster                                                        |
| async_tree_io           | 980 ms                                                 | 535 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed | 649 ms                                                 | 456 ms: 1.42x faster                                                        |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                       |
| float          | 69.0 ms                                                | 47.6 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.8 ms: 1.29x faster                                                       |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                        |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                       |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 175 us: 1.60x faster                                                        |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                        |
| tomli_loads          | 1.71 sec                                               | 1.23 sec: 1.38x faster                                                      |
| xml_etree_process    | 46.5 ms                                                | 36.4 ms: 1.28x faster                                                       |
| json_dumps           | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                       |
| xml_etree_iterparse  | 72.1 ms                                                | 70.5 ms: 1.02x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                | 52.4 ms: 1.02x faster                                                       |
| json_loads           | 16.4 us                                                | 17.4 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                       |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.61x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                       |
| django_template | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                       |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                       |
| genshi_xml      | 33.8 ms                                                | 39.8 ms: 1.18x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.4 us: 3.32x faster                                                       |
| deltablue                | 4.91 ms                                                | 2.32 ms: 2.11x faster                                                       |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                                       |
| async_tree_memoization   | 474 ms                                                 | 232 ms: 2.04x faster                                                        |
| async_tree_none          | 388 ms                                                 | 195 ms: 1.99x faster                                                        |
| logging_silent           | 117 ns                                                 | 62.2 ns: 1.88x faster                                                       |
| async_tree_io            | 980 ms                                                 | 535 ms: 1.83x faster                                                        |
| raytrace                 | 301 ms                                                 | 165 ms: 1.83x faster                                                        |
| deepcopy                 | 272 us                                                 | 153 us: 1.78x faster                                                        |
| richards_super           | 57.8 ms                                                | 34.5 ms: 1.68x faster                                                       |
| chaos                    | 65.8 ms                                                | 39.6 ms: 1.66x faster                                                       |
| pickle_pure_python       | 281 us                                                 | 175 us: 1.60x faster                                                        |
| richards                 | 48.7 ms                                                | 30.9 ms: 1.58x faster                                                       |
| asyncio_tcp              | 659 ms                                                 | 419 ms: 1.57x faster                                                        |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                        |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                       |
| deepcopy_reduce          | 2.33 us                                                | 1.55 us: 1.50x faster                                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                                       |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                        |
| sqlglot_parse            | 1.24 ms                                                | 836 us: 1.49x faster                                                        |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                        |
| nbody                    | 93.0 ms                                                | 64.1 ms: 1.45x faster                                                       |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                       |
| float                    | 69.0 ms                                                | 47.6 ms: 1.45x faster                                                       |
| generators               | 32.3 ms                                                | 22.4 ms: 1.45x faster                                                       |
| logging_format           | 4.83 us                                                | 3.37 us: 1.43x faster                                                       |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                       |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 456 ms: 1.42x faster                                                        |
| hexiom                   | 6.19 ms                                                | 4.39 ms: 1.41x faster                                                       |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                                       |
| tomli_loads              | 1.71 sec                                               | 1.23 sec: 1.38x faster                                                      |
| spectral_norm            | 94.8 ms                                                | 68.6 ms: 1.38x faster                                                       |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                       |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.37x faster                                                       |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                                        |
| pprint_safe_repr         | 641 ms                                                 | 482 ms: 1.33x faster                                                        |
| pprint_pformat           | 1.30 sec                                               | 986 ms: 1.32x faster                                                        |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                                        |
| coroutines               | 20.7 ms                                                | 15.8 ms: 1.31x faster                                                       |
| regex_compile            | 95.3 ms                                                | 73.8 ms: 1.29x faster                                                       |
| pycparser                | 877 ms                                                 | 682 ms: 1.29x faster                                                        |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                       |
| xml_etree_process        | 46.5 ms                                                | 36.4 ms: 1.28x faster                                                       |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.27x faster                                                        |
| json_dumps               | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                       |
| sympy_sum                | 92.2 ms                                                | 73.1 ms: 1.26x faster                                                       |
| scimark_lu               | 103 ms                                                 | 82.8 ms: 1.24x faster                                                       |
| fannkuch                 | 303 ms                                                 | 246 ms: 1.23x faster                                                        |
| django_template          | 26.4 ms                                                | 21.6 ms: 1.22x faster                                                       |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                                      |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.18x faster                                                       |
| sympy_str                | 165 ms                                                 | 141 ms: 1.18x faster                                                        |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                        |
| scimark_fft              | 224 ms                                                 | 192 ms: 1.17x faster                                                        |
| docutils                 | 1.73 sec                                               | 1.51 sec: 1.14x faster                                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.03 ms: 1.13x faster                                                       |
| 2to3                     | 192 ms                                                 | 171 ms: 1.12x faster                                                        |
| dask                     | 253 ms                                                 | 226 ms: 1.12x faster                                                        |
| bench_thread_pool        | 527 us                                                 | 473 us: 1.11x faster                                                        |
| sympy_expand             | 269 ms                                                 | 243 ms: 1.11x faster                                                        |
| sqlglot_optimize         | 36.8 ms                                                | 33.4 ms: 1.10x faster                                                       |
| nqueens                  | 63.8 ms                                                | 58.0 ms: 1.10x faster                                                       |
| meteor_contest           | 77.7 ms                                                | 71.6 ms: 1.09x faster                                                       |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.07x faster                                                        |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                       |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                       |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                                      |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 72.1 ms                                                | 70.5 ms: 1.02x faster                                                       |
| xml_etree_generate       | 53.5 ms                                                | 52.4 ms: 1.02x faster                                                       |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                       |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                                       |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.05x slower                                                       |
| create_gc_cycles         | 860 us                                                 | 905 us: 1.05x slower                                                        |
| json_loads               | 16.4 us                                                | 17.4 us: 1.06x slower                                                       |
| coverage                 | 41.5 ms                                                | 45.5 ms: 1.10x slower                                                       |
| genshi_xml               | 33.8 ms                                                | 39.8 ms: 1.18x slower                                                       |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                        |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                       |
| bench_mp_pool            | 37.4 ms                                                | 50.6 ms: 1.35x slower                                                       |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.42x slower                                                       |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.61x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, asyncio_websockets, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240713-3.14.0a0-bbb07e8-JIT/bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.32x