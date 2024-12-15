# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.025x faster
- HPT reliability: 74.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 214 ms: 1.12x slower                                                   |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                 |
| html5lib       | 42.4 ms                                                | 44.3 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 449 ms: 2.18x faster                                                   |
| async_tree_none         | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 86.2 ms: 1.08x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 69.0 ms                                                | 82.9 ms: 1.20x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 134 ms: 1.30x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                  |
| regex_v8       | 17.1 ms                                                | 15.5 ms: 1.10x faster                                                  |
| regex_compile  | 95.3 ms                                                | 89.4 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 72.1 ms                                                | 66.4 ms: 1.09x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.58 sec: 1.08x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 45.8 ms: 1.02x faster                                                  |
| json_dumps           | 8.11 ms                                                | 8.26 ms: 1.02x slower                                                  |
| pickle_pure_python   | 281 us                                                 | 296 us: 1.06x slower                                                   |
| json_loads           | 16.4 us                                                | 17.4 us: 1.06x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 57.4 ms: 1.07x slower                                                  |
| unpickle_pure_python | 194 us                                                 | 209 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 22.8 ms: 2.10x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 18.1 ms: 2.29x slower                                                  |
| Geometric mean         | (ref)                                                  | 2.20x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 26.4 ms                                                | 27.0 ms: 1.02x slower                                                  |
| genshi_text     | 17.3 ms                                                | 17.8 ms: 1.02x slower                                                  |
| genshi_xml      | 33.8 ms                                                | 36.4 ms: 1.08x slower                                                  |
| mako            | 9.87 ms                                                | 11.1 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 120 us: 2.70x faster                                                   |
| async_tree_io            | 980 ms                                                 | 449 ms: 2.18x faster                                                   |
| async_tree_none          | 388 ms                                                 | 206 ms: 1.88x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 238 ms: 1.72x faster                                                   |
| deepcopy                 | 272 us                                                 | 178 us: 1.52x faster                                                   |
| pylint                   | 277 ms                                                 | 189 ms: 1.47x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 23.7 us: 1.47x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                   |
| regex_dna                | 174 ms                                                 | 134 ms: 1.30x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 74.6 ms: 1.27x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.88 us: 1.24x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.03 ms: 1.21x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.5 ms: 1.18x faster                                                  |
| generators               | 32.3 ms                                                | 27.4 ms: 1.18x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 63.1 ms: 1.14x faster                                                  |
| pycparser                | 877 ms                                                 | 786 ms: 1.12x faster                                                   |
| chaos                    | 65.8 ms                                                | 59.2 ms: 1.11x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.5 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 66.4 ms: 1.09x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.58 sec: 1.08x faster                                                 |
| nbody                    | 93.0 ms                                                | 86.2 ms: 1.08x faster                                                  |
| nqueens                  | 63.8 ms                                                | 59.2 ms: 1.08x faster                                                  |
| richards_super           | 57.8 ms                                                | 53.8 ms: 1.08x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.8 ms: 1.07x faster                                                  |
| regex_compile            | 95.3 ms                                                | 89.4 ms: 1.07x faster                                                  |
| sqlite_synth             | 1.46 us                                                | 1.38 us: 1.06x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| pyflate                  | 427 ms                                                 | 413 ms: 1.03x faster                                                   |
| scimark_fft              | 224 ms                                                 | 217 ms: 1.03x faster                                                   |
| fannkuch                 | 303 ms                                                 | 294 ms: 1.03x faster                                                   |
| json                     | 3.08 ms                                                | 3.00 ms: 1.03x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 45.8 ms: 1.02x faster                                                  |
| hexiom                   | 6.19 ms                                                | 6.10 ms: 1.02x faster                                                  |
| raytrace                 | 301 ms                                                 | 297 ms: 1.02x faster                                                   |
| sqlalchemy_imperative    | 8.86 ms                                                | 8.73 ms: 1.01x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.62 sec: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| scimark_sor              | 128 ms                                                 | 129 ms: 1.00x slower                                                   |
| comprehensions           | 16.9 us                                                | 17.1 us: 1.01x slower                                                  |
| thrift                   | 572 us                                                 | 580 us: 1.01x slower                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 37.4 ms: 1.02x slower                                                  |
| json_dumps               | 8.11 ms                                                | 8.26 ms: 1.02x slower                                                  |
| pprint_safe_repr         | 641 ms                                                 | 655 ms: 1.02x slower                                                   |
| go                       | 151 ms                                                 | 154 ms: 1.02x slower                                                   |
| django_template          | 26.4 ms                                                | 27.0 ms: 1.02x slower                                                  |
| genshi_text              | 17.3 ms                                                | 17.8 ms: 1.02x slower                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                 |
| meteor_contest           | 77.7 ms                                                | 80.9 ms: 1.04x slower                                                  |
| html5lib                 | 42.4 ms                                                | 44.3 ms: 1.04x slower                                                  |
| logging_format           | 4.83 us                                                | 5.10 us: 1.06x slower                                                  |
| pickle_pure_python       | 281 us                                                 | 296 us: 1.06x slower                                                   |
| logging_simple           | 4.45 us                                                | 4.70 us: 1.06x slower                                                  |
| json_loads               | 16.4 us                                                | 17.4 us: 1.06x slower                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.64 ms: 1.06x slower                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 70.2 ms: 1.07x slower                                                  |
| sqlglot_normalize        | 190 ms                                                 | 204 ms: 1.07x slower                                                   |
| sympy_integrate          | 13.1 ms                                                | 14.1 ms: 1.07x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 57.4 ms: 1.07x slower                                                  |
| unpickle_pure_python     | 194 us                                                 | 209 us: 1.07x slower                                                   |
| genshi_xml               | 33.8 ms                                                | 36.4 ms: 1.08x slower                                                  |
| mypy2                    | 607 ms                                                 | 661 ms: 1.09x slower                                                   |
| scimark_lu               | 103 ms                                                 | 112 ms: 1.09x slower                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 80.9 ms: 1.10x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.63 ms: 1.11x slower                                                  |
| 2to3                     | 192 ms                                                 | 214 ms: 1.12x slower                                                   |
| mako                     | 9.87 ms                                                | 11.1 ms: 1.13x slower                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.63 ms: 1.13x slower                                                  |
| sqlglot_parse            | 1.24 ms                                                | 1.44 ms: 1.16x slower                                                  |
| sympy_str                | 165 ms                                                 | 196 ms: 1.18x slower                                                   |
| float                    | 69.0 ms                                                | 82.9 ms: 1.20x slower                                                  |
| coverage                 | 41.5 ms                                                | 51.7 ms: 1.25x slower                                                  |
| async_generators         | 231 ms                                                 | 300 ms: 1.30x slower                                                   |
| sympy_sum                | 92.2 ms                                                | 121 ms: 1.31x slower                                                   |
| create_gc_cycles         | 860 us                                                 | 1.14 ms: 1.33x slower                                                  |
| sympy_expand             | 269 ms                                                 | 372 ms: 1.38x slower                                                   |
| telco                    | 3.49 ms                                                | 5.07 ms: 1.45x slower                                                  |
| bench_thread_pool        | 527 us                                                 | 802 us: 1.52x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 74.0 ms: 1.98x slower                                                  |
| python_startup           | 10.9 ms                                                | 22.8 ms: 2.10x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 18.1 ms: 2.29x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (4): deltablue, logging_silent, richards, dulwich_log
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 74.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.52x