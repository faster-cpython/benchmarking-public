# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 187 ms: 1.02x faster                                   |
| chameleon      | 6.26 ms                                                | 5.08 ms: 1.23x faster                                  |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.20x faster                                 |
| html5lib       | 42.4 ms                                                | 36.6 ms: 1.16x faster                                  |
| tornado_http   | 86.7 ms                                                | 75.8 ms: 1.14x faster                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 507 ms: 1.93x faster                                   |
| async_tree_none         | 388 ms                                                 | 215 ms: 1.80x faster                                   |
| async_tree_memoization  | 474 ms                                                 | 268 ms: 1.77x faster                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 460 ms: 1.41x faster                                   |
| Geometric mean          | (ref)                                                  | 1.72x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 74.0 ms: 1.26x faster                                  |
| float          | 69.0 ms                                                | 56.0 ms: 1.23x faster                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 78.6 ms: 1.21x faster                                  |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                   |
| regex_v8       | 17.1 ms                                                | 17.0 ms: 1.01x faster                                  |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 214 us: 1.31x faster                                   |
| json_dumps           | 8.11 ms                                                | 6.52 ms: 1.24x faster                                  |
| unpickle_pure_python | 194 us                                                 | 164 us: 1.19x faster                                   |
| xml_etree_process    | 46.5 ms                                                | 41.0 ms: 1.13x faster                                  |
| tomli_loads          | 1.71 sec                                               | 1.57 sec: 1.09x faster                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 73.6 ms: 1.02x slower                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate   | 53.5 ms                                                | 57.0 ms: 1.06x slower                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.9 ms: 1.74x slower                                  |
| python_startup_no_site | 7.91 ms                                                | 14.5 ms: 1.83x slower                                  |
| Geometric mean         | (ref)                                                  | 1.78x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.68 ms: 1.29x faster                                  |
| django_template | 26.4 ms                                                | 22.2 ms: 1.19x faster                                  |
| genshi_text     | 17.3 ms                                                | 16.9 ms: 1.03x faster                                  |
| genshi_xml      | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 101 us: 3.19x faster                                   |
| async_tree_io            | 980 ms                                                 | 507 ms: 1.93x faster                                   |
| deltablue                | 4.91 ms                                                | 2.68 ms: 1.83x faster                                  |
| async_tree_none          | 388 ms                                                 | 215 ms: 1.80x faster                                   |
| async_tree_memoization   | 474 ms                                                 | 268 ms: 1.77x faster                                   |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                   |
| logging_silent           | 117 ns                                                 | 70.1 ns: 1.67x faster                                  |
| raytrace                 | 301 ms                                                 | 181 ms: 1.67x faster                                   |
| chaos                    | 65.8 ms                                                | 41.2 ms: 1.60x faster                                  |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                   |
| richards_super           | 57.8 ms                                                | 39.1 ms: 1.48x faster                                  |
| sqlglot_parse            | 1.24 ms                                                | 856 us: 1.45x faster                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 460 ms: 1.41x faster                                   |
| sqlglot_transpile        | 1.44 ms                                                | 1.02 ms: 1.41x faster                                  |
| richards                 | 48.7 ms                                                | 35.2 ms: 1.38x faster                                  |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                  |
| scimark_lu               | 103 ms                                                 | 76.7 ms: 1.34x faster                                  |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.69 ms: 1.33x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 54.2 ms: 1.32x faster                                  |
| go                       | 151 ms                                                 | 115 ms: 1.31x faster                                   |
| pickle_pure_python       | 281 us                                                 | 214 us: 1.31x faster                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 50.4 ms: 1.30x faster                                  |
| mako                     | 9.87 ms                                                | 7.68 ms: 1.29x faster                                  |
| hexiom                   | 6.19 ms                                                | 4.86 ms: 1.27x faster                                  |
| deepcopy_memo            | 34.7 us                                                | 27.4 us: 1.27x faster                                  |
| nbody                    | 93.0 ms                                                | 74.0 ms: 1.26x faster                                  |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.9 ms: 1.24x faster                                  |
| spectral_norm            | 94.8 ms                                                | 76.3 ms: 1.24x faster                                  |
| pycparser                | 877 ms                                                 | 705 ms: 1.24x faster                                   |
| json_dumps               | 8.11 ms                                                | 6.52 ms: 1.24x faster                                  |
| logging_format           | 4.83 us                                                | 3.89 us: 1.24x faster                                  |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                  |
| logging_simple           | 4.45 us                                                | 3.60 us: 1.23x faster                                  |
| chameleon                | 6.26 ms                                                | 5.08 ms: 1.23x faster                                  |
| float                    | 69.0 ms                                                | 56.0 ms: 1.23x faster                                  |
| thrift                   | 572 us                                                 | 466 us: 1.23x faster                                   |
| sympy_sum                | 92.2 ms                                                | 75.4 ms: 1.22x faster                                  |
| scimark_sor              | 128 ms                                                 | 105 ms: 1.22x faster                                   |
| pyflate                  | 427 ms                                                 | 351 ms: 1.21x faster                                   |
| regex_compile            | 95.3 ms                                                | 78.6 ms: 1.21x faster                                  |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.20x faster                                 |
| pprint_pformat           | 1.30 sec                                               | 1.08 sec: 1.20x faster                                 |
| pprint_safe_repr         | 641 ms                                                 | 533 ms: 1.20x faster                                   |
| django_template          | 26.4 ms                                                | 22.2 ms: 1.19x faster                                  |
| unpickle_pure_python     | 194 us                                                 | 164 us: 1.19x faster                                   |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                   |
| sympy_integrate          | 13.1 ms                                                | 11.3 ms: 1.16x faster                                  |
| html5lib                 | 42.4 ms                                                | 36.6 ms: 1.16x faster                                  |
| deepcopy                 | 272 us                                                 | 237 us: 1.15x faster                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.99 ms: 1.15x faster                                  |
| tornado_http             | 86.7 ms                                                | 75.8 ms: 1.14x faster                                  |
| sympy_str                | 165 ms                                                 | 145 ms: 1.14x faster                                   |
| xml_etree_process        | 46.5 ms                                                | 41.0 ms: 1.13x faster                                  |
| deepcopy_reduce          | 2.33 us                                                | 2.07 us: 1.13x faster                                  |
| scimark_fft              | 224 ms                                                 | 201 ms: 1.12x faster                                   |
| mdp                      | 1.63 sec                                               | 1.49 sec: 1.09x faster                                 |
| sympy_expand             | 269 ms                                                 | 246 ms: 1.09x faster                                   |
| tomli_loads              | 1.71 sec                                               | 1.57 sec: 1.09x faster                                 |
| fannkuch                 | 303 ms                                                 | 284 ms: 1.07x faster                                   |
| sqlglot_optimize         | 36.8 ms                                                | 34.9 ms: 1.05x faster                                  |
| meteor_contest           | 77.7 ms                                                | 74.0 ms: 1.05x faster                                  |
| coroutines               | 20.7 ms                                                | 19.8 ms: 1.05x faster                                  |
| pathlib                  | 24.5 ms                                                | 23.4 ms: 1.05x faster                                  |
| bench_thread_pool        | 527 us                                                 | 505 us: 1.05x faster                                   |
| generators               | 32.3 ms                                                | 31.5 ms: 1.03x faster                                  |
| genshi_text              | 17.3 ms                                                | 16.9 ms: 1.03x faster                                  |
| 2to3                     | 192 ms                                                 | 187 ms: 1.02x faster                                   |
| nqueens                  | 63.8 ms                                                | 62.5 ms: 1.02x faster                                  |
| json                     | 3.08 ms                                                | 3.03 ms: 1.02x faster                                  |
| regex_v8                 | 17.1 ms                                                | 17.0 ms: 1.01x faster                                  |
| sqlglot_normalize        | 190 ms                                                 | 189 ms: 1.01x faster                                   |
| pidigits                 | 282 ms                                                 | 284 ms: 1.00x slower                                   |
| genshi_xml               | 33.8 ms                                                | 34.4 ms: 1.02x slower                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.6 ms: 1.02x slower                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                  |
| xml_etree_generate       | 53.5 ms                                                | 57.0 ms: 1.06x slower                                  |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| coverage                 | 41.5 ms                                                | 46.0 ms: 1.11x slower                                  |
| mypy2                    | 607 ms                                                 | 701 ms: 1.15x slower                                   |
| gc_traversal             | 2.36 ms                                                | 2.91 ms: 1.23x slower                                  |
| async_generators         | 231 ms                                                 | 295 ms: 1.28x slower                                   |
| create_gc_cycles         | 860 us                                                 | 1.17 ms: 1.36x slower                                  |
| telco                    | 3.49 ms                                                | 4.76 ms: 1.37x slower                                  |
| bench_mp_pool            | 37.4 ms                                                | 62.5 ms: 1.67x slower                                  |
| python_startup           | 10.9 ms                                                | 18.9 ms: 1.74x slower                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.5 ms: 1.83x slower                                  |
| dask                     | 253 ms                                                 | 790 ms: 3.12x slower                                   |
| Geometric mean           | (ref)                                                  | 1.15x faster                                           |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (18) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.160x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.29x