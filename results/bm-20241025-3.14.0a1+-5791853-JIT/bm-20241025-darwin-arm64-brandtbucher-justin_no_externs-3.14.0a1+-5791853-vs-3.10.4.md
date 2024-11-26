# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.224x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 185 ms: 1.04x faster                                                      |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| html5lib       | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                     |
| tornado_http   | 86.7 ms                                                | 71.5 ms: 1.21x faster                                                     |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| async_tree_io           | 980 ms                                                 | 583 ms: 1.68x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 457 ms: 1.42x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.2 ms: 1.43x faster                                                     |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                     |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.6 ms: 1.24x faster                                                     |
| regex_dna      | 174 ms                                                 | 141 ms: 1.24x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                      |
| tomli_loads          | 1.71 sec                                               | 1.27 sec: 1.35x faster                                                    |
| xml_etree_process    | 46.5 ms                                                | 35.2 ms: 1.32x faster                                                     |
| json_dumps           | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                | 49.7 ms: 1.08x faster                                                     |
| json_loads           | 16.4 us                                                | 16.5 us: 1.00x slower                                                     |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.2 ms: 1.68x slower                                                     |
| python_startup_no_site | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.74x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.56 ms: 1.51x faster                                                     |
| django_template | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                     |
| genshi_text     | 17.3 ms                                                | 17.6 ms: 1.02x slower                                                     |
| genshi_xml      | 33.8 ms                                                | 43.9 ms: 1.30x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.5 us: 3.31x faster                                                     |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.46 ms: 2.00x faster                                                     |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| deepcopy                 | 272 us                                                 | 156 us: 1.74x faster                                                      |
| raytrace                 | 301 ms                                                 | 177 ms: 1.70x faster                                                      |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                      |
| logging_silent           | 117 ns                                                 | 69.7 ns: 1.68x faster                                                     |
| async_tree_io            | 980 ms                                                 | 583 ms: 1.68x faster                                                      |
| scimark_lu               | 103 ms                                                 | 65.6 ms: 1.57x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                                      |
| chaos                    | 65.8 ms                                                | 42.6 ms: 1.54x faster                                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                                     |
| richards_super           | 57.8 ms                                                | 38.4 ms: 1.51x faster                                                     |
| mako                     | 9.87 ms                                                | 6.56 ms: 1.51x faster                                                     |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                      |
| scimark_sor              | 128 ms                                                 | 87.3 ms: 1.47x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                      |
| nbody                    | 93.0 ms                                                | 65.2 ms: 1.43x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.13 us: 1.42x faster                                                     |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 457 ms: 1.42x faster                                                      |
| logging_format           | 4.83 us                                                | 3.42 us: 1.41x faster                                                     |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                     |
| scimark_monte_carlo      | 65.6 ms                                                | 46.5 ms: 1.41x faster                                                     |
| richards                 | 48.7 ms                                                | 34.7 ms: 1.40x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 889 us: 1.40x faster                                                      |
| thrift                   | 572 us                                                 | 422 us: 1.36x faster                                                      |
| spectral_norm            | 94.8 ms                                                | 70.1 ms: 1.35x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.27 sec: 1.35x faster                                                    |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.64 ms: 1.34x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.08 ms: 1.33x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 35.2 ms: 1.32x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 55.2 ms: 1.30x faster                                                     |
| generators               | 32.3 ms                                                | 24.9 ms: 1.30x faster                                                     |
| html5lib                 | 42.4 ms                                                | 32.8 ms: 1.29x faster                                                     |
| pyflate                  | 427 ms                                                 | 332 ms: 1.29x faster                                                      |
| pylint                   | 277 ms                                                 | 217 ms: 1.28x faster                                                      |
| pycparser                | 877 ms                                                 | 694 ms: 1.26x faster                                                      |
| comprehensions           | 16.9 us                                                | 13.6 us: 1.25x faster                                                     |
| regex_compile            | 95.3 ms                                                | 76.6 ms: 1.24x faster                                                     |
| coroutines               | 20.7 ms                                                | 16.7 ms: 1.24x faster                                                     |
| regex_dna                | 174 ms                                                 | 141 ms: 1.24x faster                                                      |
| pprint_pformat           | 1.30 sec                                               | 1.06 sec: 1.23x faster                                                    |
| pprint_safe_repr         | 641 ms                                                 | 521 ms: 1.23x faster                                                      |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.22x faster                                                     |
| tornado_http             | 86.7 ms                                                | 71.5 ms: 1.21x faster                                                     |
| hexiom                   | 6.19 ms                                                | 5.15 ms: 1.20x faster                                                     |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                      |
| sqlalchemy_declarative   | 73.3 ms                                                | 62.5 ms: 1.17x faster                                                     |
| sympy_sum                | 92.2 ms                                                | 81.0 ms: 1.14x faster                                                     |
| django_template          | 26.4 ms                                                | 23.2 ms: 1.14x faster                                                     |
| json_dumps               | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                     |
| bench_thread_pool        | 527 us                                                 | 477 us: 1.11x faster                                                      |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                     |
| json                     | 3.08 ms                                                | 2.85 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                     |
| sympy_str                | 165 ms                                                 | 153 ms: 1.08x faster                                                      |
| xml_etree_generate       | 53.5 ms                                                | 49.7 ms: 1.08x faster                                                     |
| fannkuch                 | 303 ms                                                 | 282 ms: 1.07x faster                                                      |
| sympy_expand             | 269 ms                                                 | 253 ms: 1.06x faster                                                      |
| nqueens                  | 63.8 ms                                                | 60.1 ms: 1.06x faster                                                     |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.05x faster                                                    |
| 2to3                     | 192 ms                                                 | 185 ms: 1.04x faster                                                      |
| meteor_contest           | 77.7 ms                                                | 75.1 ms: 1.04x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 12.7 ms: 1.03x faster                                                     |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| sqlglot_normalize        | 190 ms                                                 | 190 ms: 1.00x faster                                                      |
| json_loads               | 16.4 us                                                | 16.5 us: 1.00x slower                                                     |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.01x slower                                                     |
| pidigits                 | 282 ms                                                 | 284 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                     |
| genshi_text              | 17.3 ms                                                | 17.6 ms: 1.02x slower                                                     |
| sqlglot_optimize         | 36.8 ms                                                | 38.0 ms: 1.03x slower                                                     |
| coverage                 | 41.5 ms                                                | 44.0 ms: 1.06x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.96 ms: 1.25x slower                                                     |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                                      |
| genshi_xml               | 33.8 ms                                                | 43.9 ms: 1.30x slower                                                     |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.34 ms: 1.56x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 61.9 ms: 1.65x slower                                                     |
| python_startup           | 10.9 ms                                                | 18.2 ms: 1.68x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.224x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.42x