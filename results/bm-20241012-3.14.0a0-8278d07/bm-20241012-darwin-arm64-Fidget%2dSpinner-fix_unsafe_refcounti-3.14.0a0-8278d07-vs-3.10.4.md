# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: darwin-arm64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.295x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 196 ms: 1.02x slower                                                            |
| docutils       | 1.73 sec                                               | 1.41 sec: 1.23x faster                                                          |
| html5lib       | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                           |
| tornado_http   | 86.7 ms                                                | 72.6 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 192 ms: 2.02x faster                                                            |
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.88x faster                                                            |
| async_tree_io           | 980 ms                                                 | 593 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 461 ms: 1.41x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.6 ms: 1.42x faster                                                           |
| float          | 69.0 ms                                                | 49.0 ms: 1.41x faster                                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                           |
| regex_dna      | 174 ms                                                 | 146 ms: 1.19x faster                                                            |
| regex_v8       | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                           |
| regex_effbot   | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 183 us: 1.53x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                            |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                           |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                          |
| json_dumps           | 8.11 ms                                                | 7.25 ms: 1.12x faster                                                           |
| xml_etree_generate   | 53.5 ms                                                | 52.4 ms: 1.02x faster                                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                           |
| unpickle             | 8.80 us                                                | 9.12 us: 1.04x slower                                                           |
| pickle               | 6.97 us                                                | 7.34 us: 1.05x slower                                                           |
| pickle_list          | 2.74 us                                                | 2.91 us: 1.06x slower                                                           |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| unpickle_list        | 2.69 us                                                | 2.99 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.0 ms: 1.75x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 15.9 ms: 2.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.87x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                           |
| django_template | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                           |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.27x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 29.9 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.9 us: 3.48x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.22 ms: 2.21x faster                                                           |
| async_tree_none          | 388 ms                                                 | 192 ms: 2.02x faster                                                            |
| deepcopy_memo            | 34.7 us                                                | 17.3 us: 2.01x faster                                                           |
| raytrace                 | 301 ms                                                 | 154 ms: 1.95x faster                                                            |
| logging_silent           | 117 ns                                                 | 60.6 ns: 1.93x faster                                                           |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.88x faster                                                            |
| deepcopy                 | 272 us                                                 | 147 us: 1.85x faster                                                            |
| go                       | 151 ms                                                 | 81.8 ms: 1.84x faster                                                           |
| chaos                    | 65.8 ms                                                | 37.4 ms: 1.76x faster                                                           |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                            |
| sqlglot_parse            | 1.24 ms                                                | 743 us: 1.67x faster                                                            |
| richards_super           | 57.8 ms                                                | 34.8 ms: 1.66x faster                                                           |
| async_tree_io            | 980 ms                                                 | 593 ms: 1.65x faster                                                            |
| sqlglot_transpile        | 1.44 ms                                                | 898 us: 1.61x faster                                                            |
| generators               | 32.3 ms                                                | 20.3 ms: 1.59x faster                                                           |
| richards                 | 48.7 ms                                                | 31.2 ms: 1.56x faster                                                           |
| pylint                   | 277 ms                                                 | 179 ms: 1.54x faster                                                            |
| scimark_lu               | 103 ms                                                 | 67.0 ms: 1.53x faster                                                           |
| comprehensions           | 16.9 us                                                | 11.0 us: 1.53x faster                                                           |
| pickle_pure_python       | 281 us                                                 | 183 us: 1.53x faster                                                            |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                                           |
| asyncio_tcp              | 659 ms                                                 | 439 ms: 1.50x faster                                                            |
| scimark_monte_carlo      | 65.6 ms                                                | 43.7 ms: 1.50x faster                                                           |
| hexiom                   | 6.19 ms                                                | 4.14 ms: 1.50x faster                                                           |
| unpack_sequence          | 39.0 ns                                                | 26.4 ns: 1.48x faster                                                           |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                           |
| logging_format           | 4.83 us                                                | 3.34 us: 1.44x faster                                                           |
| nbody                    | 93.0 ms                                                | 65.6 ms: 1.42x faster                                                           |
| mako                     | 9.87 ms                                                | 7.00 ms: 1.41x faster                                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 461 ms: 1.41x faster                                                            |
| float                    | 69.0 ms                                                | 49.0 ms: 1.41x faster                                                           |
| crypto_pyaes             | 71.8 ms                                                | 51.2 ms: 1.40x faster                                                           |
| regex_compile            | 95.3 ms                                                | 68.3 ms: 1.40x faster                                                           |
| pprint_safe_repr         | 641 ms                                                 | 461 ms: 1.39x faster                                                            |
| pprint_pformat           | 1.30 sec                                               | 943 ms: 1.38x faster                                                            |
| pycparser                | 877 ms                                                 | 638 ms: 1.37x faster                                                            |
| thrift                   | 572 us                                                 | 419 us: 1.37x faster                                                            |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                            |
| spectral_norm            | 94.8 ms                                                | 70.8 ms: 1.34x faster                                                           |
| scimark_sor              | 128 ms                                                 | 95.9 ms: 1.34x faster                                                           |
| sympy_sum                | 92.2 ms                                                | 69.3 ms: 1.33x faster                                                           |
| html5lib                 | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                           |
| django_template          | 26.4 ms                                                | 20.0 ms: 1.32x faster                                                           |
| pyflate                  | 427 ms                                                 | 327 ms: 1.30x faster                                                            |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                           |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.27x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                          |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                           |
| coroutines               | 20.7 ms                                                | 16.7 ms: 1.24x faster                                                           |
| sympy_str                | 165 ms                                                 | 133 ms: 1.24x faster                                                            |
| docutils                 | 1.73 sec                                               | 1.41 sec: 1.23x faster                                                          |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.82 ms: 1.22x faster                                                           |
| tornado_http             | 86.7 ms                                                | 72.6 ms: 1.19x faster                                                           |
| sympy_expand             | 269 ms                                                 | 225 ms: 1.19x faster                                                            |
| sympy_integrate          | 13.1 ms                                                | 11.0 ms: 1.19x faster                                                           |
| regex_dna                | 174 ms                                                 | 146 ms: 1.19x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                           |
| scimark_fft              | 224 ms                                                 | 190 ms: 1.18x faster                                                            |
| nqueens                  | 63.8 ms                                                | 54.2 ms: 1.18x faster                                                           |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                                            |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                                            |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                          |
| fannkuch                 | 303 ms                                                 | 266 ms: 1.14x faster                                                            |
| genshi_xml               | 33.8 ms                                                | 29.9 ms: 1.13x faster                                                           |
| json_dumps               | 8.11 ms                                                | 7.25 ms: 1.12x faster                                                           |
| mdp                      | 1.63 sec                                               | 1.47 sec: 1.11x faster                                                          |
| pathlib                  | 24.5 ms                                                | 22.0 ms: 1.11x faster                                                           |
| json                     | 3.08 ms                                                | 2.82 ms: 1.09x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                                           |
| regex_v8                 | 17.1 ms                                                | 16.5 ms: 1.04x faster                                                           |
| xml_etree_generate       | 53.5 ms                                                | 52.4 ms: 1.02x faster                                                           |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| xml_etree_iterparse      | 72.1 ms                                                | 73.1 ms: 1.01x slower                                                           |
| 2to3                     | 192 ms                                                 | 196 ms: 1.02x slower                                                            |
| unpickle                 | 8.80 us                                                | 9.12 us: 1.04x slower                                                           |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                                           |
| coverage                 | 41.5 ms                                                | 43.6 ms: 1.05x slower                                                           |
| pickle                   | 6.97 us                                                | 7.34 us: 1.05x slower                                                           |
| regex_effbot             | 2.46 ms                                                | 2.60 ms: 1.06x slower                                                           |
| gc_traversal             | 2.36 ms                                                | 2.50 ms: 1.06x slower                                                           |
| pickle_list              | 2.74 us                                                | 2.91 us: 1.06x slower                                                           |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 929 us: 1.08x slower                                                            |
| unpickle_list            | 2.69 us                                                | 2.99 us: 1.11x slower                                                           |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                            |
| telco                    | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                           |
| bench_mp_pool            | 37.4 ms                                                | 50.5 ms: 1.35x slower                                                           |
| python_startup           | 10.9 ms                                                | 19.0 ms: 1.75x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 15.9 ms: 2.01x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-darwin-arm64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.295x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 0.68x