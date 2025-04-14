# Results vs. 3.10.4

- fork: python
- ref: 5d66c55c8ad0a0aeff8d
- machine: linux-x86_64
- commit hash: 5d66c55
- commit date: 2025-02-21
- overall geometric mean: 1.455x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| html5lib       | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                   |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 484 ms: 2.10x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                  |
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.18x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                  |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 84.0 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                                  |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.3 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                   |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                  |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 484 ms: 2.10x faster                                                   |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                   |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                   |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                  |
| richards_super           | 94.7 ms                                                | 50.3 ms: 1.88x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                                   |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                   |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                   |
| richards                 | 79.3 ms                                                | 43.7 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.24 ms: 1.75x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.0 ms: 1.73x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                  |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.55 ms: 1.66x faster                                                  |
| pyflate                  | 716 ms                                                 | 433 ms: 1.66x faster                                                   |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                  |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                  |
| html5lib                 | 88.9 ms                                                | 59.8 ms: 1.49x faster                                                  |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                 |
| thrift                   | 1.07 ms                                                | 758 us: 1.41x faster                                                   |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 48.3 ms: 1.37x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.75 ms: 1.36x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                   |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                   |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                   |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.32x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.8 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| nqueens                  | 106 ms                                                 | 83.3 ms: 1.27x faster                                                  |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 84.0 ms: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.15x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                   |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                  |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 89.5 ms: 1.13x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250221-3.14.0a5+-5d66c55/bm-20250221-linux-x86_64-python-5d66c55c8ad0a0aeff8d-3.14.0a5+-5d66c55.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.455x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x