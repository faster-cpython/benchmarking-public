# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| chameleon      | 6.26 ms                                                | 4.45 ms: 1.41x faster                                                 |
| docutils       | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| html5lib       | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 212 ms: 1.83x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_io           | 980 ms                                                 | 567 ms: 1.73x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 470 ms: 1.38x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.68x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| float          | 69.0 ms                                                | 47.5 ms: 1.45x faster                                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 72.5 ms: 1.31x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 172 us: 1.63x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 131 us: 1.49x faster                                                  |
| tomli_loads          | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| json_dumps           | 8.11 ms                                                | 6.10 ms: 1.33x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 50.8 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.1 ms: 1.02x faster                                                 |
| json_loads           | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| pickle_list          | 2.74 us                                                | 2.92 us: 1.07x slower                                                 |
| unpickle             | 8.80 us                                                | 9.39 us: 1.07x slower                                                 |
| pickle               | 6.97 us                                                | 7.48 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.38 ms: 1.55x faster                                                 |
| django_template | 26.4 ms                                                | 21.0 ms: 1.26x faster                                                 |
| genshi_text     | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 40.4 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 92.5 us: 3.49x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.48 ms: 1.98x faster                                                 |
| logging_silent           | 117 ns                                                 | 62.1 ns: 1.89x faster                                                 |
| raytrace                 | 301 ms                                                 | 161 ms: 1.87x faster                                                  |
| async_tree_none          | 388 ms                                                 | 212 ms: 1.83x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_io            | 980 ms                                                 | 567 ms: 1.73x faster                                                  |
| chaos                    | 65.8 ms                                                | 39.2 ms: 1.68x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 172 us: 1.63x faster                                                  |
| deepcopy_memo            | 34.7 us                                                | 21.5 us: 1.62x faster                                                 |
| richards_super           | 57.8 ms                                                | 36.2 ms: 1.60x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 424 ms: 1.55x faster                                                  |
| mako                     | 9.87 ms                                                | 6.38 ms: 1.55x faster                                                 |
| richards                 | 48.7 ms                                                | 32.2 ms: 1.51x faster                                                 |
| pylint                   | 277 ms                                                 | 183 ms: 1.51x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 833 us: 1.49x faster                                                  |
| unpickle_pure_python     | 194 us                                                 | 131 us: 1.49x faster                                                  |
| scimark_monte_carlo      | 65.6 ms                                                | 44.3 ms: 1.48x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.03 us: 1.47x faster                                                 |
| nbody                    | 93.0 ms                                                | 63.5 ms: 1.46x faster                                                 |
| go                       | 151 ms                                                 | 103 ms: 1.46x faster                                                  |
| logging_format           | 4.83 us                                                | 3.31 us: 1.46x faster                                                 |
| float                    | 69.0 ms                                                | 47.5 ms: 1.45x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 1.01 ms: 1.43x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                 |
| chameleon                | 6.26 ms                                                | 4.45 ms: 1.41x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.43 ms: 1.40x faster                                                 |
| generators               | 32.3 ms                                                | 23.2 ms: 1.40x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 51.9 ms: 1.38x faster                                                 |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 470 ms: 1.38x faster                                                  |
| comprehensions           | 16.9 us                                                | 12.3 us: 1.38x faster                                                 |
| pprint_safe_repr         | 641 ms                                                 | 466 ms: 1.38x faster                                                  |
| html5lib                 | 42.4 ms                                                | 30.9 ms: 1.37x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.25 sec: 1.37x faster                                                |
| pprint_pformat           | 1.30 sec                                               | 955 ms: 1.36x faster                                                  |
| pyflate                  | 427 ms                                                 | 314 ms: 1.36x faster                                                  |
| json_dumps               | 8.11 ms                                                | 6.10 ms: 1.33x faster                                                 |
| deepcopy                 | 272 us                                                 | 204 us: 1.33x faster                                                  |
| xml_etree_process        | 46.5 ms                                                | 35.3 ms: 1.32x faster                                                 |
| thrift                   | 572 us                                                 | 434 us: 1.32x faster                                                  |
| regex_compile            | 95.3 ms                                                | 72.5 ms: 1.31x faster                                                 |
| scimark_lu               | 103 ms                                                 | 78.6 ms: 1.31x faster                                                 |
| pycparser                | 877 ms                                                 | 671 ms: 1.31x faster                                                  |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.81 us: 1.29x faster                                                 |
| fannkuch                 | 303 ms                                                 | 235 ms: 1.29x faster                                                  |
| scimark_sor              | 128 ms                                                 | 99.9 ms: 1.28x faster                                                 |
| tornado_http             | 86.7 ms                                                | 67.7 ms: 1.28x faster                                                 |
| sympy_sum                | 92.2 ms                                                | 72.3 ms: 1.27x faster                                                 |
| django_template          | 26.4 ms                                                | 21.0 ms: 1.26x faster                                                 |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.29 sec: 1.24x faster                                                |
| scimark_fft              | 224 ms                                                 | 184 ms: 1.22x faster                                                  |
| sympy_integrate          | 13.1 ms                                                | 10.9 ms: 1.21x faster                                                 |
| sympy_str                | 165 ms                                                 | 138 ms: 1.20x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.90 ms: 1.18x faster                                                 |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| docutils                 | 1.73 sec                                               | 1.52 sec: 1.14x faster                                                |
| dask                     | 253 ms                                                 | 223 ms: 1.14x faster                                                  |
| sympy_expand             | 269 ms                                                 | 237 ms: 1.13x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 33.0 ms: 1.12x faster                                                 |
| nqueens                  | 63.8 ms                                                | 57.4 ms: 1.11x faster                                                 |
| bench_thread_pool        | 527 us                                                 | 482 us: 1.09x faster                                                  |
| pathlib                  | 24.5 ms                                                | 22.7 ms: 1.08x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 72.5 ms: 1.07x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 102 ms: 1.06x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 50.8 ms: 1.05x faster                                                 |
| json                     | 3.08 ms                                                | 2.94 ms: 1.05x faster                                                 |
| genshi_text              | 17.3 ms                                                | 17.0 ms: 1.02x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.1 ms: 1.02x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.62 sec: 1.00x faster                                                |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.4 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 17.1 us: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.58 ms: 1.05x slower                                                 |
| pickle_list              | 2.74 us                                                | 2.92 us: 1.07x slower                                                 |
| unpickle                 | 8.80 us                                                | 9.39 us: 1.07x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 920 us: 1.07x slower                                                  |
| pickle                   | 6.97 us                                                | 7.48 us: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.89 us: 1.07x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.2 us: 1.07x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.57 us: 1.08x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.7 ms: 1.10x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.61 ms: 1.10x slower                                                 |
| genshi_xml               | 33.8 ms                                                | 40.4 ms: 1.20x slower                                                 |
| async_generators         | 231 ms                                                 | 294 ms: 1.27x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 49.0 ms: 1.31x slower                                                 |
| telco                    | 3.49 ms                                                | 4.65 ms: 1.33x slower                                                 |
| flaskblogging            | 2.65 ms                                                | 3.53 ms: 1.33x slower                                                 |
| python_startup           | 10.9 ms                                                | 15.3 ms: 1.41x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 12.8 ms: 1.62x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, 2to3
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (12) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 0.89x