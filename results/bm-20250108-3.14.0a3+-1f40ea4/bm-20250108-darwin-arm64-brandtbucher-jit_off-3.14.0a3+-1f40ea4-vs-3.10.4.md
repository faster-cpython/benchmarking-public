# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_off
- machine: darwin-arm64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 160 ms: 1.19x faster                                            |
| docutils       | 1.73 sec                                               | 1.40 sec: 1.23x faster                                          |
| html5lib       | 42.4 ms                                                | 29.2 ms: 1.45x faster                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 980 ms                                                 | 365 ms: 2.69x faster                                            |
| async_tree_none         | 388 ms                                                 | 157 ms: 2.47x faster                                            |
| async_tree_memoization  | 474 ms                                                 | 197 ms: 2.41x faster                                            |
| async_tree_cpu_io_mixed | 649 ms                                                 | 415 ms: 1.57x faster                                            |
| Geometric mean          | (ref)                                                  | 2.24x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 69.0 ms                                                | 46.4 ms: 1.49x faster                                           |
| nbody          | 93.0 ms                                                | 70.0 ms: 1.33x faster                                           |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 66.8 ms: 1.43x faster                                           |
| regex_dna      | 174 ms                                                 | 138 ms: 1.27x faster                                            |
| regex_effbot   | 2.46 ms                                                | 2.05 ms: 1.20x faster                                           |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.09x faster                                           |
| Geometric mean | (ref)                                                  | 1.24x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                               | 1.19 sec: 1.44x faster                                          |
| unpickle_pure_python | 194 us                                                 | 137 us: 1.42x faster                                            |
| pickle_pure_python   | 281 us                                                 | 198 us: 1.42x faster                                            |
| xml_etree_process    | 46.5 ms                                                | 38.0 ms: 1.22x faster                                           |
| json_dumps           | 8.11 ms                                                | 7.28 ms: 1.11x faster                                           |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                            |
| xml_etree_generate   | 53.5 ms                                                | 52.4 ms: 1.02x faster                                           |
| xml_etree_iterparse  | 72.1 ms                                                | 71.6 ms: 1.01x faster                                           |
| json_loads           | 16.4 us                                                | 16.5 us: 1.00x slower                                           |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 18.8 ms: 1.73x slower                                           |
| python_startup_no_site | 7.91 ms                                                | 13.8 ms: 1.75x slower                                           |
| Geometric mean         | (ref)                                                  | 1.74x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 7.24 ms: 1.36x faster                                           |
| genshi_text     | 17.3 ms                                                | 13.5 ms: 1.28x faster                                           |
| django_template | 26.4 ms                                                | 20.9 ms: 1.26x faster                                           |
| genshi_xml      | 33.8 ms                                                | 28.3 ms: 1.20x faster                                           |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.8 us: 3.37x faster                                           |
| async_tree_io            | 980 ms                                                 | 365 ms: 2.69x faster                                            |
| async_tree_none          | 388 ms                                                 | 157 ms: 2.47x faster                                            |
| async_tree_memoization   | 474 ms                                                 | 197 ms: 2.41x faster                                            |
| deltablue                | 4.91 ms                                                | 2.34 ms: 2.10x faster                                           |
| deepcopy_memo            | 34.7 us                                                | 17.9 us: 1.94x faster                                           |
| go                       | 151 ms                                                 | 78.3 ms: 1.92x faster                                           |
| deepcopy                 | 272 us                                                 | 149 us: 1.82x faster                                            |
| logging_silent           | 117 ns                                                 | 65.0 ns: 1.80x faster                                           |
| raytrace                 | 301 ms                                                 | 168 ms: 1.79x faster                                            |
| pylint                   | 277 ms                                                 | 159 ms: 1.74x faster                                            |
| chaos                    | 65.8 ms                                                | 38.0 ms: 1.73x faster                                           |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                            |
| richards_super           | 57.8 ms                                                | 35.3 ms: 1.64x faster                                           |
| sqlglot_parse            | 1.24 ms                                                | 759 us: 1.64x faster                                            |
| scimark_sor              | 128 ms                                                 | 78.6 ms: 1.63x faster                                           |
| scimark_monte_carlo      | 65.6 ms                                                | 41.6 ms: 1.58x faster                                           |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 415 ms: 1.57x faster                                            |
| sqlglot_transpile        | 1.44 ms                                                | 926 us: 1.56x faster                                            |
| richards                 | 48.7 ms                                                | 31.6 ms: 1.54x faster                                           |
| spectral_norm            | 94.8 ms                                                | 61.6 ms: 1.54x faster                                           |
| deepcopy_reduce          | 2.33 us                                                | 1.56 us: 1.50x faster                                           |
| hexiom                   | 6.19 ms                                                | 4.14 ms: 1.49x faster                                           |
| float                    | 69.0 ms                                                | 46.4 ms: 1.49x faster                                           |
| pyflate                  | 427 ms                                                 | 290 ms: 1.47x faster                                            |
| html5lib                 | 42.4 ms                                                | 29.2 ms: 1.45x faster                                           |
| generators               | 32.3 ms                                                | 22.3 ms: 1.45x faster                                           |
| tomli_loads              | 1.71 sec                                               | 1.19 sec: 1.44x faster                                          |
| regex_compile            | 95.3 ms                                                | 66.8 ms: 1.43x faster                                           |
| pprint_pformat           | 1.30 sec                                               | 916 ms: 1.42x faster                                            |
| unpickle_pure_python     | 194 us                                                 | 137 us: 1.42x faster                                            |
| pickle_pure_python       | 281 us                                                 | 198 us: 1.42x faster                                            |
| scimark_lu               | 103 ms                                                 | 72.6 ms: 1.42x faster                                           |
| logging_simple           | 4.45 us                                                | 3.16 us: 1.41x faster                                           |
| pprint_safe_repr         | 641 ms                                                 | 455 ms: 1.41x faster                                            |
| logging_format           | 4.83 us                                                | 3.45 us: 1.40x faster                                           |
| pycparser                | 877 ms                                                 | 634 ms: 1.38x faster                                            |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.46 ms: 1.37x faster                                           |
| mako                     | 9.87 ms                                                | 7.24 ms: 1.36x faster                                           |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.36x faster                                           |
| crypto_pyaes             | 71.8 ms                                                | 52.8 ms: 1.36x faster                                           |
| nbody                    | 93.0 ms                                                | 70.0 ms: 1.33x faster                                           |
| thrift                   | 572 us                                                 | 432 us: 1.33x faster                                            |
| dulwich_log              | 35.3 ms                                                | 26.9 ms: 1.31x faster                                           |
| scimark_fft              | 224 ms                                                 | 171 ms: 1.31x faster                                            |
| coroutines               | 20.7 ms                                                | 15.8 ms: 1.31x faster                                           |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.65 ms: 1.29x faster                                           |
| genshi_text              | 17.3 ms                                                | 13.5 ms: 1.28x faster                                           |
| regex_dna                | 174 ms                                                 | 138 ms: 1.27x faster                                            |
| django_template          | 26.4 ms                                                | 20.9 ms: 1.26x faster                                           |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.3 ms: 1.26x faster                                           |
| sympy_sum                | 92.2 ms                                                | 73.5 ms: 1.25x faster                                           |
| docutils                 | 1.73 sec                                               | 1.40 sec: 1.23x faster                                          |
| xml_etree_process        | 46.5 ms                                                | 38.0 ms: 1.22x faster                                           |
| fannkuch                 | 303 ms                                                 | 248 ms: 1.22x faster                                            |
| regex_effbot             | 2.46 ms                                                | 2.05 ms: 1.20x faster                                           |
| genshi_xml               | 33.8 ms                                                | 28.3 ms: 1.20x faster                                           |
| 2to3                     | 192 ms                                                 | 160 ms: 1.19x faster                                            |
| sympy_str                | 165 ms                                                 | 138 ms: 1.19x faster                                            |
| sympy_integrate          | 13.1 ms                                                | 11.1 ms: 1.18x faster                                           |
| sympy_expand             | 269 ms                                                 | 234 ms: 1.15x faster                                            |
| nqueens                  | 63.8 ms                                                | 56.2 ms: 1.14x faster                                           |
| sqlglot_optimize         | 36.8 ms                                                | 32.5 ms: 1.13x faster                                           |
| json_dumps               | 8.11 ms                                                | 7.28 ms: 1.11x faster                                           |
| bench_thread_pool        | 527 us                                                 | 475 us: 1.11x faster                                            |
| mdp                      | 1.63 sec                                               | 1.48 sec: 1.10x faster                                          |
| pathlib                  | 24.5 ms                                                | 22.4 ms: 1.09x faster                                           |
| meteor_contest           | 77.7 ms                                                | 71.1 ms: 1.09x faster                                           |
| json                     | 3.08 ms                                                | 2.83 ms: 1.09x faster                                           |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.09x faster                                           |
| sqlglot_normalize        | 190 ms                                                 | 179 ms: 1.06x faster                                            |
| xml_etree_parse          | 108 ms                                                 | 103 ms: 1.05x faster                                            |
| xml_etree_generate       | 53.5 ms                                                | 52.4 ms: 1.02x faster                                           |
| xml_etree_iterparse      | 72.1 ms                                                | 71.6 ms: 1.01x faster                                           |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                            |
| json_loads               | 16.4 us                                                | 16.5 us: 1.00x slower                                           |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                           |
| coverage                 | 41.5 ms                                                | 45.9 ms: 1.11x slower                                           |
| async_generators         | 231 ms                                                 | 277 ms: 1.20x slower                                            |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.30x slower                                           |
| gc_traversal             | 2.36 ms                                                | 3.16 ms: 1.34x slower                                           |
| create_gc_cycles         | 860 us                                                 | 1.28 ms: 1.48x slower                                           |
| bench_mp_pool            | 37.4 ms                                                | 60.6 ms: 1.62x slower                                           |
| python_startup           | 10.9 ms                                                | 18.8 ms: 1.73x slower                                           |
| python_startup_no_site   | 7.91 ms                                                | 13.8 ms: 1.75x slower                                           |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20250108-3.14.0a3+-1f40ea4/bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.34x