# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: a94d30d
- commit date: 2024-11-09
- overall geometric mean: 1.449x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| html5lib       | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 629 ms: 2.81x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.1 ms: 1.61x faster                                                      |
| float          | 117 ms                                                 | 79.2 ms: 1.48x faster                                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                      |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                      |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.3 ms: 1.18x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 6.78 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                      |
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                       |
| generators               | 80.1 ms                                                | 27.4 ms: 2.92x faster                                                      |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 629 ms: 2.81x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                      |
| pylint                   | 551 ms                                                 | 261 ms: 2.11x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                       |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                      |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                      |
| gc_traversal             | 3.62 ms                                                | 1.97 ms: 1.84x faster                                                      |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                       |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                       |
| richards_super           | 94.7 ms                                                | 52.6 ms: 1.80x faster                                                      |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                                      |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.72x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.37 ms: 1.63x faster                                                      |
| nbody                    | 154 ms                                                 | 95.1 ms: 1.61x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                      |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                     |
| float                    | 117 ms                                                 | 79.2 ms: 1.48x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                       |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                       |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                       |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| html5lib                 | 88.9 ms                                                | 62.7 ms: 1.42x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                       |
| thrift                   | 1.07 ms                                                | 768 us: 1.40x faster                                                       |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                      |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                       |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                       |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 54.1 ms: 1.28x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.17 ms: 1.25x faster                                                      |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                       |
| scimark_fft              | 466 ms                                                 | 380 ms: 1.23x faster                                                       |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                      |
| json                     | 5.69 ms                                                | 4.79 ms: 1.19x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.3 ms: 1.18x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.17x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                      |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                       |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                                      |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                      |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 6.78 ms: 1.14x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241109-3.14.0a1+-a94d30d/bm-20241109-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a1+-a94d30d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.449x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x