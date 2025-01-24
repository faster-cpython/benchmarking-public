# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                           |
| html5lib       | 88.9 ms                                                | 71.0 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                             |
| async_tree_none         | 728 ms                                                 | 296 ms: 2.46x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 375 ms: 2.32x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 534 ms: 1.90x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.4 ms: 1.49x faster                                                            |
| nbody          | 154 ms                                                 | 143 ms: 1.07x faster                                                             |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                            |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.43 sec: 1.29x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 376 us: 1.29x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 261 us: 1.27x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 94.9 ms: 1.22x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 68.7 ms: 1.15x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                             |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 96.0 ms: 1.04x faster                                                            |
| json_loads           | 31.2 us                                                | 31.8 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.1 ms: 1.04x slower                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.39 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 41.4 ms: 1.16x faster                                                            |
| genshi_text     | 31.8 ms                                                | 28.8 ms: 1.10x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 61.0 ms: 1.08x faster                                                            |
| mako            | 16.3 ms                                                | 16.5 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                             |
| typing_runtime_protocols | 544 us                                                 | 210 us: 2.60x faster                                                             |
| generators               | 80.1 ms                                                | 32.1 ms: 2.49x faster                                                            |
| async_tree_none          | 728 ms                                                 | 296 ms: 2.46x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 375 ms: 2.32x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 534 ms: 1.90x faster                                                             |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                             |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                             |
| logging_silent           | 190 ns                                                 | 117 ns: 1.63x faster                                                             |
| deltablue                | 7.91 ms                                                | 4.89 ms: 1.62x faster                                                            |
| scimark_sor              | 220 ms                                                 | 143 ms: 1.54x faster                                                             |
| chaos                    | 115 ms                                                 | 75.5 ms: 1.53x faster                                                            |
| deepcopy                 | 479 us                                                 | 315 us: 1.52x faster                                                             |
| float                    | 117 ms                                                 | 78.4 ms: 1.49x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.6 us: 1.48x faster                                                            |
| richards_super           | 94.7 ms                                                | 64.6 ms: 1.47x faster                                                            |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                             |
| richards                 | 79.3 ms                                                | 56.1 ms: 1.41x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 91.0 ms: 1.40x faster                                                            |
| raytrace                 | 507 ms                                                 | 364 ms: 1.39x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.58 ms: 1.37x faster                                                            |
| coroutines               | 35.1 ms                                                | 25.6 ms: 1.37x faster                                                            |
| comprehensions           | 28.8 us                                                | 21.0 us: 1.37x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 87.5 ms: 1.35x faster                                                            |
| pyflate                  | 716 ms                                                 | 531 ms: 1.35x faster                                                             |
| hexiom                   | 10.4 ms                                                | 7.89 ms: 1.32x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.97 ms: 1.30x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.43 sec: 1.29x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 376 us: 1.29x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 261 us: 1.27x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                                            |
| scimark_lu               | 176 ms                                                 | 140 ms: 1.26x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                                           |
| html5lib                 | 88.9 ms                                                | 71.0 ms: 1.25x faster                                                            |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                             |
| logging_simple           | 8.30 us                                                | 6.74 us: 1.23x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 94.9 ms: 1.22x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 69.5 ms: 1.21x faster                                                            |
| logging_format           | 9.09 us                                                | 7.54 us: 1.20x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.77 sec: 1.19x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 856 ms: 1.19x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 121 ms: 1.18x faster                                                             |
| django_template          | 48.2 ms                                                | 41.4 ms: 1.16x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 68.7 ms: 1.15x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 60.9 ms: 1.14x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.8 ms: 1.12x faster                                                            |
| thrift                   | 1.07 ms                                                | 959 us: 1.12x faster                                                             |
| 2to3                     | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                                             |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                            |
| genshi_text              | 31.8 ms                                                | 28.8 ms: 1.10x faster                                                            |
| scimark_fft              | 466 ms                                                 | 429 ms: 1.08x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 61.0 ms: 1.08x faster                                                            |
| sympy_str                | 346 ms                                                 | 320 ms: 1.08x faster                                                             |
| nbody                    | 154 ms                                                 | 143 ms: 1.07x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 24.0 ms: 1.07x faster                                                            |
| sympy_expand             | 566 ms                                                 | 531 ms: 1.06x faster                                                             |
| nqueens                  | 106 ms                                                 | 99.5 ms: 1.06x faster                                                            |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 164 ms: 1.05x faster                                                             |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 96.0 ms: 1.04x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.25 ms: 1.03x faster                                                            |
| fannkuch                 | 532 ms                                                 | 517 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 550 ms: 1.02x faster                                                             |
| json                     | 5.69 ms                                                | 5.61 ms: 1.01x faster                                                            |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                                             |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                             |
| mako                     | 16.3 ms                                                | 16.5 ms: 1.01x slower                                                            |
| mdp                      | 2.85 sec                                               | 2.88 sec: 1.01x slower                                                           |
| json_loads               | 31.2 us                                                | 31.8 us: 1.02x slower                                                            |
| python_startup           | 14.6 ms                                                | 15.1 ms: 1.04x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                                            |
| meteor_contest           | 120 ms                                                 | 133 ms: 1.11x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 4.22 ms: 1.16x slower                                                            |
| telco                    | 7.27 ms                                                | 9.22 ms: 1.27x slower                                                            |
| coverage                 | 79.4 ms                                                | 114 ms: 1.44x slower                                                             |
| python_startup_no_site   | 5.93 ms                                                | 9.39 ms: 1.58x slower                                                            |
| bench_thread_pool        | 986 us                                                 | 3.50 ms: 3.54x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 89.7 ms: 3.74x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250124-3.14.0a4+-1e0f842-NOGIL/bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.51x