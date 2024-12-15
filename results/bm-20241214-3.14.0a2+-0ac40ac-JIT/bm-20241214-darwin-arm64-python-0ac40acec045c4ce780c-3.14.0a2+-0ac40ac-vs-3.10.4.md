# Results vs. 3.10.4

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: darwin-arm64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 198 ms: 1.04x slower                                                   |
| docutils       | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                 |
| html5lib       | 42.4 ms                                                | 33.5 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 376 ms: 2.60x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 204 ms: 2.32x faster                                                   |
| async_tree_none         | 388 ms                                                 | 169 ms: 2.30x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 425 ms: 1.53x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.15x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                  |
| float          | 69.0 ms                                                | 47.9 ms: 1.44x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.5 ms: 1.37x faster                                                  |
| regex_dna      | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| regex_v8       | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 194 us                                                 | 125 us: 1.56x faster                                                   |
| pickle_pure_python   | 281 us                                                 | 195 us: 1.44x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.22 sec: 1.40x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.0 ms: 1.33x faster                                                  |
| json_dumps           | 8.11 ms                                                | 7.21 ms: 1.12x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 49.2 ms: 1.09x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 70.4 ms: 1.03x faster                                                  |
| json_loads           | 16.4 us                                                | 16.5 us: 1.00x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 21.6 ms: 1.99x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.6 ms: 2.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 2.04x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                  |
| django_template | 26.4 ms                                                | 22.7 ms: 1.16x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 40.9 ms: 1.21x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 100 us: 3.22x faster                                                   |
| async_tree_io            | 980 ms                                                 | 376 ms: 2.60x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 204 ms: 2.32x faster                                                   |
| async_tree_none          | 388 ms                                                 | 169 ms: 2.30x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 17.2 us: 2.02x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.56 ms: 1.92x faster                                                  |
| deepcopy                 | 272 us                                                 | 157 us: 1.73x faster                                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                   |
| pylint                   | 277 ms                                                 | 166 ms: 1.66x faster                                                   |
| raytrace                 | 301 ms                                                 | 185 ms: 1.63x faster                                                   |
| mako                     | 9.87 ms                                                | 6.26 ms: 1.58x faster                                                  |
| scimark_sor              | 128 ms                                                 | 82.2 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 125 us: 1.56x faster                                                   |
| chaos                    | 65.8 ms                                                | 42.4 ms: 1.55x faster                                                  |
| logging_silent           | 117 ns                                                 | 75.6 ns: 1.55x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 62.0 ms: 1.53x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 425 ms: 1.53x faster                                                   |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                   |
| richards_super           | 57.8 ms                                                | 38.8 ms: 1.49x faster                                                  |
| scimark_lu               | 103 ms                                                 | 69.3 ms: 1.49x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.58 us: 1.47x faster                                                  |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 856 us: 1.45x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 45.2 ms: 1.45x faster                                                  |
| float                    | 69.0 ms                                                | 47.9 ms: 1.44x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 195 us: 1.44x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.22 sec: 1.40x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.39x faster                                                  |
| richards                 | 48.7 ms                                                | 35.0 ms: 1.39x faster                                                  |
| regex_compile            | 95.3 ms                                                | 69.5 ms: 1.37x faster                                                  |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                                   |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.62 ms: 1.34x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 53.8 ms: 1.34x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.0 ms: 1.33x faster                                                  |
| scimark_fft              | 224 ms                                                 | 171 ms: 1.31x faster                                                   |
| pycparser                | 877 ms                                                 | 675 ms: 1.30x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.44 us: 1.29x faster                                                  |
| thrift                   | 572 us                                                 | 443 us: 1.29x faster                                                   |
| logging_format           | 4.83 us                                                | 3.74 us: 1.29x faster                                                  |
| regex_dna                | 174 ms                                                 | 135 ms: 1.29x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.28x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 500 ms: 1.28x faster                                                   |
| html5lib                 | 42.4 ms                                                | 33.5 ms: 1.26x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.96 ms: 1.25x faster                                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.9 ms: 1.24x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.8 ms: 1.23x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.01 ms: 1.22x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 75.6 ms: 1.22x faster                                                  |
| comprehensions           | 16.9 us                                                | 13.9 us: 1.22x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.3 ms: 1.20x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.46 sec: 1.19x faster                                                 |
| generators               | 32.3 ms                                                | 27.3 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.94 ms: 1.17x faster                                                  |
| django_template          | 26.4 ms                                                | 22.7 ms: 1.16x faster                                                  |
| mypy2                    | 607 ms                                                 | 529 ms: 1.15x faster                                                   |
| sympy_str                | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                   |
| json_dumps               | 8.11 ms                                                | 7.21 ms: 1.12x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.8 ms: 1.12x faster                                                  |
| sympy_expand             | 269 ms                                                 | 244 ms: 1.10x faster                                                   |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 49.2 ms: 1.09x faster                                                  |
| json                     | 3.08 ms                                                | 2.85 ms: 1.08x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 15.9 ms: 1.08x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 34.3 ms: 1.07x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.9 ms: 1.07x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 502 us: 1.05x faster                                                   |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.57 sec: 1.04x faster                                                 |
| nqueens                  | 63.8 ms                                                | 61.7 ms: 1.03x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 70.4 ms: 1.03x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.5 us: 1.00x slower                                                  |
| 2to3                     | 192 ms                                                 | 198 ms: 1.04x slower                                                   |
| coverage                 | 41.5 ms                                                | 44.1 ms: 1.06x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.55 us: 1.06x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 40.9 ms: 1.21x slower                                                  |
| telco                    | 3.49 ms                                                | 4.46 ms: 1.28x slower                                                  |
| async_generators         | 231 ms                                                 | 300 ms: 1.30x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 3.07 ms: 1.30x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.29 ms: 1.50x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 63.3 ms: 1.69x slower                                                  |
| python_startup           | 10.9 ms                                                | 21.6 ms: 1.99x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 16.6 ms: 2.10x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): genshi_text
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-darwin-arm64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.37x