# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d5e47ea
- commit date: 2025-01-20
- overall geometric mean: 1.228x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                           |
| html5lib       | 88.9 ms                                                | 71.2 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                                             |
| async_tree_none         | 728 ms                                                 | 292 ms: 2.49x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 372 ms: 2.34x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 523 ms: 1.94x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.40x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.9 ms: 1.48x faster                                                            |
| nbody          | 154 ms                                                 | 139 ms: 1.11x faster                                                             |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 153 ms: 1.23x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                            |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.45 sec: 1.28x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 382 us: 1.27x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 273 us: 1.21x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| json_dumps           | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 72.1 ms: 1.10x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 96.8 ms: 1.03x faster                                                            |
| json_loads           | 31.2 us                                                | 31.7 us: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.1 ms: 1.03x slower                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.37 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 41.7 ms: 1.16x faster                                                            |
| genshi_text     | 31.8 ms                                                | 29.3 ms: 1.09x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 62.8 ms: 1.05x faster                                                            |
| mako            | 16.3 ms                                                | 16.5 ms: 1.01x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                                             |
| generators               | 80.1 ms                                                | 31.6 ms: 2.53x faster                                                            |
| typing_runtime_protocols | 544 us                                                 | 216 us: 2.51x faster                                                             |
| async_tree_none          | 728 ms                                                 | 292 ms: 2.49x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 372 ms: 2.34x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 523 ms: 1.94x faster                                                             |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                             |
| deltablue                | 7.91 ms                                                | 4.77 ms: 1.66x faster                                                            |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                             |
| logging_silent           | 190 ns                                                 | 120 ns: 1.58x faster                                                             |
| chaos                    | 115 ms                                                 | 74.3 ms: 1.55x faster                                                            |
| scimark_sor              | 220 ms                                                 | 141 ms: 1.55x faster                                                             |
| deepcopy                 | 479 us                                                 | 319 us: 1.50x faster                                                             |
| float                    | 117 ms                                                 | 78.9 ms: 1.48x faster                                                            |
| richards_super           | 94.7 ms                                                | 64.0 ms: 1.48x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 39.7 us: 1.47x faster                                                            |
| richards                 | 79.3 ms                                                | 54.9 ms: 1.44x faster                                                            |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.42x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 90.7 ms: 1.41x faster                                                            |
| raytrace                 | 507 ms                                                 | 360 ms: 1.41x faster                                                             |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                                            |
| pyflate                  | 716 ms                                                 | 521 ms: 1.37x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.60 ms: 1.35x faster                                                            |
| comprehensions           | 28.8 us                                                | 21.2 us: 1.35x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 88.1 ms: 1.34x faster                                                            |
| hexiom                   | 10.4 ms                                                | 7.83 ms: 1.33x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.94 ms: 1.32x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.45 sec: 1.28x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 382 us: 1.27x faster                                                             |
| scimark_lu               | 176 ms                                                 | 141 ms: 1.25x faster                                                             |
| html5lib                 | 88.9 ms                                                | 71.2 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.24x faster                                                            |
| regex_compile            | 188 ms                                                 | 153 ms: 1.23x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 273 us: 1.21x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                            |
| logging_simple           | 8.30 us                                                | 7.01 us: 1.18x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 71.3 ms: 1.18x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 866 ms: 1.18x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.79 sec: 1.17x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 122 ms: 1.17x faster                                                             |
| django_template          | 48.2 ms                                                | 41.7 ms: 1.16x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                           |
| logging_format           | 9.09 us                                                | 8.02 us: 1.13x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 62.0 ms: 1.12x faster                                                            |
| 2to3                     | 348 ms                                                 | 313 ms: 1.11x faster                                                             |
| thrift                   | 1.07 ms                                                | 963 us: 1.11x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                            |
| json_dumps               | 14.2 ms                                                | 12.8 ms: 1.11x faster                                                            |
| nbody                    | 154 ms                                                 | 139 ms: 1.11x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 72.1 ms: 1.10x faster                                                            |
| scimark_fft              | 466 ms                                                 | 425 ms: 1.10x faster                                                             |
| sympy_sum                | 196 ms                                                 | 180 ms: 1.09x faster                                                             |
| genshi_text              | 31.8 ms                                                | 29.3 ms: 1.09x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 21.5 ms: 1.08x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                            |
| sympy_str                | 346 ms                                                 | 323 ms: 1.07x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 24.1 ms: 1.07x faster                                                            |
| nqueens                  | 106 ms                                                 | 99.1 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.13 ms: 1.06x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 62.8 ms: 1.05x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 164 ms: 1.05x faster                                                             |
| sympy_expand             | 566 ms                                                 | 541 ms: 1.05x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 96.8 ms: 1.03x faster                                                            |
| fannkuch                 | 532 ms                                                 | 521 ms: 1.02x faster                                                             |
| json                     | 5.69 ms                                                | 5.58 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                             |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                             |
| mako                     | 16.3 ms                                                | 16.5 ms: 1.01x slower                                                            |
| json_loads               | 31.2 us                                                | 31.7 us: 1.02x slower                                                            |
| python_startup           | 14.6 ms                                                | 15.1 ms: 1.03x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.06x slower                                                            |
| meteor_contest           | 120 ms                                                 | 132 ms: 1.10x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 4.44 ms: 1.22x slower                                                            |
| telco                    | 7.27 ms                                                | 9.21 ms: 1.27x slower                                                            |
| coverage                 | 79.4 ms                                                | 107 ms: 1.35x slower                                                             |
| python_startup_no_site   | 5.93 ms                                                | 9.37 ms: 1.58x slower                                                            |
| bench_thread_pool        | 986 us                                                 | 3.49 ms: 3.54x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 89.8 ms: 3.74x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.19x faster                                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250120-3.14.0a4+-d5e47ea-NOGIL/bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.228x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.51x