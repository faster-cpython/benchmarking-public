# Results vs. 3.10.4

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: darwin-arm64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 163 ms: 1.17x faster                                                  |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.34x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.4 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 231 ms: 2.05x faster                                                  |
| async_tree_none         | 388 ms                                                 | 191 ms: 2.03x faster                                                  |
| async_tree_io           | 980 ms                                                 | 532 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 451 ms: 1.44x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 62.2 ms: 1.49x faster                                                 |
| float          | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.3 ms: 1.39x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.57 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 181 us: 1.55x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.53 ms: 1.24x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 13.6 ms: 1.25x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 10.8 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.05 ms: 1.40x faster                                                 |
| django_template | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 94.7 us: 3.41x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.10 ms: 2.34x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.06x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 231 ms: 2.05x faster                                                  |
| async_tree_none          | 388 ms                                                 | 191 ms: 2.03x faster                                                  |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| logging_silent           | 117 ns                                                 | 59.1 ns: 1.98x faster                                                 |
| deepcopy                 | 272 us                                                 | 145 us: 1.87x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                 |
| async_tree_io            | 980 ms                                                 | 532 ms: 1.84x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.68x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 739 us: 1.68x faster                                                  |
| pylint                   | 277 ms                                                 | 171 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 899 us: 1.61x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 414 ms: 1.59x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.8 us: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.56x faster                                                 |
| richards                 | 48.7 ms                                                | 31.4 ms: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 181 us: 1.55x faster                                                  |
| go                       | 151 ms                                                 | 98.9 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.3 ms: 1.51x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.11 ms: 1.51x faster                                                 |
| nbody                    | 93.0 ms                                                | 62.2 ms: 1.49x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.04 us: 1.47x faster                                                 |
| scimark_lu               | 103 ms                                                 | 70.7 ms: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 451 ms: 1.44x faster                                                  |
| generators               | 32.3 ms                                                | 22.7 ms: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| float                    | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                 |
| mako                     | 9.87 ms                                                | 7.05 ms: 1.40x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.3 ms: 1.39x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 467 ms: 1.37x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 952 ms: 1.37x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                  |
| pycparser                | 877 ms                                                 | 643 ms: 1.36x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 320 ms: 1.33x faster                                                  |
| django_template          | 26.4 ms                                                | 19.8 ms: 1.33x faster                                                 |
| scimark_sor              | 128 ms                                                 | 96.5 ms: 1.33x faster                                                 |
| thrift                   | 572 us                                                 | 433 us: 1.32x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 70.5 ms: 1.31x faster                                                 |
| tornado_http             | 86.7 ms                                                | 66.4 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.2 ms: 1.28x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.53 ms: 1.24x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                 |
| sympy_str                | 165 ms                                                 | 134 ms: 1.23x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 37.8 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 187 ms: 1.20x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.89 ms: 1.19x faster                                                 |
| nqueens                  | 63.8 ms                                                | 54.0 ms: 1.18x faster                                                 |
| 2to3                     | 192 ms                                                 | 163 ms: 1.17x faster                                                  |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.4 ms: 1.17x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 453 us: 1.16x faster                                                  |
| sympy_expand             | 269 ms                                                 | 232 ms: 1.16x faster                                                  |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.16x faster                                                  |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.15x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 169 ms: 1.13x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.3 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.2 ms: 1.09x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.1 ms: 1.06x faster                                                 |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.1 ms: 1.00x faster                                                 |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 896 us: 1.04x slower                                                  |
| regex_effbot             | 2.46 ms                                                | 2.57 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.1 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 45.9 ms: 1.23x slower                                                 |
| python_startup           | 10.9 ms                                                | 13.6 ms: 1.25x slower                                                 |
| telco                    | 3.49 ms                                                | 4.59 ms: 1.31x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 10.8 ms: 1.37x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.20x