# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: ba20c7c
- commit date: 2024-12-04
- overall geometric mean: 1.424x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                       |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 608 ms: 2.91x faster                                                       |
| async_tree_none         | 728 ms                                                 | 275 ms: 2.64x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 350 ms: 2.49x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                                      |
| float          | 117 ms                                                 | 80.7 ms: 1.45x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                      |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 61.6 ms: 1.28x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 88.3 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                      |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.33x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 608 ms: 2.91x faster                                                       |
| generators               | 80.1 ms                                                | 29.1 ms: 2.75x faster                                                      |
| async_tree_none          | 728 ms                                                 | 275 ms: 2.64x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 350 ms: 2.49x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.35 ms: 2.36x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                       |
| pylint                   | 551 ms                                                 | 272 ms: 2.02x faster                                                       |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.90x faster                                                      |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                      |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                       |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                       |
| richards_super           | 94.7 ms                                                | 53.3 ms: 1.78x faster                                                      |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                      |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                      |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.69x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                                      |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                      |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                      |
| pyflate                  | 716 ms                                                 | 475 ms: 1.51x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                                       |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                     |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                       |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                      |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                       |
| float                    | 117 ms                                                 | 80.7 ms: 1.45x faster                                                      |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                      |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.42x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                                      |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                       |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                      |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                       |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                                      |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 64.9 ms: 1.30x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 61.6 ms: 1.28x faster                                                      |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 54.1 ms: 1.28x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                      |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                      |
| json                     | 5.69 ms                                                | 4.89 ms: 1.16x faster                                                      |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 854 us: 1.16x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 88.3 ms: 1.13x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.10x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                      |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                                       |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                      |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.27 ms: 1.40x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241204-3.14.0a2+-ba20c7c/bm-20241204-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-ba20c7c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.424x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x