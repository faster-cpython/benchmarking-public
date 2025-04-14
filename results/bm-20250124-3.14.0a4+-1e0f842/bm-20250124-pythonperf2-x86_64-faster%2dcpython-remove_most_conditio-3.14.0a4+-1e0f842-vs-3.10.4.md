# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.363x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 280 ms: 1.25x faster                                                                   |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 645 ms: 2.48x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 68.7 ms: 1.62x faster                                                                  |
| nbody          | 134 ms                                                       | 87.8 ms: 1.53x faster                                                                  |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.53x faster                                                                   |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                                 |
| pickle_pure_python   | 455 us                                                       | 323 us: 1.41x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                                  |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.18x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                                   |
| xml_etree_generate   | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                                  |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                                  |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                                  |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 52.3 ms: 1.21x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.08x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 645 ms: 2.48x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.28 ms: 2.29x faster                                                                  |
| go                       | 262 ms                                                       | 125 ms: 2.10x faster                                                                   |
| generators               | 57.3 ms                                                      | 28.0 ms: 2.05x faster                                                                  |
| chaos                    | 109 ms                                                       | 58.2 ms: 1.87x faster                                                                  |
| raytrace                 | 489 ms                                                       | 263 ms: 1.86x faster                                                                   |
| pylint                   | 566 ms                                                       | 314 ms: 1.80x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                                                   |
| scimark_lu               | 167 ms                                                       | 93.1 ms: 1.79x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 51.6 ms: 1.76x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 62.0 ms: 1.73x faster                                                                  |
| logging_silent           | 167 ns                                                       | 97.4 ns: 1.72x faster                                                                  |
| sqlglot_parse            | 2.24 ms                                                      | 1.31 ms: 1.70x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                                   |
| spectral_norm            | 139 ms                                                       | 83.2 ms: 1.67x faster                                                                  |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                                   |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.66x faster                                                                  |
| deepcopy_memo            | 49.8 us                                                      | 30.2 us: 1.65x faster                                                                  |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                                   |
| float                    | 111 ms                                                       | 68.7 ms: 1.62x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 73.8 ms: 1.62x faster                                                                  |
| sqlglot_transpile        | 2.68 ms                                                      | 1.70 ms: 1.58x faster                                                                  |
| hexiom                   | 9.42 ms                                                      | 6.02 ms: 1.56x faster                                                                  |
| nbody                    | 134 ms                                                       | 87.8 ms: 1.53x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.53x faster                                                                   |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 6.17 us: 1.44x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                                 |
| logging_format           | 9.64 us                                                      | 6.75 us: 1.43x faster                                                                  |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 323 us: 1.41x faster                                                                   |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                                   |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                                 |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                                  |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                                 |
| pprint_safe_repr         | 1.05 sec                                                     | 778 ms: 1.35x faster                                                                   |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 874 us: 1.34x faster                                                                   |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                                  |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                                   |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                                   |
| nqueens                  | 115 ms                                                       | 88.7 ms: 1.30x faster                                                                  |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                                   |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                                  |
| sqlglot_normalize        | 144 ms                                                       | 113 ms: 1.27x faster                                                                   |
| sympy_str                | 360 ms                                                       | 288 ms: 1.25x faster                                                                   |
| 2to3                     | 350 ms                                                       | 280 ms: 1.25x faster                                                                   |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 922 us: 1.24x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.44 sec: 1.23x faster                                                                 |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                                  |
| sqlglot_optimize         | 70.1 ms                                                      | 57.1 ms: 1.23x faster                                                                  |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                                  |
| sympy_expand             | 600 ms                                                       | 493 ms: 1.22x faster                                                                   |
| genshi_xml               | 63.3 ms                                                      | 52.3 ms: 1.21x faster                                                                  |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                                 |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.18x faster                                                                  |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.51 ms: 1.13x faster                                                                  |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 84.1 ms: 1.10x faster                                                                  |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                                  |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.09x faster                                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.08x faster                                                                  |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                                   |
| async_generators         | 421 ms                                                       | 405 ms: 1.04x faster                                                                   |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                                   |
| telco                    | 7.23 ms                                                      | 8.03 ms: 1.11x slower                                                                  |
| coverage                 | 63.3 ms                                                      | 76.5 ms: 1.21x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.78 ms: 1.58x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.02 sec: 159.45x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                           |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250124-3.14.0a4+-1e0f842/bm-20250124-pythonperf2-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.363x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.27x