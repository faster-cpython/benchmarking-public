# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.446x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                                             |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.73x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.63x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                                            |
| nbody          | 154 ms                                                 | 93.8 ms: 1.64x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                             |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 97.7 ms: 1.18x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                            |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                            |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                            |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                             |
| generators               | 80.1 ms                                                | 27.5 ms: 2.91x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                                             |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.73x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.63x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                             |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                             |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                                             |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                            |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                                            |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                                             |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                             |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.79x faster                                                             |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.78x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                            |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                            |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                            |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                            |
| nbody                    | 154 ms                                                 | 93.8 ms: 1.64x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                             |
| pyflate                  | 716 ms                                                 | 475 ms: 1.51x faster                                                             |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.50x faster                                                             |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                            |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                             |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                            |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.45x faster                                                            |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                            |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                            |
| thrift                   | 1.07 ms                                                | 755 us: 1.42x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.38x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                             |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                            |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 63.6 ms: 1.33x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                            |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                             |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 97.7 ms: 1.18x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                            |
| async_generators         | 444 ms                                                 | 380 ms: 1.17x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 862 us: 1.14x faster                                                             |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                            |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                            |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                            |
| coverage                 | 79.4 ms                                                | 91.6 ms: 1.15x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250124-3.14.0a4+-1e0f842/bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.446x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x