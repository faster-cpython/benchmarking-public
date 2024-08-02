# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: optimizer_off
- machine: linux-x86_64
- commit hash: 118726c
- commit date: 2024-06-29
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                     |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                   |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                    |
| tornado_http   | 136 ms                                                 | 92.8 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 845 ms: 2.09x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.2 ms: 1.82x faster                                                    |
| float          | 117 ms                                                 | 71.2 ms: 1.65x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.46x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                                     |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                    |
| regex_dna      | 227 ms                                                 | 232 ms: 1.03x slower                                                     |
| regex_effbot   | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 81.8 ms: 1.22x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.45 ms: 1.26x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                    |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                     |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                    |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.63 ms: 2.18x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 845 ms: 2.09x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 28.7 us: 2.03x faster                                                    |
| richards_super           | 94.7 ms                                                | 47.5 ms: 1.99x faster                                                    |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                    |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                    |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                     |
| nbody                    | 154 ms                                                 | 84.2 ms: 1.82x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                     |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                     |
| deepcopy                 | 479 us                                                 | 273 us: 1.75x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                                    |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                     |
| float                    | 117 ms                                                 | 71.2 ms: 1.65x faster                                                    |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                                    |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                    |
| pylint                   | 551 ms                                                 | 344 ms: 1.60x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                     |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                     |
| pyflate                  | 716 ms                                                 | 455 ms: 1.58x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.75 ms: 1.54x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                     |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                    |
| tornado_http             | 136 ms                                                 | 92.8 ms: 1.47x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.49 ms: 1.44x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                   |
| scimark_fft              | 466 ms                                                 | 326 ms: 1.43x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                     |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                     |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 57.5 ms: 1.38x faster                                                    |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                    |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                                     |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                    |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.25x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 56.4 ms: 1.23x faster                                                    |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 81.8 ms: 1.22x faster                                                    |
| nqueens                  | 106 ms                                                 | 87.8 ms: 1.21x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.0 ms: 1.18x faster                                                    |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                     |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.5 ms: 1.15x faster                                                    |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                    |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                     |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                     |
| regex_dna                | 227 ms                                                 | 232 ms: 1.03x slower                                                     |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.73 ms: 1.03x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                    |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                                    |
| coverage                 | 79.4 ms                                                | 93.5 ms: 1.18x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.45 ms: 1.26x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                             |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-118726c-JIT/bm-20240629-linux-x86_64-Fidget%2dSpinner-optimizer_off-3.14.0a0-118726c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.20x