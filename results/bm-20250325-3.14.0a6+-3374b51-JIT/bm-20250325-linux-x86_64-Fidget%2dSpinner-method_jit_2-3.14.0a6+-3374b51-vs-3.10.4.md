# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: method_jit_2
- machine: linux-x86_64
- commit hash: 3374b51
- commit date: 2025-03-25
- overall geometric mean: 1.405x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                  | 1.33x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 628 ms: 2.82x faster                                                     |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 320 ms: 2.71x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.03x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.2 ms: 1.74x faster                                                    |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                    |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.43x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                     |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.20x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 334 us: 1.45x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                    |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                    |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                    |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 628 ms: 2.82x faster                                                     |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 320 ms: 2.71x faster                                                     |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.03x faster                                                     |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                    |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                                    |
| pylint                   | 551 ms                                                 | 292 ms: 1.89x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                     |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                     |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                     |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                                    |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                    |
| raytrace                 | 507 ms                                                 | 289 ms: 1.75x faster                                                     |
| nbody                    | 154 ms                                                 | 88.2 ms: 1.74x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                    |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                    |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 78.0 ms: 1.64x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.56 ms: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                   |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                     |
| scimark_fft              | 466 ms                                                 | 314 ms: 1.48x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                     |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.45x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 334 us: 1.45x faster                                                     |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                    |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.88 us: 1.41x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                    |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                    |
| comprehensions           | 28.8 us                                                | 20.7 us: 1.39x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                   |
| logging_format           | 9.09 us                                                | 6.65 us: 1.37x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 61.7 ms: 1.37x faster                                                    |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 768 ms: 1.33x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                    |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 134 ms: 1.29x faster                                                     |
| thrift                   | 1.07 ms                                                | 841 us: 1.27x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.3 ms: 1.27x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                    |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                   |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.23x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                    |
| sympy_str                | 346 ms                                                 | 286 ms: 1.21x faster                                                     |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                    |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                    |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                    |
| async_generators         | 444 ms                                                 | 402 ms: 1.10x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                    |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 908 us: 1.09x faster                                                     |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                    |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                     |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                    |
| coverage                 | 79.4 ms                                                | 93.7 ms: 1.18x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.83 ms: 1.33x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                             |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250325-3.14.0a6+-3374b51-JIT/bm-20250325-linux-x86_64-Fidget%2dSpinner-method_jit_2-3.14.0a6+-3374b51.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.405x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.32x