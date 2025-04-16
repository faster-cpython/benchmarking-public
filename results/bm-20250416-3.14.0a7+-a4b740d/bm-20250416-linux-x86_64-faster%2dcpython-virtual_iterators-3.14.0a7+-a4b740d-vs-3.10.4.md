# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.40x faster                                                          |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                        |
| html5lib       | 88.9 ms                                                | 59.6 ms: 1.49x faster                                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 610 ms: 2.90x faster                                                          |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.82x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 480 ms: 2.12x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.0 ms: 1.70x faster                                                         |
| nbody          | 154 ms                                                 | 93.9 ms: 1.64x faster                                                         |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.42x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.02 ms: 1.20x faster                                                         |
| regex_dna      | 227 ms                                                 | 203 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                  | 1.26x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                          |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                         |
| json_loads           | 31.2 us                                                | 30.1 us: 1.04x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.0 ms: 1.56x faster                                                         |
| genshi_text     | 31.8 ms                                                | 20.6 ms: 1.55x faster                                                         |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 610 ms: 2.90x faster                                                          |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.82x faster                                                          |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.38x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.39 ms: 2.33x faster                                                         |
| go                       | 240 ms                                                 | 108 ms: 2.22x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 480 ms: 2.12x faster                                                          |
| chaos                    | 115 ms                                                 | 56.5 ms: 2.04x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.03x faster                                                         |
| logging_silent           | 190 ns                                                 | 95.3 ns: 1.99x faster                                                         |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                          |
| richards_super           | 94.7 ms                                                | 49.1 ms: 1.93x faster                                                         |
| deepcopy                 | 479 us                                                 | 250 us: 1.91x faster                                                          |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                         |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                          |
| comprehensions           | 28.8 us                                                | 15.9 us: 1.81x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 73.8 ms: 1.73x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                         |
| float                    | 117 ms                                                 | 69.0 ms: 1.70x faster                                                         |
| pyflate                  | 716 ms                                                 | 431 ms: 1.66x faster                                                          |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                          |
| nbody                    | 154 ms                                                 | 93.9 ms: 1.64x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                         |
| django_template          | 48.2 ms                                                | 31.0 ms: 1.56x faster                                                         |
| genshi_text              | 31.8 ms                                                | 20.6 ms: 1.55x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                          |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                          |
| logging_format           | 9.09 us                                                | 6.02 us: 1.51x faster                                                         |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                          |
| html5lib                 | 88.9 ms                                                | 59.6 ms: 1.49x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                        |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                                          |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.43x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                                         |
| 2to3                     | 348 ms                                                 | 250 ms: 1.40x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                          |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                                         |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                        |
| fannkuch                 | 532 ms                                                 | 417 ms: 1.27x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.02 ms: 1.20x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.20x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                         |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                          |
| async_generators         | 444 ms                                                 | 394 ms: 1.13x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                          |
| regex_dna                | 227 ms                                                 | 203 ms: 1.11x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                         |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                         |
| json_loads               | 31.2 us                                                | 30.1 us: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                          |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                         |
| coverage                 | 79.4 ms                                                | 86.8 ms: 1.09x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 5.05 ms: 1.39x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                                  |
Ignored benchmarks (26) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.28x