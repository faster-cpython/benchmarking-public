# Results vs. 3.10.4

- fork: brandtbucher
- ref: faster_jit_builds
- machine: darwin-arm64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 0.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                     |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                   |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                    |
| tornado_http   | 86.7 ms                                                | 67.8 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                  | 1.21x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 195 ms: 1.99x faster                                                     |
| async_tree_memoization  | 474 ms                                                 | 240 ms: 1.97x faster                                                     |
| async_tree_io           | 980 ms                                                 | 547 ms: 1.79x faster                                                     |
| async_tree_cpu_io_mixed | 649 ms                                                 | 453 ms: 1.43x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.78x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 45.9 ms: 1.50x faster                                                    |
| nbody          | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                    |
| regex_dna      | 174 ms                                                 | 150 ms: 1.16x faster                                                     |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                    |
| regex_effbot   | 2.46 ms                                                | 2.73 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 173 us: 1.62x faster                                                     |
| unpickle_pure_python | 194 us                                                 | 133 us: 1.46x faster                                                     |
| tomli_loads          | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                   |
| xml_etree_process    | 46.5 ms                                                | 35.4 ms: 1.31x faster                                                    |
| json_dumps           | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                    |
| xml_etree_generate   | 53.5 ms                                                | 51.7 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                    |
| xml_etree_parse      | 108 ms                                                 | 109 ms: 1.02x slower                                                     |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                    |
| python_startup_no_site | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.69x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.43 ms: 1.53x faster                                                    |
| django_template | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                    |
| genshi_text     | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                    |
| genshi_xml      | 33.8 ms                                                | 39.6 ms: 1.17x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.8 us: 3.44x faster                                                    |
| deltablue                | 4.91 ms                                                | 2.28 ms: 2.15x faster                                                    |
| deepcopy_memo            | 34.7 us                                                | 16.6 us: 2.09x faster                                                    |
| async_tree_none          | 388 ms                                                 | 195 ms: 1.99x faster                                                     |
| async_tree_memoization   | 474 ms                                                 | 240 ms: 1.97x faster                                                     |
| logging_silent           | 117 ns                                                 | 61.4 ns: 1.91x faster                                                    |
| raytrace                 | 301 ms                                                 | 160 ms: 1.88x faster                                                     |
| async_tree_io            | 980 ms                                                 | 547 ms: 1.79x faster                                                     |
| deepcopy                 | 272 us                                                 | 154 us: 1.76x faster                                                     |
| chaos                    | 65.8 ms                                                | 38.5 ms: 1.71x faster                                                    |
| richards_super           | 57.8 ms                                                | 34.6 ms: 1.67x faster                                                    |
| pickle_pure_python       | 281 us                                                 | 173 us: 1.62x faster                                                     |
| asyncio_tcp              | 659 ms                                                 | 408 ms: 1.62x faster                                                     |
| richards                 | 48.7 ms                                                | 30.4 ms: 1.60x faster                                                    |
| mako                     | 9.87 ms                                                | 6.43 ms: 1.53x faster                                                    |
| deepcopy_reduce          | 2.33 us                                                | 1.54 us: 1.51x faster                                                    |
| float                    | 69.0 ms                                                | 45.9 ms: 1.50x faster                                                    |
| generators               | 32.3 ms                                                | 21.6 ms: 1.50x faster                                                    |
| scimark_monte_carlo      | 65.6 ms                                                | 43.9 ms: 1.49x faster                                                    |
| go                       | 151 ms                                                 | 101 ms: 1.49x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 835 us: 1.49x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.00 us: 1.48x faster                                                    |
| nbody                    | 93.0 ms                                                | 63.0 ms: 1.48x faster                                                    |
| logging_format           | 4.83 us                                                | 3.29 us: 1.47x faster                                                    |
| unpickle_pure_python     | 194 us                                                 | 133 us: 1.46x faster                                                     |
| pylint                   | 277 ms                                                 | 190 ms: 1.46x faster                                                     |
| sqlglot_transpile        | 1.44 ms                                                | 1.00 ms: 1.44x faster                                                    |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 453 ms: 1.43x faster                                                     |
| hexiom                   | 6.19 ms                                                | 4.36 ms: 1.42x faster                                                    |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                                    |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.39x faster                                                    |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                    |
| pyflate                  | 427 ms                                                 | 311 ms: 1.37x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.24 sec: 1.37x faster                                                   |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                    |
| pprint_safe_repr         | 641 ms                                                 | 487 ms: 1.32x faster                                                     |
| xml_etree_process        | 46.5 ms                                                | 35.4 ms: 1.31x faster                                                    |
| json_dumps               | 8.11 ms                                                | 6.19 ms: 1.31x faster                                                    |
| pprint_pformat           | 1.30 sec                                               | 1.00 sec: 1.30x faster                                                   |
| thrift                   | 572 us                                                 | 440 us: 1.30x faster                                                     |
| regex_compile            | 95.3 ms                                                | 73.4 ms: 1.30x faster                                                    |
| scimark_lu               | 103 ms                                                 | 80.2 ms: 1.28x faster                                                    |
| tornado_http             | 86.7 ms                                                | 67.8 ms: 1.28x faster                                                    |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.27x faster                                                     |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                    |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 73.4 ms: 1.26x faster                                                    |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                                    |
| pycparser                | 877 ms                                                 | 708 ms: 1.24x faster                                                     |
| django_template          | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                    |
| scimark_fft              | 224 ms                                                 | 182 ms: 1.23x faster                                                     |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                                     |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.89 ms: 1.18x faster                                                    |
| sympy_integrate          | 13.1 ms                                                | 11.2 ms: 1.17x faster                                                    |
| regex_dna                | 174 ms                                                 | 150 ms: 1.16x faster                                                     |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 470 us: 1.12x faster                                                     |
| sqlglot_optimize         | 36.8 ms                                                | 32.8 ms: 1.12x faster                                                    |
| nqueens                  | 63.8 ms                                                | 57.1 ms: 1.12x faster                                                    |
| sympy_expand             | 269 ms                                                 | 241 ms: 1.11x faster                                                     |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.11x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 70.9 ms: 1.10x faster                                                    |
| sqlglot_normalize        | 190 ms                                                 | 175 ms: 1.09x faster                                                     |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                     |
| dask                     | 253 ms                                                 | 234 ms: 1.08x faster                                                     |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                                    |
| genshi_text              | 17.3 ms                                                | 16.5 ms: 1.05x faster                                                    |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                    |
| xml_etree_generate       | 53.5 ms                                                | 51.7 ms: 1.03x faster                                                    |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                     |
| xml_etree_iterparse      | 72.1 ms                                                | 72.7 ms: 1.01x slower                                                    |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                    |
| xml_etree_parse          | 108 ms                                                 | 109 ms: 1.02x slower                                                     |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                    |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                    |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                     |
| coverage                 | 41.5 ms                                                | 46.0 ms: 1.11x slower                                                    |
| regex_effbot             | 2.46 ms                                                | 2.73 ms: 1.11x slower                                                    |
| genshi_xml               | 33.8 ms                                                | 39.6 ms: 1.17x slower                                                    |
| async_generators         | 231 ms                                                 | 289 ms: 1.25x slower                                                     |
| telco                    | 3.49 ms                                                | 4.51 ms: 1.29x slower                                                    |
| bench_mp_pool            | 37.4 ms                                                | 51.4 ms: 1.37x slower                                                    |
| python_startup           | 10.9 ms                                                | 17.1 ms: 1.57x slower                                                    |
| python_startup_no_site   | 7.91 ms                                                | 14.3 ms: 1.81x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                             |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240727-3.14.0a0-60b7e71-JIT/bm-20240727-darwin-arm64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 0.71x