# Results vs. 3.10.4

- fork: kumaraditya303
- ref: disable__asyncio
- machine: linux-x86_64
- commit hash: a0a0f85
- commit date: 2024-12-15
- overall geometric mean: 1.389x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                       |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 1.03 sec: 1.72x faster                                                     |
| async_tree_none         | 728 ms                                                 | 522 ms: 1.40x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 632 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 796 ms: 1.28x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.43x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.8 ms: 1.67x faster                                                      |
| float          | 117 ms                                                 | 77.0 ms: 1.52x faster                                                      |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.38x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.2 ms: 1.19x faster                                                      |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.34x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                       |
| generators               | 80.1 ms                                                | 27.2 ms: 2.95x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                      |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                       |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                      |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                      |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                       |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                       |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                       |
| richards_super           | 94.7 ms                                                | 53.1 ms: 1.79x faster                                                      |
| djangocms                | 38.4 us                                                | 21.5 us: 1.78x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 72.7 ms: 1.76x faster                                                      |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 1.03 sec: 1.72x faster                                                     |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.71x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                                      |
| nbody                    | 154 ms                                                 | 91.8 ms: 1.67x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                      |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                      |
| float                    | 117 ms                                                 | 77.0 ms: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                       |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                                      |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                                      |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| thrift                   | 1.07 ms                                                | 756 us: 1.42x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                       |
| async_tree_none          | 728 ms                                                 | 522 ms: 1.40x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 632 ms: 1.38x faster                                                       |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                       |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                       |
| nqueens                  | 106 ms                                                 | 79.0 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.7 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 796 ms: 1.28x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.27x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                      |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.2 ms: 1.19x faster                                                      |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 858 us: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                      |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                       |
| async_generators         | 444 ms                                                 | 423 ms: 1.05x faster                                                       |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                       |
| mypy2                    | 894 ms                                                 | 942 ms: 1.05x slower                                                       |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                      |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 5.02 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                               |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241215-3.14.0a2+-a0a0f85/bm-20241215-linux-x86_64-kumaraditya303-disable__asyncio-3.14.0a2+-a0a0f85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.389x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.28x