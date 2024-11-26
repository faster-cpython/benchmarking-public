# Results vs. 3.10.4

- fork: faster-cpython
- ref: more_robust_immortal
- machine: darwin-arm64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.300x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.20x faster                                                            |
| docutils       | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                          |
| html5lib       | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                           |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 192 ms: 2.02x faster                                                            |
| async_tree_memoization  | 474 ms                                                 | 251 ms: 1.88x faster                                                            |
| async_tree_io           | 980 ms                                                 | 593 ms: 1.65x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 459 ms: 1.42x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 65.4 ms: 1.42x faster                                                           |
| float          | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 67.8 ms: 1.40x faster                                                           |
| regex_dna      | 174 ms                                                 | 148 ms: 1.18x faster                                                            |
| regex_v8       | 17.1 ms                                                | 16.7 ms: 1.02x faster                                                           |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 184 us: 1.53x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 142 us: 1.37x faster                                                            |
| json_dumps           | 8.11 ms                                                | 6.22 ms: 1.30x faster                                                           |
| xml_etree_process    | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                           |
| tomli_loads          | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                | 52.1 ms: 1.03x faster                                                           |
| json_loads           | 16.4 us                                                | 16.7 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 73.4 ms: 1.02x slower                                                           |
| unpickle             | 8.80 us                                                | 9.07 us: 1.03x slower                                                           |
| pickle               | 6.97 us                                                | 7.33 us: 1.05x slower                                                           |
| pickle_dict          | 17.0 us                                                | 18.1 us: 1.06x slower                                                           |
| pickle_list          | 2.74 us                                                | 2.96 us: 1.08x slower                                                           |
| unpickle_list        | 2.69 us                                                | 2.96 us: 1.10x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 14.2 ms: 1.79x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.67x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                           |
| django_template | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                           |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.27x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 29.8 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 93.1 us: 3.47x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.23 ms: 2.21x faster                                                           |
| deepcopy_memo            | 34.7 us                                                | 17.1 us: 2.03x faster                                                           |
| async_tree_none          | 388 ms                                                 | 192 ms: 2.02x faster                                                            |
| raytrace                 | 301 ms                                                 | 153 ms: 1.97x faster                                                            |
| logging_silent           | 117 ns                                                 | 60.5 ns: 1.94x faster                                                           |
| async_tree_memoization   | 474 ms                                                 | 251 ms: 1.88x faster                                                            |
| deepcopy                 | 272 us                                                 | 147 us: 1.85x faster                                                            |
| go                       | 151 ms                                                 | 81.6 ms: 1.85x faster                                                           |
| chaos                    | 65.8 ms                                                | 36.3 ms: 1.81x faster                                                           |
| asyncio_websockets       | 410 ms                                                 | 241 ms: 1.70x faster                                                            |
| sqlglot_parse            | 1.24 ms                                                | 737 us: 1.69x faster                                                            |
| richards_super           | 57.8 ms                                                | 34.4 ms: 1.68x faster                                                           |
| async_tree_io            | 980 ms                                                 | 593 ms: 1.65x faster                                                            |
| sqlglot_transpile        | 1.44 ms                                                | 896 us: 1.61x faster                                                            |
| generators               | 32.3 ms                                                | 20.3 ms: 1.60x faster                                                           |
| richards                 | 48.7 ms                                                | 31.2 ms: 1.56x faster                                                           |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                            |
| scimark_lu               | 103 ms                                                 | 66.9 ms: 1.54x faster                                                           |
| comprehensions           | 16.9 us                                                | 11.0 us: 1.54x faster                                                           |
| asyncio_tcp              | 659 ms                                                 | 430 ms: 1.53x faster                                                            |
| deepcopy_reduce          | 2.33 us                                                | 1.52 us: 1.53x faster                                                           |
| pickle_pure_python       | 281 us                                                 | 184 us: 1.53x faster                                                            |
| hexiom                   | 6.19 ms                                                | 4.14 ms: 1.50x faster                                                           |
| unpack_sequence          | 39.0 ns                                                | 26.4 ns: 1.48x faster                                                           |
| scimark_monte_carlo      | 65.6 ms                                                | 44.4 ms: 1.47x faster                                                           |
| logging_simple           | 4.45 us                                                | 3.05 us: 1.46x faster                                                           |
| logging_format           | 4.83 us                                                | 3.34 us: 1.45x faster                                                           |
| nbody                    | 93.0 ms                                                | 65.4 ms: 1.42x faster                                                           |
| mako                     | 9.87 ms                                                | 6.97 ms: 1.42x faster                                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 459 ms: 1.42x faster                                                            |
| float                    | 69.0 ms                                                | 48.9 ms: 1.41x faster                                                           |
| crypto_pyaes             | 71.8 ms                                                | 51.2 ms: 1.40x faster                                                           |
| regex_compile            | 95.3 ms                                                | 67.8 ms: 1.40x faster                                                           |
| pprint_safe_repr         | 641 ms                                                 | 457 ms: 1.40x faster                                                            |
| pprint_pformat           | 1.30 sec                                               | 940 ms: 1.39x faster                                                            |
| thrift                   | 572 us                                                 | 416 us: 1.38x faster                                                            |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                            |
| unpickle_pure_python     | 194 us                                                 | 142 us: 1.37x faster                                                            |
| spectral_norm            | 94.8 ms                                                | 70.2 ms: 1.35x faster                                                           |
| scimark_sor              | 128 ms                                                 | 95.1 ms: 1.35x faster                                                           |
| django_template          | 26.4 ms                                                | 19.9 ms: 1.33x faster                                                           |
| html5lib                 | 42.4 ms                                                | 32.0 ms: 1.32x faster                                                           |
| sympy_sum                | 92.2 ms                                                | 69.7 ms: 1.32x faster                                                           |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                                            |
| json_dumps               | 8.11 ms                                                | 6.22 ms: 1.30x faster                                                           |
| dulwich_log              | 35.3 ms                                                | 27.4 ms: 1.29x faster                                                           |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.27x faster                                                           |
| coroutines               | 20.7 ms                                                | 16.6 ms: 1.25x faster                                                           |
| xml_etree_process        | 46.5 ms                                                | 37.4 ms: 1.24x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                          |
| docutils                 | 1.73 sec                                               | 1.40 sec: 1.24x faster                                                          |
| sympy_str                | 165 ms                                                 | 134 ms: 1.24x faster                                                            |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.82 ms: 1.22x faster                                                           |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.20x faster                                                           |
| 2to3                     | 192 ms                                                 | 160 ms: 1.20x faster                                                            |
| sympy_expand             | 269 ms                                                 | 226 ms: 1.19x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 30.9 ms: 1.19x faster                                                           |
| regex_dna                | 174 ms                                                 | 148 ms: 1.18x faster                                                            |
| scimark_fft              | 224 ms                                                 | 191 ms: 1.18x faster                                                            |
| nqueens                  | 63.8 ms                                                | 54.4 ms: 1.17x faster                                                           |
| bench_thread_pool        | 527 us                                                 | 455 us: 1.16x faster                                                            |
| fannkuch                 | 303 ms                                                 | 262 ms: 1.15x faster                                                            |
| sqlglot_normalize        | 190 ms                                                 | 166 ms: 1.14x faster                                                            |
| tomli_loads              | 1.71 sec                                               | 1.49 sec: 1.14x faster                                                          |
| genshi_xml               | 33.8 ms                                                | 29.8 ms: 1.14x faster                                                           |
| mdp                      | 1.63 sec                                               | 1.46 sec: 1.12x faster                                                          |
| pathlib                  | 24.5 ms                                                | 21.9 ms: 1.12x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 70.5 ms: 1.10x faster                                                           |
| json                     | 3.08 ms                                                | 2.87 ms: 1.08x faster                                                           |
| xml_etree_generate       | 53.5 ms                                                | 52.1 ms: 1.03x faster                                                           |
| regex_v8                 | 17.1 ms                                                | 16.7 ms: 1.02x faster                                                           |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                            |
| json_loads               | 16.4 us                                                | 16.7 us: 1.02x slower                                                           |
| xml_etree_iterparse      | 72.1 ms                                                | 73.4 ms: 1.02x slower                                                           |
| unpickle                 | 8.80 us                                                | 9.07 us: 1.03x slower                                                           |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                                           |
| pickle                   | 6.97 us                                                | 7.33 us: 1.05x slower                                                           |
| gc_traversal             | 2.36 ms                                                | 2.49 ms: 1.05x slower                                                           |
| coverage                 | 41.5 ms                                                | 43.9 ms: 1.06x slower                                                           |
| pickle_dict              | 17.0 us                                                | 18.1 us: 1.06x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 918 us: 1.07x slower                                                            |
| regex_effbot             | 2.46 ms                                                | 2.63 ms: 1.07x slower                                                           |
| pickle_list              | 2.74 us                                                | 2.96 us: 1.08x slower                                                           |
| unpickle_list            | 2.69 us                                                | 2.96 us: 1.10x slower                                                           |
| async_generators         | 231 ms                                                 | 276 ms: 1.19x slower                                                            |
| bench_mp_pool            | 37.4 ms                                                | 49.3 ms: 1.32x slower                                                           |
| telco                    | 3.49 ms                                                | 4.64 ms: 1.33x slower                                                           |
| python_startup           | 10.9 ms                                                | 17.0 ms: 1.57x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 14.2 ms: 1.79x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                                    |

Benchmark hidden because not significant (2): tornado_http, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.300x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.78x