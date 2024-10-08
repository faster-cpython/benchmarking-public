# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: darwin-arm64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 0.87x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 190 ms: 1.01x faster                                                  |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                |
| html5lib       | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 243 ms: 1.95x faster                                                  |
| async_tree_io           | 980 ms                                                 | 550 ms: 1.78x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.5 ms: 1.56x faster                                                 |
| float          | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.2 ms: 1.38x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 187 us: 1.50x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 145 us: 1.34x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.52 ms: 1.24x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 38.6 ms: 1.21x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                 |
| json_loads           | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.4 ms: 1.69x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.20 ms: 1.37x faster                                                 |
| django_template | 26.4 ms                                                | 20.2 ms: 1.31x faster                                                 |
| genshi_text     | 17.3 ms                                                | 14.2 ms: 1.22x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.6 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 96.2 us: 3.36x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.28x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.02x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 17.4 us: 2.00x faster                                                 |
| async_tree_none          | 388 ms                                                 | 197 ms: 1.97x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 243 ms: 1.95x faster                                                  |
| logging_silent           | 117 ns                                                 | 62.0 ns: 1.89x faster                                                 |
| chaos                    | 65.8 ms                                                | 35.5 ms: 1.85x faster                                                 |
| deepcopy                 | 272 us                                                 | 148 us: 1.84x faster                                                  |
| async_tree_io            | 980 ms                                                 | 550 ms: 1.78x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 746 us: 1.67x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.9 ms: 1.66x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 406 ms: 1.63x faster                                                  |
| sqlglot_transpile        | 1.44 ms                                                | 913 us: 1.58x faster                                                  |
| nbody                    | 93.0 ms                                                | 59.5 ms: 1.56x faster                                                 |
| generators               | 32.3 ms                                                | 20.7 ms: 1.56x faster                                                 |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.55x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.51 us: 1.54x faster                                                 |
| richards                 | 48.7 ms                                                | 31.7 ms: 1.54x faster                                                 |
| go                       | 151 ms                                                 | 98.1 ms: 1.54x faster                                                 |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| scimark_lu               | 103 ms                                                 | 67.9 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.5 ms: 1.51x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 187 us: 1.50x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.14 ms: 1.50x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.43x faster                                                 |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 50.6 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.8 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 68.1 ms: 1.39x faster                                                 |
| regex_compile            | 95.3 ms                                                | 69.2 ms: 1.38x faster                                                 |
| mako                     | 9.87 ms                                                | 7.20 ms: 1.37x faster                                                 |
| pycparser                | 877 ms                                                 | 640 ms: 1.37x faster                                                  |
| scimark_sor              | 128 ms                                                 | 93.6 ms: 1.37x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 145 us: 1.34x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.6 ms: 1.34x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 481 ms: 1.33x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 980 ms: 1.33x faster                                                  |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| thrift                   | 572 us                                                 | 432 us: 1.32x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 27.0 ms: 1.31x faster                                                 |
| django_template          | 26.4 ms                                                | 20.2 ms: 1.31x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 71.5 ms: 1.29x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.3 ms: 1.27x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.52 ms: 1.24x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.6 ms: 1.24x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.79 ms: 1.23x faster                                                 |
| genshi_text              | 17.3 ms                                                | 14.2 ms: 1.22x faster                                                 |
| sympy_str                | 165 ms                                                 | 135 ms: 1.22x faster                                                  |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 38.6 ms: 1.21x faster                                                 |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.4 ms: 1.19x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 448 us: 1.18x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.16x faster                                                  |
| sympy_expand             | 269 ms                                                 | 233 ms: 1.15x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 32.2 ms: 1.14x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.45 sec: 1.13x faster                                                |
| genshi_xml               | 33.8 ms                                                | 30.6 ms: 1.11x faster                                                 |
| sqlglot_normalize        | 190 ms                                                 | 173 ms: 1.10x faster                                                  |
| meteor_contest           | 77.7 ms                                                | 72.4 ms: 1.07x faster                                                 |
| json                     | 3.08 ms                                                | 2.96 ms: 1.04x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.6 ms: 1.04x faster                                                 |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| 2to3                     | 192 ms                                                 | 190 ms: 1.01x faster                                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.47 ms: 1.00x slower                                                 |
| xml_etree_generate       | 53.5 ms                                                | 54.0 ms: 1.01x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                                  |
| xml_etree_iterparse      | 72.1 ms                                                | 74.8 ms: 1.04x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 896 us: 1.04x slower                                                  |
| json_loads               | 16.4 us                                                | 17.2 us: 1.04x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.48 ms: 1.05x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.2 ms: 1.09x slower                                                 |
| async_generators         | 231 ms                                                 | 282 ms: 1.22x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.8 ms: 1.30x slower                                                 |
| telco                    | 3.49 ms                                                | 4.59 ms: 1.32x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.4 ms: 1.51x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.4 ms: 1.69x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-darwin-arm64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 0.87x