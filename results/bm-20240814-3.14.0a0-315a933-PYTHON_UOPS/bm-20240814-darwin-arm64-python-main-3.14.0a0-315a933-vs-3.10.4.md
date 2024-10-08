# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 315a933
- commit date: 2024-08-14
- overall geometric mean: 1.12x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 192 ms                                                 | 186 ms: 1.03x faster                                  |
| docutils       | 1.73 sec                                               | 1.70 sec: 1.02x faster                                |
| html5lib       | 42.4 ms                                                | 35.3 ms: 1.20x faster                                 |
| tornado_http   | 86.7 ms                                                | 70.9 ms: 1.22x faster                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 205 ms: 1.90x faster                                  |
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.89x faster                                  |
| async_tree_io           | 980 ms                                                 | 577 ms: 1.70x faster                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.41x faster                                  |
| Geometric mean          | (ref)                                                  | 1.71x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 69.0 ms                                                | 55.5 ms: 1.24x faster                                 |
| nbody          | 93.0 ms                                                | 75.9 ms: 1.23x faster                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                  |
| regex_v8       | 17.1 ms                                                | 16.8 ms: 1.02x faster                                 |
| regex_compile  | 95.3 ms                                                | 94.5 ms: 1.01x faster                                 |
| regex_effbot   | 2.46 ms                                                | 2.48 ms: 1.01x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 213 us: 1.32x faster                                  |
| json_dumps           | 8.11 ms                                                | 6.65 ms: 1.22x faster                                 |
| unpickle_pure_python | 194 us                                                 | 165 us: 1.18x faster                                  |
| xml_etree_process    | 46.5 ms                                                | 41.9 ms: 1.11x faster                                 |
| tomli_loads          | 1.71 sec                                               | 1.59 sec: 1.07x faster                                |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| json_loads           | 16.4 us                                                | 17.3 us: 1.05x slower                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 78.1 ms: 1.08x slower                                 |
| xml_etree_generate   | 53.5 ms                                                | 60.5 ms: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.9 ms: 1.56x slower                                 |
| python_startup_no_site | 7.91 ms                                                | 13.9 ms: 1.76x slower                                 |
| Geometric mean         | (ref)                                                  | 1.65x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 26.4 ms                                                | 24.1 ms: 1.09x faster                                 |
| mako            | 9.87 ms                                                | 9.09 ms: 1.09x faster                                 |
| genshi_text     | 17.3 ms                                                | 16.4 ms: 1.06x faster                                 |
| genshi_xml      | 33.8 ms                                                | 35.6 ms: 1.05x slower                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 108 us: 2.99x faster                                  |
| async_tree_none          | 388 ms                                                 | 205 ms: 1.90x faster                                  |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.89x faster                                  |
| raytrace                 | 301 ms                                                 | 173 ms: 1.74x faster                                  |
| async_tree_io            | 980 ms                                                 | 577 ms: 1.70x faster                                  |
| asyncio_tcp              | 659 ms                                                 | 430 ms: 1.53x faster                                  |
| deltablue                | 4.91 ms                                                | 3.29 ms: 1.49x faster                                 |
| deepcopy                 | 272 us                                                 | 185 us: 1.47x faster                                  |
| chaos                    | 65.8 ms                                                | 45.7 ms: 1.44x faster                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.41x faster                                  |
| logging_simple           | 4.45 us                                                | 3.20 us: 1.39x faster                                 |
| deepcopy_memo            | 34.7 us                                                | 25.1 us: 1.39x faster                                 |
| logging_format           | 4.83 us                                                | 3.50 us: 1.38x faster                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.70 us: 1.37x faster                                 |
| pylint                   | 277 ms                                                 | 208 ms: 1.33x faster                                  |
| go                       | 151 ms                                                 | 114 ms: 1.33x faster                                  |
| pickle_pure_python       | 281 us                                                 | 213 us: 1.32x faster                                  |
| sqlglot_parse            | 1.24 ms                                                | 951 us: 1.31x faster                                  |
| thrift                   | 572 us                                                 | 442 us: 1.30x faster                                  |
| logging_silent           | 117 ns                                                 | 90.6 ns: 1.29x faster                                 |
| richards_super           | 57.8 ms                                                | 45.2 ms: 1.28x faster                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                 |
| scimark_lu               | 103 ms                                                 | 81.5 ms: 1.26x faster                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.16 ms: 1.24x faster                                 |
| float                    | 69.0 ms                                                | 55.5 ms: 1.24x faster                                 |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                |
| nbody                    | 93.0 ms                                                | 75.9 ms: 1.23x faster                                 |
| tornado_http             | 86.7 ms                                                | 70.9 ms: 1.22x faster                                 |
| json_dumps               | 8.11 ms                                                | 6.65 ms: 1.22x faster                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                  |
| html5lib                 | 42.4 ms                                                | 35.3 ms: 1.20x faster                                 |
| richards                 | 48.7 ms                                                | 41.0 ms: 1.19x faster                                 |
| pycparser                | 877 ms                                                 | 739 ms: 1.19x faster                                  |
| unpickle_pure_python     | 194 us                                                 | 165 us: 1.18x faster                                  |
| crypto_pyaes             | 71.8 ms                                                | 62.6 ms: 1.15x faster                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 57.2 ms: 1.15x faster                                 |
| scimark_sor              | 128 ms                                                 | 112 ms: 1.14x faster                                  |
| xml_etree_process        | 46.5 ms                                                | 41.9 ms: 1.11x faster                                 |
| pprint_safe_repr         | 641 ms                                                 | 581 ms: 1.10x faster                                  |
| pyflate                  | 427 ms                                                 | 387 ms: 1.10x faster                                  |
| pprint_pformat           | 1.30 sec                                               | 1.19 sec: 1.10x faster                                |
| django_template          | 26.4 ms                                                | 24.1 ms: 1.09x faster                                 |
| mako                     | 9.87 ms                                                | 9.09 ms: 1.09x faster                                 |
| tomli_loads              | 1.71 sec                                               | 1.59 sec: 1.07x faster                                |
| hexiom                   | 6.19 ms                                                | 5.79 ms: 1.07x faster                                 |
| genshi_text              | 17.3 ms                                                | 16.4 ms: 1.06x faster                                 |
| mdp                      | 1.63 sec                                               | 1.55 sec: 1.05x faster                                |
| sympy_sum                | 92.2 ms                                                | 88.3 ms: 1.04x faster                                 |
| pathlib                  | 24.5 ms                                                | 23.7 ms: 1.03x faster                                 |
| 2to3                     | 192 ms                                                 | 186 ms: 1.03x faster                                  |
| json                     | 3.08 ms                                                | 3.03 ms: 1.02x faster                                 |
| regex_v8                 | 17.1 ms                                                | 16.8 ms: 1.02x faster                                 |
| docutils                 | 1.73 sec                                               | 1.70 sec: 1.02x faster                                |
| bench_thread_pool        | 527 us                                                 | 519 us: 1.02x faster                                  |
| sympy_integrate          | 13.1 ms                                                | 13.0 ms: 1.01x faster                                 |
| regex_compile            | 95.3 ms                                                | 94.5 ms: 1.01x faster                                 |
| spectral_norm            | 94.8 ms                                                | 94.3 ms: 1.01x faster                                 |
| comprehensions           | 16.9 us                                                | 16.9 us: 1.00x faster                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                  |
| sympy_expand             | 269 ms                                                 | 268 ms: 1.00x faster                                  |
| sympy_str                | 165 ms                                                 | 166 ms: 1.01x slower                                  |
| regex_effbot             | 2.46 ms                                                | 2.48 ms: 1.01x slower                                 |
| scimark_fft              | 224 ms                                                 | 226 ms: 1.01x slower                                  |
| generators               | 32.3 ms                                                | 32.9 ms: 1.02x slower                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                 |
| sqlglot_optimize         | 36.8 ms                                                | 38.4 ms: 1.04x slower                                 |
| create_gc_cycles         | 860 us                                                 | 902 us: 1.05x slower                                  |
| genshi_xml               | 33.8 ms                                                | 35.6 ms: 1.05x slower                                 |
| json_loads               | 16.4 us                                                | 17.3 us: 1.05x slower                                 |
| meteor_contest           | 77.7 ms                                                | 82.6 ms: 1.06x slower                                 |
| nqueens                  | 63.8 ms                                                | 67.9 ms: 1.07x slower                                 |
| sqlglot_normalize        | 190 ms                                                 | 204 ms: 1.07x slower                                  |
| fannkuch                 | 303 ms                                                 | 326 ms: 1.08x slower                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 78.1 ms: 1.08x slower                                 |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.08x slower                                 |
| xml_etree_generate       | 53.5 ms                                                | 60.5 ms: 1.13x slower                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.92 ms: 1.14x slower                                 |
| async_generators         | 231 ms                                                 | 292 ms: 1.26x slower                                  |
| bench_mp_pool            | 37.4 ms                                                | 50.1 ms: 1.34x slower                                 |
| telco                    | 3.49 ms                                                | 5.04 ms: 1.44x slower                                 |
| python_startup           | 10.9 ms                                                | 16.9 ms: 1.56x slower                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.9 ms: 1.76x slower                                 |
| Geometric mean           | (ref)                                                  | 1.12x faster                                          |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240814-3.14.0a0-315a933-PYTHON_UOPS/bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.64x