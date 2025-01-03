# Results vs. 3.10.4

- fork: eendebakpt
- ref: 05f479c7b36947e5f3e9
- machine: darwin-arm64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                       |
| docutils       | 1.73 sec                                               | 1.38 sec: 1.25x faster                                                     |
| html5lib       | 42.4 ms                                                | 28.8 ms: 1.47x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 363 ms: 2.70x faster                                                       |
| async_tree_none         | 388 ms                                                 | 158 ms: 2.45x faster                                                       |
| async_tree_memoization  | 474 ms                                                 | 199 ms: 2.38x faster                                                       |
| async_tree_cpu_io_mixed | 649 ms                                                 | 414 ms: 1.57x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.9 ms: 1.47x faster                                                      |
| nbody          | 93.0 ms                                                | 67.5 ms: 1.38x faster                                                      |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 65.0 ms: 1.46x faster                                                      |
| regex_dna      | 174 ms                                                 | 137 ms: 1.28x faster                                                       |
| regex_effbot   | 2.46 ms                                                | 2.08 ms: 1.18x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                  | 1.24x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                               | 1.19 sec: 1.44x faster                                                     |
| pickle_pure_python   | 281 us                                                 | 196 us: 1.43x faster                                                       |
| unpickle_pure_python | 194 us                                                 | 136 us: 1.43x faster                                                       |
| xml_etree_process    | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                      |
| json_dumps           | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                | 51.6 ms: 1.04x faster                                                      |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                       |
| json_loads           | 16.4 us                                                | 16.3 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                      |
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.56x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.13 ms: 1.38x faster                                                      |
| genshi_text     | 17.3 ms                                                | 13.1 ms: 1.32x faster                                                      |
| django_template | 26.4 ms                                                | 20.3 ms: 1.30x faster                                                      |
| genshi_xml      | 33.8 ms                                                | 28.0 ms: 1.21x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.8 us: 3.48x faster                                                      |
| async_tree_io            | 980 ms                                                 | 363 ms: 2.70x faster                                                       |
| async_tree_none          | 388 ms                                                 | 158 ms: 2.45x faster                                                       |
| async_tree_memoization   | 474 ms                                                 | 199 ms: 2.38x faster                                                       |
| deltablue                | 4.91 ms                                                | 2.30 ms: 2.14x faster                                                      |
| go                       | 151 ms                                                 | 77.1 ms: 1.95x faster                                                      |
| deepcopy_memo            | 34.7 us                                                | 18.1 us: 1.92x faster                                                      |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                       |
| logging_silent           | 117 ns                                                 | 64.9 ns: 1.81x faster                                                      |
| raytrace                 | 301 ms                                                 | 168 ms: 1.80x faster                                                       |
| chaos                    | 65.8 ms                                                | 37.2 ms: 1.77x faster                                                      |
| pylint                   | 277 ms                                                 | 158 ms: 1.75x faster                                                       |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                                       |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                                      |
| sqlglot_parse            | 1.24 ms                                                | 760 us: 1.64x faster                                                       |
| scimark_sor              | 128 ms                                                 | 78.6 ms: 1.63x faster                                                      |
| sqlglot_transpile        | 1.44 ms                                                | 912 us: 1.58x faster                                                       |
| scimark_monte_carlo      | 65.6 ms                                                | 41.8 ms: 1.57x faster                                                      |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 414 ms: 1.57x faster                                                       |
| spectral_norm            | 94.8 ms                                                | 61.4 ms: 1.54x faster                                                      |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.54x faster                                                      |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                                      |
| hexiom                   | 6.19 ms                                                | 4.15 ms: 1.49x faster                                                      |
| pyflate                  | 427 ms                                                 | 289 ms: 1.48x faster                                                       |
| float                    | 69.0 ms                                                | 46.9 ms: 1.47x faster                                                      |
| html5lib                 | 42.4 ms                                                | 28.8 ms: 1.47x faster                                                      |
| regex_compile            | 95.3 ms                                                | 65.0 ms: 1.46x faster                                                      |
| generators               | 32.3 ms                                                | 22.5 ms: 1.44x faster                                                      |
| tomli_loads              | 1.71 sec                                               | 1.19 sec: 1.44x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 196 us: 1.43x faster                                                       |
| pprint_pformat           | 1.30 sec                                               | 912 ms: 1.43x faster                                                       |
| unpickle_pure_python     | 194 us                                                 | 136 us: 1.43x faster                                                       |
| scimark_lu               | 103 ms                                                 | 72.3 ms: 1.42x faster                                                      |
| logging_simple           | 4.45 us                                                | 3.13 us: 1.42x faster                                                      |
| pprint_safe_repr         | 641 ms                                                 | 453 ms: 1.42x faster                                                       |
| logging_format           | 4.83 us                                                | 3.42 us: 1.41x faster                                                      |
| comprehensions           | 16.9 us                                                | 12.1 us: 1.40x faster                                                      |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.34 ms: 1.40x faster                                                      |
| pycparser                | 877 ms                                                 | 631 ms: 1.39x faster                                                       |
| mako                     | 9.87 ms                                                | 7.13 ms: 1.38x faster                                                      |
| nbody                    | 93.0 ms                                                | 67.5 ms: 1.38x faster                                                      |
| crypto_pyaes             | 71.8 ms                                                | 52.8 ms: 1.36x faster                                                      |
| thrift                   | 572 us                                                 | 427 us: 1.34x faster                                                       |
| genshi_text              | 17.3 ms                                                | 13.1 ms: 1.32x faster                                                      |
| scimark_fft              | 224 ms                                                 | 171 ms: 1.31x faster                                                       |
| django_template          | 26.4 ms                                                | 20.3 ms: 1.30x faster                                                      |
| dulwich_log              | 35.3 ms                                                | 27.2 ms: 1.30x faster                                                      |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                      |
| sympy_sum                | 92.2 ms                                                | 71.7 ms: 1.29x faster                                                      |
| sqlalchemy_declarative   | 73.3 ms                                                | 57.2 ms: 1.28x faster                                                      |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.67 ms: 1.28x faster                                                      |
| regex_dna                | 174 ms                                                 | 137 ms: 1.28x faster                                                       |
| docutils                 | 1.73 sec                                               | 1.38 sec: 1.25x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                      |
| fannkuch                 | 303 ms                                                 | 245 ms: 1.24x faster                                                       |
| sympy_str                | 165 ms                                                 | 135 ms: 1.22x faster                                                       |
| sympy_integrate          | 13.1 ms                                                | 10.8 ms: 1.22x faster                                                      |
| genshi_xml               | 33.8 ms                                                | 28.0 ms: 1.21x faster                                                      |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                       |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                       |
| regex_effbot             | 2.46 ms                                                | 2.08 ms: 1.18x faster                                                      |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                                      |
| mypy2                    | 607 ms                                                 | 516 ms: 1.18x faster                                                       |
| nqueens                  | 63.8 ms                                                | 54.4 ms: 1.17x faster                                                      |
| bench_thread_pool        | 527 us                                                 | 468 us: 1.13x faster                                                       |
| json_dumps               | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                      |
| sqlglot_normalize        | 190 ms                                                 | 171 ms: 1.11x faster                                                       |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                                      |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                     |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                                      |
| json                     | 3.08 ms                                                | 2.87 ms: 1.07x faster                                                      |
| regex_v8                 | 17.1 ms                                                | 16.0 ms: 1.07x faster                                                      |
| xml_etree_generate       | 53.5 ms                                                | 51.6 ms: 1.04x faster                                                      |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.04x faster                                                       |
| json_loads               | 16.4 us                                                | 16.3 us: 1.01x faster                                                      |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                       |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                                      |
| coverage                 | 41.5 ms                                                | 45.4 ms: 1.09x slower                                                      |
| async_generators         | 231 ms                                                 | 277 ms: 1.20x slower                                                       |
| telco                    | 3.49 ms                                                | 4.40 ms: 1.26x slower                                                      |
| gc_traversal             | 2.36 ms                                                | 3.09 ms: 1.31x slower                                                      |
| create_gc_cycles         | 860 us                                                 | 1.27 ms: 1.48x slower                                                      |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                      |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                      |
| bench_mp_pool            | 37.4 ms                                                | 59.1 ms: 1.58x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-darwin-arm64-eendebakpt-05f479c7b36947e5f3e9-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.34x