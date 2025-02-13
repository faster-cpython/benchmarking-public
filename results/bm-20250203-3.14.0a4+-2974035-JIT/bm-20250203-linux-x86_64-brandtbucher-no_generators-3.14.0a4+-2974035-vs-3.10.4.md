# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_generators
- machine: linux-x86_64
- commit hash: 2974035
- commit date: 2025-02-03
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                                  |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 627 ms: 2.82x faster                                                  |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.62x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| nbody          | 154 ms                                                 | 92.5 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.43x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 95.3 ms: 1.21x faster                                                 |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.89 ms: 1.65x faster                                                 |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                 |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 47.5 ms: 1.39x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.51x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 627 ms: 2.82x faster                                                  |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.62x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                 |
| generators               | 80.1 ms                                                | 37.1 ms: 2.16x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                 |
| scimark_sor              | 220 ms                                                 | 114 ms: 1.92x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                 |
| go                       | 240 ms                                                 | 127 ms: 1.89x faster                                                  |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.87x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 70.9 ms: 1.80x faster                                                 |
| spectral_norm            | 170 ms                                                 | 94.7 ms: 1.79x faster                                                 |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                                 |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                 |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                                  |
| float                    | 117 ms                                                 | 67.4 ms: 1.74x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                |
| logging_silent           | 190 ns                                                 | 112 ns: 1.69x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                 |
| nbody                    | 154 ms                                                 | 92.5 ms: 1.66x faster                                                 |
| mako                     | 16.3 ms                                                | 9.89 ms: 1.65x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                 |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                  |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                 |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.88 us: 1.45x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.19 ms: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                                 |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.82 us: 1.43x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.42x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 47.5 ms: 1.39x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 750 ms: 1.36x faster                                                  |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                                  |
| nqueens                  | 106 ms                                                 | 78.2 ms: 1.35x faster                                                 |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                                 |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.7 ms: 1.28x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 95.3 ms: 1.21x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| async_generators         | 444 ms                                                 | 383 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                  |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                                 |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.56 ms: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 80.1 ms: 3.34x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250203-3.14.0a4+-2974035-JIT/bm-20250203-linux-x86_64-brandtbucher-no_generators-3.14.0a4+-2974035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x