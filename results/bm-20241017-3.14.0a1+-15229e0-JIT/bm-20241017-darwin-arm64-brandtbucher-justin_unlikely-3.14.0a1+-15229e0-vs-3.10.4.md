# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_unlikely
- machine: darwin-arm64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 183 ms: 1.05x faster                                                    |
| docutils       | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                  |
| html5lib       | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                                    |
| async_tree_memoization  | 474 ms                                                 | 245 ms: 1.93x faster                                                    |
| async_tree_io           | 980 ms                                                 | 582 ms: 1.68x faster                                                    |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                   |
| nbody          | 93.0 ms                                                | 65.5 ms: 1.42x faster                                                   |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 75.8 ms: 1.26x faster                                                   |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                    |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 180 us: 1.56x faster                                                    |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.48x faster                                                    |
| tomli_loads          | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 35.0 ms: 1.33x faster                                                   |
| json_dumps           | 8.11 ms                                                | 7.14 ms: 1.14x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 50.8 ms: 1.05x faster                                                   |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 72.9 ms: 1.01x slower                                                   |
| unpickle             | 8.80 us                                                | 9.13 us: 1.04x slower                                                   |
| pickle_list          | 2.74 us                                                | 2.86 us: 1.05x slower                                                   |
| pickle               | 6.97 us                                                | 7.32 us: 1.05x slower                                                   |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                   |
| unpickle_list        | 2.69 us                                                | 2.96 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.2 ms: 1.76x slower                                                   |
| python_startup_no_site | 7.91 ms                                                | 14.8 ms: 1.87x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.82x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.48 ms: 1.52x faster                                                   |
| django_template | 26.4 ms                                                | 22.8 ms: 1.16x faster                                                   |
| genshi_text     | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                   |
| genshi_xml      | 33.8 ms                                                | 42.9 ms: 1.27x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.9 us: 3.30x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.06x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.41 ms: 2.04x faster                                                   |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                                    |
| async_tree_memoization   | 474 ms                                                 | 245 ms: 1.93x faster                                                    |
| deepcopy                 | 272 us                                                 | 156 us: 1.75x faster                                                    |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                                    |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                                    |
| async_tree_io            | 980 ms                                                 | 582 ms: 1.68x faster                                                    |
| logging_silent           | 117 ns                                                 | 69.9 ns: 1.68x faster                                                   |
| scimark_lu               | 103 ms                                                 | 64.6 ms: 1.59x faster                                                   |
| chaos                    | 65.8 ms                                                | 41.8 ms: 1.57x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 180 us: 1.56x faster                                                    |
| go                       | 151 ms                                                 | 98.2 ms: 1.53x faster                                                   |
| mako                     | 9.87 ms                                                | 6.48 ms: 1.52x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.49x faster                                                   |
| richards_super           | 57.8 ms                                                | 38.7 ms: 1.49x faster                                                   |
| scimark_sor              | 128 ms                                                 | 86.1 ms: 1.49x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.48x faster                                                    |
| asyncio_tcp              | 659 ms                                                 | 456 ms: 1.45x faster                                                    |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 45.9 ms: 1.43x faster                                                   |
| float                    | 69.0 ms                                                | 48.4 ms: 1.43x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 873 us: 1.42x faster                                                    |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                                   |
| nbody                    | 93.0 ms                                                | 65.5 ms: 1.42x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                    |
| richards                 | 48.7 ms                                                | 35.2 ms: 1.38x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 69.8 ms: 1.36x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.26 sec: 1.36x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.07 ms: 1.35x faster                                                   |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                                    |
| xml_etree_process        | 46.5 ms                                                | 35.0 ms: 1.33x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 54.1 ms: 1.33x faster                                                   |
| comprehensions           | 16.9 us                                                | 12.9 us: 1.31x faster                                                   |
| pyflate                  | 427 ms                                                 | 327 ms: 1.30x faster                                                    |
| pprint_safe_repr         | 641 ms                                                 | 496 ms: 1.29x faster                                                    |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.28x faster                                                  |
| generators               | 32.3 ms                                                | 25.2 ms: 1.28x faster                                                   |
| pycparser                | 877 ms                                                 | 683 ms: 1.28x faster                                                    |
| regex_compile            | 95.3 ms                                                | 75.8 ms: 1.26x faster                                                   |
| hexiom                   | 6.19 ms                                                | 4.95 ms: 1.25x faster                                                   |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                   |
| html5lib                 | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                   |
| dulwich_log              | 35.3 ms                                                | 28.8 ms: 1.23x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                                  |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                    |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.17x faster                                                    |
| sympy_sum                | 92.2 ms                                                | 79.3 ms: 1.16x faster                                                   |
| django_template          | 26.4 ms                                                | 22.8 ms: 1.16x faster                                                   |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                    |
| json_dumps               | 8.11 ms                                                | 7.14 ms: 1.14x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                                    |
| docutils                 | 1.73 sec                                               | 1.58 sec: 1.10x faster                                                  |
| nqueens                  | 63.8 ms                                                | 58.2 ms: 1.10x faster                                                   |
| sympy_str                | 165 ms                                                 | 151 ms: 1.09x faster                                                    |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                                   |
| sympy_expand             | 269 ms                                                 | 247 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.19 ms: 1.07x faster                                                   |
| json                     | 3.08 ms                                                | 2.88 ms: 1.07x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 50.8 ms: 1.05x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.55 sec: 1.05x faster                                                  |
| 2to3                     | 192 ms                                                 | 183 ms: 1.05x faster                                                    |
| meteor_contest           | 77.7 ms                                                | 74.6 ms: 1.04x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.04x faster                                                   |
| genshi_text              | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                                    |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.01x slower                                                    |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.9 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 37.5 ms: 1.02x slower                                                   |
| unpickle                 | 8.80 us                                                | 9.13 us: 1.04x slower                                                   |
| pickle_list              | 2.74 us                                                | 2.86 us: 1.05x slower                                                   |
| coverage                 | 41.5 ms                                                | 43.5 ms: 1.05x slower                                                   |
| pickle                   | 6.97 us                                                | 7.32 us: 1.05x slower                                                   |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.05x slower                                                   |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                   |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                   |
| unpickle_list            | 2.69 us                                                | 2.96 us: 1.10x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.95 ms: 1.25x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 42.9 ms: 1.27x slower                                                   |
| async_generators         | 231 ms                                                 | 295 ms: 1.27x slower                                                    |
| telco                    | 3.49 ms                                                | 4.67 ms: 1.34x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.31 ms: 1.52x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 61.8 ms: 1.65x slower                                                   |
| python_startup           | 10.9 ms                                                | 19.2 ms: 1.76x slower                                                   |
| python_startup_no_site   | 7.91 ms                                                | 14.8 ms: 1.87x slower                                                   |
| unpack_sequence          | 39.0 ns                                                | 77.0 ns: 1.97x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                            |

Benchmark hidden because not significant (3): pylint, tornado_http, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241017-3.14.0a1+-15229e0-JIT/bm-20241017-darwin-arm64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.43x