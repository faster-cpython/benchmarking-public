# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc1
- machine: darwin-arm64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.65x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                         |
| chameleon      | 6.26 ms                                                | 4.36 ms: 1.43x faster                                        |
| docutils       | 1.73 sec                                               | 1.45 sec: 1.19x faster                                       |
| html5lib       | 42.4 ms                                                | 31.7 ms: 1.34x faster                                        |
| tornado_http   | 86.7 ms                                                | 67.3 ms: 1.29x faster                                        |
| Geometric mean | (ref)                                                  | 1.29x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 210 ms: 1.85x faster                                         |
| async_tree_memoization  | 474 ms                                                 | 260 ms: 1.82x faster                                         |
| async_tree_io           | 980 ms                                                 | 555 ms: 1.76x faster                                         |
| async_tree_cpu_io_mixed | 649 ms                                                 | 468 ms: 1.39x faster                                         |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.6 ms: 1.53x faster                                        |
| float          | 69.0 ms                                                | 48.5 ms: 1.42x faster                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 69.3 ms: 1.38x faster                                        |
| regex_dna      | 174 ms                                                 | 151 ms: 1.16x faster                                         |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                        |
| regex_effbot   | 2.46 ms                                                | 2.59 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.54x faster                                         |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                         |
| json_dumps           | 8.11 ms                                                | 6.22 ms: 1.30x faster                                        |
| xml_etree_process    | 46.5 ms                                                | 38.0 ms: 1.22x faster                                        |
| tomli_loads          | 1.71 sec                                               | 1.46 sec: 1.17x faster                                       |
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| xml_etree_generate   | 53.5 ms                                                | 53.2 ms: 1.00x faster                                        |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.4 ms: 1.41x slower                                        |
| python_startup_no_site | 7.91 ms                                                | 12.7 ms: 1.60x slower                                        |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.23 ms: 1.37x faster                                        |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                        |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                        |
| genshi_xml      | 33.8 ms                                                | 30.1 ms: 1.12x faster                                        |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 88.5 us: 3.65x faster                                        |
| deltablue                | 4.91 ms                                                | 2.15 ms: 2.28x faster                                        |
| raytrace                 | 301 ms                                                 | 148 ms: 2.03x faster                                         |
| logging_silent           | 117 ns                                                 | 60.9 ns: 1.92x faster                                        |
| chaos                    | 65.8 ms                                                | 34.5 ms: 1.91x faster                                        |
| async_tree_none          | 388 ms                                                 | 210 ms: 1.85x faster                                         |
| async_tree_memoization   | 474 ms                                                 | 260 ms: 1.82x faster                                         |
| async_tree_io            | 980 ms                                                 | 555 ms: 1.76x faster                                         |
| sqlglot_parse            | 1.24 ms                                                | 741 us: 1.68x faster                                         |
| richards_super           | 57.8 ms                                                | 34.7 ms: 1.67x faster                                        |
| sqlglot_transpile        | 1.44 ms                                                | 904 us: 1.60x faster                                         |
| comprehensions           | 16.9 us                                                | 10.6 us: 1.60x faster                                        |
| asyncio_tcp              | 659 ms                                                 | 414 ms: 1.59x faster                                         |
| pylint                   | 277 ms                                                 | 178 ms: 1.56x faster                                         |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.54x faster                                         |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                        |
| nbody                    | 93.0 ms                                                | 60.6 ms: 1.53x faster                                        |
| scimark_monte_carlo      | 65.6 ms                                                | 42.9 ms: 1.53x faster                                        |
| scimark_lu               | 103 ms                                                 | 67.9 ms: 1.51x faster                                        |
| hexiom                   | 6.19 ms                                                | 4.10 ms: 1.51x faster                                        |
| go                       | 151 ms                                                 | 101 ms: 1.50x faster                                         |
| deepcopy_memo            | 34.7 us                                                | 23.2 us: 1.49x faster                                        |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                        |
| crypto_pyaes             | 71.8 ms                                                | 50.0 ms: 1.44x faster                                        |
| logging_simple           | 4.45 us                                                | 3.10 us: 1.44x faster                                        |
| chameleon                | 6.26 ms                                                | 4.36 ms: 1.43x faster                                        |
| float                    | 69.0 ms                                                | 48.5 ms: 1.42x faster                                        |
| generators               | 32.3 ms                                                | 22.9 ms: 1.41x faster                                        |
| spectral_norm            | 94.8 ms                                                | 67.4 ms: 1.41x faster                                        |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 468 ms: 1.39x faster                                         |
| regex_compile            | 95.3 ms                                                | 69.3 ms: 1.38x faster                                        |
| pycparser                | 877 ms                                                 | 638 ms: 1.37x faster                                         |
| pprint_pformat           | 1.30 sec                                               | 953 ms: 1.37x faster                                         |
| mako                     | 9.87 ms                                                | 7.23 ms: 1.37x faster                                        |
| pprint_safe_repr         | 641 ms                                                 | 469 ms: 1.36x faster                                         |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                         |
| scimark_sor              | 128 ms                                                 | 95.2 ms: 1.35x faster                                        |
| html5lib                 | 42.4 ms                                                | 31.7 ms: 1.34x faster                                        |
| mypy2                    | 607 ms                                                 | 455 ms: 1.34x faster                                         |
| pyflate                  | 427 ms                                                 | 321 ms: 1.33x faster                                         |
| deepcopy                 | 272 us                                                 | 205 us: 1.32x faster                                         |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                        |
| thrift                   | 572 us                                                 | 435 us: 1.32x faster                                         |
| sympy_sum                | 92.2 ms                                                | 70.2 ms: 1.31x faster                                        |
| json_dumps               | 8.11 ms                                                | 6.22 ms: 1.30x faster                                        |
| dulwich_log              | 35.3 ms                                                | 27.3 ms: 1.29x faster                                        |
| coroutines               | 20.7 ms                                                | 16.0 ms: 1.29x faster                                        |
| tornado_http             | 86.7 ms                                                | 67.3 ms: 1.29x faster                                        |
| deepcopy_reduce          | 2.33 us                                                | 1.83 us: 1.27x faster                                        |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.27x faster                                       |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                        |
| sympy_str                | 165 ms                                                 | 133 ms: 1.25x faster                                         |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                        |
| xml_etree_process        | 46.5 ms                                                | 38.0 ms: 1.22x faster                                        |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                         |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.84 ms: 1.21x faster                                        |
| nqueens                  | 63.8 ms                                                | 53.3 ms: 1.20x faster                                        |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                         |
| fannkuch                 | 303 ms                                                 | 254 ms: 1.19x faster                                         |
| docutils                 | 1.73 sec                                               | 1.45 sec: 1.19x faster                                       |
| sympy_expand             | 269 ms                                                 | 228 ms: 1.18x faster                                         |
| sqlglot_optimize         | 36.8 ms                                                | 31.3 ms: 1.18x faster                                        |
| tomli_loads              | 1.71 sec                                               | 1.46 sec: 1.17x faster                                       |
| regex_dna                | 174 ms                                                 | 151 ms: 1.16x faster                                         |
| dask                     | 253 ms                                                 | 220 ms: 1.15x faster                                         |
| mdp                      | 1.63 sec                                               | 1.43 sec: 1.14x faster                                       |
| bench_thread_pool        | 527 us                                                 | 463 us: 1.14x faster                                         |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                         |
| genshi_xml               | 33.8 ms                                                | 30.1 ms: 1.12x faster                                        |
| meteor_contest           | 77.7 ms                                                | 70.4 ms: 1.10x faster                                        |
| json                     | 3.08 ms                                                | 2.90 ms: 1.06x faster                                        |
| pathlib                  | 24.5 ms                                                | 23.8 ms: 1.03x faster                                        |
| xml_etree_parse          | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| xml_etree_generate       | 53.5 ms                                                | 53.2 ms: 1.00x faster                                        |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                        |
| create_gc_cycles         | 860 us                                                 | 880 us: 1.02x slower                                         |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                        |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                        |
| regex_effbot             | 2.46 ms                                                | 2.59 ms: 1.05x slower                                        |
| coverage                 | 41.5 ms                                                | 45.0 ms: 1.09x slower                                        |
| async_generators         | 231 ms                                                 | 283 ms: 1.22x slower                                         |
| bench_mp_pool            | 37.4 ms                                                | 47.9 ms: 1.28x slower                                        |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                        |
| python_startup           | 10.9 ms                                                | 15.4 ms: 1.41x slower                                        |
| python_startup_no_site   | 7.91 ms                                                | 12.7 ms: 1.60x slower                                        |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_iterparse, pidigits
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-darwin-arm64-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.291x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.65x