# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.263x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 169 ms: 1.13x faster                                                   |
| docutils       | 1.73 sec                                               | 1.42 sec: 1.22x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 381 ms: 2.57x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 206 ms: 2.29x faster                                                   |
| async_tree_none         | 388 ms                                                 | 170 ms: 2.28x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 426 ms: 1.52x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.13x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 68.4 ms: 1.36x faster                                                  |
| float          | 69.0 ms                                                | 51.4 ms: 1.34x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 70.7 ms: 1.35x faster                                                  |
| regex_dna      | 174 ms                                                 | 136 ms: 1.29x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 15.7 ms: 1.10x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 208 us: 1.35x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 153 us: 1.27x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 39.3 ms: 1.18x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.35 ms: 1.10x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                  |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 21.4 ms: 1.97x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.5 ms: 2.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 2.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                  |
| django_template | 26.4 ms                                                | 21.2 ms: 1.24x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.8 ms: 1.18x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 31.5 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 98.6 us: 3.27x faster                                                  |
| async_tree_io            | 980 ms                                                 | 381 ms: 2.57x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 206 ms: 2.29x faster                                                   |
| async_tree_none          | 388 ms                                                 | 170 ms: 2.28x faster                                                   |
| deltablue                | 4.91 ms                                                | 2.47 ms: 1.99x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 18.1 us: 1.91x faster                                                  |
| deepcopy                 | 272 us                                                 | 151 us: 1.79x faster                                                   |
| raytrace                 | 301 ms                                                 | 170 ms: 1.77x faster                                                   |
| go                       | 151 ms                                                 | 86.9 ms: 1.73x faster                                                  |
| pylint                   | 277 ms                                                 | 161 ms: 1.72x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| logging_silent           | 117 ns                                                 | 69.3 ns: 1.69x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.0 ms: 1.69x faster                                                  |
| richards_super           | 57.8 ms                                                | 36.9 ms: 1.57x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 800 us: 1.55x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 61.8 ms: 1.53x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 426 ms: 1.52x faster                                                   |
| sqlglot_transpile        | 1.44 ms                                                | 971 us: 1.49x faster                                                   |
| richards                 | 48.7 ms                                                | 33.4 ms: 1.46x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.61 us: 1.44x faster                                                  |
| mako                     | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 46.1 ms: 1.42x faster                                                  |
| generators               | 32.3 ms                                                | 22.8 ms: 1.42x faster                                                  |
| scimark_lu               | 103 ms                                                 | 73.6 ms: 1.40x faster                                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.49 ms: 1.37x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.26 us: 1.37x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.54 ms: 1.36x faster                                                  |
| nbody                    | 93.0 ms                                                | 68.4 ms: 1.36x faster                                                  |
| logging_format           | 4.83 us                                                | 3.57 us: 1.35x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.35x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 208 us: 1.35x faster                                                   |
| regex_compile            | 95.3 ms                                                | 70.7 ms: 1.35x faster                                                  |
| float                    | 69.0 ms                                                | 51.4 ms: 1.34x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                  |
| scimark_sor              | 128 ms                                                 | 95.6 ms: 1.34x faster                                                  |
| pycparser                | 877 ms                                                 | 658 ms: 1.33x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 986 ms: 1.32x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 485 ms: 1.32x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 54.5 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                                   |
| pyflate                  | 427 ms                                                 | 327 ms: 1.30x faster                                                   |
| scimark_fft              | 224 ms                                                 | 174 ms: 1.29x faster                                                   |
| regex_dna                | 174 ms                                                 | 136 ms: 1.29x faster                                                   |
| dulwich_log              | 35.3 ms                                                | 27.8 ms: 1.27x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 153 us: 1.27x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.72 ms: 1.26x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.7 ms: 1.25x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 73.9 ms: 1.25x faster                                                  |
| django_template          | 26.4 ms                                                | 21.2 ms: 1.24x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.42 sec: 1.22x faster                                                 |
| regex_effbot             | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.4 ms: 1.19x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 39.3 ms: 1.18x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.8 ms: 1.18x faster                                                  |
| sympy_str                | 165 ms                                                 | 141 ms: 1.17x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.14x faster                                                  |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                   |
| 2to3                     | 192 ms                                                 | 169 ms: 1.13x faster                                                   |
| sympy_expand             | 269 ms                                                 | 237 ms: 1.13x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 32.7 ms: 1.12x faster                                                  |
| json_dumps               | 8.11 ms                                                | 7.35 ms: 1.10x faster                                                  |
| nqueens                  | 63.8 ms                                                | 58.2 ms: 1.10x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.7 ms: 1.10x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.10x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 483 us: 1.09x faster                                                   |
| json                     | 3.08 ms                                                | 2.86 ms: 1.08x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.3 ms: 1.08x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.52 sec: 1.07x faster                                                 |
| genshi_xml               | 33.8 ms                                                | 31.5 ms: 1.07x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.07x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                                   |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                                  |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 3.07 ms: 1.30x slower                                                  |
| telco                    | 3.49 ms                                                | 4.60 ms: 1.32x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.27 ms: 1.48x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 63.4 ms: 1.70x slower                                                  |
| python_startup           | 10.9 ms                                                | 21.4 ms: 1.97x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.5 ms: 2.09x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, mypy2
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.263x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.34x