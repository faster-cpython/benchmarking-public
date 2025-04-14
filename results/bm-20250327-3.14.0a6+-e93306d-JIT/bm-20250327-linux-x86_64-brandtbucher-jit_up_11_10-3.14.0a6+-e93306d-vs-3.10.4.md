# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_10
- machine: linux-x86_64
- commit hash: e93306d
- commit date: 2025-03-27
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                                 |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                               |
| html5lib       | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| Geometric mean | (ref)                                                  | 1.31x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                 |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.76x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 491 ms: 2.07x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.8 ms: 1.78x faster                                                |
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.48x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                               |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                |
| mako            | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                 |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.76x faster                                                 |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                                |
| deltablue                | 7.91 ms                                                | 3.08 ms: 2.57x faster                                                |
| richards_super           | 94.7 ms                                                | 40.6 ms: 2.33x faster                                                |
| richards                 | 79.3 ms                                                | 35.3 ms: 2.24x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 491 ms: 2.07x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                 |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                 |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                 |
| spectral_norm            | 170 ms                                                 | 92.6 ms: 1.83x faster                                                |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                 |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                 |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                 |
| float                    | 117 ms                                                 | 65.8 ms: 1.78x faster                                                |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 77.2 ms: 1.65x faster                                                |
| pyflate                  | 716 ms                                                 | 453 ms: 1.58x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                 |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.93 ms: 1.50x faster                                                |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.49x faster                                                |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                                |
| html5lib                 | 88.9 ms                                                | 63.3 ms: 1.40x faster                                                |
| dulwich_log              | 84.3 ms                                                | 60.5 ms: 1.39x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.8 ms: 1.39x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                                |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                               |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 782 ms: 1.30x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.65 sec: 1.28x faster                                               |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                 |
| sympy_str                | 346 ms                                                 | 278 ms: 1.25x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.7 ms: 1.22x faster                                                |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                                |
| sympy_expand             | 566 ms                                                 | 479 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                               |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                |
| async_generators         | 444 ms                                                 | 420 ms: 1.06x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                 |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                         |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-e93306d-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_up_11_10-3.14.0a6+-e93306d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x