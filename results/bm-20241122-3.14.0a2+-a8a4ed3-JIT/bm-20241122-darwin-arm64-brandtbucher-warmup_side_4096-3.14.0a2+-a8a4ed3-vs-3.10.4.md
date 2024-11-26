# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: darwin-arm64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.234x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                                     |
| docutils       | 1.73 sec                                               | 1.49 sec: 1.17x faster                                                   |
| html5lib       | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                    |
| Geometric mean | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.88x faster                                                     |
| async_tree_none         | 388 ms                                                 | 208 ms: 1.86x faster                                                     |
| async_tree_io           | 980 ms                                                 | 606 ms: 1.62x faster                                                     |
| async_tree_cpu_io_mixed | 649 ms                                                 | 469 ms: 1.38x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.67x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                    |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                    |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 70.4 ms: 1.35x faster                                                    |
| regex_dna      | 174 ms                                                 | 135 ms: 1.29x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.02 ms: 1.22x faster                                                    |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.23x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 122 us: 1.59x faster                                                     |
| pickle_pure_python   | 281 us                                                 | 193 us: 1.45x faster                                                     |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                    |
| json_dumps           | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                    |
| xml_etree_generate   | 53.5 ms                                                | 49.9 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.8 ms: 1.82x slower                                                    |
| python_startup_no_site | 7.91 ms                                                | 15.1 ms: 1.91x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.86x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.21 ms: 1.59x faster                                                    |
| django_template | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                    |
| genshi_xml      | 33.8 ms                                                | 40.2 ms: 1.19x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 99.1 us: 3.26x faster                                                    |
| deepcopy_memo            | 34.7 us                                                | 17.5 us: 1.98x faster                                                    |
| deltablue                | 4.91 ms                                                | 2.56 ms: 1.92x faster                                                    |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.88x faster                                                     |
| async_tree_none          | 388 ms                                                 | 208 ms: 1.86x faster                                                     |
| pylint                   | 277 ms                                                 | 156 ms: 1.77x faster                                                     |
| deepcopy                 | 272 us                                                 | 157 us: 1.73x faster                                                     |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                     |
| raytrace                 | 301 ms                                                 | 182 ms: 1.65x faster                                                     |
| async_tree_io            | 980 ms                                                 | 606 ms: 1.62x faster                                                     |
| unpickle_pure_python     | 194 us                                                 | 122 us: 1.59x faster                                                     |
| mako                     | 9.87 ms                                                | 6.21 ms: 1.59x faster                                                    |
| logging_silent           | 117 ns                                                 | 75.9 ns: 1.54x faster                                                    |
| richards_super           | 57.8 ms                                                | 38.1 ms: 1.52x faster                                                    |
| chaos                    | 65.8 ms                                                | 43.6 ms: 1.51x faster                                                    |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                     |
| scimark_lu               | 103 ms                                                 | 68.5 ms: 1.50x faster                                                    |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.49x faster                                                    |
| scimark_sor              | 128 ms                                                 | 87.0 ms: 1.47x faster                                                    |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                    |
| scimark_monte_carlo      | 65.6 ms                                                | 45.0 ms: 1.46x faster                                                    |
| pickle_pure_python       | 281 us                                                 | 193 us: 1.45x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 862 us: 1.44x faster                                                     |
| richards                 | 48.7 ms                                                | 34.2 ms: 1.42x faster                                                    |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                    |
| sqlglot_transpile        | 1.44 ms                                                | 1.03 ms: 1.40x faster                                                    |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 469 ms: 1.38x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 70.1 ms: 1.35x faster                                                    |
| regex_compile            | 95.3 ms                                                | 70.4 ms: 1.35x faster                                                    |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.60 ms: 1.34x faster                                                    |
| pyflate                  | 427 ms                                                 | 323 ms: 1.32x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                    |
| pprint_pformat           | 1.30 sec                                               | 990 ms: 1.32x faster                                                     |
| crypto_pyaes             | 71.8 ms                                                | 54.6 ms: 1.32x faster                                                    |
| pprint_safe_repr         | 641 ms                                                 | 492 ms: 1.30x faster                                                     |
| thrift                   | 572 us                                                 | 440 us: 1.30x faster                                                     |
| html5lib                 | 42.4 ms                                                | 32.6 ms: 1.30x faster                                                    |
| pycparser                | 877 ms                                                 | 677 ms: 1.29x faster                                                     |
| logging_format           | 4.83 us                                                | 3.75 us: 1.29x faster                                                    |
| regex_dna                | 174 ms                                                 | 135 ms: 1.29x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.46 us: 1.29x faster                                                    |
| hexiom                   | 6.19 ms                                                | 4.87 ms: 1.27x faster                                                    |
| comprehensions           | 16.9 us                                                | 13.5 us: 1.25x faster                                                    |
| sqlalchemy_declarative   | 73.3 ms                                                | 59.0 ms: 1.24x faster                                                    |
| sympy_sum                | 92.2 ms                                                | 74.4 ms: 1.24x faster                                                    |
| regex_effbot             | 2.46 ms                                                | 2.02 ms: 1.22x faster                                                    |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                     |
| dulwich_log              | 35.3 ms                                                | 29.5 ms: 1.20x faster                                                    |
| generators               | 32.3 ms                                                | 27.1 ms: 1.19x faster                                                    |
| coroutines               | 20.7 ms                                                | 17.6 ms: 1.18x faster                                                    |
| docutils                 | 1.73 sec                                               | 1.49 sec: 1.17x faster                                                   |
| sympy_str                | 165 ms                                                 | 144 ms: 1.15x faster                                                     |
| django_template          | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                    |
| json_dumps               | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                    |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                     |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 11.7 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.05 ms: 1.12x faster                                                    |
| sympy_expand             | 269 ms                                                 | 243 ms: 1.11x faster                                                     |
| pathlib                  | 24.5 ms                                                | 22.6 ms: 1.08x faster                                                    |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.08x faster                                                    |
| bench_thread_pool        | 527 us                                                 | 489 us: 1.08x faster                                                     |
| sqlglot_optimize         | 36.8 ms                                                | 34.3 ms: 1.07x faster                                                    |
| xml_etree_generate       | 53.5 ms                                                | 49.9 ms: 1.07x faster                                                    |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                    |
| meteor_contest           | 77.7 ms                                                | 73.2 ms: 1.06x faster                                                    |
| nqueens                  | 63.8 ms                                                | 61.7 ms: 1.03x faster                                                    |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                                     |
| mdp                      | 1.63 sec                                               | 1.60 sec: 1.02x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                     |
| xml_etree_iterparse      | 72.1 ms                                                | 73.9 ms: 1.02x slower                                                    |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                                    |
| coverage                 | 41.5 ms                                                | 45.5 ms: 1.10x slower                                                    |
| genshi_xml               | 33.8 ms                                                | 40.2 ms: 1.19x slower                                                    |
| gc_traversal             | 2.36 ms                                                | 2.96 ms: 1.25x slower                                                    |
| telco                    | 3.49 ms                                                | 4.47 ms: 1.28x slower                                                    |
| async_generators         | 231 ms                                                 | 304 ms: 1.32x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.53x slower                                                    |
| bench_mp_pool            | 37.4 ms                                                | 61.6 ms: 1.65x slower                                                    |
| python_startup           | 10.9 ms                                                | 19.8 ms: 1.82x slower                                                    |
| python_startup_no_site   | 7.91 ms                                                | 15.1 ms: 1.91x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, genshi_text, json_loads
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-darwin-arm64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.234x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.36x