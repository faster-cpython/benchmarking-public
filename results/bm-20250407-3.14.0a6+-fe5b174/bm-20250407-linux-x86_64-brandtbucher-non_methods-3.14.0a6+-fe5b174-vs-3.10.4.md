# Results vs. 3.10.4

- fork: brandtbucher
- ref: non_methods
- machine: linux-x86_64
- commit hash: fe5b174
- commit date: 2025-04-07
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                                |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 61.2 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 609 ms: 2.90x faster                                                |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.86x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.82x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 483 ms: 2.11x faster                                                |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.8 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 90.9 ms: 1.69x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.45x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 123 ms: 1.53x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                               |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                |
| Geometric mean | (ref)                                                  | 1.21x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.67x faster                                              |
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.37x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.22x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 83.2 ms: 1.20x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.52x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                               |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                |
| async_tree_io            | 1.77 sec                                               | 609 ms: 2.90x faster                                                |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.86x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.82x faster                                                |
| generators               | 80.1 ms                                                | 30.1 ms: 2.66x faster                                               |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                              |
| go                       | 240 ms                                                 | 109 ms: 2.19x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 483 ms: 2.11x faster                                                |
| chaos                    | 115 ms                                                 | 55.3 ms: 2.09x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                               |
| logging_silent           | 190 ns                                                 | 93.5 ns: 2.03x faster                                               |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                |
| richards_super           | 94.7 ms                                                | 47.8 ms: 1.98x faster                                               |
| raytrace                 | 507 ms                                                 | 256 ms: 1.98x faster                                                |
| deepcopy                 | 479 us                                                 | 246 us: 1.95x faster                                                |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                               |
| float                    | 117 ms                                                 | 65.8 ms: 1.78x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                               |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                               |
| spectral_norm            | 170 ms                                                 | 97.7 ms: 1.74x faster                                               |
| nbody                    | 154 ms                                                 | 90.9 ms: 1.69x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.67x faster                                              |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.60 us: 1.60x faster                                               |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                |
| regex_compile            | 188 ms                                                 | 123 ms: 1.53x faster                                                |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                               |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.52x faster                                               |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                               |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                               |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                               |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                               |
| html5lib                 | 88.9 ms                                                | 61.2 ms: 1.45x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                               |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.60 ms: 1.41x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                               |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                                |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.38x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.37x faster                                               |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.35x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.30x faster                                                |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.22x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 83.2 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                               |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                               |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.13x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                               |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.65 ms: 1.05x slower                                               |
| coverage                 | 79.4 ms                                                | 85.1 ms: 1.07x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.64 ms: 1.28x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                               |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250407-3.14.0a6+-fe5b174/bm-20250407-linux-x86_64-brandtbucher-non_methods-3.14.0a6+-fe5b174.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.27x