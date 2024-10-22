# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                  |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.17x faster                                                |
| html5lib       | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.1 ms: 1.48x faster                                                 |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 407 ms: 2.14x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 844 ms: 2.09x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 75.6 ms: 2.03x faster                                                 |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.52x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.42x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.7 ms: 1.22x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                 |
| django_template | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 55.6 ms: 1.19x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                  |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                 |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 407 ms: 2.14x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.9 us: 2.10x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 844 ms: 2.09x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                                 |
| nbody                    | 154 ms                                                 | 75.6 ms: 2.03x faster                                                 |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                 |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.96x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.6 ms: 1.95x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                 |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                  |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                 |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                                  |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                                 |
| mako                     | 16.3 ms                                                | 9.73 ms: 1.68x faster                                                 |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                  |
| pyflate                  | 716 ms                                                 | 429 ms: 1.67x faster                                                  |
| pylint                   | 551 ms                                                 | 332 ms: 1.66x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.45 ms: 1.61x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                 |
| logging_format           | 9.09 us                                                | 5.99 us: 1.52x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.1 ms: 1.48x faster                                                 |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                                  |
| regex_compile            | 188 ms                                                 | 132 ms: 1.42x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                |
| fannkuch                 | 532 ms                                                 | 380 ms: 1.40x faster                                                  |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.4 ms: 1.36x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.34x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                 |
| thrift                   | 1.07 ms                                                | 804 us: 1.33x faster                                                  |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 54.9 ms: 1.26x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                 |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 81.7 ms: 1.22x faster                                                 |
| sympy_sum                | 196 ms                                                 | 163 ms: 1.21x faster                                                  |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 21.7 ms: 1.19x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 55.6 ms: 1.19x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.17x faster                                                |
| sympy_expand             | 566 ms                                                 | 488 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                 |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                  |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                 |
| telco                    | 7.27 ms                                                | 8.23 ms: 1.13x slower                                                 |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-d19b26c-JIT/bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.19x