# Results vs. 3.10.4

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 176 ms: 1.09x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.41 ms: 1.42x faster                                                  |
| docutils       | 1.73 sec                                               | 1.54 sec: 1.13x faster                                                 |
| html5lib       | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 254 ms: 1.87x faster                                                   |
| async_tree_none         | 388 ms                                                 | 221 ms: 1.76x faster                                                   |
| async_tree_io           | 980 ms                                                 | 567 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 69.0 ms                                                | 49.2 ms: 1.40x faster                                                  |
| nbody          | 93.0 ms                                                | 70.2 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                   |
| regex_compile  | 95.3 ms                                                | 83.5 ms: 1.14x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                  |
| regex_effbot   | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.53x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                   |
| tomli_loads          | 1.71 sec                                               | 1.28 sec: 1.33x faster                                                 |
| json_dumps           | 8.11 ms                                                | 6.35 ms: 1.28x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 36.7 ms: 1.27x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 70.0 ms: 1.03x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                  |
| pickle               | 6.97 us                                                | 7.20 us: 1.03x slower                                                  |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| unpickle             | 8.80 us                                                | 9.25 us: 1.05x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.03 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 17.1 ms: 2.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.94x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                  |
| django_template | 26.4 ms                                                | 20.8 ms: 1.27x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.6 ms: 1.19x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 32.9 ms: 1.03x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.22x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 69.8 us: 4.63x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.36 ms: 2.08x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 254 ms: 1.87x faster                                                   |
| logging_silent           | 117 ns                                                 | 65.6 ns: 1.79x faster                                                  |
| async_tree_none          | 388 ms                                                 | 221 ms: 1.76x faster                                                   |
| async_tree_io            | 980 ms                                                 | 567 ms: 1.73x faster                                                   |
| chaos                    | 65.8 ms                                                | 38.1 ms: 1.73x faster                                                  |
| raytrace                 | 301 ms                                                 | 178 ms: 1.69x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.0 ms: 1.65x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 768 us: 1.62x faster                                                   |
| asyncio_tcp              | 659 ms                                                 | 410 ms: 1.61x faster                                                   |
| pylint                   | 277 ms                                                 | 178 ms: 1.55x faster                                                   |
| richards                 | 48.7 ms                                                | 31.4 ms: 1.55x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 938 us: 1.54x faster                                                   |
| crypto_pyaes             | 71.8 ms                                                | 46.9 ms: 1.53x faster                                                  |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.53x faster                                                   |
| scimark_monte_carlo      | 65.6 ms                                                | 44.5 ms: 1.47x faster                                                  |
| go                       | 151 ms                                                 | 105 ms: 1.43x faster                                                   |
| mako                     | 9.87 ms                                                | 6.89 ms: 1.43x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 24.2 us: 1.43x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 455 ms: 1.43x faster                                                   |
| chameleon                | 6.26 ms                                                | 4.41 ms: 1.42x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.0 us: 1.41x faster                                                  |
| float                    | 69.0 ms                                                | 49.2 ms: 1.40x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                   |
| logging_simple           | 4.45 us                                                | 3.26 us: 1.37x faster                                                  |
| logging_format           | 4.83 us                                                | 3.54 us: 1.36x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.28 sec: 1.33x faster                                                 |
| nbody                    | 93.0 ms                                                | 70.2 ms: 1.32x faster                                                  |
| html5lib                 | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                                   |
| pycparser                | 877 ms                                                 | 670 ms: 1.31x faster                                                   |
| pyflate                  | 427 ms                                                 | 328 ms: 1.30x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 497 ms: 1.29x faster                                                   |
| json_dumps               | 8.11 ms                                                | 6.35 ms: 1.28x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 1.02 sec: 1.28x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.86 ms: 1.27x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 74.5 ms: 1.27x faster                                                  |
| django_template          | 26.4 ms                                                | 20.8 ms: 1.27x faster                                                  |
| scimark_lu               | 103 ms                                                 | 81.0 ms: 1.27x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 36.7 ms: 1.27x faster                                                  |
| deepcopy                 | 272 us                                                 | 215 us: 1.26x faster                                                   |
| deepcopy_reduce          | 2.33 us                                                | 1.86 us: 1.26x faster                                                  |
| mypy2                    | 607 ms                                                 | 490 ms: 1.24x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.31 sec: 1.23x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 76.0 ms: 1.21x faster                                                  |
| coroutines               | 20.7 ms                                                | 17.2 ms: 1.20x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                   |
| scimark_sor              | 128 ms                                                 | 107 ms: 1.20x faster                                                   |
| create_gc_cycles         | 860 us                                                 | 719 us: 1.20x faster                                                   |
| generators               | 32.3 ms                                                | 27.1 ms: 1.20x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 29.6 ms: 1.19x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.6 ms: 1.19x faster                                                  |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                                   |
| sympy_integrate          | 13.1 ms                                                | 11.2 ms: 1.17x faster                                                  |
| fannkuch                 | 303 ms                                                 | 259 ms: 1.17x faster                                                   |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| regex_compile            | 95.3 ms                                                | 83.5 ms: 1.14x faster                                                  |
| scimark_fft              | 224 ms                                                 | 199 ms: 1.13x faster                                                   |
| dask                     | 253 ms                                                 | 225 ms: 1.13x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.54 sec: 1.13x faster                                                 |
| gunicorn                 | 1.30 ms                                                | 1.16 ms: 1.12x faster                                                  |
| aiohttp                  | 1.22 ms                                                | 1.11 ms: 1.10x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.12 ms: 1.10x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.7 ms: 1.09x faster                                                  |
| 2to3                     | 192 ms                                                 | 176 ms: 1.09x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 176 ms: 1.08x faster                                                   |
| bench_thread_pool        | 527 us                                                 | 491 us: 1.07x faster                                                   |
| meteor_contest           | 77.7 ms                                                | 73.3 ms: 1.06x faster                                                  |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                  |
| nqueens                  | 63.8 ms                                                | 61.2 ms: 1.04x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.57 sec: 1.04x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 70.0 ms: 1.03x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 32.9 ms: 1.03x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.01x faster                                                  |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                   |
| xml_etree_generate       | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.40 ms: 1.02x slower                                                  |
| pickle                   | 6.97 us                                                | 7.20 us: 1.03x slower                                                  |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.55 ms: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.25 us: 1.05x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.07x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                  |
| sqlite_synth             | 1.46 us                                                | 1.59 us: 1.09x slower                                                  |
| coverage                 | 41.5 ms                                                | 46.5 ms: 1.12x slower                                                  |
| unpickle_list            | 2.69 us                                                | 3.03 us: 1.13x slower                                                  |
| async_generators         | 231 ms                                                 | 301 ms: 1.30x slower                                                   |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 51.2 ms: 1.37x slower                                                  |
| python_startup           | 10.9 ms                                                | 18.9 ms: 1.74x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 17.1 ms: 2.16x slower                                                  |
| unpack_sequence          | 39.0 ns                                                | 113 ns: 2.89x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (3): tornado_http, pidigits, pathlib
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x


# Memory

- memory change: 1.63x