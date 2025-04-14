# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_validity
- machine: linux-x86_64
- commit hash: aee117b
- commit date: 2025-02-18
- overall geometric mean: 1.460x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.25x faster                                              |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.73x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                               |
| nbody          | 154 ms                                                 | 91.6 ms: 1.68x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                               |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.80 sec: 1.75x faster                                              |
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.9 ms: 1.19x faster                                               |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                               |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                               |
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                               |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.44x faster                                                |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                               |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.73x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                               |
| go                       | 240 ms                                                 | 124 ms: 1.94x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                               |
| richards_super           | 94.7 ms                                                | 50.4 ms: 1.88x faster                                               |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                                |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.81x faster                                               |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.80 sec: 1.75x faster                                              |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                               |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                               |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                               |
| nbody                    | 154 ms                                                 | 91.6 ms: 1.68x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                               |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.53 ms: 1.59x faster                                               |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                               |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                                |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                               |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                               |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.32 ms: 1.50x faster                                               |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                              |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 705 ms: 1.44x faster                                                |
| pycparser                | 1.58 sec                                               | 1.10 sec: 1.44x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| thrift                   | 1.07 ms                                                | 751 us: 1.43x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                               |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 52.9 ms: 1.31x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                               |
| nqueens                  | 106 ms                                                 | 82.4 ms: 1.28x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                               |
| dulwich_log              | 84.3 ms                                                | 66.1 ms: 1.28x faster                                               |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                               |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.25x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.9 ms: 1.19x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                               |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                               |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                              |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                               |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                               |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                               |
| async_generators         | 444 ms                                                 | 415 ms: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.54 ms: 1.04x slower                                               |
| coverage                 | 79.4 ms                                                | 90.3 ms: 1.14x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.88 ms: 1.35x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.38x slower                                               |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                        |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250218-3.14.0a5+-aee117b-JIT/bm-20250218-linux-x86_64-brandtbucher-no_validity-3.14.0a5+-aee117b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.460x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.28x