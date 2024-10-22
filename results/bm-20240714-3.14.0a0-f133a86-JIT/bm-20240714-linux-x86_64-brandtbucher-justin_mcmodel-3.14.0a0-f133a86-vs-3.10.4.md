# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: f133a86
- commit date: 2024-07-14
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.30x faster                                                  |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.2 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 845 ms: 2.09x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 77.1 ms: 1.99x faster                                                 |
| float          | 117 ms                                                 | 69.6 ms: 1.68x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.51x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.9 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 27.5 us: 1.13x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                 |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 56.1 ms: 1.18x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                                  |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                 |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.54 ms: 2.23x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 845 ms: 2.09x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.2 us: 2.07x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.03x faster                                                 |
| chaos                    | 115 ms                                                 | 57.4 ms: 2.01x faster                                                 |
| nbody                    | 154 ms                                                 | 77.1 ms: 1.99x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.3 ms: 1.96x faster                                                 |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.9 ms: 1.91x faster                                                 |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.78x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.78x faster                                                  |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                  |
| float                    | 117 ms                                                 | 69.6 ms: 1.68x faster                                                 |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                  |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                 |
| pylint                   | 551 ms                                                 | 334 ms: 1.65x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.47 ms: 1.61x faster                                                 |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                 |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                 |
| tornado_http             | 136 ms                                                 | 93.2 ms: 1.46x faster                                                 |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                                  |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                                 |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.34x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                 |
| thrift                   | 1.07 ms                                                | 811 us: 1.32x faster                                                  |
| 2to3                     | 348 ms                                                 | 269 ms: 1.30x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 54.6 ms: 1.27x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                 |
| nqueens                  | 106 ms                                                 | 85.8 ms: 1.23x faster                                                 |
| dask                     | 441 ms                                                 | 361 ms: 1.22x faster                                                  |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                  |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 21.7 ms: 1.19x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.1 ms: 1.18x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.9 ms: 1.16x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                |
| sympy_expand             | 566 ms                                                 | 492 ms: 1.15x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| json_loads               | 31.2 us                                                | 27.5 us: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                                |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                 |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.09 ms: 1.11x slower                                                 |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-f133a86-JIT/bm-20240714-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-f133a86.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.18x