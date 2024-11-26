# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: darwin-arm64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.135x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 0.80x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 192 ms: 1.02x slower                                   |
| chameleon      | 5.08 ms                                                | 6.26 ms: 1.23x slower                                  |
| docutils       | 1.44 sec                                               | 1.73 sec: 1.20x slower                                 |
| html5lib       | 36.6 ms                                                | 42.4 ms: 1.16x slower                                  |
| tornado_http   | 75.8 ms                                                | 86.7 ms: 1.14x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_generators        | 295 ms                                                 | 231 ms: 1.28x faster                                   |
| coroutines              | 19.8 ms                                                | 20.7 ms: 1.05x slower                                  |
| async_tree_cpu_io_mixed | 460 ms                                                 | 649 ms: 1.41x slower                                   |
| asyncio_websockets      | 242 ms                                                 | 410 ms: 1.70x slower                                   |
| async_tree_memoization  | 268 ms                                                 | 474 ms: 1.77x slower                                   |
| async_tree_none         | 215 ms                                                 | 388 ms: 1.80x slower                                   |
| async_tree_io           | 507 ms                                                 | 980 ms: 1.93x slower                                   |
| Geometric mean          | (ref)                                                  | 1.43x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                   |
| float          | 56.0 ms                                                | 69.0 ms: 1.23x slower                                  |
| nbody          | 74.0 ms                                                | 93.0 ms: 1.26x slower                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.46 ms: 1.07x faster                                  |
| regex_v8       | 17.0 ms                                                | 17.1 ms: 1.01x slower                                  |
| regex_dna      | 149 ms                                                 | 174 ms: 1.17x slower                                   |
| regex_compile  | 78.6 ms                                                | 95.3 ms: 1.21x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_generate   | 57.0 ms                                                | 53.5 ms: 1.06x faster                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.03x faster                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 72.1 ms: 1.02x faster                                  |
| tomli_loads          | 1.57 sec                                               | 1.71 sec: 1.09x slower                                 |
| xml_etree_process    | 41.0 ms                                                | 46.5 ms: 1.13x slower                                  |
| unpickle_pure_python | 164 us                                                 | 194 us: 1.19x slower                                   |
| json_dumps           | 6.52 ms                                                | 8.11 ms: 1.24x slower                                  |
| pickle_pure_python   | 214 us                                                 | 281 us: 1.31x slower                                   |
| Geometric mean       | (ref)                                                  | 1.09x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 7.91 ms: 1.83x faster                                  |
| python_startup         | 18.9 ms                                                | 10.9 ms: 1.74x faster                                  |
| Geometric mean         | (ref)                                                  | 1.78x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 33.8 ms: 1.02x faster                                  |
| genshi_text     | 16.9 ms                                                | 17.3 ms: 1.03x slower                                  |
| django_template | 22.2 ms                                                | 26.4 ms: 1.19x slower                                  |
| mako            | 7.68 ms                                                | 9.87 ms: 1.29x slower                                  |
| Geometric mean  | (ref)                                                  | 1.11x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| dask                     | 790 ms                                                 | 253 ms: 3.12x faster                                   |
| python_startup_no_site   | 14.5 ms                                                | 7.91 ms: 1.83x faster                                  |
| python_startup           | 18.9 ms                                                | 10.9 ms: 1.74x faster                                  |
| bench_mp_pool            | 62.5 ms                                                | 37.4 ms: 1.67x faster                                  |
| telco                    | 4.76 ms                                                | 3.49 ms: 1.37x faster                                  |
| create_gc_cycles         | 1.17 ms                                                | 860 us: 1.36x faster                                   |
| async_generators         | 295 ms                                                 | 231 ms: 1.28x faster                                   |
| gc_traversal             | 2.91 ms                                                | 2.36 ms: 1.23x faster                                  |
| mypy2                    | 701 ms                                                 | 607 ms: 1.15x faster                                   |
| coverage                 | 46.0 ms                                                | 41.5 ms: 1.11x faster                                  |
| regex_effbot             | 2.63 ms                                                | 2.46 ms: 1.07x faster                                  |
| xml_etree_generate       | 57.0 ms                                                | 53.5 ms: 1.06x faster                                  |
| json_loads               | 17.0 us                                                | 16.4 us: 1.03x faster                                  |
| xml_etree_iterparse      | 73.6 ms                                                | 72.1 ms: 1.02x faster                                  |
| genshi_xml               | 34.4 ms                                                | 33.8 ms: 1.02x faster                                  |
| pidigits                 | 284 ms                                                 | 282 ms: 1.00x faster                                   |
| sqlglot_normalize        | 189 ms                                                 | 190 ms: 1.01x slower                                   |
| regex_v8                 | 17.0 ms                                                | 17.1 ms: 1.01x slower                                  |
| json                     | 3.03 ms                                                | 3.08 ms: 1.02x slower                                  |
| nqueens                  | 62.5 ms                                                | 63.8 ms: 1.02x slower                                  |
| 2to3                     | 187 ms                                                 | 192 ms: 1.02x slower                                   |
| genshi_text              | 16.9 ms                                                | 17.3 ms: 1.03x slower                                  |
| generators               | 31.5 ms                                                | 32.3 ms: 1.03x slower                                  |
| bench_thread_pool        | 505 us                                                 | 527 us: 1.05x slower                                   |
| pathlib                  | 23.4 ms                                                | 24.5 ms: 1.05x slower                                  |
| coroutines               | 19.8 ms                                                | 20.7 ms: 1.05x slower                                  |
| meteor_contest           | 74.0 ms                                                | 77.7 ms: 1.05x slower                                  |
| sqlglot_optimize         | 34.9 ms                                                | 36.8 ms: 1.05x slower                                  |
| fannkuch                 | 284 ms                                                 | 303 ms: 1.07x slower                                   |
| tomli_loads              | 1.57 sec                                               | 1.71 sec: 1.09x slower                                 |
| sympy_expand             | 246 ms                                                 | 269 ms: 1.09x slower                                   |
| mdp                      | 1.49 sec                                               | 1.63 sec: 1.09x slower                                 |
| scimark_fft              | 201 ms                                                 | 224 ms: 1.12x slower                                   |
| deepcopy_reduce          | 2.07 us                                                | 2.33 us: 1.13x slower                                  |
| xml_etree_process        | 41.0 ms                                                | 46.5 ms: 1.13x slower                                  |
| sympy_str                | 145 ms                                                 | 165 ms: 1.14x slower                                   |
| tornado_http             | 75.8 ms                                                | 86.7 ms: 1.14x slower                                  |
| scimark_sparse_mat_mult  | 2.99 ms                                                | 3.42 ms: 1.15x slower                                  |
| deepcopy                 | 237 us                                                 | 272 us: 1.15x slower                                   |
| html5lib                 | 36.6 ms                                                | 42.4 ms: 1.16x slower                                  |
| sympy_integrate          | 11.3 ms                                                | 13.1 ms: 1.16x slower                                  |
| regex_dna                | 149 ms                                                 | 174 ms: 1.17x slower                                   |
| unpickle_pure_python     | 164 us                                                 | 194 us: 1.19x slower                                   |
| django_template          | 22.2 ms                                                | 26.4 ms: 1.19x slower                                  |
| pprint_safe_repr         | 533 ms                                                 | 641 ms: 1.20x slower                                   |
| pprint_pformat           | 1.08 sec                                               | 1.30 sec: 1.20x slower                                 |
| docutils                 | 1.44 sec                                               | 1.73 sec: 1.20x slower                                 |
| regex_compile            | 78.6 ms                                                | 95.3 ms: 1.21x slower                                  |
| pyflate                  | 351 ms                                                 | 427 ms: 1.21x slower                                   |
| scimark_sor              | 105 ms                                                 | 128 ms: 1.22x slower                                   |
| sympy_sum                | 75.4 ms                                                | 92.2 ms: 1.22x slower                                  |
| thrift                   | 466 us                                                 | 572 us: 1.23x slower                                   |
| float                    | 56.0 ms                                                | 69.0 ms: 1.23x slower                                  |
| chameleon                | 5.08 ms                                                | 6.26 ms: 1.23x slower                                  |
| logging_simple           | 3.60 us                                                | 4.45 us: 1.23x slower                                  |
| dulwich_log              | 28.5 ms                                                | 35.3 ms: 1.24x slower                                  |
| logging_format           | 3.89 us                                                | 4.83 us: 1.24x slower                                  |
| json_dumps               | 6.52 ms                                                | 8.11 ms: 1.24x slower                                  |
| pycparser                | 705 ms                                                 | 877 ms: 1.24x slower                                   |
| spectral_norm            | 76.3 ms                                                | 94.8 ms: 1.24x slower                                  |
| sqlalchemy_declarative   | 58.9 ms                                                | 73.3 ms: 1.24x slower                                  |
| nbody                    | 74.0 ms                                                | 93.0 ms: 1.26x slower                                  |
| deepcopy_memo            | 27.4 us                                                | 34.7 us: 1.27x slower                                  |
| hexiom                   | 4.86 ms                                                | 6.19 ms: 1.27x slower                                  |
| mako                     | 7.68 ms                                                | 9.87 ms: 1.29x slower                                  |
| scimark_monte_carlo      | 50.4 ms                                                | 65.6 ms: 1.30x slower                                  |
| pickle_pure_python       | 214 us                                                 | 281 us: 1.31x slower                                   |
| go                       | 115 ms                                                 | 151 ms: 1.31x slower                                   |
| crypto_pyaes             | 54.2 ms                                                | 71.8 ms: 1.32x slower                                  |
| sqlalchemy_imperative    | 6.69 ms                                                | 8.86 ms: 1.33x slower                                  |
| scimark_lu               | 76.7 ms                                                | 103 ms: 1.34x slower                                   |
| comprehensions           | 12.3 us                                                | 16.9 us: 1.38x slower                                  |
| richards                 | 35.2 ms                                                | 48.7 ms: 1.38x slower                                  |
| sqlglot_transpile        | 1.02 ms                                                | 1.44 ms: 1.41x slower                                  |
| async_tree_cpu_io_mixed  | 460 ms                                                 | 649 ms: 1.41x slower                                   |
| sqlglot_parse            | 856 us                                                 | 1.24 ms: 1.45x slower                                  |
| richards_super           | 39.1 ms                                                | 57.8 ms: 1.48x slower                                  |
| pylint                   | 180 ms                                                 | 277 ms: 1.54x slower                                   |
| chaos                    | 41.2 ms                                                | 65.8 ms: 1.60x slower                                  |
| raytrace                 | 181 ms                                                 | 301 ms: 1.67x slower                                   |
| logging_silent           | 70.1 ns                                                | 117 ns: 1.67x slower                                   |
| asyncio_websockets       | 242 ms                                                 | 410 ms: 1.70x slower                                   |
| async_tree_memoization   | 268 ms                                                 | 474 ms: 1.77x slower                                   |
| async_tree_none          | 215 ms                                                 | 388 ms: 1.80x slower                                   |
| deltablue                | 2.68 ms                                                | 4.91 ms: 1.83x slower                                  |
| async_tree_io            | 507 ms                                                 | 980 ms: 1.93x slower                                   |
| typing_runtime_protocols | 101 us                                                 | 323 us: 3.19x slower                                   |
| Geometric mean           | (ref)                                                  | 1.15x slower                                           |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.135x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 0.80x