# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_optimizer_equali
- machine: linux-x86_64
- commit hash: 3f0f396
- commit date: 2025-03-06
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                        |
| nbody          | 154 ms                                                 | 98.9 ms: 1.55x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 207 us: 1.59x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                        |
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                        |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                        |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 332 ms: 2.62x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                         |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                        |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                        |
| richards_super           | 94.7 ms                                                | 50.4 ms: 1.88x faster                                                        |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                         |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                         |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                                         |
| spectral_norm            | 170 ms                                                 | 94.4 ms: 1.80x faster                                                        |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                        |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 74.1 ms: 1.73x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                        |
| pyflate                  | 716 ms                                                 | 427 ms: 1.68x faster                                                         |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.63x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.40 ms: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 207 us: 1.59x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| nbody                    | 154 ms                                                 | 98.9 ms: 1.55x faster                                                        |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                        |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                         |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                        |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                         |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.44 ms: 1.46x faster                                                        |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                        |
| thrift                   | 1.07 ms                                                | 758 us: 1.41x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.9 ms: 1.39x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                         |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                         |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                        |
| nqueens                  | 106 ms                                                 | 82.8 ms: 1.28x faster                                                        |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                       |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 876 us: 1.13x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| async_generators         | 444 ms                                                 | 404 ms: 1.10x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                        |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                        |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.66 ms: 1.05x slower                                                        |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.00 ms: 1.38x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.7 ms: 3.40x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250306-3.14.0a5+-3f0f396-JIT/bm-20250306-linux-x86_64-brandtbucher-jit_optimizer_equali-3.14.0a5+-3f0f396.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.440x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x