# Results vs. 3.10.4

- fork: bdraco
- ref: speed_up_async_sched
- machine: darwin-arm64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.77x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 192 ms: 2.02x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 243 ms: 1.95x faster                                                  |
| async_tree_io           | 980 ms                                                 | 598 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 457 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                 |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.30 ms: 1.29x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.7 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.2 ms: 1.00x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 73.8 ms: 1.02x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.5 ms: 1.52x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.5 ms: 1.71x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.61x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.94 ms: 1.42x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 90.9 us: 3.55x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.13 ms: 2.30x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.06x faster                                                 |
| async_tree_none          | 388 ms                                                 | 192 ms: 2.02x faster                                                  |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 243 ms: 1.95x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.2 ns: 1.91x faster                                                 |
| deepcopy                 | 272 us                                                 | 144 us: 1.89x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                 |
| richards_super           | 57.8 ms                                                | 33.4 ms: 1.73x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.93 us: 1.71x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 739 us: 1.68x faster                                                  |
| async_tree_io            | 980 ms                                                 | 598 ms: 1.64x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 897 us: 1.61x faster                                                  |
| richards                 | 48.7 ms                                                | 30.4 ms: 1.60x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 416 ms: 1.59x faster                                                  |
| generators               | 32.3 ms                                                | 20.4 ms: 1.58x faster                                                 |
| nbody                    | 93.0 ms                                                | 59.4 ms: 1.57x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.55x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.7 ms: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.06 ms: 1.53x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 43.3 ms: 1.51x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                 |
| go                       | 151 ms                                                 | 106 ms: 1.43x faster                                                  |
| regex_compile            | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 6.94 ms: 1.42x faster                                                 |
| logging_format           | 4.83 us                                                | 3.40 us: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 457 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.9 ms: 1.41x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 930 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 457 ms: 1.40x faster                                                  |
| spectral_norm            | 94.8 ms                                                | 67.7 ms: 1.40x faster                                                 |
| scimark_sor              | 128 ms                                                 | 93.3 ms: 1.37x faster                                                 |
| pycparser                | 877 ms                                                 | 643 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| thrift                   | 572 us                                                 | 423 us: 1.35x faster                                                  |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 69.1 ms: 1.33x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.1 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.30 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| sympy_str                | 165 ms                                                 | 131 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.8 ms: 1.26x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 37.7 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.78 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 449 us: 1.17x faster                                                  |
| fannkuch                 | 303 ms                                                 | 260 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 168 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.1 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.5 ms: 1.07x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.5 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                 |
| json                     | 3.08 ms                                                | 3.01 ms: 1.02x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.2 ms: 1.00x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 73.8 ms: 1.02x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.47 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 906 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.3 ms: 1.07x slower                                                 |
| async_generators         | 231 ms                                                 | 281 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.7 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.78 ms: 1.37x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.5 ms: 1.52x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.5 ms: 1.71x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240824-3.14.0a0-f78838c/bm-20240824-darwin-arm64-bdraco-speed_up_async_sched-3.14.0a0-f78838c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.77x