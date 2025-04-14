# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_stitch_2048
- machine: linux-x86_64
- commit hash: 9003e9b
- commit date: 2025-03-06
- overall geometric mean: 1.444x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                    |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                                    |
| async_tree_none         | 728 ms                                                 | 266 ms: 2.73x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 332 ms: 2.62x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| nbody          | 154 ms                                                 | 92.7 ms: 1.66x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.42x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                   |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.63x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                    |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                   |
| django_template | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                   |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                    |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                                    |
| async_tree_none          | 728 ms                                                 | 266 ms: 2.73x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 332 ms: 2.62x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                    |
| go                       | 240 ms                                                 | 118 ms: 2.04x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                   |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                    |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                   |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                    |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                    |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.82x faster                                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                    |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                  |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                                   |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                   |
| nbody                    | 154 ms                                                 | 92.7 ms: 1.66x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.63x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.62x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                   |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                    |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                   |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.53x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                    |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                    |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                    |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.50 ms: 1.44x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 55.3 ms: 1.43x faster                                                   |
| thrift                   | 1.07 ms                                                | 751 us: 1.43x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                    |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                    |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                    |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                    |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                   |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.71 us: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                    |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                    |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.63 ms: 1.05x slower                                                   |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.56 ms: 1.26x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.43 ms: 1.50x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250306-3.14.0a5+-9003e9b-JIT/bm-20250306-linux-x86_64-brandtbucher-jit_stitch_2048-3.14.0a5+-9003e9b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.444x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x