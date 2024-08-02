# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 192 ms                                                 | 182 ms: 1.06x faster                                                  |
| chameleon      | 6.26 ms                                                | 4.29 ms: 1.46x faster                                                 |
| docutils       | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                |
| html5lib       | 42.4 ms                                                | 31.0 ms: 1.37x faster                                                 |
| tornado_http   | 86.7 ms                                                | 66.2 ms: 1.31x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 388 ms                                                 | 209 ms: 1.86x faster                                                  |
| async_tree_memoization  | 474 ms                                                 | 258 ms: 1.83x faster                                                  |
| async_tree_io           | 980 ms                                                 | 566 ms: 1.73x faster                                                  |
| async_tree_cpu_io_mixed | 649 ms                                                 | 468 ms: 1.39x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.69x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 93.0 ms                                                | 60.3 ms: 1.54x faster                                                 |
| float          | 69.0 ms                                                | 48.2 ms: 1.43x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.3 ms                                                | 68.2 ms: 1.40x faster                                                 |
| regex_dna      | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| regex_v8       | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| regex_effbot   | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 281 us                                                 | 178 us: 1.58x faster                                                  |
| unpickle_pure_python | 194 us                                                 | 140 us: 1.39x faster                                                  |
| json_dumps           | 8.11 ms                                                | 6.29 ms: 1.29x faster                                                 |
| xml_etree_process    | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                 |
| tomli_loads          | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_generate   | 53.5 ms                                                | 52.2 ms: 1.03x faster                                                 |
| xml_etree_iterparse  | 72.1 ms                                                | 71.6 ms: 1.01x faster                                                 |
| json_loads           | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| unpickle             | 8.80 us                                                | 9.33 us: 1.06x slower                                                 |
| pickle               | 6.97 us                                                | 7.45 us: 1.07x slower                                                 |
| unpickle_list        | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_dict          | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| pickle_list          | 2.74 us                                                | 3.00 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                | 14.0 ms: 1.29x slower                                                 |
| python_startup_no_site | 7.91 ms                                                | 11.5 ms: 1.45x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.37x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| django_template | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                 |
| genshi_text     | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| genshi_xml      | 33.8 ms                                                | 29.7 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 323 us                                                 | 91.7 us: 3.52x faster                                                 |
| deltablue                | 4.91 ms                                                | 2.14 ms: 2.30x faster                                                 |
| raytrace                 | 301 ms                                                 | 147 ms: 2.05x faster                                                  |
| logging_silent           | 117 ns                                                 | 60.0 ns: 1.95x faster                                                 |
| chaos                    | 65.8 ms                                                | 34.3 ms: 1.92x faster                                                 |
| async_tree_none          | 388 ms                                                 | 209 ms: 1.86x faster                                                  |
| async_tree_memoization   | 474 ms                                                 | 258 ms: 1.83x faster                                                  |
| async_tree_io            | 980 ms                                                 | 566 ms: 1.73x faster                                                  |
| sqlglot_parse            | 1.24 ms                                                | 733 us: 1.70x faster                                                  |
| richards_super           | 57.8 ms                                                | 34.3 ms: 1.69x faster                                                 |
| sqlglot_transpile        | 1.44 ms                                                | 892 us: 1.62x faster                                                  |
| pylint                   | 277 ms                                                 | 172 ms: 1.61x faster                                                  |
| comprehensions           | 16.9 us                                                | 10.7 us: 1.59x faster                                                 |
| pickle_pure_python       | 281 us                                                 | 178 us: 1.58x faster                                                  |
| richards                 | 48.7 ms                                                | 31.1 ms: 1.57x faster                                                 |
| scimark_monte_carlo      | 65.6 ms                                                | 42.2 ms: 1.55x faster                                                 |
| asyncio_tcp              | 659 ms                                                 | 425 ms: 1.55x faster                                                  |
| nbody                    | 93.0 ms                                                | 60.3 ms: 1.54x faster                                                 |
| scimark_lu               | 103 ms                                                 | 66.8 ms: 1.54x faster                                                 |
| deepcopy_memo            | 34.7 us                                                | 22.6 us: 1.54x faster                                                 |
| hexiom                   | 6.19 ms                                                | 4.08 ms: 1.52x faster                                                 |
| go                       | 151 ms                                                 | 100 ms: 1.50x faster                                                  |
| chameleon                | 6.26 ms                                                | 4.29 ms: 1.46x faster                                                 |
| logging_simple           | 4.45 us                                                | 3.07 us: 1.45x faster                                                 |
| crypto_pyaes             | 71.8 ms                                                | 49.6 ms: 1.45x faster                                                 |
| logging_format           | 4.83 us                                                | 3.35 us: 1.44x faster                                                 |
| float                    | 69.0 ms                                                | 48.2 ms: 1.43x faster                                                 |
| mako                     | 9.87 ms                                                | 6.91 ms: 1.43x faster                                                 |
| generators               | 32.3 ms                                                | 22.9 ms: 1.41x faster                                                 |
| spectral_norm            | 94.8 ms                                                | 67.2 ms: 1.41x faster                                                 |
| regex_compile            | 95.3 ms                                                | 68.2 ms: 1.40x faster                                                 |
| unpickle_pure_python     | 194 us                                                 | 140 us: 1.39x faster                                                  |
| pycparser                | 877 ms                                                 | 632 ms: 1.39x faster                                                  |
| async_tree_cpu_io_mixed  | 649 ms                                                 | 468 ms: 1.39x faster                                                  |
| pprint_safe_repr         | 641 ms                                                 | 462 ms: 1.39x faster                                                  |
| pprint_pformat           | 1.30 sec                                               | 943 ms: 1.38x faster                                                  |
| html5lib                 | 42.4 ms                                                | 31.0 ms: 1.37x faster                                                 |
| scimark_sor              | 128 ms                                                 | 94.0 ms: 1.36x faster                                                 |
| django_template          | 26.4 ms                                                | 19.4 ms: 1.36x faster                                                 |
| deepcopy                 | 272 us                                                 | 200 us: 1.36x faster                                                  |
| thrift                   | 572 us                                                 | 428 us: 1.34x faster                                                  |
| pyflate                  | 427 ms                                                 | 320 ms: 1.33x faster                                                  |
| sympy_sum                | 92.2 ms                                                | 69.9 ms: 1.32x faster                                                 |
| tornado_http             | 86.7 ms                                                | 66.2 ms: 1.31x faster                                                 |
| deepcopy_reduce          | 2.33 us                                                | 1.79 us: 1.30x faster                                                 |
| coroutines               | 20.7 ms                                                | 15.9 ms: 1.30x faster                                                 |
| json_dumps               | 8.11 ms                                                | 6.29 ms: 1.29x faster                                                 |
| sympy_integrate          | 13.1 ms                                                | 10.3 ms: 1.27x faster                                                 |
| genshi_text              | 17.3 ms                                                | 13.7 ms: 1.26x faster                                                 |
| xml_etree_process        | 46.5 ms                                                | 36.9 ms: 1.26x faster                                                 |
| sympy_str                | 165 ms                                                 | 132 ms: 1.26x faster                                                  |
| asyncio_tcp_ssl          | 1.60 sec                                               | 1.28 sec: 1.25x faster                                                |
| scimark_fft              | 224 ms                                                 | 180 ms: 1.24x faster                                                  |
| scimark_sparse_mat_mult  | 3.42 ms                                                | 2.77 ms: 1.24x faster                                                 |
| fannkuch                 | 303 ms                                                 | 249 ms: 1.21x faster                                                  |
| nqueens                  | 63.8 ms                                                | 52.6 ms: 1.21x faster                                                 |
| docutils                 | 1.73 sec                                               | 1.44 sec: 1.21x faster                                                |
| sympy_expand             | 269 ms                                                 | 227 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 36.8 ms                                                | 31.0 ms: 1.19x faster                                                 |
| tomli_loads              | 1.71 sec                                               | 1.46 sec: 1.17x faster                                                |
| regex_dna                | 174 ms                                                 | 149 ms: 1.17x faster                                                  |
| dask                     | 253 ms                                                 | 220 ms: 1.15x faster                                                  |
| sqlglot_normalize        | 190 ms                                                 | 167 ms: 1.14x faster                                                  |
| bench_thread_pool        | 527 us                                                 | 463 us: 1.14x faster                                                  |
| genshi_xml               | 33.8 ms                                                | 29.7 ms: 1.14x faster                                                 |
| meteor_contest           | 77.7 ms                                                | 69.8 ms: 1.11x faster                                                 |
| mdp                      | 1.63 sec                                               | 1.49 sec: 1.09x faster                                                |
| pathlib                  | 24.5 ms                                                | 22.5 ms: 1.09x faster                                                 |
| 2to3                     | 192 ms                                                 | 182 ms: 1.06x faster                                                  |
| json                     | 3.08 ms                                                | 2.95 ms: 1.04x faster                                                 |
| xml_etree_parse          | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_generate       | 53.5 ms                                                | 52.2 ms: 1.03x faster                                                 |
| xml_etree_iterparse      | 72.1 ms                                                | 71.6 ms: 1.01x faster                                                 |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| regex_v8                 | 17.1 ms                                                | 17.3 ms: 1.01x slower                                                 |
| json_loads               | 16.4 us                                                | 16.9 us: 1.03x slower                                                 |
| gc_traversal             | 2.36 ms                                                | 2.46 ms: 1.04x slower                                                 |
| regex_effbot             | 2.46 ms                                                | 2.56 ms: 1.04x slower                                                 |
| sqlite_synth             | 1.46 us                                                | 1.54 us: 1.06x slower                                                 |
| create_gc_cycles         | 860 us                                                 | 910 us: 1.06x slower                                                  |
| unpickle                 | 8.80 us                                                | 9.33 us: 1.06x slower                                                 |
| pickle                   | 6.97 us                                                | 7.45 us: 1.07x slower                                                 |
| unpickle_list            | 2.69 us                                                | 2.90 us: 1.08x slower                                                 |
| pickle_dict              | 17.0 us                                                | 18.3 us: 1.08x slower                                                 |
| pickle_list              | 2.74 us                                                | 3.00 us: 1.09x slower                                                 |
| coverage                 | 41.5 ms                                                | 45.9 ms: 1.11x slower                                                 |
| async_generators         | 231 ms                                                 | 279 ms: 1.21x slower                                                  |
| bench_mp_pool            | 37.4 ms                                                | 45.7 ms: 1.22x slower                                                 |
| flaskblogging            | 2.65 ms                                                | 3.40 ms: 1.29x slower                                                 |
| python_startup           | 10.9 ms                                                | 14.0 ms: 1.29x slower                                                 |
| telco                    | 3.49 ms                                                | 4.61 ms: 1.32x slower                                                 |
| python_startup_no_site   | 7.91 ms                                                | 11.5 ms: 1.45x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (12) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 0.62x