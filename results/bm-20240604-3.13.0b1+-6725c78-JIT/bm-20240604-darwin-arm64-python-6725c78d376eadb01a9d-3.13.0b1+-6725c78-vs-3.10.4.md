# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 0.74x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 172 ms: 1.12x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.41 ms: 1.42x faster                                                  |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.9 ms: 1.33x faster                                                  |
| tornado_http   | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 209 ms: 1.86x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 259 ms: 1.83x faster                                                   |
| async_tree_io           | 980 ms                                                 | 550 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 466 ms: 1.39x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.70x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                  |
| float          | 69.0 ms                                                | 47.4 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.7 ms: 1.31x faster                                                  |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 173 us: 1.62x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.49x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.11 ms: 1.33x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 35.9 ms: 1.30x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 51.4 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 70.3 ms: 1.03x faster                                                  |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.13 us: 1.04x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.88 us: 1.07x slower                                                  |
| pickle               | 6.97 us                                                | 7.49 us: 1.07x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.6 ms: 1.44x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.37 ms: 1.55x faster                                                  |
| django_template | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                  |
| genshi_text     | 17.3 ms                                                | 16.0 ms: 1.09x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 39.5 ms: 1.17x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.1 us: 3.47x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.48 ms: 1.98x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.2 ns: 1.88x faster                                                  |
| async_tree_none          | 388 ms                                                 | 209 ms: 1.86x faster                                                   |
| raytrace                 | 301 ms                                                 | 164 ms: 1.84x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 259 ms: 1.83x faster                                                   |
| async_tree_io            | 980 ms                                                 | 550 ms: 1.78x faster                                                   |
| chaos                    | 65.8 ms                                                | 39.1 ms: 1.68x faster                                                  |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 173 us: 1.62x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 21.7 us: 1.60x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 419 ms: 1.57x faster                                                   |
| mako                     | 9.87 ms                                                | 6.37 ms: 1.55x faster                                                  |
| richards                 | 48.7 ms                                                | 31.5 ms: 1.55x faster                                                  |
| pylint                   | 277 ms                                                 | 180 ms: 1.54x faster                                                   |
| mypy2                    | 607 ms                                                 | 404 ms: 1.50x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 831 us: 1.50x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 44.0 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.49x faster                                                   |
| nbody                    | 93.0 ms                                                | 63.6 ms: 1.46x faster                                                  |
| float                    | 69.0 ms                                                | 47.4 ms: 1.46x faster                                                  |
| go                       | 151 ms                                                 | 103 ms: 1.46x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                  |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.41 ms: 1.42x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.37 ms: 1.42x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 67.1 ms: 1.41x faster                                                  |
| generators               | 32.3 ms                                                | 23.0 ms: 1.41x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 459 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 466 ms: 1.39x faster                                                   |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.39x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 947 ms: 1.38x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                                 |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                                   |
| html5lib                 | 42.4 ms                                                | 31.9 ms: 1.33x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.11 ms: 1.33x faster                                                  |
| deepcopy                 | 272 us                                                 | 207 us: 1.31x faster                                                   |
| regex_compile            | 95.3 ms                                                | 72.7 ms: 1.31x faster                                                  |
| thrift                   | 572 us                                                 | 437 us: 1.31x faster                                                   |
| scimark_lu               | 103 ms                                                 | 78.7 ms: 1.31x faster                                                  |
| pycparser                | 877 ms                                                 | 672 ms: 1.30x faster                                                   |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.9 ms: 1.30x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.24 sec: 1.29x faster                                                 |
| fannkuch                 | 303 ms                                                 | 235 ms: 1.29x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.82 us: 1.28x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 71.9 ms: 1.28x faster                                                  |
| tornado_http             | 86.7 ms                                                | 67.9 ms: 1.28x faster                                                  |
| scimark_sor              | 128 ms                                                 | 101 ms: 1.27x faster                                                   |
| django_template          | 26.4 ms                                                | 21.3 ms: 1.24x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.0 ms: 1.22x faster                                                  |
| scimark_fft              | 224 ms                                                 | 186 ms: 1.21x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.21x faster                                                  |
| sympy_str                | 165 ms                                                 | 137 ms: 1.20x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 1.04 ms: 1.18x faster                                                  |
| gunicorn                 | 1.30 ms                                                | 1.11 ms: 1.18x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.92 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.15x faster                                                 |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                   |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.44 sec: 1.13x faster                                                 |
| sqlglot_optimize         | 36.8 ms                                                | 32.7 ms: 1.12x faster                                                  |
| nqueens                  | 63.8 ms                                                | 56.8 ms: 1.12x faster                                                  |
| 2to3                     | 192 ms                                                 | 172 ms: 1.12x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 478 us: 1.10x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                                  |
| genshi_text              | 17.3 ms                                                | 16.0 ms: 1.09x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.06x faster                                                   |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 51.4 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 70.3 ms: 1.03x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                   |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.13 us: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 909 us: 1.06x slower                                                   |
| unpickle_list            | 2.69 us                                                | 2.88 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.49 us: 1.07x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.1 ms: 1.09x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 39.5 ms: 1.17x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.25 ms: 1.23x slower                                                  |
| async_generators         | 231 ms                                                 | 296 ms: 1.28x slower                                                   |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 49.9 ms: 1.34x slower                                                  |
| python_startup           | 10.9 ms                                                | 15.6 ms: 1.44x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.61x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 0.74x