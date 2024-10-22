# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: darwin-arm64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 0.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 162 ms: 1.18x faster                                                            |
| docutils       | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                          |
| html5lib       | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                           |
| tornado_http   | 86.7 ms                                                | 65.1 ms: 1.33x faster                                                           |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization  | 474 ms                                                 | 235 ms: 2.02x faster                                                            |
| async_tree_none         | 388 ms                                                 | 197 ms: 1.97x faster                                                            |
| async_tree_io           | 980 ms                                                 | 530 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 456 ms: 1.42x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 62.2 ms: 1.50x faster                                                           |
| float          | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                           |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                           |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                            |
| regex_v8       | 17.1 ms                                                | 17.7 ms: 1.03x slower                                                           |
| regex_effbot   | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 182 us: 1.55x faster                                                            |
| unpickle_pure_python | 194 us                                                 | 143 us: 1.36x faster                                                            |
| json_dumps           | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                           |
| xml_etree_process    | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                           |
| tomli_loads          | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                           |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                           |
| json_loads           | 16.4 us                                                | 17.0 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                           |
| python_startup_no_site | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                           |
| django_template | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                           |
| genshi_text     | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                           |
| genshi_xml      | 33.8 ms                                                | 30.8 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.7 us: 3.48x faster                                                           |
| deltablue                | 4.91 ms                                                | 2.09 ms: 2.35x faster                                                           |
| deepcopy_memo            | 34.7 us                                                | 16.7 us: 2.08x faster                                                           |
| raytrace                 | 301 ms                                                 | 146 ms: 2.06x faster                                                            |
| async_tree_memoization   | 474 ms                                                 | 235 ms: 2.02x faster                                                            |
| logging_silent           | 117 ns                                                 | 59.3 ns: 1.98x faster                                                           |
| async_tree_none          | 388 ms                                                 | 197 ms: 1.97x faster                                                            |
| chaos                    | 65.8 ms                                                | 34.8 ms: 1.89x faster                                                           |
| deepcopy                 | 272 us                                                 | 146 us: 1.86x faster                                                            |
| async_tree_io            | 980 ms                                                 | 530 ms: 1.85x faster                                                            |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.69x faster                                                           |
| sqlglot_parse            | 1.24 ms                                                | 741 us: 1.68x faster                                                            |
| sqlglot_transpile        | 1.44 ms                                                | 902 us: 1.60x faster                                                            |
| asyncio_tcp              | 659 ms                                                 | 421 ms: 1.57x faster                                                            |
| generators               | 32.3 ms                                                | 20.7 ms: 1.57x faster                                                           |
| richards                 | 48.7 ms                                                | 31.2 ms: 1.56x faster                                                           |
| comprehensions           | 16.9 us                                                | 10.9 us: 1.56x faster                                                           |
| deepcopy_reduce          | 2.33 us                                                | 1.49 us: 1.56x faster                                                           |
| pylint                   | 277 ms                                                 | 179 ms: 1.55x faster                                                            |
| pickle_pure_python       | 281 us                                                 | 182 us: 1.55x faster                                                            |
| scimark_monte_carlo      | 65.6 ms                                                | 42.7 ms: 1.54x faster                                                           |
| hexiom                   | 6.19 ms                                                | 4.11 ms: 1.51x faster                                                           |
| nbody                    | 93.0 ms                                                | 62.2 ms: 1.50x faster                                                           |
| scimark_lu               | 103 ms                                                 | 69.3 ms: 1.48x faster                                                           |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                           |
| logging_format           | 4.83 us                                                | 3.33 us: 1.45x faster                                                           |
| go                       | 151 ms                                                 | 104 ms: 1.44x faster                                                            |
| spectral_norm            | 94.8 ms                                                | 66.0 ms: 1.44x faster                                                           |
| float                    | 69.0 ms                                                | 48.3 ms: 1.43x faster                                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 456 ms: 1.42x faster                                                            |
| mako                     | 9.87 ms                                                | 6.93 ms: 1.42x faster                                                           |
| crypto_pyaes             | 71.8 ms                                                | 50.5 ms: 1.42x faster                                                           |
| regex_compile            | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                           |
| pprint_safe_repr         | 641 ms                                                 | 464 ms: 1.38x faster                                                            |
| pprint_pformat           | 1.30 sec                                               | 948 ms: 1.38x faster                                                            |
| pycparser                | 877 ms                                                 | 639 ms: 1.37x faster                                                            |
| unpickle_pure_python     | 194 us                                                 | 143 us: 1.36x faster                                                            |
| html5lib                 | 42.4 ms                                                | 31.5 ms: 1.35x faster                                                           |
| django_template          | 26.4 ms                                                | 19.7 ms: 1.34x faster                                                           |
| scimark_sor              | 128 ms                                                 | 96.1 ms: 1.33x faster                                                           |
| tornado_http             | 86.7 ms                                                | 65.1 ms: 1.33x faster                                                           |
| thrift                   | 572 us                                                 | 431 us: 1.33x faster                                                            |
| pyflate                  | 427 ms                                                 | 324 ms: 1.32x faster                                                            |
| sympy_sum                | 92.2 ms                                                | 70.0 ms: 1.32x faster                                                           |
| coroutines               | 20.7 ms                                                | 16.1 ms: 1.28x faster                                                           |
| json_dumps               | 8.11 ms                                                | 6.41 ms: 1.26x faster                                                           |
| sympy_integrate          | 13.1 ms                                                | 10.4 ms: 1.26x faster                                                           |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.27 sec: 1.26x faster                                                          |
| xml_etree_process        | 46.5 ms                                                | 37.2 ms: 1.25x faster                                                           |
| genshi_text              | 17.3 ms                                                | 14.0 ms: 1.24x faster                                                           |
| sympy_str                | 165 ms                                                 | 133 ms: 1.24x faster                                                            |
| scimark_fft              | 224 ms                                                 | 183 ms: 1.23x faster                                                            |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.80 ms: 1.22x faster                                                           |
| nqueens                  | 63.8 ms                                                | 53.8 ms: 1.19x faster                                                           |
| 2to3                     | 192 ms                                                 | 162 ms: 1.18x faster                                                            |
| sqlglot_optimize         | 36.8 ms                                                | 31.2 ms: 1.18x faster                                                           |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                            |
| sympy_expand             | 269 ms                                                 | 230 ms: 1.17x faster                                                            |
| docutils                 | 1.73 sec                                               | 1.48 sec: 1.17x faster                                                          |
| bench_thread_pool        | 527 us                                                 | 453 us: 1.16x faster                                                            |
| mdp                      | 1.63 sec                                               | 1.41 sec: 1.16x faster                                                          |
| tomli_loads              | 1.71 sec                                               | 1.48 sec: 1.15x faster                                                          |
| dask                     | 253 ms                                                 | 221 ms: 1.15x faster                                                            |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                            |
| fannkuch                 | 303 ms                                                 | 267 ms: 1.13x faster                                                            |
| genshi_xml               | 33.8 ms                                                | 30.8 ms: 1.10x faster                                                           |
| meteor_contest           | 77.7 ms                                                | 71.5 ms: 1.09x faster                                                           |
| pathlib                  | 24.5 ms                                                | 22.9 ms: 1.07x faster                                                           |
| json                     | 3.08 ms                                                | 2.95 ms: 1.05x faster                                                           |
| xml_etree_generate       | 53.5 ms                                                | 52.3 ms: 1.02x faster                                                           |
| xml_etree_parse          | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                            |
| asyncio_websockets       | 410 ms                                                 | 408 ms: 1.00x faster                                                            |
| xml_etree_iterparse      | 72.1 ms                                                | 72.8 ms: 1.01x slower                                                           |
| regex_v8                 | 17.1 ms                                                | 17.7 ms: 1.03x slower                                                           |
| json_loads               | 16.4 us                                                | 17.0 us: 1.03x slower                                                           |
| regex_effbot             | 2.46 ms                                                | 2.54 ms: 1.03x slower                                                           |
| create_gc_cycles         | 860 us                                                 | 893 us: 1.04x slower                                                            |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                           |
| coverage                 | 41.5 ms                                                | 44.7 ms: 1.08x slower                                                           |
| async_generators         | 231 ms                                                 | 280 ms: 1.21x slower                                                            |
| bench_mp_pool            | 37.4 ms                                                | 46.9 ms: 1.25x slower                                                           |
| telco                    | 3.49 ms                                                | 4.61 ms: 1.32x slower                                                           |
| python_startup           | 10.9 ms                                                | 14.9 ms: 1.37x slower                                                           |
| python_startup_no_site   | 7.91 ms                                                | 12.3 ms: 1.55x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 0.78x