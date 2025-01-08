# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.499x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 249 ms: 1.40x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 57.9 ms: 1.54x faster                                                 |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.6 ms: 1.84x faster                                                 |
| float          | 117 ms                                                 | 66.4 ms: 1.76x faster                                                 |
| pidigits       | 191 ms                                                 | 197 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                  |
| regex_dna      | 227 ms                                                 | 196 ms: 1.15x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.57x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                 |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                 |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.7 ms: 1.57x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 154 us: 3.53x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                                  |
| generators               | 80.1 ms                                                | 27.1 ms: 2.95x faster                                                 |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                  |
| deltablue                | 7.91 ms                                                | 2.98 ms: 2.66x faster                                                 |
| go                       | 240 ms                                                 | 109 ms: 2.21x faster                                                  |
| chaos                    | 115 ms                                                 | 54.2 ms: 2.13x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                                  |
| logging_silent           | 190 ns                                                 | 93.0 ns: 2.04x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 58.3 ms: 2.03x faster                                                 |
| scimark_sor              | 220 ms                                                 | 109 ms: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 273 ms: 2.02x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                 |
| richards_super           | 94.7 ms                                                | 47.1 ms: 2.01x faster                                                 |
| raytrace                 | 507 ms                                                 | 252 ms: 2.01x faster                                                  |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                 |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                                  |
| spectral_norm            | 170 ms                                                 | 90.8 ms: 1.87x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 69.4 ms: 1.84x faster                                                 |
| nbody                    | 154 ms                                                 | 83.6 ms: 1.84x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.19 ms: 1.83x faster                                                 |
| hexiom                   | 10.4 ms                                                | 5.80 ms: 1.79x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                 |
| float                    | 117 ms                                                 | 66.4 ms: 1.76x faster                                                 |
| pyflate                  | 716 ms                                                 | 407 ms: 1.76x faster                                                  |
| scimark_lu               | 176 ms                                                 | 101 ms: 1.74x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.50 ms: 1.72x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                |
| coroutines               | 35.1 ms                                                | 21.2 ms: 1.66x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.61x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.09 ms: 1.58x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.57x faster                                                  |
| django_template          | 48.2 ms                                                | 30.7 ms: 1.57x faster                                                 |
| scimark_fft              | 466 ms                                                 | 301 ms: 1.55x faster                                                  |
| html5lib                 | 88.9 ms                                                | 57.9 ms: 1.54x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.43 us: 1.53x faster                                                 |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                 |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                                 |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| pathlib                  | 20.5 ms                                                | 14.2 ms: 1.44x faster                                                 |
| nqueens                  | 106 ms                                                 | 74.1 ms: 1.43x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                  |
| 2to3                     | 348 ms                                                 | 249 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                  |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                                  |
| sympy_sum                | 196 ms                                                 | 144 ms: 1.36x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 62.4 ms: 1.35x faster                                                 |
| sympy_str                | 346 ms                                                 | 261 ms: 1.32x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 52.4 ms: 1.32x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| sympy_expand             | 566 ms                                                 | 444 ms: 1.27x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 829 us: 1.19x faster                                                  |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                 |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                 |
| json                     | 5.69 ms                                                | 4.91 ms: 1.16x faster                                                 |
| regex_dna                | 227 ms                                                 | 196 ms: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.88 sec: 1.01x slower                                                |
| coverage                 | 79.4 ms                                                | 81.1 ms: 1.02x slower                                                 |
| pidigits                 | 191 ms                                                 | 197 ms: 1.03x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.96 ms: 1.37x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.54 ms: 1.57x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 80.7 ms: 3.36x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.47x faster                                                          |

Benchmark hidden because not significant (1): telco
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-f1d3190-CLANG/bm-20250107-linux-x86_64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.499x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.36x

# Memory
- memory change: 1.27x