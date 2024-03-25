# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 164 ms: 1.17x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.46 ms: 1.40x faster                                                  |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                 |
| html5lib       | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.89x faster                                                   |
| async_tree_none         | 388 ms                                                 | 220 ms: 1.77x faster                                                   |
| async_tree_io           | 980 ms                                                 | 561 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.70x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 51.2 ms: 1.35x faster                                                  |
| nbody          | 93.0 ms                                                | 71.0 ms: 1.31x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 70.0 ms: 1.36x faster                                                  |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 185 us: 1.52x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 148 us: 1.32x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.52 sec: 1.12x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.4 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 69.6 ms: 1.04x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 54.6 ms: 1.02x slower                                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.04x slower                                                  |
| pickle               | 6.97 us                                                | 7.25 us: 1.04x slower                                                  |
| unpickle             | 8.80 us                                                | 9.17 us: 1.04x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.95 us: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 13.0 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.06 ms: 1.40x faster                                                  |
| django_template | 26.4 ms                                                | 20.3 ms: 1.30x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.21x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 31.2 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 69.7 us: 4.64x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.27 ms: 2.17x faster                                                  |
| raytrace                 | 301 ms                                                 | 156 ms: 1.93x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.89x faster                                                   |
| logging_silent           | 117 ns                                                 | 65.1 ns: 1.80x faster                                                  |
| chaos                    | 65.8 ms                                                | 36.9 ms: 1.78x faster                                                  |
| async_tree_none          | 388 ms                                                 | 220 ms: 1.77x faster                                                   |
| async_tree_io            | 980 ms                                                 | 561 ms: 1.74x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 748 us: 1.66x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 399 ms: 1.65x faster                                                   |
| pylint                   | 277 ms                                                 | 168 ms: 1.65x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.7 ms: 1.62x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 909 us: 1.59x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 47.1 ms: 1.53x faster                                                  |
| comprehensions           | 16.9 us                                                | 11.2 us: 1.52x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 185 us: 1.52x faster                                                   |
| richards                 | 48.7 ms                                                | 32.3 ms: 1.51x faster                                                  |
| scimark_lu               | 103 ms                                                 | 68.5 ms: 1.50x faster                                                  |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                   |
| hexiom                   | 6.19 ms                                                | 4.20 ms: 1.48x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 23.6 us: 1.47x faster                                                  |
| unpack_sequence          | 39.0 ns                                                | 26.5 ns: 1.47x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.6 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| chameleon                | 6.26 ms                                                | 4.46 ms: 1.40x faster                                                  |
| mako                     | 9.87 ms                                                | 7.06 ms: 1.40x faster                                                  |
| regex_compile            | 95.3 ms                                                | 70.0 ms: 1.36x faster                                                  |
| logging_format           | 4.83 us                                                | 3.55 us: 1.36x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.29 us: 1.35x faster                                                  |
| float                    | 69.0 ms                                                | 51.2 ms: 1.35x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 972 ms: 1.34x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 478 ms: 1.34x faster                                                   |
| spectral_norm            | 94.8 ms                                                | 71.3 ms: 1.33x faster                                                  |
| pycparser                | 877 ms                                                 | 661 ms: 1.33x faster                                                   |
| sympy_sum                | 92.2 ms                                                | 70.0 ms: 1.32x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 148 us: 1.32x faster                                                   |
| nbody                    | 93.0 ms                                                | 71.0 ms: 1.31x faster                                                  |
| django_template          | 26.4 ms                                                | 20.3 ms: 1.30x faster                                                  |
| mypy2                    | 607 ms                                                 | 466 ms: 1.30x faster                                                   |
| pyflate                  | 427 ms                                                 | 329 ms: 1.30x faster                                                   |
| thrift                   | 572 us                                                 | 442 us: 1.29x faster                                                   |
| scimark_sor              | 128 ms                                                 | 100 ms: 1.28x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.28x faster                                                  |
| deepcopy                 | 272 us                                                 | 213 us: 1.28x faster                                                   |
| json_dumps               | 8.11 ms                                                | 6.36 ms: 1.27x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.86 us: 1.26x faster                                                  |
| sympy_str                | 165 ms                                                 | 132 ms: 1.25x faster                                                   |
| html5lib                 | 42.4 ms                                                | 34.0 ms: 1.25x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.5 ms: 1.24x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 28.6 ms: 1.24x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.23x faster                                                 |
| gunicorn                 | 1.30 ms                                                | 1.08 ms: 1.21x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.21x faster                                                  |
| create_gc_cycles         | 860 us                                                 | 712 us: 1.21x faster                                                   |
| coroutines               | 20.7 ms                                                | 17.3 ms: 1.20x faster                                                  |
| generators               | 32.3 ms                                                | 27.1 ms: 1.19x faster                                                  |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                 |
| 2to3                     | 192 ms                                                 | 164 ms: 1.17x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.9 ms: 1.15x faster                                                  |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 1.07 ms: 1.15x faster                                                  |
| dask                     | 253 ms                                                 | 222 ms: 1.14x faster                                                   |
| nqueens                  | 63.8 ms                                                | 55.9 ms: 1.14x faster                                                  |
| scimark_fft              | 224 ms                                                 | 197 ms: 1.14x faster                                                   |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.02 ms: 1.14x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.52 sec: 1.12x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 171 ms: 1.11x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 477 us: 1.11x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 71.2 ms: 1.09x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 99.4 ms: 1.08x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 31.2 ms: 1.08x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.52 sec: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 69.6 ms: 1.04x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                   |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.39 ms: 1.01x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 54.6 ms: 1.02x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.04x slower                                                  |
| pickle                   | 6.97 us                                                | 7.25 us: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.17 us: 1.04x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.56 us: 1.07x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.95 us: 1.08x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| coverage                 | 41.5 ms                                                | 47.2 ms: 1.14x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 45.1 ms: 1.21x slower                                                  |
| async_generators         | 231 ms                                                 | 286 ms: 1.24x slower                                                   |
| telco                    | 3.49 ms                                                | 4.53 ms: 1.30x slower                                                  |
| python_startup           | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 13.0 ms: 1.65x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (2): tornado_http, pathlib
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x


# Memory

- memory change: 1.14x