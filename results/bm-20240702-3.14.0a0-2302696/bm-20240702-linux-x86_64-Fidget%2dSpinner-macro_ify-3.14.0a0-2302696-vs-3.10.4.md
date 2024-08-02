# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: macro_ify
- machine: linux-x86_64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                               |
| html5lib       | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                |
| tornado_http   | 136 ms                                                 | 90.3 ms: 1.51x faster                                                |
| Geometric mean | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 405 ms: 2.15x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 844 ms: 2.09x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.4 ms: 1.78x faster                                                |
| float          | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                 |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                 |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.49x faster                                                |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 405 ms: 2.15x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 844 ms: 2.09x faster                                                 |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                 |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                 |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                 |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.81x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                 |
| pylint                   | 551 ms                                                 | 307 ms: 1.79x faster                                                 |
| nbody                    | 154 ms                                                 | 86.4 ms: 1.78x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.78x faster                                                |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.1 ms: 1.75x faster                                                |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                                |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.63x faster                                                |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                 |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                 |
| float                    | 117 ms                                                 | 76.5 ms: 1.53x faster                                                |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.3 ms: 1.51x faster                                                |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.51x faster                                                |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                               |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                                |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                               |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                               |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                               |
| fannkuch                 | 532 ms                                                 | 387 ms: 1.37x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                |
| nqueens                  | 106 ms                                                 | 78.8 ms: 1.34x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                 |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                |
| scimark_fft              | 466 ms                                                 | 357 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 788 us: 1.25x faster                                                 |
| dask                     | 441 ms                                                 | 357 ms: 1.23x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                               |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                                |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.13x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                 |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                 |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.57 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                |
| telco                    | 7.27 ms                                                | 8.27 ms: 1.14x slower                                                |
| coverage                 | 79.4 ms                                                | 92.3 ms: 1.16x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                         |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.11x