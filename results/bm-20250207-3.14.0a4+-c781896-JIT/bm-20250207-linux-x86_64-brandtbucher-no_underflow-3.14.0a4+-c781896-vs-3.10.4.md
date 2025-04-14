# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_underflow
- machine: linux-x86_64
- commit hash: c781896
- commit date: 2025-02-07
- overall geometric mean: 1.460x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                 |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                               |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                |
| Geometric mean | (ref)                                                  | 1.34x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                                 |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.71x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.68x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.5 ms: 1.68x faster                                                |
| nbody          | 154 ms                                                 | 94.3 ms: 1.63x faster                                                |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                |
| regex_dna      | 227 ms                                                 | 204 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                               |
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.43x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 96.4 ms: 1.20x faster                                                |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                |
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                |
| Geometric mean  | (ref)                                                  | 1.49x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                 |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                                 |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.71x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.68x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                 |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                 |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                 |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                 |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                 |
| spectral_norm            | 170 ms                                                 | 92.0 ms: 1.85x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                 |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 71.1 ms: 1.80x faster                                                |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                |
| float                    | 117 ms                                                 | 69.5 ms: 1.68x faster                                                |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                |
| pyflate                  | 716 ms                                                 | 428 ms: 1.67x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                                 |
| mako                     | 16.3 ms                                                | 9.91 ms: 1.65x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.35 ms: 1.64x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                |
| nbody                    | 154 ms                                                 | 94.3 ms: 1.63x faster                                                |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                 |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                 |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.19 us: 1.47x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.43x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                               |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.39x faster                                                |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                               |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                |
| dulwich_log              | 84.3 ms                                                | 65.7 ms: 1.28x faster                                                |
| nqueens                  | 106 ms                                                 | 82.6 ms: 1.28x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.3 ms: 1.27x faster                                                |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 96.4 ms: 1.20x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.05 ms: 1.19x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                               |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                 |
| regex_dna                | 227 ms                                                 | 204 ms: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                |
| async_generators         | 444 ms                                                 | 409 ms: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                                |
| coverage                 | 79.4 ms                                                | 89.9 ms: 1.13x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                         |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250207-3.14.0a4+-c781896-JIT/bm-20250207-linux-x86_64-brandtbucher-no_underflow-3.14.0a4+-c781896.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.460x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.28x