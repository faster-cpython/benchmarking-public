# Results vs. 3.10.4

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: darwin-arm64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.27x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 0.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 161 ms: 1.19x faster                                                   |
| chameleon      | 6.26 ms                                                | 4.31 ms: 1.45x faster                                                  |
| docutils       | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| html5lib       | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                  |
| tornado_http   | 86.7 ms                                                | 65.4 ms: 1.33x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 207 ms: 1.87x faster                                                   |
| async_tree_memoization  | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| async_tree_io           | 980 ms                                                 | 558 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed | 649 ms                                                 | 465 ms: 1.40x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.9 ms: 1.53x faster                                                  |
| float          | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                  |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 178 us: 1.58x faster                                                   |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                   |
| json_dumps           | 8.11 ms                                                | 6.42 ms: 1.26x faster                                                  |
| xml_etree_process    | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.44 sec: 1.18x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                  |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| unpickle             | 8.80 us                                                | 9.22 us: 1.05x slower                                                  |
| pickle               | 6.97 us                                                | 7.49 us: 1.07x slower                                                  |
| unpickle_list        | 2.69 us                                                | 2.91 us: 1.08x slower                                                  |
| pickle_dict          | 17.0 us                                                | 18.5 us: 1.09x slower                                                  |
| pickle_list          | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.2 ms: 1.31x slower                                                  |
| python_startup_no_site | 7.91 ms                                                | 11.2 ms: 1.42x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                  |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                  |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                  |
| genshi_xml      | 33.8 ms                                                | 29.9 ms: 1.13x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 90.5 us: 3.57x faster                                                  |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.28x faster                                                  |
| raytrace                 | 301 ms                                                 | 149 ms: 2.03x faster                                                   |
| logging_silent           | 117 ns                                                 | 61.6 ns: 1.90x faster                                                  |
| chaos                    | 65.8 ms                                                | 34.8 ms: 1.89x faster                                                  |
| async_tree_none          | 388 ms                                                 | 207 ms: 1.87x faster                                                   |
| async_tree_memoization   | 474 ms                                                 | 255 ms: 1.85x faster                                                   |
| async_tree_io            | 980 ms                                                 | 558 ms: 1.76x faster                                                   |
| sqlglot_parse            | 1.24 ms                                                | 738 us: 1.69x faster                                                   |
| pylint                   | 277 ms                                                 | 168 ms: 1.65x faster                                                   |
| richards_super           | 57.8 ms                                                | 35.2 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 897 us: 1.61x faster                                                   |
| mypy2                    | 607 ms                                                 | 379 ms: 1.60x faster                                                   |
| pickle_pure_python       | 281 us                                                 | 178 us: 1.58x faster                                                   |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.55x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 42.5 ms: 1.54x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 428 ms: 1.54x faster                                                   |
| scimark_lu               | 103 ms                                                 | 66.8 ms: 1.54x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 22.6 us: 1.54x faster                                                  |
| richards                 | 48.7 ms                                                | 31.8 ms: 1.53x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.9 ms: 1.53x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.09 ms: 1.51x faster                                                  |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                                   |
| chameleon                | 6.26 ms                                                | 4.31 ms: 1.45x faster                                                  |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 49.9 ms: 1.44x faster                                                  |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                  |
| mako                     | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 66.8 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.7 ms: 1.42x faster                                                  |
| generators               | 32.3 ms                                                | 23.1 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 465 ms: 1.40x faster                                                   |
| regex_compile            | 95.3 ms                                                | 68.5 ms: 1.39x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 942 ms: 1.38x faster                                                   |
| pprint_safe_repr         | 641 ms                                                 | 464 ms: 1.38x faster                                                   |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                   |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                   |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                  |
| scimark_sor              | 128 ms                                                 | 94.8 ms: 1.35x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.4 ms: 1.35x faster                                                  |
| pyflate                  | 427 ms                                                 | 317 ms: 1.35x faster                                                   |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                                   |
| tornado_http             | 86.7 ms                                                | 65.4 ms: 1.33x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.7 ms: 1.32x faster                                                  |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                                   |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.23 sec: 1.30x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.80 us: 1.30x faster                                                  |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.5 ms: 1.28x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.42 ms: 1.26x faster                                                  |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                   |
| xml_etree_process        | 46.5 ms                                                | 37.3 ms: 1.25x faster                                                  |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                  |
| scimark_fft              | 224 ms                                                 | 183 ms: 1.23x faster                                                   |
| aiohttp                  | 1.22 ms                                                | 999 us: 1.22x faster                                                   |
| gunicorn                 | 1.30 ms                                                | 1.06 ms: 1.22x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.80 ms: 1.22x faster                                                  |
| nqueens                  | 63.8 ms                                                | 52.4 ms: 1.22x faster                                                  |
| fannkuch                 | 303 ms                                                 | 249 ms: 1.22x faster                                                   |
| docutils                 | 1.73 sec                                               | 1.43 sec: 1.21x faster                                                 |
| 2to3                     | 192 ms                                                 | 161 ms: 1.19x faster                                                   |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.44 sec: 1.18x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                   |
| dask                     | 253 ms                                                 | 217 ms: 1.17x faster                                                   |
| mdp                      | 1.63 sec                                               | 1.41 sec: 1.16x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 459 us: 1.15x faster                                                   |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                                   |
| genshi_xml               | 33.8 ms                                                | 29.9 ms: 1.13x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 70.0 ms: 1.11x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                  |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 71.7 ms: 1.01x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                  |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.22 us: 1.05x slower                                                  |
| create_gc_cycles         | 860 us                                                 | 901 us: 1.05x slower                                                   |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                                  |
| pickle                   | 6.97 us                                                | 7.49 us: 1.07x slower                                                  |
| unpickle_list            | 2.69 us                                                | 2.91 us: 1.08x slower                                                  |
| coverage                 | 41.5 ms                                                | 45.1 ms: 1.09x slower                                                  |
| pickle_dict              | 17.0 us                                                | 18.5 us: 1.09x slower                                                  |
| pickle_list              | 2.74 us                                                | 2.99 us: 1.09x slower                                                  |
| flaskblogging            | 2.65 ms                                                | 3.06 ms: 1.16x slower                                                  |
| async_generators         | 231 ms                                                 | 280 ms: 1.21x slower                                                   |
| bench_mp_pool            | 37.4 ms                                                | 46.4 ms: 1.24x slower                                                  |
| python_startup           | 10.9 ms                                                | 14.2 ms: 1.31x slower                                                  |
| telco                    | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| python_startup_no_site   | 7.91 ms                                                | 11.2 ms: 1.42x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-darwin-arm64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 0.78x