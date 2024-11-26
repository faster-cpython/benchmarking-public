# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: darwin-arm64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                   |
| docutils       | 1.73 sec                                               | 1.40 sec: 1.23x faster                                                 |
| html5lib       | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                  |
| tornado_http   | 86.7 ms                                                | 72.4 ms: 1.20x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 199 ms: 1.95x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 249 ms: 1.90x faster                                                   |
| async_tree_io           | 980 ms                                                 | 583 ms: 1.68x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 457 ms: 1.42x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 66.0 ms: 1.41x faster                                                  |
| float          | 69.0 ms                                                | 49.8 ms: 1.39x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.1 ms: 1.40x faster                                                  |
| regex_dna      | 174 ms                                                 | 142 ms: 1.23x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.45 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.53x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                 |
| json_dumps           | 8.11 ms                                                | 7.18 ms: 1.13x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                  |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.77x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                  |
| django_template | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                  |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.0 us: 3.47x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.24 ms: 2.20x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.0 us: 2.05x faster                                                  |
| raytrace                 | 301 ms                                                 | 154 ms: 1.96x faster                                                   |
| async_tree_none          | 388 ms                                                 | 199 ms: 1.95x faster                                                   |
| logging_silent           | 117 ns                                                 | 60.9 ns: 1.92x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 249 ms: 1.90x faster                                                   |
| deepcopy                 | 272 us                                                 | 145 us: 1.88x faster                                                   |
| go                       | 151 ms                                                 | 82.4 ms: 1.83x faster                                                  |
| chaos                    | 65.8 ms                                                | 36.8 ms: 1.79x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                   |
| async_tree_io            | 980 ms                                                 | 583 ms: 1.68x faster                                                   |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 746 us: 1.67x faster                                                   |
| generators               | 32.3 ms                                                | 20.1 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 902 us: 1.60x faster                                                   |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.56x faster                                                  |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                   |
| scimark_lu               | 103 ms                                                 | 67.0 ms: 1.53x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.53x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.52x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.13 ms: 1.50x faster                                                  |
| comprehensions           | 16.9 us                                                | 11.4 us: 1.48x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.2 ms: 1.48x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                  |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 457 ms: 1.42x faster                                                   |
| mako                     | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.1 ms: 1.41x faster                                                  |
| nbody                    | 93.0 ms                                                | 66.0 ms: 1.41x faster                                                  |
| regex_compile            | 95.3 ms                                                | 68.1 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 459 ms: 1.40x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 935 ms: 1.40x faster                                                   |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.36 ms: 1.39x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 51.7 ms: 1.39x faster                                                  |
| float                    | 69.0 ms                                                | 49.8 ms: 1.39x faster                                                  |
| pycparser                | 877 ms                                                 | 635 ms: 1.38x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                   |
| thrift                   | 572 us                                                 | 419 us: 1.36x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 70.0 ms: 1.35x faster                                                  |
| scimark_sor              | 128 ms                                                 | 96.1 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.8 ms: 1.32x faster                                                  |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                                   |
| sqlalchemy_declarative   | 73.3 ms                                                | 56.0 ms: 1.31x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.6 ms: 1.28x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.5 ms: 1.25x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                  |
| sympy_str                | 165 ms                                                 | 134 ms: 1.23x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.40 sec: 1.23x faster                                                 |
| regex_dna                | 174 ms                                                 | 142 ms: 1.23x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.82 ms: 1.21x faster                                                  |
| tornado_http             | 86.7 ms                                                | 72.4 ms: 1.20x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.20x faster                                                  |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                   |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                                  |
| scimark_fft              | 224 ms                                                 | 192 ms: 1.17x faster                                                   |
| nqueens                  | 63.8 ms                                                | 54.8 ms: 1.16x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 453 us: 1.16x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                 |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                   |
| json_dumps               | 8.11 ms                                                | 7.18 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 70.6 ms: 1.10x faster                                                  |
| json                     | 3.08 ms                                                | 2.90 ms: 1.06x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.45 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.6 ms: 1.03x slower                                                  |
| coverage                 | 41.5 ms                                                | 43.7 ms: 1.05x slower                                                  |
| async_generators         | 231 ms                                                 | 277 ms: 1.20x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.93 ms: 1.24x slower                                                  |
| telco                    | 3.49 ms                                                | 4.59 ms: 1.32x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 1.31 ms: 1.52x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 59.9 ms: 1.60x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-darwin-arm64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.299x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.31x