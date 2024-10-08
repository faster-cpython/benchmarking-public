# Results vs. 3.10.4

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: darwin-arm64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 184 ms: 1.04x faster                                                  |
| docutils       | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| html5lib       | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 248 ms: 1.91x faster                                                  |
| async_tree_io           | 980 ms                                                 | 592 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 59.4 ms: 1.56x faster                                                 |
| float          | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| regex_dna      | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| regex_v8       | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| regex_effbot   | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.25x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| xml_etree_generate   | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| json_loads           | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 16.0 ms: 1.47x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.57x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.95 ms: 1.42x faster                                                 |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.0 us: 3.55x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 16.9 us: 2.05x faster                                                 |
| raytrace                 | 301 ms                                                 | 149 ms: 2.03x faster                                                  |
| async_tree_none          | 388 ms                                                 | 194 ms: 2.00x faster                                                  |
| logging_silent           | 117 ns                                                 | 61.0 ns: 1.92x faster                                                 |
| async_tree_memoization   | 474 ms                                                 | 248 ms: 1.91x faster                                                  |
| deepcopy                 | 272 us                                                 | 143 us: 1.90x faster                                                  |
| chaos                    | 65.8 ms                                                | 35.7 ms: 1.84x faster                                                 |
| richards_super           | 57.8 ms                                                | 33.3 ms: 1.74x faster                                                 |
| comprehensions           | 16.9 us                                                | 9.99 us: 1.69x faster                                                 |
| sqlglot_parse            | 1.24 ms                                                | 747 us: 1.66x faster                                                  |
| async_tree_io            | 980 ms                                                 | 592 ms: 1.65x faster                                                  |
| asyncio_tcp              | 659 ms                                                 | 403 ms: 1.64x faster                                                  |
| richards                 | 48.7 ms                                                | 30.4 ms: 1.60x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 904 us: 1.60x faster                                                  |
| generators               | 32.3 ms                                                | 20.5 ms: 1.57x faster                                                 |
| nbody                    | 93.0 ms                                                | 59.4 ms: 1.56x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.50 us: 1.55x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                                  |
| pylint                   | 277 ms                                                 | 182 ms: 1.52x faster                                                  |
| hexiom                   | 6.19 ms                                                | 4.07 ms: 1.52x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 43.2 ms: 1.52x faster                                                 |
| scimark_lu               | 103 ms                                                 | 68.1 ms: 1.51x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.09 us: 1.44x faster                                                 |
| logging_format           | 4.83 us                                                | 3.39 us: 1.42x faster                                                 |
| go                       | 151 ms                                                 | 106 ms: 1.42x faster                                                  |
| regex_compile            | 95.3 ms                                                | 66.9 ms: 1.42x faster                                                 |
| mako                     | 9.87 ms                                                | 6.95 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 451 ms: 1.42x faster                                                  |
| float                    | 69.0 ms                                                | 48.6 ms: 1.42x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.0 ms: 1.42x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                                  |
| crypto_pyaes             | 71.8 ms                                                | 51.1 ms: 1.41x faster                                                 |
| pprint_pformat           | 1.30 sec                                               | 928 ms: 1.41x faster                                                  |
| scimark_sor              | 128 ms                                                 | 92.8 ms: 1.38x faster                                                 |
| thrift                   | 572 us                                                 | 418 us: 1.37x faster                                                  |
| pycparser                | 877 ms                                                 | 641 ms: 1.37x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.2 ms: 1.36x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                  |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 69.0 ms: 1.34x faster                                                 |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                                  |
| dulwich_log              | 35.3 ms                                                | 26.9 ms: 1.31x faster                                                 |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.29x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.32 ms: 1.28x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.26x faster                                                  |
| genshi_text              | 17.3 ms                                                | 13.9 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.25x faster                                                 |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.78 ms: 1.23x faster                                                 |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| regex_dna                | 174 ms                                                 | 145 ms: 1.20x faster                                                  |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                 |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.47 sec: 1.18x faster                                                |
| sqlglot_optimize         | 36.8 ms                                                | 31.1 ms: 1.18x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 447 us: 1.18x faster                                                  |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.16x faster                                                  |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                |
| mdp                      | 1.63 sec                                               | 1.42 sec: 1.15x faster                                                |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 30.2 ms: 1.12x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 71.9 ms: 1.08x faster                                                 |
| pathlib                  | 24.5 ms                                                | 23.3 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                 |
| 2to3                     | 192 ms                                                 | 184 ms: 1.04x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 16.6 ms: 1.03x faster                                                 |
| xml_etree_generate       | 53.5 ms                                                | 53.1 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_effbot             | 2.46 ms                                                | 2.46 ms: 1.00x slower                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 74.1 ms: 1.03x slower                                                 |
| xml_etree_parse          | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| gc_traversal             | 2.36 ms                                                | 2.45 ms: 1.04x slower                                                 |
| json_loads               | 16.4 us                                                | 17.2 us: 1.05x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 903 us: 1.05x slower                                                  |
| coverage                 | 41.5 ms                                                | 44.6 ms: 1.07x slower                                                 |
| async_generators         | 231 ms                                                 | 285 ms: 1.23x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 48.3 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.72 ms: 1.35x slower                                                 |
| python_startup           | 10.9 ms                                                | 16.0 ms: 1.47x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 13.2 ms: 1.67x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): tornado_http, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240826-3.14.0a0-fe85a82/bm-20240826-darwin-arm64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.68x