# Results vs. 3.10.4

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: darwin-arm64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.03x faster
- HPT reliability: 99.77%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 192 ms: 1.00x slower                                                   |
| chameleon      | 6.26 ms                                                | 4.46 ms: 1.40x faster                                                  |
| docutils       | 1.73 sec                                               | 2.60 sec: 1.50x slower                                                 |
| html5lib       | 42.4 ms                                                | 38.1 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 649 ms                                                 | 2.80 sec: 4.31x slower                                                 |
| async_tree_none         | 388 ms                                                 | 2.21 sec: 5.69x slower                                                 |
| async_tree_memoization  | 474 ms                                                 | 2.82 sec: 5.96x slower                                                 |
| async_tree_io           | 980 ms                                                 | 8.92 sec: 9.10x slower                                                 |
| Geometric mean          | (ref)                                                  | 6.04x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 70.3 ms: 1.32x faster                                                  |
| float          | 69.0 ms                                                | 89.5 ms: 1.30x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 82.0 ms: 1.16x faster                                                  |
| regex_dna      | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.52x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.31 sec: 1.31x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 41.1 ms: 1.13x faster                                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.11 us: 1.04x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle               | 6.97 us                                                | 7.44 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| xml_etree_generate   | 53.5 ms                                                | 60.2 ms: 1.13x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 132 ms: 1.22x slower                                                   |
| xml_etree_iterparse  | 72.1 ms                                                | 106 ms: 1.47x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.8 ms: 1.64x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 16.1 ms: 2.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.82x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.90 ms: 1.43x faster                                                  |
| django_template | 26.4 ms                                                | 20.5 ms: 1.29x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.7 ms: 1.18x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 35.7 ms: 1.06x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 69.6 us: 4.64x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.46 ms: 2.00x faster                                                  |
| logging_silent           | 117 ns                                                 | 65.5 ns: 1.79x faster                                                  |
| chaos                    | 65.8 ms                                                | 38.6 ms: 1.71x faster                                                  |
| raytrace                 | 301 ms                                                 | 179 ms: 1.68x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.0 ms: 1.65x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 418 ms: 1.58x faster                                                   |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.54x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 47.0 ms: 1.53x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.52x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 826 us: 1.50x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 44.7 ms: 1.47x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                  |
| mako                     | 9.87 ms                                                | 6.90 ms: 1.43x faster                                                  |
| go                       | 151 ms                                                 | 105 ms: 1.43x faster                                                   |
| deepcopy_memo            | 34.7 us                                                | 24.4 us: 1.42x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.46 ms: 1.40x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.2 us: 1.39x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.30 us: 1.35x faster                                                  |
| logging_format           | 4.83 us                                                | 3.60 us: 1.34x faster                                                  |
| nbody                    | 93.0 ms                                                | 70.3 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                                   |
| tomli_loads              | 1.71 sec                                               | 1.31 sec: 1.31x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 492 ms: 1.30x faster                                                   |
| pyflate                  | 427 ms                                                 | 330 ms: 1.29x faster                                                   |
| django_template          | 26.4 ms                                                | 20.5 ms: 1.29x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.82 ms: 1.29x faster                                                  |
| deepcopy                 | 272 us                                                 | 213 us: 1.27x faster                                                   |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.27x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 74.5 ms: 1.27x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.39 ms: 1.27x faster                                                  |
| scimark_lu               | 103 ms                                                 | 81.4 ms: 1.26x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.86 us: 1.25x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 75.0 ms: 1.23x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.22x faster                                                 |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.20x faster                                                   |
| sympy_str                | 165 ms                                                 | 138 ms: 1.20x faster                                                   |
| generators               | 32.3 ms                                                | 27.1 ms: 1.19x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.19x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.8 ms: 1.19x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.7 ms: 1.18x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.8 ms: 1.16x faster                                                  |
| regex_compile            | 95.3 ms                                                | 82.0 ms: 1.16x faster                                                  |
| fannkuch                 | 303 ms                                                 | 261 ms: 1.16x faster                                                   |
| create_gc_cycles         | 860 us                                                 | 749 us: 1.15x faster                                                   |
| regex_dna                | 174 ms                                                 | 152 ms: 1.15x faster                                                   |
| mypy2                    | 607 ms                                                 | 531 ms: 1.14x faster                                                   |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 41.1 ms: 1.13x faster                                                  |
| scimark_fft              | 224 ms                                                 | 199 ms: 1.13x faster                                                   |
| html5lib                 | 42.4 ms                                                | 38.1 ms: 1.11x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 174 ms: 1.09x faster                                                   |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.14 ms: 1.09x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 493 us: 1.07x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 34.7 ms: 1.06x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 73.9 ms: 1.05x faster                                                  |
| json                     | 3.08 ms                                                | 2.93 ms: 1.05x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.17 ms: 1.05x faster                                                  |
| pycparser                | 877 ms                                                 | 840 ms: 1.04x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.25 ms: 1.04x faster                                                  |
| nqueens                  | 63.8 ms                                                | 61.6 ms: 1.04x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.60 sec: 1.02x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                  |
| 2to3                     | 192 ms                                                 | 192 ms: 1.00x slower                                                   |
| gc_traversal             | 2.36 ms                                                | 2.43 ms: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.11 us: 1.04x slower                                                  |
| genshi_xml               | 33.8 ms                                                | 35.7 ms: 1.06x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.44 us: 1.07x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.64 ms: 1.07x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.59 us: 1.09x slower                                                  |
| xml_etree_generate       | 53.5 ms                                                | 60.2 ms: 1.13x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.05 us: 1.13x slower                                                  |
| coverage                 | 41.5 ms                                                | 47.2 ms: 1.14x slower                                                  |
| xml_etree_parse          | 108 ms                                                 | 132 ms: 1.22x slower                                                   |
| float                    | 69.0 ms                                                | 89.5 ms: 1.30x slower                                                  |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 54.0 ms: 1.44x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 106 ms: 1.47x slower                                                   |
| async_generators         | 231 ms                                                 | 344 ms: 1.49x slower                                                   |
| docutils                 | 1.73 sec                                               | 2.60 sec: 1.50x slower                                                 |
| python_startup           | 10.9 ms                                                | 17.8 ms: 1.64x slower                                                  |
| dask                     | 253 ms                                                 | 456 ms: 1.80x slower                                                   |
| python_startup_no_site   | 7.91 ms                                                | 16.1 ms: 2.03x slower                                                  |
| pylint                   | 277 ms                                                 | 588 ms: 2.13x slower                                                   |
| unpack_sequence          | 39.0 ns                                                | 113 ns: 2.89x slower                                                   |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 2.80 sec: 4.31x slower                                                 |
| async_tree_none          | 388 ms                                                 | 2.21 sec: 5.69x slower                                                 |
| async_tree_memoization   | 474 ms                                                 | 2.82 sec: 5.96x slower                                                 |
| async_tree_io            | 980 ms                                                 | 8.92 sec: 9.10x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (4): tornado_http, asyncio_websockets, pidigits, pathlib
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-darwin-arm64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 99.77% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.60x