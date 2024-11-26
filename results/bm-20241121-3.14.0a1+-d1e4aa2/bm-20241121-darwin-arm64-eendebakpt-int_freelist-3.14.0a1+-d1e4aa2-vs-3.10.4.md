# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: darwin-arm64
- commit hash: d1e4aa2
- commit date: 2024-11-21
- overall geometric mean: 1.255x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 168 ms: 1.14x faster                                               |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.20x faster                                             |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                              |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 203 ms: 1.91x faster                                               |
| async_tree_memoization  | 474 ms                                                 | 250 ms: 1.90x faster                                               |
| async_tree_io           | 980 ms                                                 | 582 ms: 1.68x faster                                               |
| async_tree_cpu_io_mixed | 649 ms                                                 | 468 ms: 1.39x faster                                               |
| Geometric mean          | (ref)                                                  | 1.71x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 68.2 ms: 1.36x faster                                              |
| float          | 69.0 ms                                                | 52.5 ms: 1.31x faster                                              |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.21x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 70.6 ms: 1.35x faster                                              |
| regex_dna      | 174 ms                                                 | 135 ms: 1.29x faster                                               |
| regex_v8       | 17.1 ms                                                | 15.8 ms: 1.09x faster                                              |
| regex_effbot   | 2.46 ms                                                | 2.29 ms: 1.07x faster                                              |
| Geometric mean | (ref)                                                  | 1.19x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 207 us: 1.36x faster                                               |
| unpickle_pure_python | 194 us                                                 | 153 us: 1.27x faster                                               |
| xml_etree_process    | 46.5 ms                                                | 39.5 ms: 1.18x faster                                              |
| tomli_loads          | 1.71 sec                                               | 1.47 sec: 1.16x faster                                             |
| json_dumps           | 8.11 ms                                                | 7.29 ms: 1.11x faster                                              |
| json_loads           | 16.4 us                                                | 16.6 us: 1.01x slower                                              |
| xml_etree_generate   | 53.5 ms                                                | 54.2 ms: 1.01x slower                                              |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                               |
| xml_etree_iterparse  | 72.1 ms                                                | 76.6 ms: 1.06x slower                                              |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 7.91 ms                                                | 13.9 ms: 1.75x slower                                              |
| python_startup         | 10.9 ms                                                | 19.4 ms: 1.79x slower                                              |
| Geometric mean         | (ref)                                                  | 1.77x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.92 ms: 1.43x faster                                              |
| django_template | 26.4 ms                                                | 20.9 ms: 1.26x faster                                              |
| genshi_text     | 17.3 ms                                                | 14.4 ms: 1.20x faster                                              |
| genshi_xml      | 33.8 ms                                                | 30.8 ms: 1.10x faster                                              |
| Geometric mean  | (ref)                                                  | 1.24x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 97.8 us: 3.30x faster                                              |
| deltablue                | 4.91 ms                                                | 2.45 ms: 2.01x faster                                              |
| async_tree_none          | 388 ms                                                 | 203 ms: 1.91x faster                                               |
| async_tree_memoization   | 474 ms                                                 | 250 ms: 1.90x faster                                               |
| deepcopy_memo            | 34.7 us                                                | 18.4 us: 1.89x faster                                              |
| raytrace                 | 301 ms                                                 | 169 ms: 1.79x faster                                               |
| deepcopy                 | 272 us                                                 | 154 us: 1.77x faster                                               |
| go                       | 151 ms                                                 | 87.3 ms: 1.73x faster                                              |
| logging_silent           | 117 ns                                                 | 67.9 ns: 1.73x faster                                              |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.69x faster                                               |
| async_tree_io            | 980 ms                                                 | 582 ms: 1.68x faster                                               |
| chaos                    | 65.8 ms                                                | 40.5 ms: 1.62x faster                                              |
| sqlglot_parse            | 1.24 ms                                                | 794 us: 1.57x faster                                               |
| richards_super           | 57.8 ms                                                | 37.2 ms: 1.55x faster                                              |
| spectral_norm            | 94.8 ms                                                | 62.1 ms: 1.53x faster                                              |
| sqlglot_transpile        | 1.44 ms                                                | 966 us: 1.49x faster                                               |
| pylint                   | 277 ms                                                 | 187 ms: 1.48x faster                                               |
| deepcopy_reduce          | 2.33 us                                                | 1.60 us: 1.46x faster                                              |
| scimark_monte_carlo      | 65.6 ms                                                | 45.3 ms: 1.45x faster                                              |
| richards                 | 48.7 ms                                                | 33.7 ms: 1.44x faster                                              |
| generators               | 32.3 ms                                                | 22.5 ms: 1.44x faster                                              |
| mako                     | 9.87 ms                                                | 6.92 ms: 1.43x faster                                              |
| scimark_lu               | 103 ms                                                 | 73.7 ms: 1.40x faster                                              |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 468 ms: 1.39x faster                                               |
| hexiom                   | 6.19 ms                                                | 4.47 ms: 1.39x faster                                              |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                              |
| logging_simple           | 4.45 us                                                | 3.26 us: 1.37x faster                                              |
| nbody                    | 93.0 ms                                                | 68.2 ms: 1.36x faster                                              |
| comprehensions           | 16.9 us                                                | 12.4 us: 1.36x faster                                              |
| sqlalchemy_imperative    | 8.86 ms                                                | 6.52 ms: 1.36x faster                                              |
| pickle_pure_python       | 281 us                                                 | 207 us: 1.36x faster                                               |
| logging_format           | 4.83 us                                                | 3.58 us: 1.35x faster                                              |
| regex_compile            | 95.3 ms                                                | 70.6 ms: 1.35x faster                                              |
| scimark_sor              | 128 ms                                                 | 95.4 ms: 1.34x faster                                              |
| pycparser                | 877 ms                                                 | 655 ms: 1.34x faster                                               |
| pprint_pformat           | 1.30 sec                                               | 980 ms: 1.33x faster                                               |
| pprint_safe_repr         | 641 ms                                                 | 482 ms: 1.33x faster                                               |
| crypto_pyaes             | 71.8 ms                                                | 54.1 ms: 1.33x faster                                              |
| float                    | 69.0 ms                                                | 52.5 ms: 1.31x faster                                              |
| thrift                   | 572 us                                                 | 436 us: 1.31x faster                                               |
| pyflate                  | 427 ms                                                 | 326 ms: 1.31x faster                                               |
| scimark_fft              | 224 ms                                                 | 173 ms: 1.29x faster                                               |
| regex_dna                | 174 ms                                                 | 135 ms: 1.29x faster                                               |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.67 ms: 1.28x faster                                              |
| dulwich_log              | 35.3 ms                                                | 27.8 ms: 1.27x faster                                              |
| unpickle_pure_python     | 194 us                                                 | 153 us: 1.27x faster                                               |
| sympy_sum                | 92.2 ms                                                | 72.7 ms: 1.27x faster                                              |
| django_template          | 26.4 ms                                                | 20.9 ms: 1.26x faster                                              |
| sqlalchemy_declarative   | 73.3 ms                                                | 58.5 ms: 1.25x faster                                              |
| genshi_text              | 17.3 ms                                                | 14.4 ms: 1.20x faster                                              |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.20x faster                                             |
| coroutines               | 20.7 ms                                                | 17.4 ms: 1.19x faster                                              |
| sympy_str                | 165 ms                                                 | 140 ms: 1.18x faster                                               |
| xml_etree_process        | 46.5 ms                                                | 39.5 ms: 1.18x faster                                              |
| tomli_loads              | 1.71 sec                                               | 1.47 sec: 1.16x faster                                             |
| sympy_integrate          | 13.1 ms                                                | 11.5 ms: 1.14x faster                                              |
| 2to3                     | 192 ms                                                 | 168 ms: 1.14x faster                                               |
| sympy_expand             | 269 ms                                                 | 235 ms: 1.14x faster                                               |
| fannkuch                 | 303 ms                                                 | 268 ms: 1.13x faster                                               |
| bench_thread_pool        | 527 us                                                 | 473 us: 1.12x faster                                               |
| json_dumps               | 8.11 ms                                                | 7.29 ms: 1.11x faster                                              |
| nqueens                  | 63.8 ms                                                | 57.4 ms: 1.11x faster                                              |
| pathlib                  | 24.5 ms                                                | 22.1 ms: 1.11x faster                                              |
| sqlglot_optimize         | 36.8 ms                                                | 33.2 ms: 1.11x faster                                              |
| genshi_xml               | 33.8 ms                                                | 30.8 ms: 1.10x faster                                              |
| regex_v8                 | 17.1 ms                                                | 15.8 ms: 1.09x faster                                              |
| mdp                      | 1.63 sec                                               | 1.51 sec: 1.08x faster                                             |
| sqlglot_normalize        | 190 ms                                                 | 177 ms: 1.07x faster                                               |
| regex_effbot             | 2.46 ms                                                | 2.29 ms: 1.07x faster                                              |
| meteor_contest           | 77.7 ms                                                | 72.7 ms: 1.07x faster                                              |
| json                     | 3.08 ms                                                | 2.89 ms: 1.07x faster                                              |
| pidigits                 | 282 ms                                                 | 284 ms: 1.01x slower                                               |
| json_loads               | 16.4 us                                                | 16.6 us: 1.01x slower                                              |
| xml_etree_generate       | 53.5 ms                                                | 54.2 ms: 1.01x slower                                              |
| xml_etree_parse          | 108 ms                                                 | 110 ms: 1.02x slower                                               |
| sqlite_synth             | 1.46 us                                                | 1.52 us: 1.04x slower                                              |
| xml_etree_iterparse      | 72.1 ms                                                | 76.6 ms: 1.06x slower                                              |
| coverage                 | 41.5 ms                                                | 44.2 ms: 1.07x slower                                              |
| async_generators         | 231 ms                                                 | 281 ms: 1.22x slower                                               |
| gc_traversal             | 2.36 ms                                                | 2.92 ms: 1.23x slower                                              |
| telco                    | 3.49 ms                                                | 4.53 ms: 1.30x slower                                              |
| create_gc_cycles         | 860 us                                                 | 1.30 ms: 1.51x slower                                              |
| bench_mp_pool            | 37.4 ms                                                | 60.9 ms: 1.63x slower                                              |
| python_startup_no_site   | 7.91 ms                                                | 13.9 ms: 1.75x slower                                              |
| python_startup           | 10.9 ms                                                | 19.4 ms: 1.79x slower                                              |
| Geometric mean           | (ref)                                                  | 1.25x faster                                                       |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (19) of results/bm-20241121-3.14.0a1+-d1e4aa2/bm-20241121-darwin-arm64-eendebakpt-int_freelist-3.14.0a1+-d1e4aa2.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.255x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.33x