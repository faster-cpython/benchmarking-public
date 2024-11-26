# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: darwin-arm64
- commit hash: c2fad93
- commit date: 2024-10-17
- overall geometric mean: 1.270x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 170 ms: 1.13x faster                                           |
| docutils       | 1.73 sec                                               | 1.50 sec: 1.16x faster                                         |
| html5lib       | 42.4 ms                                                | 32.7 ms: 1.29x faster                                          |
| Geometric mean | (ref)                                                  | 1.18x faster                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 198 ms: 1.97x faster                                           |
| async_tree_memoization  | 474 ms                                                 | 262 ms: 1.81x faster                                           |
| async_tree_io           | 980 ms                                                 | 580 ms: 1.69x faster                                           |
| async_tree_cpu_io_mixed | 649 ms                                                 | 454 ms: 1.43x faster                                           |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.2 ms: 1.49x faster                                          |
| nbody          | 93.0 ms                                                | 63.7 ms: 1.46x faster                                          |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.0 ms: 1.32x faster                                          |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                           |
| regex_v8       | 17.1 ms                                                | 17.0 ms: 1.01x faster                                          |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 176 us: 1.59x faster                                           |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.48x faster                                           |
| xml_etree_process    | 46.5 ms                                                | 33.9 ms: 1.37x faster                                          |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.36x faster                                         |
| json_dumps           | 8.11 ms                                                | 6.16 ms: 1.31x faster                                          |
| xml_etree_generate   | 53.5 ms                                                | 49.5 ms: 1.08x faster                                          |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                           |
| unpickle             | 8.80 us                                                | 9.07 us: 1.03x slower                                          |
| pickle               | 6.97 us                                                | 7.29 us: 1.05x slower                                          |
| pickle_dict          | 17.0 us                                                | 18.6 us: 1.10x slower                                          |
| unpickle_list        | 2.69 us                                                | 3.00 us: 1.11x slower                                          |
| pickle_list          | 2.74 us                                                | 3.11 us: 1.14x slower                                          |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                   |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.2 ms: 1.77x slower                                          |
| python_startup_no_site | 7.91 ms                                                | 14.9 ms: 1.88x slower                                          |
| Geometric mean         | (ref)                                                  | 1.82x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.43 ms: 1.53x faster                                          |
| django_template | 26.4 ms                                                | 20.2 ms: 1.30x faster                                          |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.20x faster                                          |
| genshi_xml      | 33.8 ms                                                | 32.1 ms: 1.05x faster                                          |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.0 us: 3.40x faster                                          |
| deltablue                | 4.91 ms                                                | 2.31 ms: 2.13x faster                                          |
| deepcopy_memo            | 34.7 us                                                | 16.6 us: 2.09x faster                                          |
| logging_silent           | 117 ns                                                 | 56.4 ns: 2.08x faster                                          |
| async_tree_none          | 388 ms                                                 | 198 ms: 1.97x faster                                           |
| deepcopy                 | 272 us                                                 | 149 us: 1.82x faster                                           |
| async_tree_memoization   | 474 ms                                                 | 262 ms: 1.81x faster                                           |
| richards_super           | 57.8 ms                                                | 33.4 ms: 1.73x faster                                          |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                           |
| async_tree_io            | 980 ms                                                 | 580 ms: 1.69x faster                                           |
| raytrace                 | 301 ms                                                 | 180 ms: 1.67x faster                                           |
| chaos                    | 65.8 ms                                                | 39.8 ms: 1.65x faster                                          |
| richards                 | 48.7 ms                                                | 29.9 ms: 1.63x faster                                          |
| scimark_lu               | 103 ms                                                 | 64.0 ms: 1.61x faster                                          |
| pickle_pure_python       | 281 us                                                 | 176 us: 1.59x faster                                           |
| go                       | 151 ms                                                 | 96.1 ms: 1.57x faster                                          |
| deepcopy_reduce          | 2.33 us                                                | 1.49 us: 1.56x faster                                          |
| sqlglot_parse            | 1.24 ms                                                | 808 us: 1.54x faster                                           |
| mako                     | 9.87 ms                                                | 6.43 ms: 1.53x faster                                          |
| scimark_sor              | 128 ms                                                 | 85.8 ms: 1.49x faster                                          |
| float                    | 69.0 ms                                                | 46.2 ms: 1.49x faster                                          |
| asyncio_tcp              | 659 ms                                                 | 442 ms: 1.49x faster                                           |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.48x faster                                           |
| logging_simple           | 4.45 us                                                | 3.02 us: 1.47x faster                                          |
| scimark_monte_carlo      | 65.6 ms                                                | 44.6 ms: 1.47x faster                                          |
| sqlglot_transpile        | 1.44 ms                                                | 984 us: 1.47x faster                                           |
| nbody                    | 93.0 ms                                                | 63.7 ms: 1.46x faster                                          |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                          |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 454 ms: 1.43x faster                                           |
| pylint                   | 277 ms                                                 | 195 ms: 1.42x faster                                           |
| pprint_safe_repr         | 641 ms                                                 | 456 ms: 1.41x faster                                           |
| hexiom                   | 6.19 ms                                                | 4.47 ms: 1.39x faster                                          |
| spectral_norm            | 94.8 ms                                                | 68.6 ms: 1.38x faster                                          |
| crypto_pyaes             | 71.8 ms                                                | 52.2 ms: 1.38x faster                                          |
| xml_etree_process        | 46.5 ms                                                | 33.9 ms: 1.37x faster                                          |
| pprint_pformat           | 1.30 sec                                               | 952 ms: 1.37x faster                                           |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.36x faster                                         |
| comprehensions           | 16.9 us                                                | 12.5 us: 1.36x faster                                          |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                           |
| thrift                   | 572 us                                                 | 423 us: 1.35x faster                                           |
| pycparser                | 877 ms                                                 | 650 ms: 1.35x faster                                           |
| generators               | 32.3 ms                                                | 24.2 ms: 1.34x faster                                          |
| regex_compile            | 95.3 ms                                                | 72.0 ms: 1.32x faster                                          |
| json_dumps               | 8.11 ms                                                | 6.16 ms: 1.31x faster                                          |
| django_template          | 26.4 ms                                                | 20.2 ms: 1.30x faster                                          |
| html5lib                 | 42.4 ms                                                | 32.7 ms: 1.29x faster                                          |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                          |
| sympy_sum                | 92.2 ms                                                | 74.5 ms: 1.24x faster                                          |
| dulwich_log              | 35.3 ms                                                | 28.6 ms: 1.23x faster                                          |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.23x faster                                         |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                           |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.20x faster                                          |
| fannkuch                 | 303 ms                                                 | 257 ms: 1.18x faster                                           |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                           |
| sympy_str                | 165 ms                                                 | 142 ms: 1.16x faster                                           |
| docutils                 | 1.73 sec                                               | 1.50 sec: 1.16x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.97 ms: 1.15x faster                                          |
| sympy_expand             | 269 ms                                                 | 236 ms: 1.14x faster                                           |
| 2to3                     | 192 ms                                                 | 170 ms: 1.13x faster                                           |
| nqueens                  | 63.8 ms                                                | 56.6 ms: 1.13x faster                                          |
| sympy_integrate          | 13.1 ms                                                | 11.8 ms: 1.11x faster                                          |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                           |
| pathlib                  | 24.5 ms                                                | 22.2 ms: 1.10x faster                                          |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                         |
| sqlglot_normalize        | 190 ms                                                 | 174 ms: 1.09x faster                                           |
| sqlglot_optimize         | 36.8 ms                                                | 33.8 ms: 1.09x faster                                          |
| xml_etree_generate       | 53.5 ms                                                | 49.5 ms: 1.08x faster                                          |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                          |
| genshi_xml               | 33.8 ms                                                | 32.1 ms: 1.05x faster                                          |
| meteor_contest           | 77.7 ms                                                | 74.5 ms: 1.04x faster                                          |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.01x faster                                           |
| regex_v8                 | 17.1 ms                                                | 17.0 ms: 1.01x faster                                          |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                           |
| unpickle                 | 8.80 us                                                | 9.07 us: 1.03x slower                                          |
| pickle                   | 6.97 us                                                | 7.29 us: 1.05x slower                                          |
| coverage                 | 41.5 ms                                                | 43.5 ms: 1.05x slower                                          |
| sqlite_synth             | 1.46 us                                                | 1.53 us: 1.05x slower                                          |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                          |
| pickle_dict              | 17.0 us                                                | 18.6 us: 1.10x slower                                          |
| unpickle_list            | 2.69 us                                                | 3.00 us: 1.11x slower                                          |
| pickle_list              | 2.74 us                                                | 3.11 us: 1.14x slower                                          |
| gc_traversal             | 2.36 ms                                                | 2.91 ms: 1.23x slower                                          |
| async_generators         | 231 ms                                                 | 288 ms: 1.25x slower                                           |
| telco                    | 3.49 ms                                                | 4.56 ms: 1.31x slower                                          |
| create_gc_cycles         | 860 us                                                 | 1.29 ms: 1.50x slower                                          |
| bench_mp_pool            | 37.4 ms                                                | 61.0 ms: 1.63x slower                                          |
| python_startup           | 10.9 ms                                                | 19.2 ms: 1.77x slower                                          |
| python_startup_no_site   | 7.91 ms                                                | 14.9 ms: 1.88x slower                                          |
| unpack_sequence          | 39.0 ns                                                | 75.2 ns: 1.93x slower                                          |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                   |

Benchmark hidden because not significant (3): tornado_http, json_loads, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241017-3.14.0a0-c2fad93-JIT/bm-20241017-darwin-arm64-nick%2darm-codecache-3.14.0a0-c2fad93.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.270x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.40x