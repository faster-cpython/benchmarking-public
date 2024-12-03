# Results vs. 3.10.4

- fork: faster-cpython
- ref: faster_marking
- machine: linux-x86_64
- commit hash: 1545508
- commit date: 2024-12-03
- overall geometric mean: 1.427x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                       |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 632 ms: 2.80x faster                                                       |
| async_tree_none         | 728 ms                                                 | 284 ms: 2.57x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 348 ms: 2.50x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 510 ms: 1.99x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.45x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.7 ms: 1.64x faster                                                      |
| float          | 117 ms                                                 | 79.1 ms: 1.48x faster                                                      |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 334 us: 1.45x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 60.9 ms: 1.30x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 87.7 ms: 1.13x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                      |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                                       |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 632 ms: 2.80x faster                                                       |
| async_tree_none          | 728 ms                                                 | 284 ms: 2.57x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 348 ms: 2.50x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.30 ms: 2.40x faster                                                      |
| pylint                   | 551 ms                                                 | 273 ms: 2.02x faster                                                       |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 510 ms: 1.99x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                      |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                      |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                       |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                       |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.80x faster                                                      |
| logging_silent           | 190 ns                                                 | 108 ns: 1.75x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 73.5 ms: 1.74x faster                                                      |
| djangocms                | 38.4 us                                                | 22.2 us: 1.73x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                      |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                       |
| richards                 | 79.3 ms                                                | 46.4 ms: 1.71x faster                                                      |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.69x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                                      |
| nbody                    | 154 ms                                                 | 93.7 ms: 1.64x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                      |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                      |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                     |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                      |
| float                    | 117 ms                                                 | 79.1 ms: 1.48x faster                                                      |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                       |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| coroutines               | 35.1 ms                                                | 24.1 ms: 1.45x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 334 us: 1.45x faster                                                       |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                      |
| thrift                   | 1.07 ms                                                | 764 us: 1.40x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                      |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                     |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 60.9 ms: 1.30x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                                      |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                       |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                      |
| json                     | 5.69 ms                                                | 4.79 ms: 1.19x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 853 us: 1.16x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 87.7 ms: 1.13x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                       |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                       |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                       |
| coverage                 | 79.4 ms                                                | 83.5 ms: 1.05x slower                                                      |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.47 ms: 1.23x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.24 ms: 1.38x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                               |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241203-3.14.0a2+-1545508/bm-20241203-linux-x86_64-faster%2dcpython-faster_marking-3.14.0a2+-1545508.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.427x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x