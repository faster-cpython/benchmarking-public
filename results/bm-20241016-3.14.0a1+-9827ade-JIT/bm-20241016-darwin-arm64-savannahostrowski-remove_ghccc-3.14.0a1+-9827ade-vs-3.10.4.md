# Results vs. 3.10.4

- fork: savannahostrowski
- ref: remove_ghccc
- machine: darwin-arm64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.234x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 182 ms: 1.05x faster                                                      |
| docutils       | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| html5lib       | 42.4 ms                                                | 33.8 ms: 1.25x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization  | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| async_tree_io           | 980 ms                                                 | 584 ms: 1.68x faster                                                      |
| async_tree_cpu_io_mixed | 649 ms                                                 | 458 ms: 1.42x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.73x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.2 ms: 1.47x faster                                                     |
| float          | 69.0 ms                                                | 47.7 ms: 1.45x faster                                                     |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 74.0 ms: 1.29x faster                                                     |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                      |
| regex_v8       | 17.1 ms                                                | 16.9 ms: 1.02x faster                                                     |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 179 us: 1.57x faster                                                      |
| unpickle_pure_python | 194 us                                                 | 132 us: 1.47x faster                                                      |
| tomli_loads          | 1.71 sec                                               | 1.23 sec: 1.39x faster                                                    |
| xml_etree_process    | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                     |
| json_dumps           | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                | 49.8 ms: 1.08x faster                                                     |
| json_loads           | 16.4 us                                                | 16.5 us: 1.00x slower                                                     |
| xml_etree_iterparse  | 72.1 ms                                                | 73.2 ms: 1.02x slower                                                     |
| unpickle             | 8.80 us                                                | 9.04 us: 1.03x slower                                                     |
| pickle               | 6.97 us                                                | 7.37 us: 1.06x slower                                                     |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                     |
| pickle_list          | 2.74 us                                                | 2.97 us: 1.08x slower                                                     |
| unpickle_list        | 2.69 us                                                | 2.97 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 19.0 ms: 1.75x slower                                                     |
| python_startup_no_site | 7.91 ms                                                | 14.7 ms: 1.86x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.80x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.30 ms: 1.57x faster                                                     |
| django_template | 26.4 ms                                                | 22.5 ms: 1.18x faster                                                     |
| genshi_text     | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                     |
| genshi_xml      | 33.8 ms                                                | 38.4 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 95.3 us: 3.39x faster                                                     |
| deepcopy_memo            | 34.7 us                                                | 16.8 us: 2.07x faster                                                     |
| deltablue                | 4.91 ms                                                | 2.42 ms: 2.03x faster                                                     |
| async_tree_none          | 388 ms                                                 | 200 ms: 1.94x faster                                                      |
| async_tree_memoization   | 474 ms                                                 | 246 ms: 1.93x faster                                                      |
| raytrace                 | 301 ms                                                 | 169 ms: 1.79x faster                                                      |
| deepcopy                 | 272 us                                                 | 155 us: 1.75x faster                                                      |
| asyncio_websockets       | 410 ms                                                 | 242 ms: 1.70x faster                                                      |
| async_tree_io            | 980 ms                                                 | 584 ms: 1.68x faster                                                      |
| logging_silent           | 117 ns                                                 | 70.7 ns: 1.66x faster                                                     |
| chaos                    | 65.8 ms                                                | 41.8 ms: 1.57x faster                                                     |
| pickle_pure_python       | 281 us                                                 | 179 us: 1.57x faster                                                      |
| mako                     | 9.87 ms                                                | 6.30 ms: 1.57x faster                                                     |
| scimark_lu               | 103 ms                                                 | 65.7 ms: 1.56x faster                                                     |
| go                       | 151 ms                                                 | 96.8 ms: 1.56x faster                                                     |
| scimark_sor              | 128 ms                                                 | 82.4 ms: 1.56x faster                                                     |
| deepcopy_reduce          | 2.33 us                                                | 1.53 us: 1.52x faster                                                     |
| richards_super           | 57.8 ms                                                | 38.3 ms: 1.51x faster                                                     |
| asyncio_tcp              | 659 ms                                                 | 443 ms: 1.49x faster                                                      |
| unpickle_pure_python     | 194 us                                                 | 132 us: 1.47x faster                                                      |
| nbody                    | 93.0 ms                                                | 63.2 ms: 1.47x faster                                                     |
| sqlglot_parse            | 1.24 ms                                                | 849 us: 1.46x faster                                                      |
| scimark_monte_carlo      | 65.6 ms                                                | 45.0 ms: 1.46x faster                                                     |
| float                    | 69.0 ms                                                | 47.7 ms: 1.45x faster                                                     |
| logging_simple           | 4.45 us                                                | 3.09 us: 1.44x faster                                                     |
| logging_format           | 4.83 us                                                | 3.37 us: 1.43x faster                                                     |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 458 ms: 1.42x faster                                                      |
| richards                 | 48.7 ms                                                | 34.5 ms: 1.41x faster                                                     |
| spectral_norm            | 94.8 ms                                                | 68.1 ms: 1.39x faster                                                     |
| tomli_loads              | 1.71 sec                                               | 1.23 sec: 1.39x faster                                                    |
| sqlglot_transpile        | 1.44 ms                                                | 1.04 ms: 1.39x faster                                                     |
| pprint_safe_repr         | 641 ms                                                 | 470 ms: 1.36x faster                                                      |
| xml_etree_process        | 46.5 ms                                                | 34.3 ms: 1.36x faster                                                     |
| pprint_pformat           | 1.30 sec                                               | 961 ms: 1.36x faster                                                      |
| crypto_pyaes             | 71.8 ms                                                | 53.1 ms: 1.35x faster                                                     |
| thrift                   | 572 us                                                 | 426 us: 1.34x faster                                                      |
| pyflate                  | 427 ms                                                 | 318 ms: 1.34x faster                                                      |
| pylint                   | 277 ms                                                 | 210 ms: 1.32x faster                                                      |
| comprehensions           | 16.9 us                                                | 13.0 us: 1.30x faster                                                     |
| pycparser                | 877 ms                                                 | 673 ms: 1.30x faster                                                      |
| regex_compile            | 95.3 ms                                                | 74.0 ms: 1.29x faster                                                     |
| generators               | 32.3 ms                                                | 25.2 ms: 1.28x faster                                                     |
| html5lib                 | 42.4 ms                                                | 33.8 ms: 1.25x faster                                                     |
| hexiom                   | 6.19 ms                                                | 4.95 ms: 1.25x faster                                                     |
| dulwich_log              | 35.3 ms                                                | 28.5 ms: 1.24x faster                                                     |
| coroutines               | 20.7 ms                                                | 16.7 ms: 1.24x faster                                                     |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.30 sec: 1.24x faster                                                    |
| scimark_fft              | 224 ms                                                 | 185 ms: 1.21x faster                                                      |
| django_template          | 26.4 ms                                                | 22.5 ms: 1.18x faster                                                     |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                      |
| sympy_sum                | 92.2 ms                                                | 79.2 ms: 1.16x faster                                                     |
| fannkuch                 | 303 ms                                                 | 265 ms: 1.14x faster                                                      |
| json_dumps               | 8.11 ms                                                | 7.23 ms: 1.12x faster                                                     |
| bench_thread_pool        | 527 us                                                 | 474 us: 1.11x faster                                                      |
| docutils                 | 1.73 sec                                               | 1.57 sec: 1.10x faster                                                    |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 3.11 ms: 1.10x faster                                                     |
| sympy_str                | 165 ms                                                 | 151 ms: 1.10x faster                                                      |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                     |
| sympy_expand             | 269 ms                                                 | 249 ms: 1.08x faster                                                      |
| xml_etree_generate       | 53.5 ms                                                | 49.8 ms: 1.08x faster                                                     |
| json                     | 3.08 ms                                                | 2.87 ms: 1.07x faster                                                     |
| nqueens                  | 63.8 ms                                                | 59.9 ms: 1.06x faster                                                     |
| meteor_contest           | 77.7 ms                                                | 73.1 ms: 1.06x faster                                                     |
| genshi_text              | 17.3 ms                                                | 16.3 ms: 1.06x faster                                                     |
| sympy_integrate          | 13.1 ms                                                | 12.5 ms: 1.05x faster                                                     |
| 2to3                     | 192 ms                                                 | 182 ms: 1.05x faster                                                      |
| mdp                      | 1.63 sec                                               | 1.56 sec: 1.04x faster                                                    |
| sqlglot_normalize        | 190 ms                                                 | 186 ms: 1.02x faster                                                      |
| regex_v8                 | 17.1 ms                                                | 16.9 ms: 1.02x faster                                                     |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                                      |
| sqlglot_optimize         | 36.8 ms                                                | 36.9 ms: 1.00x slower                                                     |
| json_loads               | 16.4 us                                                | 16.5 us: 1.00x slower                                                     |
| xml_etree_iterparse      | 72.1 ms                                                | 73.2 ms: 1.02x slower                                                     |
| unpickle                 | 8.80 us                                                | 9.04 us: 1.03x slower                                                     |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                     |
| pickle                   | 6.97 us                                                | 7.37 us: 1.06x slower                                                     |
| coverage                 | 41.5 ms                                                | 44.1 ms: 1.06x slower                                                     |
| regex_effbot             | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                     |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                     |
| pickle_list              | 2.74 us                                                | 2.97 us: 1.08x slower                                                     |
| unpickle_list            | 2.69 us                                                | 2.97 us: 1.10x slower                                                     |
| genshi_xml               | 33.8 ms                                                | 38.4 ms: 1.14x slower                                                     |
| gc_traversal             | 2.36 ms                                                | 2.95 ms: 1.25x slower                                                     |
| async_generators         | 231 ms                                                 | 295 ms: 1.27x slower                                                      |
| telco                    | 3.49 ms                                                | 4.55 ms: 1.31x slower                                                     |
| create_gc_cycles         | 860 us                                                 | 1.32 ms: 1.54x slower                                                     |
| unpack_sequence          | 39.0 ns                                                | 62.2 ns: 1.59x slower                                                     |
| bench_mp_pool            | 37.4 ms                                                | 61.7 ms: 1.65x slower                                                     |
| python_startup           | 10.9 ms                                                | 19.0 ms: 1.75x slower                                                     |
| python_startup_no_site   | 7.91 ms                                                | 14.7 ms: 1.86x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                              |

Benchmark hidden because not significant (2): tornado_http, xml_etree_parse
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.234x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.43x