# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.228x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 186 ms: 1.03x faster                                                      |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                     |
| tornado_http   | 86.7 ms                                                | 73.1 ms: 1.19x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| async_tree_io           | 980 ms                                                 | 582 ms: 1.68x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.0 ms: 1.43x faster                                                     |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 76.6 ms: 1.24x faster                                                     |
| regex_dna      | 174 ms                                                 | 144 ms: 1.21x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                      |
| tomli_loads          | 1.71 sec                                               | 1.27 sec: 1.34x faster                                                    |
| xml_etree_process    | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                     |
| json_dumps           | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                | 49.6 ms: 1.08x faster                                                     |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.1 ms: 1.66x slower                                                     |
| python_startup_no_site | 7.91 ms                                                | 14.3 ms: 1.80x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.73x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.58 ms: 1.50x faster                                                     |
| django_template | 26.4 ms                                                | 24.1 ms: 1.09x faster                                                     |
| genshi_text     | 17.3 ms                                                | 16.6 ms: 1.05x faster                                                     |
| genshi_xml      | 33.8 ms                                                | 44.1 ms: 1.30x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.6 us: 3.31x faster                                                     |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.43 ms: 2.02x faster                                                     |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| raytrace                 | 301 ms                                                 | 172 ms: 1.75x faster                                                      |
| deepcopy                 | 272 us                                                 | 156 us: 1.74x faster                                                      |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                      |
| async_tree_io            | 980 ms                                                 | 582 ms: 1.68x faster                                                      |
| logging_silent           | 117 ns                                                 | 70.3 ns: 1.67x faster                                                     |
| scimark_lu               | 103 ms                                                 | 64.1 ms: 1.61x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                      |
| chaos                    | 65.8 ms                                                | 42.3 ms: 1.55x faster                                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                     |
| richards_super           | 57.8 ms                                                | 38.4 ms: 1.51x faster                                                     |
| mako                     | 9.87 ms                                                | 6.58 ms: 1.50x faster                                                     |
| go                       | 151 ms                                                 | 102 ms: 1.48x faster                                                      |
| scimark_sor              | 128 ms                                                 | 86.8 ms: 1.48x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 45.8 ms: 1.43x faster                                                     |
| nbody                    | 93.0 ms                                                | 65.0 ms: 1.43x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.11 us: 1.43x faster                                                     |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                     |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                      |
| logging_format           | 4.83 us                                                | 3.42 us: 1.41x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 888 us: 1.40x faster                                                      |
| richards                 | 48.7 ms                                                | 34.8 ms: 1.40x faster                                                     |
| spectral_norm            | 94.8 ms                                                | 69.6 ms: 1.36x faster                                                     |
| thrift                   | 572 us                                                 | 423 us: 1.35x faster                                                      |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.56 ms: 1.35x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.27 sec: 1.34x faster                                                    |
| xml_etree_process        | 46.5 ms                                                | 34.6 ms: 1.34x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.08 ms: 1.33x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 54.9 ms: 1.31x faster                                                     |
| generators               | 32.3 ms                                                | 24.9 ms: 1.30x faster                                                     |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                     |
| pyflate                  | 427 ms                                                 | 330 ms: 1.29x faster                                                      |
| pylint                   | 277 ms                                                 | 215 ms: 1.29x faster                                                      |
| pycparser                | 877 ms                                                 | 693 ms: 1.26x faster                                                      |
| pprint_safe_repr         | 641 ms                                                 | 511 ms: 1.25x faster                                                      |
| coroutines               | 20.7 ms                                                | 16.5 ms: 1.25x faster                                                     |
| pprint_pformat           | 1.30 sec                                               | 1.04 sec: 1.25x faster                                                    |
| comprehensions           | 16.9 us                                                | 13.5 us: 1.25x faster                                                     |
| regex_compile            | 95.3 ms                                                | 76.6 ms: 1.24x faster                                                     |
| regex_dna                | 174 ms                                                 | 144 ms: 1.21x faster                                                      |
| dulwich_log              | 35.3 ms                                                | 29.2 ms: 1.21x faster                                                     |
| hexiom                   | 6.19 ms                                                | 5.17 ms: 1.20x faster                                                     |
| tornado_http             | 86.7 ms                                                | 73.1 ms: 1.19x faster                                                     |
| sqlalchemy_declarative   | 73.3 ms                                                | 61.9 ms: 1.18x faster                                                     |
| scimark_fft              | 224 ms                                                 | 192 ms: 1.17x faster                                                      |
| sympy_sum                | 92.2 ms                                                | 80.4 ms: 1.15x faster                                                     |
| json_dumps               | 8.11 ms                                                | 7.16 ms: 1.13x faster                                                     |
| fannkuch                 | 303 ms                                                 | 269 ms: 1.13x faster                                                      |
| bench_thread_pool        | 527 us                                                 | 471 us: 1.12x faster                                                      |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| django_template          | 26.4 ms                                                | 24.1 ms: 1.09x faster                                                     |
| pathlib                  | 24.5 ms                                                | 22.6 ms: 1.09x faster                                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.17 ms: 1.08x faster                                                     |
| xml_etree_generate       | 53.5 ms                                                | 49.6 ms: 1.08x faster                                                     |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                     |
| sympy_str                | 165 ms                                                 | 154 ms: 1.08x faster                                                      |
| sympy_expand             | 269 ms                                                 | 250 ms: 1.08x faster                                                      |
| nqueens                  | 63.8 ms                                                | 59.4 ms: 1.07x faster                                                     |
| genshi_text              | 17.3 ms                                                | 16.6 ms: 1.05x faster                                                     |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                                    |
| meteor_contest           | 77.7 ms                                                | 74.6 ms: 1.04x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 12.7 ms: 1.03x faster                                                     |
| 2to3                     | 192 ms                                                 | 186 ms: 1.03x faster                                                      |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                     |
| xml_etree_parse          | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                     |
| sqlglot_optimize         | 36.8 ms                                                | 38.0 ms: 1.03x slower                                                     |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                     |
| coverage                 | 41.5 ms                                                | 44.0 ms: 1.06x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.94 ms: 1.24x slower                                                     |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                      |
| genshi_xml               | 33.8 ms                                                | 44.1 ms: 1.30x slower                                                     |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.54x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 61.6 ms: 1.65x slower                                                     |
| python_startup           | 10.9 ms                                                | 18.1 ms: 1.66x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 14.3 ms: 1.80x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (2): sqlglot_normalize, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.228x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.43x