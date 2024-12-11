# Results vs. 3.10.4

- fork: eendebakpt
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b034948
- commit date: 2024-12-07
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                               |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                             |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                               |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 337 ms: 2.58x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                               |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.5 ms: 1.64x faster                                              |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                              |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.30 ms: 1.10x faster                                              |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                              |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                             |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                               |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                              |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                              |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                              |
| genshi_text     | 31.8 ms                                                | 22.6 ms: 1.41x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                               |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                               |
| generators               | 80.1 ms                                                | 28.4 ms: 2.82x faster                                              |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 337 ms: 2.58x faster                                               |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                               |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                               |
| pylint                   | 551 ms                                                 | 275 ms: 2.01x faster                                               |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                              |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                               |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                              |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                               |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.74x faster                                              |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                              |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                              |
| nbody                    | 154 ms                                                 | 93.5 ms: 1.64x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                              |
| pyflate                  | 716 ms                                                 | 452 ms: 1.59x faster                                               |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.58x faster                                               |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.54x faster                                              |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                              |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                              |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                               |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                               |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                              |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                              |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                              |
| genshi_text              | 31.8 ms                                                | 22.6 ms: 1.41x faster                                              |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                              |
| thrift                   | 1.07 ms                                                | 763 us: 1.40x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.38x faster                                               |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                               |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.36x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                               |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                              |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                              |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                              |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.30x faster                                              |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                              |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                             |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                              |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                               |
| json                     | 5.69 ms                                                | 4.78 ms: 1.19x faster                                              |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 861 us: 1.15x faster                                               |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.30 ms: 1.10x faster                                              |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                              |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                              |
| mdp                      | 2.85 sec                                               | 2.68 sec: 1.06x faster                                             |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                               |
| coverage                 | 79.4 ms                                                | 83.5 ms: 1.05x slower                                              |
| mypy2                    | 894 ms                                                 | 943 ms: 1.05x slower                                               |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.08x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.50 ms: 1.24x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.22 ms: 1.37x slower                                              |
| bench_mp_pool            | 24.0 ms                                                | 78.6 ms: 3.27x slower                                              |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                       |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241207-3.14.0a2+-b034948/bm-20241207-linux-x86_64-eendebakpt-int_freelist-3.14.0a2+-b034948.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.431x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x