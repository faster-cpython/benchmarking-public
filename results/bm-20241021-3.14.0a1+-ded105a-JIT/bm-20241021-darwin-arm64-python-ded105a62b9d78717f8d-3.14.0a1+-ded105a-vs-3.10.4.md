# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: darwin-arm64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 183 ms: 1.05x faster                                                   |
| docutils       | 1.73 sec                                               | 1.55 sec: 1.11x faster                                                 |
| html5lib       | 42.4 ms                                                | 32.3 ms: 1.31x faster                                                  |
| tornado_http   | 86.7 ms                                                | 75.2 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.96x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 263 ms: 1.80x faster                                                   |
| async_tree_io           | 980 ms                                                 | 579 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 456 ms: 1.43x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 48.2 ms: 1.43x faster                                                  |
| nbody          | 93.0 ms                                                | 65.7 ms: 1.42x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.7 ms: 1.27x faster                                                  |
| regex_dna      | 174 ms                                                 | 142 ms: 1.23x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 34.5 ms: 1.35x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 50.0 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.2 ms: 1.58x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.62x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                  |
| django_template | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.7 ms: 1.04x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 42.2 ms: 1.25x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.1 us: 3.29x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.39 ms: 2.06x faster                                                  |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.96x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 263 ms: 1.80x faster                                                   |
| raytrace                 | 301 ms                                                 | 170 ms: 1.77x faster                                                   |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| async_tree_io            | 980 ms                                                 | 579 ms: 1.69x faster                                                   |
| logging_silent           | 117 ns                                                 | 69.7 ns: 1.68x faster                                                  |
| chaos                    | 65.8 ms                                                | 41.7 ms: 1.58x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                   |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                   |
| scimark_lu               | 103 ms                                                 | 66.6 ms: 1.54x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                  |
| richards_super           | 57.8 ms                                                | 37.9 ms: 1.53x faster                                                  |
| mako                     | 9.87 ms                                                | 6.47 ms: 1.53x faster                                                  |
| go                       | 151 ms                                                 | 98.9 ms: 1.52x faster                                                  |
| scimark_sor              | 128 ms                                                 | 85.9 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 45.6 ms: 1.44x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.11 us: 1.43x faster                                                  |
| float                    | 69.0 ms                                                | 48.2 ms: 1.43x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 869 us: 1.43x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 456 ms: 1.43x faster                                                   |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                  |
| nbody                    | 93.0 ms                                                | 65.7 ms: 1.42x faster                                                  |
| richards                 | 48.7 ms                                                | 34.5 ms: 1.41x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 69.2 ms: 1.37x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                 |
| thrift                   | 572 us                                                 | 423 us: 1.35x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.07 ms: 1.35x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 34.5 ms: 1.35x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 53.9 ms: 1.33x faster                                                  |
| html5lib                 | 42.4 ms                                                | 32.3 ms: 1.31x faster                                                  |
| pyflate                  | 427 ms                                                 | 327 ms: 1.31x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 998 ms: 1.31x faster                                                   |
| comprehensions           | 16.9 us                                                | 13.0 us: 1.30x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 497 ms: 1.29x faster                                                   |
| pycparser                | 877 ms                                                 | 683 ms: 1.28x faster                                                   |
| generators               | 32.3 ms                                                | 25.2 ms: 1.28x faster                                                  |
| regex_compile            | 95.3 ms                                                | 74.7 ms: 1.27x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                  |
| hexiom                   | 6.19 ms                                                | 5.02 ms: 1.23x faster                                                  |
| regex_dna                | 174 ms                                                 | 142 ms: 1.23x faster                                                   |
| dulwich_log              | 35.3 ms                                                | 29.1 ms: 1.21x faster                                                  |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.18x faster                                                   |
| fannkuch                 | 303 ms                                                 | 258 ms: 1.17x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 79.6 ms: 1.16x faster                                                  |
| tornado_http             | 86.7 ms                                                | 75.2 ms: 1.15x faster                                                  |
| django_template          | 26.4 ms                                                | 23.1 ms: 1.14x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.13 ms: 1.14x faster                                                  |
| pathlib                  | 24.5 ms                                                | 21.9 ms: 1.12x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.55 sec: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                   |
| sympy_str                | 165 ms                                                 | 151 ms: 1.10x faster                                                   |
| nqueens                  | 63.8 ms                                                | 58.3 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.15 ms: 1.09x faster                                                  |
| sympy_expand             | 269 ms                                                 | 248 ms: 1.08x faster                                                   |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.0 ms: 1.07x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.53 sec: 1.06x faster                                                 |
| 2to3                     | 192 ms                                                 | 183 ms: 1.05x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 12.6 ms: 1.05x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 74.4 ms: 1.04x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.7 ms: 1.04x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.03x faster                                                   |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 37.3 ms: 1.01x slower                                                  |
| coverage                 | 41.5 ms                                                | 43.6 ms: 1.05x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.95 ms: 1.25x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 42.2 ms: 1.25x slower                                                  |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                                   |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.31x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.53x slower                                                  |
| python_startup           | 10.9 ms                                                | 17.2 ms: 1.58x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 61.3 ms: 1.64x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-darwin-arm64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.43x